training_file = "primary.csv";
test_file = "primary_test.csv";
% test_file = "../../../../data/testing_set.csv";

M = csvread(training_file);
% Test_M = csvread(test_file);

M = M(randperm(size(M, 1)), :);

test_size = 1000;

idx = 1 + size(M, 1) - test_size;

X = M(1:idx, 1:end - 1);
y = M(1:idx, end);

% training_labels = y(1:10000, :);
% training_set = X(1:10000, :);

% testing_labels = y(10001:end, :);
% testing_set = X(10001:end, :);

training_labels = y;
training_set = X;

testing_set = M(idx:end, 1:end - 1);
testing_labels = M(idx:end, end);
% testing_set = M(1:test_size, 1:end - 1);
% testing_labels = M(1:test_size, end)

% highest = 0;
% best_c = -8;
% best_g = -8;

% for c = -8:8
% 	for g = -8:8
% 		lib_opt = sprintf('-c %f -g %f', 3.162^-c, 3.162^-g)
% 		model = svmtrain(training_labels, training_set, [, lib_opt]);
% 		[predicted_label, accuracy, prob_estimates] = svmpredict(testing_labels, testing_set, model);
% 		if accuracy(1) > highest
% 			highest = accuracy(1);
% 			best_c = c;
% 			best_g = g;
% 		disp(best_c);
% 		disp(best_g);
% 		disp(accuracy(1));
% 		end
% 	end
% end

model = svmtrain(training_labels, training_set, [, '-c 3.0 -g 70.0']);

[predicted_label, accuracy, prob_estimates] = svmpredict(testing_labels, testing_set, model);

% disp("~~~~~~~~best c value~~~~~~~~")
% disp(best_c)
% disp("~~~~~~~~best g value~~~~~~~~")
% disp(best_g)
% disp("~~~~~~~~best accuracy~~~~~~~~")
% disp(highest)

disp("-----Predicted Labels-----");
%disp(predicted_label);
disp("-----Original Labels-----");
%disp(testing_labels);
disp("-----Accuracy-----");
disp(accuracy);

