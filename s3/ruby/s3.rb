require 'aws-sdk-s3'
require 'pry'
require 'nokogiri'
require 'securerandom'

bucket_name = ENV['BUCKET_NAME'] || "aws-examples-#{SecureRandom.hex(4)}"
region = 'ca-central-1'

client = Aws::S3::Client.new(region: region)
s3 = Aws::S3::Resource.new(client: client)

resp = client.create_bucket(
  bucket: bucket_name,
  create_bucket_configuration: {
    location_constraint: region
  }
)

number_of_files = 1 + rand(6)
puts "number_of_files: #{number_of_files}"

number_of_files.times.each do |i|
  puts "i: #{i}"
  filename = "file_#{i}.txt"
  output_path = "/tmp/#{filename}"
  File.open(output_path, 'w') do |f|
    f.write SecureRandom.uuid
  end
  File.open(output_path, 'rb') do |f|
    s3.bucket(bucket_name).object(filename).put(body: f)
  end
end
