% training_file = "../../../../data/num_training_set_shuffled.csv";
% test_file = "../../../../data/testing_set.csv";

% SPECTF = csvread(training_file);
% labels = SPECTF(:, end);
% features = SPECTF(:, 1:end-1);
% features_sparse = sparse(features);
% libsvmwrite('SPECTFlibsvm.train', labels, features_sparse);

training_file = "to_convert.csv";

SPECTF = csvread(training_file);
labels = SPECTF(:, end);
features = SPECTF(:, 1:end-1);
features_sparse = sparse(features);
libsvmwrite('converted.train', labels, features_sparse);