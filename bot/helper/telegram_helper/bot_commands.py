#!/usr/bin/env python3
from bot import CMD_SUFFIX, config_dict

class _BotCommands:
    def __init__(self):
        self.StartCommand = 'start'
        self.MirrorCommand = [f'pea{CMD_SUFFIX}', f'p{CMD_SUFFIX}']
        self.QbMirrorCommand = [f'qbmirror{CMD_SUFFIX}', f'pm{CMD_SUFFIX}']
        self.YtdlCommand = [f'peaytdl{CMD_SUFFIX}', f'py{CMD_SUFFIX}']
        self.LeechCommand = [f'leech{CMD_SUFFIX}', f'pl{CMD_SUFFIX}']
        self.QbLeechCommand = [f'peaqbleech{CMD_SUFFIX}', f'pql{CMD_SUFFIX}']
        self.YtdlLeechCommand = [f'peaytdlleech{CMD_SUFFIX}', f'pyl{CMD_SUFFIX}']
        if config_dict['SHOW_EXTRA_CMDS']:
            self.MirrorCommand.extend([f'peaunzip{CMD_SUFFIX}', f'puzm{CMD_SUFFIX}', f'pzip{CMD_SUFFIX}', f'pzm{CMD_SUFFIX}'])
            self.QbMirrorCommand.extend([f'peaqbunzip{CMD_SUFFIX}', f'pquzm{CMD_SUFFIX}', f'pqbzip{CMD_SUFFIX}', f'pqzm{CMD_SUFFIX}'])
            self.YtdlCommand.extend([f'peaytdlzip{CMD_SUFFIX}', f'yz{CMD_SUFFIX}'])
            self.LeechCommand.extend([f'peaunzipleech{CMD_SUFFIX}', f'uzl{CMD_SUFFIX}', f'zipleech{CMD_SUFFIX}', f'zl{CMD_SUFFIX}'])
            self.QbLeechCommand.extend([f'peaqbunzipleech{CMD_SUFFIX}', f'quzl{CMD_SUFFIX}', f'qbzipleech{CMD_SUFFIX}', f'qzl{CMD_SUFFIX}'])
            self.YtdlLeechCommand.extend([f'peaytdlzipleech{CMD_SUFFIX}', f'yzl{CMD_SUFFIX}'])
        self.CloneCommand = [f'peaclone{CMD_SUFFIX}', f'c{CMD_SUFFIX}']
        self.CountCommand = f'peacount{CMD_SUFFIX}'
        self.DeleteCommand = f'peadel{CMD_SUFFIX}'
        self.CancelMirror = f'peacancel{CMD_SUFFIX}'
        self.CancelAllCommand = [f'peacancelall{CMD_SUFFIX}', 'pcancellallbot']
        self.ListCommand = f'pealist{CMD_SUFFIX}'
        self.SearchCommand = f'peasearch{CMD_SUFFIX}'
        self.StatusCommand = [f'peastatus{CMD_SUFFIX}', f's{CMD_SUFFIX}', 'statusall']
        self.UsersCommand = f'peausers{CMD_SUFFIX}'
        self.AuthorizeCommand = [f'peaauthorize{CMD_SUFFIX}', f'a{CMD_SUFFIX}']
        self.UnAuthorizeCommand = [f'peaunauthorize{CMD_SUFFIX}', f'ua{CMD_SUFFIX}']
        self.AddBlackListCommand = [f'peablacklist{CMD_SUFFIX}', f'bl{CMD_SUFFIX}']
        self.RmBlackListCommand = [f'pearmblacklist{CMD_SUFFIX}', f'rbl{CMD_SUFFIX}']
        self.AddSudoCommand = f'peaaddsudo{CMD_SUFFIX}'
        self.RmSudoCommand = f'pearmsudo{CMD_SUFFIX}'
        self.PingCommand = [f'peaping{CMD_SUFFIX}', f'p{CMD_SUFFIX}']
        self.RestartCommand = [f'pearestart{CMD_SUFFIX}', f'r{CMD_SUFFIX}', 'restartall']
        self.StatsCommand = [f'peastats{CMD_SUFFIX}', f'st{CMD_SUFFIX}']
        self.HelpCommand = f'peahelp{CMD_SUFFIX}'
        self.LogCommand = f'pealog{CMD_SUFFIX}'
        self.ShellCommand = f'peashell{CMD_SUFFIX}'
        self.EvalCommand = f'peaeval{CMD_SUFFIX}'
        self.ExecCommand = f'peaexec{CMD_SUFFIX}'
        self.ClearLocalsCommand = f'peaclearlocals{CMD_SUFFIX}'
        self.BotSetCommand = [f'peabsetting{CMD_SUFFIX}', f'bs{CMD_SUFFIX}']
        self.UserSetCommand = [f'peausetting{CMD_SUFFIX}', f'us{CMD_SUFFIX}']
        self.BtSelectCommand = f'peabtsel{CMD_SUFFIX}'
        self.CategorySelect = f'peactsel{CMD_SUFFIX}'
        self.SpeedCommand = [f'peaspeedtest{CMD_SUFFIX}', f'sp{CMD_SUFFIX}']
        self.RssCommand = f'pearss{CMD_SUFFIX}'
        self.LoginCommand = 'pealogin'
        self.AddImageCommand = f'peaaddimg{CMD_SUFFIX}'
        self.ImagesCommand = f'peaimages{CMD_SUFFIX}'
        self.IMDBCommand = f'peaimdb{CMD_SUFFIX}'
        self.AniListCommand = f'peaanime{CMD_SUFFIX}'
        self.AnimeHelpCommand = f'peaanimehelp{CMD_SUFFIX}'
        self.MediaInfoCommand = [f'peamediainfo{CMD_SUFFIX}', f'mi{CMD_SUFFIX}']
        self.MyDramaListCommand = f'peamdl{CMD_SUFFIX}'
        self.GDCleanCommand = [f'peagdclean{CMD_SUFFIX}', f'gc{CMD_SUFFIX}']
        self.BroadcastCommand = [f'peabroadcast{CMD_SUFFIX}', f'bc{CMD_SUFFIX}']

BotCommands = _BotCommands()
