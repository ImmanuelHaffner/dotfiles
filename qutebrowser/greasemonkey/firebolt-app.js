// ==UserScript==
// @name         Night Owl Theme - Firebolt App
// @namespace    http://tampermonkey.net/
// @version      1.0
// @description  Apply Night Owl color theme to Firebolt App
// @author       Immanuel Haffner
// @match        https://*.go.firebolt.io/*
// @match        https://*.staging-go.firebolt.io/*
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    const style = document.createElement('style');
    style.textContent = `

        html, body {
          background-color: #021727 !important;
          color: #d6deeb !important;
        }

        a, a:link, a:visited {
          color: #82aaff !important;
        }

        a:hover, a:active {
          color: #c792ea !important;
        }

        /* Sidebar background and borders */
        ._root_1ipq4_1,
        ._sidebarHead_1ipq4_38,
        ._listItem_kskh1_1,
        ._item_1ipq4_12 {
          background-color: #011221 !important;
          color: #d6deeb !important;
          border-color: #234d70 !important;
        }

        /* Selected item highlight */
        ._selected_kskh1_39 {
          background-color: #1d3b53 !important;
          color: #82aaff !important;
        }

        /* Text color */
        ._name_uf4k3_28,
        ._navLabel_kskh1_16,
        ._helpIcon_uf4k3_25 {
          color: #d6deeb !important;
        }

        /* Icons stroke overrides */
        svg path[data-role="stroke"],
        svg rect,
        svg circle {
          stroke: #82aaff !important;
          fill: #d6deeb !important;
        }

        /* User avatar circle background and text */
        ._container_uf4k3_14 {
          background-color: #1f395d !important;
          color: #d6deeb !important;
        }

        /* Hover/focus states */
        ._listItem_kskh1_1:hover,
        ._item_1ipq4_12:hover {
          background-color: #0e293f !important;
          color: #82aaff !important;
        }

        /* Theme switch highlight */
        ._slider_uqosq_44,
        ._switch_uqosq_33 {
          background-color: #234d70 !important;
        }

        ._slider_uqosq_44 svg path {
          fill: #c792ea !important;
        }

        /* Help icon tint */
        ._helpIcon_uf4k3_25 svg rect,
        ._helpIcon_uf4k3_25 svg path {
          fill: #7fdbca !important;
          stroke: #7fdbca !important;
        }

        [class*="_label__prefix_"],
        [class*="_label_izwgg_193"],
        [class*="_databaseLabel_"],
        [class*="_header_izwgg_83"],
        [data-testid="object-exporer-header"],
        [class*="_search_izwgg_93"],
        [class*="_inputContainer_izwgg_128"],
        [data-testid="databases-search-input"],
        [class*="_title_izwgg_53"],
        [class*="_tree_izwgg_256"],
        [class*="_node_izwgg_234"],
        [class*="_node_gw9yk_6"],
        [class*="_panel_izwgg_75"],
        [class*="MuiOutlinedInput-root"],
        [class*="_content_8lpa2_12"],
        [class*="_root_vmga4_1"],
        [class*="_root_1bht1_7"],
        [class*="_wrapper_1bht1_14"],
        [class*="_tabsWrapper_1bht1_19"],
        [class*="_tab_1bht1_19"],
        [class*="_root_upxym_33"],
        [class*="_body_upxym_56"],
        [class*="_title_upxym_85"],
        [class*="_iconWrapper_upxym_97"],
        [class*="_closeIcon_upxym_113"],
        [class*="_addButton_1bht1_39"],
        [class*="_root_1xl89_1"],
        [class*="_selectorsPanel_5ybuy_495"],
        [class*="_selector_12w2w_421"],
        [class*="_button_12w2w_307"],
        [class*="_chip_1c3wu_7"],
        [class*="_documentActionsPanel_1b00p_1"],
        [class*="_root_8kdpx_7"],
        [class*="_content_8kdpx_15"],
        [class*="_arrowIconWrapper_8kdpx_63"],
        [class*="_root_wttua_1"],
        [class*="_body_wttua_7"],
        [class*="_codeMirrorContainer_1g7ga_1"],
        [class*="_root_1f933_7"],
        [class*="_tabsPanel_1f933_16"],
        [class*="_panel_1f933_25"],
        [class*="_tab_1f933_16"],
        [class*="_icon_1f933_36"],
        [class*="_label_1f933_55"],
        ._root_5ybuy_484,
        .cm-scroller, .cm-content,
        .cm-gutters, .cm-gutter, .cm-gutterElement {
            background-color: #011627 !important;
            color: #d6deeb !important;
            border-color: #1e293b !important;
        }

        [class*="_gradientBoundaryRight_upxym_68"] {
            background-color: rgb(1, 22, 39) !important;
            background: linear-gradient(90deg,transparent 0%,#01111d 70%) !important;
        }

        ._root_upxym_33._active_upxym_151 ._body_upxym_56 {
            background-color: #0b2942 !important;
        }

        button[class*="_tab_"],
        span[class*="_title_"],
        div[class*="_icon_"],
        div[class*="_menuIconContainer_"],
        svg {
            color: #d6deeb !important;
        }

        [class*="MuiOutlinedInput-notchedOutline"] {
            border-color: #3c4c63 !important;
        }

        .cm-activeLine.cm-line {
            background-color: #0b2942 !important;
        }
    `;
    document.head.appendChild(style);
})();
