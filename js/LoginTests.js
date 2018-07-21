
function testLabelFieldGrouping(form) {
    var labels = form.querySelectorAll('label');
    var inputs = form.querySelectorAll('input');
    if(labels.len != inputs.len) {
        console.log('[warning]', 'number of labels doesn\'t match number of inputs')
    }
    for(var i=0; i < inputs.length && i < labels.length; i++) {
        const inputStyle = getComputedStyle(inputs[i])
        const labelStyle = getComputedStyle(labels[i])
        console.log('INPUT')
        console.log('offset Left & Top', inputs[i]['offsetLeft'], inputs[i]['offsetTop'])
        console.log('width & height', inputStyle['width'], inputStyle['height'])
        console.log('LABEL')
        console.log('offset Left & Top', labels[i]['offsetLeft'], labels[i]['offsetTop'])
        console.log('width & height', labelStyle['width'], labelStyle['height'])
        console.log('\n\n')
    }
}


// L1 Present fields in a single column layout.

module.exports = {
    testLabelFieldGrouping: testLabelFieldGrouping
}