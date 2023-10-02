function join_the_soviet_union() {
    document.getElementById('main-logo').scrollIntoView(scrollIntoViewOptions="smooth");
    let bounce_interval = 0;
    let bounce_value = 1;
    let bounce_max = 1.2;
    let bounce_direction = 1;
    let bounce_element_on = 1;
    let bounce_element_1 = document.getElementById("wl-email");
    let bounce_element_2 = document.getElementById("wl-submit");

    bounce_interval = setInterval(() => {
        if (bounce_element_on == 1) {
            if (bounce_direction == 1) {
                bounce_value += 0.04;
                if (bounce_value >= bounce_max) {
                    bounce_direction = -1;
                }
            } else if (bounce_direction == -1) {
                bounce_value -= 0.04;
                if (bounce_value <= 1) {
                    bounce_direction = 1;
                    bounce_element_on = 2;
                }
            }
            bounce_element_1.style.transform = "scale(" + bounce_value + ")";
        }
        if (bounce_element_on == 2) {
            if (bounce_direction == 1) {
                bounce_value += 0.04;
                if (bounce_value >= bounce_max) {
                    bounce_direction = -1;
                }
            } else if (bounce_direction == -1) {
                bounce_value -= 0.04;
                if (bounce_value <= 1) {
                    clearInterval(bounce_interval);
                }
            }
            bounce_element_2.style.transform = "scale(" + bounce_value + ")";
        }
    }, 40);
}