# ============================================================================
# FILE: __init__.py
# AUTHOR: Philip Karlsson <philipkarlsson at me.com>
# License: MIT license
# ============================================================================

import neovim
from neovim_bolt_cli.neovim_bolt_cli import neovim_bolt_cli


@neovim.plugin
class NeovimBoltHandlers(object):
    def __init__(self, nvim):
        self.nvim = nvim
        self.bolt = neovim_bolt_cli(nvim, log=False)

    @neovim.command("Tc", range='', nargs='*', sync=True)
    def tc_explore(self, args, range):
        self.bolt.tc_explore(args, range)

    @neovim.command("Tcd", range='', nargs='*', sync=True)
    def tc_explore_dual(self, args, range):
        self.bolt.tc_explore_dual(args, range)

    @neovim.command("TcExpEnter", range='', nargs='*', sync=True)
    def tc_enter(self, args, range):
        self.bolt.tc_enter(args, range)

    @neovim.command("TcExpUp", range='', nargs='*', sync=True)
    def tc_up(self, args, range):
        self.bolt.tc_up(args, range)

    @neovim.command("TcExpDown", range='', nargs='*', sync=True)
    def tc_down(self, args, range):
        self.bolt.tc_down(args, range)

    @neovim.command("TcExpClose", range='', nargs='*', sync=True)
    def tc_close(self, args, range):
        self.bolt.tc_close(args, range)

    @neovim.command("TcExpTab", range='', nargs='*', sync=True)
    def tc_tab(self, args, range):
        self.bolt.tc_tab(args, range)

    @neovim.command("TcSetCwd", range='', nargs='*', sync=True)
    def tc_set_cwd(self, args, range):
        self.bolt.tc_set_cwd(args, range)

    @neovim.command("BoltMove", range='', nargs='*', sync=True)
    def bolt_move(self, args, range):
        self.bolt.move(args, range)

    @neovim.command("BoltRename", range='', nargs='*', sync=True)
    def bolt_rename(self, args, range):
        self.bolt.rename(args, range)

    @neovim.command("BoltCopy", range='', nargs='*', sync=True)
    def bolt_copy(self, args, range):
        self.bolt.copy(args, range)

    @neovim.command("BoltMkdir", range='', nargs='*', sync=True)
    def bolt_mkdir(self, args, range):
        self.bolt.mkdir(args, range)

    @neovim.command("BoltCreateFile", range='', nargs='*', sync=True)
    def bolt_createFile(self, args, range):
        self.bolt.createFile(args, range)

    @neovim.command("BoltDelete", range='', nargs='*', sync=True)
    def bolt_delete(self, args, range):
        self.bolt.delete(args, range)

    @neovim.command("TcSearch", range='', nargs='*', sync=True)
    def tc_search(self, args, range):
        self.bolt.tc_search(args, range)

    @neovim.command("TcSearchToggle", range='', nargs='*', sync=True)
    def tc_search_toggle(self, args, range):
        self.bolt.tc_search_toggle(args, range)

    @neovim.autocmd("TextChangedI", pattern='TC_Input', sync=True)
    def insert_changed(self):
        self.bolt.handle_input()
