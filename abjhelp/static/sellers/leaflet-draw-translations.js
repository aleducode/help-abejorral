
let leafletDrawTranslations = {
  // format: {
  // 	numeric: {
  // 		delimiters: {
  // 			thousands: ',',
  // 			decimal: '.'
  // 		}
  // 	}
  // },
  draw: {
    toolbar: {
      // #TODO: this should be reorganized where actions are nested in actions
      // ex: actions.undo  or actions.cancel
      actions: {
        title: 'Cancelar dibujo',
        text: 'Cancelar'
      },
      finish: {
        title: 'Finalizar dibujo',
        text: 'Finalizar'
      },
      undo: {
        title: 'Eliminar el último punto dibujado',
        text: 'Eliminar último punto'
      },
      buttons: {
        polyline: 'Dibujar una línea',
        polygon: 'Dibujar un polígono',
        rectangle: 'Dibujar un rectángulo',
        circle: 'Dibujar un círculo',
        marker: 'Dibujar un marcador',
        circlemarker: 'Dibujar un marcador circular'
      }
    },
    handlers: {
      circle: {
        tooltip: {
          start: 'Haga clic y arrastrar para dibujar un círculo.'
        },
        radius: 'Radio'
      },
      circlemarker: {
        tooltip: {
          start: 'Haga clic en el mapa para colocar el marcador de círculo.'
        }
      },
      marker: {
        tooltip: {
          start: 'Haga clic en el mapa para colocar un marcador.'
        }
      },
      polygon: {
        tooltip: {
          start: 'Haga clic para empezar a dibujar la figura.',
          cont: 'Haga clic para continuar a dibujar la figura.',
          end: 'Haga clic en el primer punto para cerrar esta forma.'
        }
      },
      polyline: {
        error: '<strong>Error:</strong> shape edges cannot cross!',
        tooltip: {
          start: 'Click to start drawing line.',
          cont: 'Click to continue drawing line.',
          end: 'Click last point to finish line.'
        }
      },
      rectangle: {
        tooltip: {
          start: 'Click and drag to draw rectangle.'
        }
      },
      simpleshape: {
        tooltip: {
          end: 'Suelta el mouse para finalizar de dibujar.'
        }
      }
    }
  },
  edit: {
    toolbar: {
      actions: {
        save: {
          title: 'Guardar cambios.',
          text: 'Guardar'
        },
        cancel: {
          title: 'Cancelar la edición, descarta todos los cambios\n.',
          text: 'Cancelar'
        },
        clearAll: {
          title: 'Limpiar todos los layers.',
          text: 'Limpiar todo'
        }
      },
      buttons: {
        edit: 'Editar.',
        editDisabled: 'No layers to edit.',
        remove: 'Eliminar todo.',
        removeDisabled: 'No layers to delete.'
      }
    },
    handlers: {
      edit: {
        tooltip: {
          text: 'Arrastre las figuras o el marcador para editar la figura.',
          subtext: 'Haga clic en cancelar para deshacer cambios.'
        }
      },
      remove: {
        tooltip: {
          text: 'Click on a feature to remove'
        }
      }
    }
  }
}