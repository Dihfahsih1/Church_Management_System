/*! Select2 4.0.13 | https://github.com/select2/select2/blob/master/LICENSE.md */
var dalLoadLanguage=function(e){var n;e&&e.fn&&e.fn.select2&&e.fn.select2.amd&&(n=e.fn.select2.amd),n.define("select2/i18n/lv",[],function(){function u(e,n,t,u){return 11===e?n:e%10==1?t:u}return{inputTooLong:function(e){var n=e.input.length-e.maximum,t="Lūdzu ievadiet par  "+n;return(t+=" simbol"+u(n,"iem","u","iem"))+" mazāk"},inputTooShort:function(e){var n=e.minimum-e.input.length;return"Lūdzu ievadiet vēl "+n+(" simbol"+u(n,"us","u","us"))},loadingMore:function(){return"Datu ielāde…"},maximumSelected:function(e){return"Jūs varat izvēlēties ne vairāk kā "+e.maximum+(" element"+u(e.maximum,"us","u","us"))},noResults:function(){return"Sakritību nav"},searching:function(){return"Meklēšana…"},removeAllItems:function(){return"Noņemt visus vienumus"}}}),n.define,n.require},event=new CustomEvent("dal-language-loaded",{lang:"lv"});document.dispatchEvent(event);