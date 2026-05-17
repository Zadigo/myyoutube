package s3storage

import (
	"bytes"
	"context"
	"fmt"

	"github.com/aws/aws-sdk-go-v2/aws"
	"github.com/aws/aws-sdk-go-v2/config"
	"github.com/aws/aws-sdk-go-v2/credentials"
	"github.com/aws/aws-sdk-go-v2/service/s3"
)

type S3Storage struct {
	Client     *s3.Client
	BucketName string
}

func (s *S3Storage) CreateStorage(bucket, region, accessKey, secretKey string) (*S3Storage, error) {
	config, err := config.LoadDefaultConfig(
		context.TODO(),
		config.WithRegion("region"),
		config.WithCredentialsProvider(credentials.NewStaticCredentialsProvider(accessKey, secretKey, "")),
	)

	if err != nil {
		return nil, fmt.Errorf("failed to load config: %w", err)
	}

	return &S3Storage{
		Client:     s3.NewFromConfig(config),
		BucketName: bucket,
	}, nil
}

func (s *S3Storage) UploadFile(ctx context.Context, file []byte, filename, contentType string) (string, error) {
	_, err := s.Client.PutObject(ctx, &s3.PutObjectInput{
		Bucket:      aws.String(s.BucketName),
		Key:         aws.String(filename),
		Body:        bytes.NewReader(file),
		ContentType: aws.String(contentType),
	})

	if err != nil {
		return "", fmt.Errorf("failed to upload file: %w", err)
	}

	url := fmt.Sprintf("https://%s.s3.amazonaws.com/%s", s.BucketName, filename)
	return url, nil
}

func (s *S3Storage) UploadImage(imageBytes []byte, filename, contentType string) (string, error) {
	url, err := s.UploadFile(context.Background(), imageBytes, "myfolder/photo.jpg", "image/jpeg")
	if err != nil {
		return "", err
	} else {
		return url, nil
	}
}

func (s *S3Storage) UploadVideo(videoBytes []byte, filename, contentType string) (string, error) {
	url, err := s.UploadFile(context.Background(), videoBytes, "myfolder/video.mp4", "video/mp4")
	if err != nil {
		return "", err
	} else {
		return url, nil
	}
}

// func (s *S3Storage) MultiPartUpload(fileBytes []byte, filename, contentType string) (string, error) {
// 	uploader := manager.NewUploader(s.Client)
// 	_, err := uploader.Upload(context.Background(), &s3.PutObjectInput{
// 		Bucket:      aws.String(s.BucketName),
// 		Key:         aws.String(filename),
// 		Body:        bytes.NewReader(fileBytes),
// 		ContentType: aws.String(contentType),
// 	})

// 	if err != nil {
// 		return "", err
// 	}
// }

func NewS3Storage() *S3Storage {
	return &S3Storage{}
}
