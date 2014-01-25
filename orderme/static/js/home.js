$("#star").raty({
    size: 19,
    score: 3,
    starOn: "{{ static('img/vote/star-on.png') }}",
    starOff: "{{ static('img/vote/star-off.png') }}",
    starHalf: "{{ static('components/raty/lib/img/star-half.png') }}"
});