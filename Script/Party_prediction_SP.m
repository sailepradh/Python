%% Loading and initializing the data
[target_variables, target_names, data, feature_names] = ...
    load_HS_vaalikone('data_vk_training.csv');
[int_variables, classes1, classes2] = struct2int(target_variables);

%% Loading test data
[test_variables, test_data] = ...
    load_test_data('test-data.csv');
[test_int_variables, test_classes1, test_classes2] = struct2int(test_variables);

%% Some Naive Bayes calculations:

%% Feature selection with Naive Bayes:
data2 = data;
feature_names2 = feature_names;
scores = zeros(size(data2,2),1);
for i =1:199
    truth = int_variables(:,2);
    [ pijs, p_r, w0, w ] = parameters( [data2(1:400,i)], int_variables(1:400,2), size(classes2,1) );
    party_predictions = prediction( [data2(401:800,i)], w, w0 );
    results = evaluation(party_predictions,truth(401:800));
    scores(i) = sum(results{2}(1,1));
end
[best, best_index] = max(scores);
selected_features = data2(:,best_index);
selected_feature_names = feature_names2(1,best_index);
data2(:,best_index)= [];
feature_names2(best_index) = [];

for k=1:99
    scores = zeros(size(data2,2),1);
    for i =1:size(data2,2)
        truth = int_variables(:,2);
        [ pijs, p_r, w0, w ] = parameters( [data2(1:400,i), selected_features(1:400,:)], int_variables(1:400,2), size(classes2,1) );
        party_predictions = prediction( [data2(401:800,i), selected_features(401:800,:)], w, w0 );
        results = evaluation(party_predictions,truth(401:800));
        scores(i) = sum(results{2}(1,1));
    end
    [best, best_index] = max(scores);
    selected_features = [selected_features, data2(:,best_index)];
    selected_feature_names = [selected_feature_names, feature_names2(1,best_index)];
    data2(:,best_index)= [];
    feature_names2(best_index) = [];
end

%% Backward selection for Naive Bayes
truth = int_variables(:,2);
selected_features;
[ pijs, p_r, w0, w ] = parameters( selected_features(1:400,:), int_variables(1:400,2), size(classes2,1) );
party_predictions = prediction( selected_features(401:800,:), w, w0 );
results = evaluation(party_predictions,truth(401:800));
score = sum(results{2}(1,1));

for k=1:99
    scores = zeros(size(selected_features,2),1);
    for i =1:size(selected_features,2)
        truth = int_variables(:,2);
        temp = selected_features;
        temp(:,i) = [];
        [ pijs, p_r, w0, w ] = parameters( temp(1:400,:), int_variables(1:400,2), size(classes2,1) );
        party_predictions = prediction( temp(401:800,:), w, w0 );
        results = evaluation(party_predictions,truth(401:800));
        scores(i) = sum(results{2}(1,1));
    end
    if score > max(scores)
        break
    end
    [score, worst_index] = max(scores); %The variable, removal of which maximizes the score
    selected_features(:,worst_index) = [];
    selected_feature_names(worst_index) = [];
end

%% Naive Bayes
sel_feat_ind = selected_feature_indexes( selected_feature_names, feature_names );

%% Computing the test F-score for parties of the rest of the test data using the selected features
truth =  int_variables(:,2);
[pijs, p_r, w0, w ] = parameters([selected_features(1:800,:)], int_variables(1:800,2), size(classes2,1) );
predictions = prediction(data([801:1037],[sel_feat_ind]), w, w0 );
results = evaluation(predictions,truth(801:1037));
test_score = results{2}(1,1);

%% Computing the test F-score for parties (Naive Bayes)
truth = test_int_variables(:,2);
[ pijs, p_r, w0, w ] = parameters( [selected_features], int_variables(1:1037,2), size(classes2,1) );
party_predictions = prediction( test_data(:,sel_feat_ind), w, w0 );
results = evaluation(party_predictions,truth);
test_score = results{2}(1,1);



%% Plot the F-score with different collections of variables (Naive Bayes)

truth = test_int_variables(:,2);
N = size(selected_features, 2);
test_scores = zeros(N);
for i=1:N
    [ pijs, p_r, w0, w ] = parameters( selected_features(:,1:i), int_variables(1:1037,2), size(classes2,1) );
    party_predictions = prediction( test_data(:,sel_feat_ind(1:i)), w, w0 );
    results = evaluation(party_predictions,truth);
    test_scores(i) = results{2}(1,1);
end
plot([1:N],test_scores)
hold
for i=1:N
    [ pijs, p_r, w0, w ] = parameters( selected_features(1:500,1:i), int_variables(1:500,2), size(classes2,1) );
    party_predictions = prediction( selected_features(501:650,1:i), w, w0 );
    results = evaluation(party_predictions,int_variables(501:650,2));
    test_scores(i) = results{2}(1,1);
end
plot([1:N],test_scores)

for i=1:N
    [ pijs, p_r, w0, w ] = parameters( selected_features(1:650,1:i), int_variables(1:650,2), size(classes2,1) );
    party_predictions = prediction( selected_features(651:800,1:i), w, w0 );
    results = evaluation(party_predictions,int_variables(651:800,2));
    test_scores(i) = results{2}(1,1);
