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

    // Night Owl Color Palette
    const colors = {
        fg: '#d6deeb',
        bg: '#021727',
        foldedBg: '#092135',
        blue: '#82aaff',
        blue8: '#5ca7e4',
        magenta: '#c792ea',
        cyan2: '#7fdbca',
        red: '#ff5874',
        orange: '#f78c6c',
        yellow: '#ffd602',
        green: '#c5e478',
        gray6: '#7e97ac',
        uiBorder: '#5f7e97',
        dark: '#010d18',
        dark2: '#021320'
    };

    // Create and inject CSS
    const style = document.createElement('style');
    style.textContent = `
        /* Global background and text colors */
        html, body {
            background-color: ${colors.bg} !important;
            color: ${colors.fg} !important;
        }

        /* Links */
        a, a:link, a:visited {
            color: ${colors.blue} !important;
        }

        a:hover, a:active {
            color: ${colors.magenta} !important;
        }

        /* Main containers */
        header, nav, footer, section, main, div, aside {
            background-color: ${colors.bg} !important;
            color: ${colors.fg} !important;
        }

        /* Form elements */
        button, input, select, textarea {
            background-color: ${colors.foldedBg} !important;
            color: ${colors.fg} !important;
            border-color: ${colors.uiBorder} !important;
        }

        /* Specific Okta components */
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
        .MuiScopedCssBaseline-root,
        .enduser-app,
        .content-frame,
        .main-container {
            background-color: ${colors.foldedBg} !important;
            color: ${colors.fg} !important;
        }

        /* App cards */
        .chiclet--article {
            background-color: ${colors.bg} !important;
            border: 1px solid ${colors.uiBorder} !important;
        }

        .chiclet--article:hover {
            background-color: ${colors.foldedBg} !important;
            border-color: ${colors.blue} !important;
        }

        /* Buttons */
        .MuiButton-root,
        .MuiButtonBase-root {
            background-color: ${colors.blue} !important;
            color: ${colors.bg} !important;
        }

        .MuiButton-root:hover,
        .MuiButtonBase-root:hover {
            background-color: ${colors.magenta} !important;
            color: ${colors.bg} !important;
        }

        /* Typography */
        .MuiTypography-root,
        .MuiInputBase-root,
        .MuiFormLabel-root,
        .MuiScopedCssBaseline-root,
        label,
        span,
        p,
        h1, h2, h3, h4, h5, h6 {
            color: ${colors.fg} !important;
        }

        /* Okta-specific text elements */
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
        .support-text,
        .dropdown-menu--button-header,
        .dropdown-menu--button-sub {
            color: ${colors.fg} !important;
        }

        /* SVG icons */
        svg path, svg circle {
            fill: ${colors.fg} !important;
            stroke: ${colors.fg} !important;
        }

        /* Header menu items */
        .iframe-header-menu-item {
            color: ${colors.fg} !important;
            background-color: transparent !important;
        }

        .iframe-header-menu-item:hover,
        .iframe-header-menu-item.active {
            color: ${colors.blue} !important;
            background-color: ${colors.foldedBg} !important;
        }

        /* Search input */
        .MuiInputBase-input {
            background-color: ${colors.foldedBg} !important;
            color: ${colors.fg} !important;
        }

        /* Dropdown menus */
        .dropdown-menu--items {
            background-color: ${colors.foldedBg} !important;
            border-color: ${colors.uiBorder} !important;
        }

        .topbar--item {
            color: ${colors.fg} !important;
        }

        .topbar--item:hover {
            color: ${colors.blue} !important;
            background-color: ${colors.bg} !important;
        }

        /* Section headers */
        .section--collapse-arrow-icon path,
        .section--expand-arrow-icon path {
            fill: ${colors.fg} !important;
        }

        .section--collapse-arrow-icon circle,
        .section--expand-arrow-icon circle {
            stroke: ${colors.fg} !important;
        }

        /* Remove shadows */
        * {
            box-shadow: none !important;
        }

        /* Browser compatibility banner */
        .unsupported-browser-banner-wrap {
            background-color: ${colors.foldedBg} !important;
            border-color: ${colors.cyan2} !important;
            color: ${colors.fg} !important;
        }

        /* Special styled buttons */
        .MuiBox-root.qfchmkz-1ga44m7 {
            background-color: ${colors.blue8} !important;
            color: ${colors.bg} !important;
        }

        .MuiBox-root.qfchmkz-1ga44m7:hover {
            background-color: ${colors.magenta} !important;
        }

        /* Side navigation */
        .tb--sidenav-header {
            background: inherit !important;
        }

        .side-nav--container .side-nav {
            border-right: 5px solid rgba(0,0,0,.15) !important;
        }

        /* Footer links */
        .footer-link {
            color: ${colors.fg} !important;
        }

        .footer-link:hover {
            color: ${colors.blue} !important;
        }

        /* App card settings button */
        .chiclet--action {
            background-color: transparent !important;
        }

        .chiclet--action:hover {
            background-color: ${colors.foldedBg} !important;
        }

        .chiclet--action-kebab circle {
            fill: ${colors.gray6} !important;
        }

        /* Search icon */
        .MuiInputAdornment-root svg path {
            fill: ${colors.fg} !important;
        }

        /* Form labels */
        .MuiInputLabel-root {
            color: ${colors.fg} !important;
        }

        /* Section rename buttons */
        button[data-se="section-rename"] svg path {
            fill: ${colors.blue} !important;
            stroke: ${colors.blue} !important;
        }

        /* Tabs and navigation */
        .floating-header {
            background-color: ${colors.foldedBg} !important;
        }

        /* Override any white backgrounds */
        [style*="background-color: #ffffff"],
        [style*="background-color: white"],
        [style*="background: #ffffff"],
        [style*="background: white"] {
            background-color: ${colors.bg} !important;
        }

        /* Override any black text */
        [style*="color: #000000"],
        [style*="color: black"] {
            color: ${colors.fg} !important;
        }
    `;

    // Wait for DOM to be ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', function() {
            document.head.appendChild(style);
        });
    } else {
        document.head.appendChild(style);
    }

    // Also apply to dynamically loaded content
    const observer = new MutationObserver(function(mutations) {
        mutations.forEach(function(mutation) {
            mutation.addedNodes.forEach(function(node) {
                if (node.nodeType === 1) { // Element node
                    // Re-apply styles to new elements if needed
                    if (node.style && node.style.backgroundColor === '#ffffff') {
                        node.style.backgroundColor = colors.bg;
                    }
                    if (node.style && node.style.color === '#000000') {
                        node.style.color = colors.fg;
                    }
                }
            });
        });
    });

    observer.observe(document.body, {
        childList: true,
        subtree: true
    });
})();
