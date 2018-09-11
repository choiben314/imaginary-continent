training_file = "primary.csv";
test_file = "primary_test.csv";
% test_file = "../../../../data/testing_set.csv";

M = csvread(training_file);
% Test_M = csvread(test_file);

M = M(randperm(size(M, 1)), :);

test_size = 10;

idx = 1 + size(M, 1) - test_size;

X = M(1:idx, 1:end);
y = M(1:idx, end);

% training_labels = y(1:10000, :);
% training_set = X(1:10000, :);

% testing_labels = y(10001:end, :);
% testing_set = X(10001:end, :);

training_labels = y;
training_set = X;

testing_set = M(idx:end, 1:end);
testing_labels = M(idx:end, end);

model = svmtrain(training_labels, training_set, [, '-c 0.1 -g 70']);

[predicted_label, accuracy, prob_estimates] = svmpredict(testing_labels, testing_set, model);
disp("-----Predicted Labels-----");
disp(predicted_label);
disp("-----Original Labels-----");
disp(testing_labels);
disp("-----Accuracy-----");
disp(accuracy);

