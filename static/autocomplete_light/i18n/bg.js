/*! Select2 4.0.13 | https://github.com/select2/select2/blob/master/LICENSE.md */
var dalLoadLanguage=function(n){var e;n&&n.fn&&n.fn.select2&&n.fn.select2.amd&&(e=n.fn.select2.amd),e.define("select2/i18n/bg",[],function(){return{inputTooLong:function(n){var e=n.input.length-n.maximum,t="Моля въведете с "+e+" по-малко символ";return 1<e&&(t+="a"),t},inputTooShort:function(n){var e=n.minimum-n.input.length,t="Моля въведете още "+e+" символ";return 1<e&&(t+="a"),t},loadingMore:function(){return"Зареждат се още…"},maximumSelected:function(n){var e="Можете да направите до "+n.maximum+" ";return 1<n.maximum?e+="избора":e+="избор",e},noResults:function(){return"Няма намерени съвпадения"},searching:function(){return"Търсене…"},removeAllItems:function(){return"Премахнете всички елементи"}}}),e.define,e.require},event=new CustomEvent("dal-language-loaded",{lang:"bg"});document.dispatchEvent(event);