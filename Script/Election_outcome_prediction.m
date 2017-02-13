%% Loading and initializing the data
[target_variables, target_names, data, feature_names] = ...
    load_HS_vaalikone('data_vk_training.csv');
[int_variables, classes1, classes2] = struct2int(target_variables);

%% Loading test data
[test_variables, test_data] = ...
    load_test_data('test-data.csv');
[test_int_variables, test_classes1, test_classes2] = struct2int(test_variables);

%% Classifying election results
% Running some functions here to get some results...
[ pijs, p_r, w0, w ] = parameters( data(1:500,:), int_variables(1:500,1), size(classes1,1) );
TE1 = classification_error( data(1:500,:), int_variables(1:500,1), w, w0 );
VE1 = classification_error( data(501:1037,:), int_variables(501:1037,1), w, w0 );
predictions = prediction( data(501:1037,:), w, w0 );
results = evaluation(predictions,int_variables(501:1037,1));

%% LDA for election results
truth = test_int_variables(:,1);
sel_feat_ind = [1:size(data,2)];
election_predictions = LDA_predict(data, int_variables(:,1), sel_feat_ind, test_data);
results = evaluation(election_predictions,truth);
score = sum(results{2}(1,1));

%% Feature selection for election outcomes:
scores = zeros(size(data,2),1);
for i =1:199
    truth = int_variables(:,1);
    [ pijs, p_r, w0, w ] = parameters( [data(1:500,i)], int_variables(1:500,1), size(classes1,1) );
    predictions = prediction( [data(501:1037,i)], w, w0 );
    results = evaluation(predictions,truth(501:1037));
    scores(i) = sum(results{2}(1,1));
end

[best, best_index] = max(scores)

for i =1:199
    truth = int_variables(:,1);
    [ pijs, p_r, w0, w ] = parameters( [data(1:500,i), data(1:500,best_index)], int_variables(1:500,1), size(classes1,1) );
    predictions = prediction( [data(501:1037,i), data(501:1037,best_index)], w, w0 );
    results = evaluation(predictions,truth(501:1037));
    scores(i) = sum(results{2}(1,1));
end

[second, second_index] = max(scores)
%% Forward loop for election results
data2 = data;
feature_names2 = feature_names;
scores = zeros(size(data2,2),1);
for i =1:199
    truth = int_variables(:,1);
    [ pijs, p_r, w0, w ] = parameters( [data2(1:500,i)], int_variables(1:500,1), size(classes1,1) );
    predictions = prediction( [data2(501:1037,i)], w, w0 );
    results = evaluation(predictions,truth(501:1037));
    scores(i) = sum(results{2}(1,1));
end
[best, best_index] = max(scores);
selected_features = data2(:,best_index);
selected_feature_names = feature_names2(1,best_index);
data2(:,best_index)= [];
feature_names2(best_index) = [];

for k=1:1
    scores = zeros(size(data2,2),1);
    for i =1:size(data2,2)
        truth = int_variables(:,1);
        [ pijs, p_r, w0, w ] = parameters( [data2(1:500,i), selected_features(1:500,:)], int_variables(1:500,1), size(classes1,1) );
        predictions = prediction( [data2(501:1037,i), selected_features(501:1037,:)], w, w0 );
        results = evaluation(predictions,truth(501:1037));
        scores(i) = sum(results{2}(1,1));
    end
    [best, best_index] = max(scores);
    selected_features = [selected_features, data2(:,best_index)];
    selected_feature_names = [selected_feature_names, feature_names2(1,best_index)];
    data2(:,best_index)= [];
    feature_names2(best_index) = [];
end

% Finding the feature indexes
N = length(selected_feature_names);
sel_feat_ind = zeros(1,N);
for j=1:N
    ind = strfind(feature_names, selected_feature_names{j});
    for i=1:size(ind,2)
        if(ind{i} == 1)
            sel_feat_ind(j)=i; 
        end;
    end;
end
    
% Computing the test F-score for election results

truth = test_int_variables(:,1);
[ pijs, p_r, w0, w ] = parameters( [selected_features], int_variables(1:1037,1), size(classes1,1) );
predictions = prediction( test_data(:,sel_feat_ind), w, w0 );
results = evaluation(predictions,truth);
test_score = results{2}(1,1);

%% Gradient Ascent for election outcomes
[w1 f1] = gradascent(data(1:500,1:30), int_variables(1:500,1), rand(30,1), 0.01);
[w2 f2] = gradascent(data(1:500,31:60), int_variables(1:500,1), rand(30,1), 0.01, 'verbose');
[w3 f3] = gradascent(data(1:500,61:90), int_variables(1:500,1), rand(30,1), 0.01);
[w4 f4] = gradascent(data(1:500,91:120), int_variables(1:500,1), rand(30,1), 0.01);
[w5 f5] = gradascent(data(1:500,121:150), int_variables(1:500,1), rand(30,1), 0.01);
[w6 f6] = gradascent(data(1:500,151:180), int_variables(1:500,1), rand(30,1), 0.01);
[w7 f7] = gradascent(data(1:500,181:199), int_variables(1:500,1), rand(19,1), 0.01);

C = cov(data);
[V,D] = eig(C);
Z = data*V;
Z = fliplr(Z);
[wPCA fPCA] = gradascent(Z(1:500,1:40), int_variables(1:500,1), rand(30,1), 0.01);
