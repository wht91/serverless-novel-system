import csv
import tempfile
import os

def generate_csv():
    data = [
        ["Author Name", "Novel Type", "Novel Name", "About the Novel"],
        ["Thuwunna Bumi", "Romance", "The Beloved", "A heartwarming love story set in the enchanting countryside."],
        ["Kyaw Win Maung", "Thriller", "What If", "A gripping thriller that will keep you on the edge of your seat."],
        ["Journal Kyaw Ma Ma Lay", "Biography", "Chit Saar Zee Bwe", "The inspiring life story of a remarkable individual."],
        ["Mya Than Tint", "Classic", "The Wanderer", "A timeless classic that captures the essence of a bygone era."],
        ["Mya Than Tint", "Historical Fiction", "The Palace", "An enthralling tale of love, betrayal, and redemption set in a historical backdrop."],
        ["Bawa Thiri Maung", "Sci-Fi", "Through Space", "An imaginative science fiction novel that explores the mysteries of parallel worlds."],
        ["San Mon Aung", "Horror", "Shadow's Call", "A spine-chilling horror story that will send shivers down your spine."],
        ["Juu", "Fantasy", "Realm of Magic", "Immerse yourself in a captivating fantasy world filled with magical creatures and epic adventures."],
        ["Kyaw Myo Naing", "Mystery", "Hidden Secrets", "Unravel the secrets and solve the puzzles in this gripping mystery novel."],
        ["Bhin Khine", "Adventure", "Lost Treasure", "Join the fearless adventurers on a thrilling quest for hidden treasure."],
        ["Pandavaram", "Political Fiction", "Nation's Struggle", "A thought-provoking political fiction exploring the struggles of a nation."],
        ["Nu Nu Yi", "Literary Fiction", "The Forgotten One", "A beautifully crafted literary fiction that delves into themes of identity and memory."],
        ["Cho Cho Aye", "Satire", "The Jester", "A humorous and satirical take on society and its follies."],
        ["Wai Wai", "Historical Romance", "Love and Valor", "A sweeping historical romance that combines love and bravery in a tumultuous era."],
        ["Htin Lin", "Drama", "The Actor", "An introspective drama depicting the journey of an aspiring actor."],
        ["Mya Than Tint", "Poetry", "The Poet", "A collection of evocative poems that explore the depths of human emotions."],
        ["Mya Than Tint", "Social Commentary", "Voices of Society", "A powerful social commentary that sheds light on contemporary issues."],
        ["Khin Myo Chit", "Autobiography", "Unforgettable Journey", "An inspiring autobiography chronicling a remarkable life journey."],
        ["Shwe Oo Daung", "Family Saga", "Legacy of the Family", "A sweeping family saga spanning generations and exploring the bonds of kinship."]
    ]

    with tempfile.NamedTemporaryFile(mode='w', delete=False, encoding='utf-8', newline='') as temp_file:
        writer = csv.writer(temp_file)
        writer.writerows(data)

        # Get the path of the temporary file
        temp_file_path = temp_file.name

    return temp_file_path

def lambda_handler(event, context):
    csv_file_path = generate_csv()

    with open(csv_file_path, 'rb') as file:
        csv_data = file.read()

    os.remove(csv_file_path)  # Remove the temporary file

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/csv',
            'Content-Disposition': 'attachment; filename=novels.csv'
        },
        'body': csv_data
    }