end
plot([1:N],test_scores)

plot([1:N],0.3)

%% LDA stuff below

%% Forward selection with LDA: (TAKES TIME!)
data2 = data;
feature_names2 = feature_names;
selected_feature_names = [];
scores = zeros(size(data2,2),1);
for i =1:199
    truth = int_variables(:,2);
    sel_feat_ind = selected_feature_indexes( [selected_feature_names feature_names2(1,i)], feature_names );
    party_predictions = LDA_predict(data2(1:500,:), int_variables(1:500,2), sel_feat_ind, data2(501:650,:));
    results = evaluation(party_predictions,truth(501:650));
    scores(i) = sum(results{2}(1,1));
end
[best, best_index] = max(scores);
selected_features = data2(:,best_index);
selected_feature_names = feature_names2(1,best_index);
data2(:,best_index)= [];
feature_names2(best_index) = [];

for k=1:150
    scores = zeros(size(data2,2),1);
    tic
    for i =1:size(data2,2)
        truth = int_variables(:,2);
        sel_feat_ind = selected_feature_indexes( [selected_feature_names feature_names2(1,i)], feature_names );
        party_predictions = LDA_predict(data(1:500,:), int_variables(1:500,2), sel_feat_ind, data(501:1037,:));
        results = evaluation(party_predictions,truth(501:1037));
        scores(i) = sum(results{2}(1,1));
    end
    toc
    [best, best_index] = max(scores);
    selected_features = [selected_features, data2(:,best_index)];
    selected_feature_names = [selected_feature_names, feature_names2(1,best_index)];
    data2(:,best_index)= [];
    feature_names2(best_index) = [];
end

%% Backward selection for LDA
truth = int_variables(:,2);
selected_features = data;
sel_feat_ind = [1:size(data,2)];
removed_ind = zeros(size(data,2));
% Initial score for comparing:
party_predictions = LDA_predict(data(1:400,:), int_variables(1:400,2), sel_feat_ind, data(401:800,:));
results = evaluation(party_predictions,truth(401:800));
score = sum(results{2}(1,1))
% 
for k=1:120
    scores = zeros(size(selected_features,2),1);
    for i =1:size(sel_feat_ind,2)
        truth = int_variables(:,2);
        temp = sel_feat_ind;
        temp(:,i) = [];
        party_predictions = LDA_predict(data(1:400,:),int_variables(1:400,2),temp, data(401:800,:));
        results = evaluation(party_predictions,truth(401:800));
        scores(i) = sum(results{2}(1,1));
    end
    if score > max(scores)
        k
    end
    [score, worst_index] = max(scores); %The variable, removal of which maximizes the score
    removed_ind(k) = sel_feat_ind(:,worst_index);
    sel_feat_ind(:,worst_index) = [];
    %selected_features(:,worst_index) = [];
    %selected_feature_names(worst_index) = [];
    score
end


%% Print LDA test score

%sel_feat_ind = [1:size(data,2)];
%sel_feat_ind = selected_feature_indexes( selected_feature_names, feature_names );
% Computing the test F-score for parties

truth = test_int_variables(:,2);
party_predictions = LDA_predict(data(1:1037,:), int_variables(1:1037,2), sel_feat_ind, test_data(:,:));
results = evaluation(party_predictions,truth);
test_score = results{2}(1,1)


%% Plot the F-score with different collections of variables (LDA)

truth = int_variables(800:1037,2);
N = size(selected_features, 2);
test_scores = zeros(N);
for i=1:N
    sel_feat_ind = [1:size(data,2)];
    sel_feat_ind(removed_ind(1:i)) = [];
    party_predictions = LDA_predict(data(1:800,:), int_variables(1:800,2), sel_feat_ind, data(801:1037,:));
    results = evaluation(party_predictions,truth);
    test_scores(i) = results{2}(1,1);
end
plot([1:N],test_scores)
hold
%% REMEMBER TO ASSIGN I!
i = best_i_above;
sel_feat_ind = [1:size(data,2)];
sel_feat_ind(removed_ind(1:i)) = [];
party_predictions = LDA_predict(data(1:1037,:), int_variables(1:1037,2), sel_feat_ind, test_data(:,:));
results = evaluation(party_predictions,truth);
test_score = results{2}(1,1)

%%
for i=1:N
    party_predictions = LDA_predict(data(1:500,:), int_variables(1:500,2), sel_feat_ind(1:i), data(501:650,:));
    results = evaluation(party_predictions,int_variables(501:650,2));
    test_scores(i) = results{2}(1,1);
end
plot([1:N],test_scores)
%%
for i=1:N
    party_predictions = LDA_predict(data(1:650,:), int_variables(1:650,2), sel_feat_ind(1:i), data(651:800,:));
    results = evaluation(party_predictions,int_variables(651:800,2));
    test_scores(i) = results{2}(1,1);
end
plot([1:N],test_scores)


