// ==UserScript==
// @name        SIC CMS Custom CSS
// @namespace   https://cms.sic.saarland
// @description Custom CSS for the SIC CMS to make it Solarized dark
// @include     *cms.sic.saarland/*
// @run-at      document-start
// @version     1
// @author      Immanuel Haffner
// ==/UserScript==

(function IIFE() {
    'use strict';

    document.addEventListener('readystatechange', function onReadyStateChange() {
        if (document.readyState == 'interactive') {
            const style = document.createElement('style');
            document.head.appendChild(style);
            style.innerHTML = `

:root {
    /* Solarized colors */
    --base03:    #002b36;
    --base02:    #073642;
    --base01:    #586e75;
    --base00:    #657b83;
    --base0:     #839496;
    --base1:     #93a1a1;
    --base2:     #eee8d5;
    --base3:     #fdf6e3;
    --yellow:    #b58900;
    --orange:    #cb4b16;
    --red:       #dc322f;
    --magenta:   #d33682;
    --violet:    #6c71c4;
    --blue:      #268bd2;
    --cyan:      #2aa198;
    --green:     #859900;
}

body
{
    background-color: var(--base03) !important;
}

.container
{
    color: var(--base1);
}

h1 small, h2 small, h3 small, h4 small, h5 small, h6 small
{
    color: var(--base0);
}

a, a:hover
{
    color: var(--blue);
}

.label, .badge
{
    background-color: var(--base00);
    color: var(--base2);
}

.btn, .btn:hover
{
    background-color: var(--base1);
    color: var(--base02);
    background-image: unset;
    border-style: none !important;
    border-image: unset;
    text-shadow: none;
}

.btn-success, .btn-success:hover
{
    background-color: var(--green);
    color: var(--base03);
}

.site-logo img
{
    display: none;
}

.table-striped tbody>tr:nth-child(odd)>td, .table-striped tbody>tr:nth-child(odd)>th
{
    background-color: var(--base03) !important;
}

pre
{
    background-color: var(--base02);
}

code, pre
{
    color: var(--base1);
}

textarea, input[type="text"], input[type="password"], input[type="datetime"], input[type="datetime-local"],
input[type="date"], input[type="month"], input[type="time"], input[type="week"], input[type="number"],
input[type="email"], input[type="url"], input[type="search"], input[type="tel"], input[type="color"], .uneditable-input
{
    background-color: var(--base01);
    color: var(--base2);
}

.dropdown-menu
{
    background-color: var(--base02);
}

.dropdown-menu>li>a
{
    color: var(--base1);
}

.dropdown-menu .divider
{
    background-color: var(--base1);
    border: none;
}

.modal
{
    background-color: var(--base03);
}

.modal-footer
{
    background-color: var(--base03);
    border-top: none;
}

.modal-header
{
    border-bottom: none;
}

.table th, .table td
{
    border-top: 1px solid var(--base00);
}

.cke_editable
{
    color: var(--base2);
}

            `;

            document.querySelectorAll('.icon-white').forEach(function (el) {
                el.classList.remove('icon-white');
            });
        }
    });
})();
