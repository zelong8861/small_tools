                    <script type="text/javascript">
                        function key_up() {
                            var old_value = $('#id_search_input').val();
                            setTimeout(function () {
                                var new_value = $('#id_search_input').val();
                                if (old_value == new_value) {
                                    document.search_form.submit();
                                }
                            }, 1500);
                        }
                    </script>
