/** A besoin des variables suivantes :
 * content_rul : contient l'url du content de la leçon
 * update_content_url : contient l'url de la vue d'update de la leçon
 * empty_content_message : contient le message à afficher si le content est vide
 * ! PAREIL pour `toc` et `remark` à la place de `content` !
 */
jQuery(document).ready(function() {
    /* VARIABLES */
    var edit_class = 'glyphicon-pencil';
    var confirm_class = 'glyphicon-ok';
    var lesson_button = $('#lesson_button');
    var remarks_button = $('#remarks_button');
    var lesson_div = $('#lesson');
    var toc_div = $('#toc');
    var remarks_div = $('#remarks');
    /* EVENT */
    lesson_button.on('click', content_update_view);
    remarks_button.on('click', remarks_update_view);
    /* FONCTIONS */
    // Permet de raffraichir un champ, étant donné :
    // thing_url : l'url contenant le contenu
    // thing_div : le div où le mettre
    // empty_... : le truc à dire si on a un contenu vide
    function get_thing(thing_url, thing_div, empty_thing_message) {
        $.get(thing_url, function(data) {
                if(jQuery.trim(data).length==0) {
                    thing_div.html(empty_thing_message);
                } else {
                    thing_div.html(data);
                }
            });
    }
    // fonction de raffraichissement du contenu
    function get_content() { get_thing(content_url, lesson_div, empty_content_message);}
    // fonction de raffraichissement du toc
    function get_toc() { get_thing(toc_url, toc_div, empty_toc_message);}
    // fonction de raffraichissement du contenu de la leçon et de son toc
    function get_lesson() { get_toc(); get_content();}
    function get_remarks() {get_thing(remarks_url, remarks_div, empty_remarks_message);}
    // Pour changer le content
    function content_update_view() {
        if(lesson_button.hasClass(edit_class)) {
            lesson_div.load(update_content_url);
            //$('id_content').textareaAutoSize();  N'a pas l'air de fonctionne :(
        } else {
                var csrf_value  = $('#content-form').find('[name=csrfmiddlewaretoken]').val();
                var content_value = $('#id_content').val();
                $.post(
                        update_content_url,
                        {   content : content_value,
                            csrfmiddlewaretoken : csrf_value
                        },
                        function() {
                            get_lesson();
                        });
        }
        lesson_button.toggleClass(edit_class);
        lesson_button.toggleClass(confirm_class);
    }
    // Pour changer les remarks
    function remarks_update_view() {
        if(remarks_button.hasClass(edit_class)) {
            remarks_div.load(update_remarks_url);
        } else {
                var csrf_value  = $('#remarks-form').find('[name=csrfmiddlewaretoken]').val();
                var remarks_value = $('#id_remarks').val();
                $.post(
                        update_remarks_url,
                        {   remarks : remarks_value,
                            csrfmiddlewaretoken : csrf_value
                        },
                        function() {
                            get_remarks();
                        });
        }
        remarks_button.toggleClass(edit_class);
        remarks_button.toggleClass(confirm_class);
    }
    // On initialise
    get_lesson();
    get_remarks();
    lesson_button.addClass(edit_class);
    remarks_button.addClass(edit_class);
});
