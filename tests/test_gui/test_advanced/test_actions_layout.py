from unittest.mock import MagicMock, patch

import pytest
from PySide2.QtCore import Qt
from PySide2.QtTest import QTest

from node_launcher.gui.advanced.actions_layout import ActionsLayout


@pytest.fixture
def actions_layout() -> ActionsLayout:
    node_set = MagicMock()
    node_set.bitcoin.file.path = '/test/bitcoin/file.conf'
    node_set.lnd.file.path = '/test/lnd/file.conf'
    actions_layout = ActionsLayout(node_set)
    return actions_layout


class TestActionsLayout(object):
    @patch('node_launcher.gui.advanced.actions_layout.reveal')
    def test_show_bitcoin_conf(self,
                              reveal_patch: MagicMock,
                              actions_layout: ActionsLayout,
                              qtbot: QTest):
        qtbot.mouseClick(actions_layout.show_bitcoin_conf, Qt.LeftButton)
        reveal_patch.assert_called_with('/test/bitcoin')

    @patch('node_launcher.gui.advanced.actions_layout.reveal')
    def test_show_lnd_conf(self,
                              reveal_patch: MagicMock,
                              actions_layout: ActionsLayout,
                              qtbot: QTest):
        qtbot.mouseClick(actions_layout.show_lnd_conf, Qt.LeftButton)
        reveal_patch.assert_called_with('/test/lnd')
