const app = {
    buildForm() {
      return [
        $('#Datum/Tijd').val(),
        $('#Bericht').val(),
        $('#Prio').val(),
        $('#Voertuig').val(),
      ];
    },
    addRow(dataTable, data) {
      const addedRow = dataTable.row.add(data).draw();
      addedRow.show().draw(false);
  
      const addedRowNode = addedRow.node();
      console.log(addedRowNode);
      $(addedRowNode).addClass('highlight');
    },
    selectRow(dataTable) {
      if ($(this).hasClass('selected')) {
        $(this).removeClass('selected');
      } else {
        dataTable.$('tr.selected').removeClass('selected');
        $(this).addClass('selected');
      }
    },
    start() {
      const dataTable = $('#realtime').DataTable({
        data: dataSet,
        columns: [
          { title: 'Datum/Tijd' }, 
          { title: 'Bericht' },
          { title: 'Prio' },
          { title: 'Voertuig' },
        ]
      });
  
  
      // Pusher
      //var pusher = new Pusher('App Key', {
      //  cluster: 'CLUSTER',
      // encrypted: true
      //});
  
     // var channel = pusher.subscribe('records');
     // channel.bind('new-record', (data) => {
     //   this.addRow(dataTable, data);
      //});
    }
  };
  
  $(document).ready(() => app.start());