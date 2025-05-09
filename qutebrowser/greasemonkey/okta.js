// ==UserScript==
// @name         Night Owl Theme - Okta
// @namespace    http://tampermonkey.net/
// @version      1.0
// @description  Apply the Night Owl color theme to Okta dashboard
// @author       Immanuel Haffner
// @match        https://firebolt-sso.okta.com/*
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    const style = document.createElement('style');
    style.innerHTML = `
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

        header, nav, footer, section, main, div, aside {
            background-color: #021727 !important;
            color: #d6deeb !important;
        }

        button, input, select, textarea {
            background-color: #092135 !important;
            color: #d6deeb !important;
            // border: 1px solid #7fdbca !important;
        }

        .dropdown-menu--items-wrapper,
        .MuiBox-root,
        .chiclet--container,
        .dashboard--footer,
        .dashboard--header-search-container,
        .side-nav--container,
        .side-nav,
        .tb--sidenav-subitem .tb--sidenav-subitem-icon svg,
        .tb--sidenav-subitem .tb--sidenav-subitem-label,
        .tb--sidenav-item .tb--sidenav-item-label,
        .dashboard--sort-apps-header.dashboard--sort-apps-header-grid-view-margin,
        .MuiScopedCssBaseline-root {
            background-color: #092135 !important;
            color: #d6deeb !important;
        }

        .chiclet--article {
            background-color: #021727 !important;
        }

        .MuiButton-root,
        .MuiButtonBase-root {
            background-color: #82aaff !important;
            color: #021727 !important;
            // border-radius: 4px !important;
        }

        .MuiButton-root:hover,
        .MuiButtonBase-root:hover {
            background-color: #c792ea !important;
            color: #021727 !important;
        }

        .MuiTypography-root,
        .MuiInputBase-root,
        .MuiFormLabel-root,
        .MuiScopedCssBaseline-root,
        label,
        span,
        p,
        h1, h2, h3, h4, h5, h6 {
            color: #d6deeb !important;
        }

        o-link,
        o-dropdown-menu,
        o-text-input,
        o-button,
        .dropdown-menu--button-content,
        .chiclet--app-title,
        .topbar--user-details,
        .user-details--fullname,
        .user-details--email,
        .nav-item--primary-label,
        .nav-item--secondary-label,
        .dashboard--footer-support-title,
        .footer--support-link,
        .support-text {
            color: #d6deeb !important;
        }

        svg path, svg circle {
            fill: #d6deeb !important;
            stroke: #d6deeb !important;
        }

        // img {
        //     filter: brightness(0.9) contrast(1.1);
        // }

        * {
            box-shadow: none !important;
        }

        .unsupported-browser-banner-wrap {
            background-color: #092135 !important;
            border-color: #7fdbca !important;
            color: #d6deeb !important;
        }

        .MuiBox-root.qfchmkz-1ga44m7 {
            background-color: #5ca7e4 !important;
            color: #021727 !important;
        }

        .MuiBox-root.qfchmkz-1ga44m7:hover {
            background-color: #c792ea !important;
        }

        .nav-item--primary-label,
        .nav-item--secondary-label,
        .user-details--fullname,
        .user-details--email {
            color: #d6deeb !important;
        }

        .tb--sidenav-header {
            background: inherit !important;
        }

        .side-nav--container .side-nav {
            border-right: 5px solid rgba(0,0,0,.15) !important;
        }
    `;
    document.head.appendChild(style);
})();
