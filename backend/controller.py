
def add_annotation(topic_id, data):
    """
    puts a new annotation in the database
    
    data fields:
        start_index
        end_index
        start_paragraph
        end_paragraph
        text
    """
    Annotation.create(
                parent=topic_id,
                start_index=data['start_index'],
                end_index=data['end_index'],
                start_paragraph=data['start_paragraph'],
                end_paragraph=data['end_paragraph'],
                body=data['text']
    )


def add_comment(annotation_id, text):
    Comment.create(parent=annotation_id, body=text)

def get_topics():
    return [{'title': t.title, 'id' t.id} for t in Topic.select()]