%% PCA for parties
test_scores = zeros(60,1);
for i=60:-1:1;
    C = cov(selected_features);
    [V,D] = eig(C);
    Z = selected_features*V(:,i:end);
    Z = fliplr(Z);

    truth = test_int_variables(:,2);
    [ pijs, p_r, w0, w ] = parameters( Z, int_variables(1:1037,2), size(classes2,1) );
    test_Z = fliplr(test_data(:,sel_feat_ind)*V(:,i:end));
    party_predictions = prediction( test_Z, w, w0 );
    results = evaluation(party_predictions,truth);
    test_scores(i) = results{2}(1,1);
end
%%
plot([1:60],test_scores)

%% Feature selection after PCA (problems?)
C = cov(selected_features);
[V,D] = eig(C);
Z = selected_features*V;
data2 = fliplr(Z);
feature_names2 = selected_feature_names;
scores = zeros(size(data2,2),1);

for i =1:size(data2,2)
    truth = int_variables(:,2);
    [ pijs, p_r, w0, w ] = parameters( [data2(1:500,i)], int_variables(1:500,2), size(classes2,1) );
    party_predictions = prediction( [data2(501:1037,i)], w, w0 );
    results = evaluation(party_predictions,truth(501:1037));
    scores(i) = sum(results{2}(1,1));
end

[best, best_index] = max(scores);
selected_PCA_features = data2(:,best_index);
selected_PCA_feature_names = feature_names2(1,best_index);
data2(:,best_index)= [];
feature_names2(best_index) = [];

for k=1:39
    scores = zeros(size(data2,2),1);
    for i =1:size(data2,2)
        truth = int_variables(:,2);
        [ pijs, p_r, w0, w ] = parameters( [data2(1:500,i), selected_features(1:500,:)], int_variables(1:500,2), size(classes2,1) );
        party_predictions = prediction( [data2(501:1037,i), selected_features(501:1037,:)], w, w0 );
        results = evaluation(party_predictions,truth(501:1037));
        scores(i) = sum(results{2}(1,1));
    end
    [best, best_index] = max(scores);
    selected_PCA_features = [selected_PCA_features, data2(:,best_index)];
    selected_PCA_feature_names = [selected_PCA_feature_names, feature_names2(1,best_index)];
    data2(:,best_index)= [];
    feature_names2(best_index) = [];
end
%
N = length(selected_PCA_feature_names);
sel_feat_ind = zeros(1,N);
for j=1:N
    ind = strfind(selected_feature_names, selected_PCA_feature_names{j});
    for i=1:size(ind,2)
        if(ind{i} == 1)
            sel_feat_ind(j)=i; 
        end;
    end;
end

% Computing the test F-score for parties

truth = test_int_variables(:,2);
[ pijs, p_r, w0, w ] = parameters( [selected_PCA_features], int_variables(1:1037,2), size(classes2,1) );
party_predictions = prediction( test_data(:,sel_feat_ind), w, w0 );
results = evaluation(party_predictions,truth);
test_score = results{2}(1,1);

%% Classifying the candidate parties
[ pijs, p_r, w0, w ] = parameters( data(1:500,:), int_variables(1:500,2), size(classes2,1) );
TE2 = classification_error( data(1:500,:), int_variables(1:500,2), w, w0 );
VE2 = classification_error( data(501:1037,:), int_variables(501:1037,2), w, w0 );

%% PCA
C = cov(data);
[V,D] = eig(C);
TE = zeros(60,2);
VE = zeros(60,2);
for i=140:199;

    Z = data*V(:,i:end);
    Z = fliplr(Z);

    [ pijs, p_r, w0, w ] = parameters( Z(1:500,:), int_variables(1:500,1), size(classes1,1) );
    TE(i-139,1) = classification_error( Z(1:500,:), int_variables(1:500,1), w, w0 );
    VE(i-139,1) = classification_error( Z(501:1037,:), int_variables(501:1037,1), w, w0 );

    [ pijs, p_r, w0, w ] = parameters( Z(1:500,:), int_variables(1:500,2), size(classes2,1) );
    TE(i-139,2) = classification_error( Z(1:500,:), int_variables(1:500,2), w, w0 );
    VE(i-139,2) = classification_error( Z(501:1037,:), int_variables(501:1037,2), w, w0 );
end
plot(TE(:,1),1:60)
figure
plot(VE(:,1),1:60)
figure
plot(TE(:,2),1:60)
figure
plot(VE(:,2),1:60)



%% Gradient Ascent for candidate parties (FUNCTION NOT YET ADAPTED!)

[ pijs, p_r, w0, w ] = parameters( Z(1:500,:), int_variables(1:500,2), size(classes2,1) );
[ w_best, w0_best, s_best, L_best, L_current, s ] = GradientAscent( Z(1:500,:), int_variables(1:500,2), w, w0, 0.01 );

training_error = classification_error( Z(1:500,:), int_variables(1:500,2), w, w0 );
validation_error = classification_error( Z(501:1037,:), int_variables(501:1037,2), w, w0 );

%% Implement K-fold crossvalidation ?


%% Saving the results into a csv-file:
int_variables = [election_party_predictions party_party_predictions];
target_class = int2label(int_variables, classes1, classes2);
cell2csv('prediction-79831P-400587.csv',target_class);
%%

