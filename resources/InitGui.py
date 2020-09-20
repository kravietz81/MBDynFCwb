import os
import sys
import FreeCAD as App
import FreeCADGui as Gui

import MBDyn_locator
MBDwbPath = os.path.dirname(MBDyn_locator.__file__)
MBDwb_icons_path = os.path.join(MBDwbPath, 'icons')



class MbdynGui(Workbench):

    def __init__(self):
        self.__class__.Icon = """
            /* XPM */
            static char *_857_5567c986d2e71b01ca23671d10617805d3f636aef74fac3a0f42400b43825347[] = {
            /* columns rows colors chars-per-pixel */
            "16 16 6 1 ",
            "  c red",
            ". c #808000",
            "X c yellow",
            "o c #808080",
            "O c #C0C0C0",
            "+ c white",
            /* pixels */
            "++++++++++++++++",
            "++++++++++++++++",
            "++++++++++++++++",
            "++++++++++++++++",
            "++++++++++++++++",
            "++++++++++++++++",
            "+++++XXOO+++XXOO",
            "++++OXX  ++OXX  ",
            "oo++ .+O ++ .+++",
            "O O  +++XO  ++++",
            "+O  ++++O  +++++",
            "++++++++++++++++",
            "++++++++++++++++",
            "++++++++++++++++",
            "++++++++++++++++",
            "++++++++++++++++"
            };
            """
        self.__class__.MenuText = "MBDyn"
        self.__class__.ToolTip = "Model for Mbdyn simulation"


    def GetClassName(self):
        return "Gui::PythonWorkbench"

    def Initialize(self):
        import os
        import FreeCAD as App
        import FreeCADGui as Gui
        import MBDyn_locator
        MBDwbPath = os.path.dirname(MBDyn_locator.__file__)
        MBDwb_icons_path = os.path.join(MBDwbPath, 'icons')
        import MBDyn_guitools.m_values
        import MBDyn_guitools.MBDynFreeCAD
        import MBDyn_guitools.body_AS4_cmd
        import MBDyn_guitools.ref_cmd
        import MBDyn_guitools.struct_node_cmd
        import MBDyn_guitools.revpin_joint_AS4_2_cmd
        import MBDyn_guitools.hinge_joint_AS4_cmd
        import MBDyn_guitools.postproc_AS4_cmd
        import MBDyn_guitools.total_joint_cmd
        import MBDyn_guitools.total_pinjoint_cmd
        import MBDyn_guitools.ramp_drive_cmd
        import MBDyn_guitools.axial_rot_joint_AS4_cmd
        import MBDyn_viewproviders.view_workbench_container
        
        from MBDyn_settings.wdgt_solver_settings import wdgt_solver_settings
  
        self.list = ["CommandCreaArborecense", "mbdyn_configure", "mbdyn_launchGui", "body_sel_cmd",
                    "ref_cmd", "struct_node_cmd", "revpin_joint_cmd",
                    "hinge_joint_cmd", "total_joint_cmd", "total_pinjoint_cmd",
                    "axial_rot_joint_cmd", "ramp_drive_cmd", "postproc_cmd"]
        self.appendToolbar("Mbdyn_comands", self.list)
        self.appendMenu("Mbdyn_menu", self.list)
        Log("Loading MyModule... done\n")
        # Add preferences page on the main window toolbar: Edit/ preferences.../mbdyn
        Gui.addPreferencePage(wdgt_solver_settings, "MBDyn")
        img_path = os.path.join(MBDwb_icons_path, 'preferences-MBDyn.svg')
        Gui.addIcon("preferences-mbdyn", img_path)

    def Activated(self):
        App.Console.PrintMessage("MBDyn Workbench Activated")


    def Deactivated(self):
        Msg("MyWorkbench.Deactivated()\n")

Gui.addWorkbench(MbdynGui)