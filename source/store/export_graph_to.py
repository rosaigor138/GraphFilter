import networkx as nx
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from matplotlib import pyplot as plt
import network2tikz as nxtikz

from source.domain.utils_file import change_gml_file, create_g6_file
from source.store.project_information_store import project_information_store


class ExportGraphTo:
    name = None

    def __init__(self):
        self.all = ExportGraphTo.__subclasses__()
        self.dict_name_export_graph_to: {str: ExportGraphTo} = {}
        for formats in self.all:
            self.dict_name_export_graph_to[formats.name] = formats
        self.file_path = None

    @staticmethod
    def export():
        file_dialog = QFileDialog()
        file_path = file_dialog.getSaveFileName(directory=project_information_store.get_file_name())
        export_graph_to.file_path = file_path[0].strip(project_information_store.get_file_type())
        if export_graph_to.file_path == '':
            return False

    @staticmethod
    def success_export_alert_box(file_type):
        dlg = QMessageBox()
        dlg.setIcon(QMessageBox.Information)
        dlg.setText(f"The graph was exported to the {file_type} format and saved in the following directory: \n"
                    f"{export_graph_to.file_path}")
        dlg.setWindowTitle("Exported successfully")
        dlg.exec()

    @staticmethod
    def same_format_alert_box():
        dlg = QMessageBox()
        dlg.setIcon(QMessageBox.Warning)
        dlg.setText("The graph is already in this format, please try another format")
        dlg.setWindowTitle("Same format")
        dlg.exec()


class ExportToGML(ExportGraphTo):
    name = "Graph (.gml)"

    @staticmethod
    def export():
        if project_information_store.get_file_type() == '.gml':
            return ExportGraphTo.same_format_alert_box()
        export = ExportGraphTo.export()
        if export is not False:
            change_gml_file(export_graph_to.file_path)
            ExportGraphTo.success_export_alert_box('gml')


class ExportToG6(ExportGraphTo):
    name = "Graph6 (.g6)"

    @staticmethod
    def export():
        if project_information_store.get_file_type() == '.g6':
            return ExportGraphTo.same_format_alert_box()
        export = ExportGraphTo.export()
        if export is not False:
            create_g6_file(export_graph_to.file_path + ".g6",
                           nx.to_graph6_bytes(project_information_store.current_graph, header=False).decode('utf-8')
                           )
            ExportGraphTo.success_export_alert_box('graph6')


class ExportToTXT(ExportGraphTo):
    name = "Graph6 (.txt)"

    @staticmethod
    def export():
        if project_information_store.get_file_type() == '.txt':
            return ExportGraphTo.same_format_alert_box()
        export = ExportGraphTo.export()
        if export is not False:
            create_g6_file(export_graph_to.file_path + ".txt",
                           nx.to_graph6_bytes(project_information_store.current_graph, header=False).decode('utf-8')
                           )
            ExportGraphTo.success_export_alert_box('txt')


class ExportToPNG(ExportGraphTo):
    name = "Image (.png)"

    @staticmethod
    def export():
        export = ExportGraphTo.export()
        if export is not False:
            nx.draw_networkx(project_information_store.current_graph,
                             pos=project_information_store.current_graph_pos,
                             node_color='#EEF25C')
            plt.savefig(f"{export_graph_to.file_path}.png", format="PNG")
            plt.close()
            ExportGraphTo.success_export_alert_box('png')


class ExportToPDF(ExportGraphTo):
    name = "Image (.pdf)"

    @staticmethod
    def export():
        export = ExportGraphTo.export()
        if export is not False:
            nx.draw_networkx(project_information_store.current_graph,
                             pos=project_information_store.current_graph_pos,
                             node_color='#EEF25C')
            plt.savefig(f"{export_graph_to.file_path}.pdf", format="PDF")
            plt.close()
            ExportGraphTo.success_export_alert_box('pdf')


class ExportToTikZ(ExportGraphTo):
    name = "Latex Tikz (.latex)"

    @staticmethod
    def export():
        export = ExportGraphTo.export()
        if export is not False:
            style = {}
            style['node_label'] = list(project_information_store.current_graph_pos.keys())
            style['node_color'] = "white"
            nxtikz.plot(project_information_store.current_graph,
                        f"{export_graph_to.file_path}.tex",
                        layout=project_information_store.current_graph_pos,
                        node_size=0.4,
                        **style)
            ExportGraphTo.success_export_alert_box('tikz')


export_graph_to = ExportGraphTo()

dict_name_export_graph_to = export_graph_to.dict_name_export_graph_to