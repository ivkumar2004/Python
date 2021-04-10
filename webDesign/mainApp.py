import os
import web

render = web.template.render('templates/')

urls = (
    '/', 'Index',
    '/award_month', 'AwardMonth'
)
app = web.application(urls, globals())


class Index:
    def GET(self):
        return render.indexcalendar()


class AwardMonth:
    def GET(self):
        data_str = web.input()
        file_data = {}
        award_month = data_str.awardmonth.replace(" ", "").replace("-", "")
        is_folder = self.validate_month_folder(award_month)
        base_folder = ""
        if is_folder:
            base_folder = os.path.join('static', award_month)
            file_data = self.read_folder_data(base_folder)
        file_data["Lightbox"] = self.map_image('static', file_data.keys())
        print(award_month, base_folder, is_folder, file_data)

        return render.slideshow(file_data)

    @staticmethod
    def validate_month_folder(award_month):
        if not os.path.isdir('static'):
            return False
        base_folder = os.path.join('static', award_month)
        if not os.path.isdir(base_folder):
            return False
        return True

    @staticmethod
    def read_folder_data(base_folder):
        file_data = {}
        for root, dirs, files in os.walk(base_folder):
            for name in files:
                temp_file = os.path.join(root, name)
                print(temp_file)
                file_array = temp_file.split("\\")
                print(file_array)
                tmp_key = "other"
                if file_array[-2] in file_data:
                    tmp_key = file_array[-2]
                file_data[tmp_key].append(temp_file)
            for name in dirs:
                print(os.path.join(root, name))
                file_data[name] = []
        return file_data

    @staticmethod
    def map_image(base_folder, file_list):
        mapping_dict = {}
        for file_name in file_list:
            if os.path.exists(os.path.join(base_folder, file_name+".jpg")):
                mapping_dict[file_name] = os.path.join(base_folder, file_name+".jpg")
            else:
                mapping_dict[file_name] = os.path.join(base_folder, "Other.jpg")
        print("Mapping Dict", mapping_dict)
        return mapping_dict


if __name__ == "__main__":
    app.run()
