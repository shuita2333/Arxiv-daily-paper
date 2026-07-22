# 📦 其他研究 | 2026年07月23日

> 本类共 **241** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-241](./part-05.md)

---

### 51. [Building a European Multilingual Evaluation Dataset: The MMLU Localisation Project within the EMT Network](https://arxiv.org/abs/2607.18432)

**<font color=#1a73e8>作者：</font>** Pilar Sánchez-Gijón, Susana Valdez, Sofía Calvo Del Barrio 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper reports on a collaboration between the Directorate-General for Translation (DGT) and the European Master's in Translation (EMT) to localise the MMLU dataset into 11 European languages. Beyond creating a more inclusive benchmark for LLM evaluation, the project offers master's students authentic, project-based professional training in translation, revision, project management, and multilingual coordination, while highlighting key methodological, administrative, and workflow challenges.

---


### 52. [Intelligence from Learnable Novelty](https://arxiv.org/abs/2607.18433)

**<font color=#1a73e8>作者：</font>** Yanbo Zhang, Michael Levin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Intelligence appears under different names in different fields: as data compression in statistics and machine learning, as universal computation in dynamical systems, and as adaptive behavior in agents. Each field carries its own objective, and the two most influential drives often fail in mirror image: novelty search, which seeks surprise, is transfixed by a noisy television screen, while the free-energy principle, which avoids surprise, is most content in a dark room. Both failures have a single cause: each objective treats as one quantity the surprise a learner can convert into knowledge and the surprise it never can. Here we show that the learnable part of that information, which we call learnable novelty, yields the seemingly disparate projections of intelligence, and we give a closed-form estimator of it built on a cheap and differentiable reservoir computer. Used as a measure, with no supervision of any kind, the estimator recovers decades of complexity classification, ranking the Turing-complete rule~110 highest among the elementary cellular automata. Used as an objective, its gradient carries a neural cellular automaton from simple dynamics into a regime of solitons, the traveling, colliding structures by which rule~110 computes, as well as organizes the representation of an image encoder around the ten digit classes of MNIST, fully unsupervised: no label ever enters training. Handed to a reinforcement-learning agent as an intrinsic reward, it supplies the exploration that task rewards lack, improving on the task baseline in nine of ten environments and collapsing in none. Complexity generation, abstraction, and exploration, ordinarily pursued with unrelated objectives in separate fields, thus emerge from ascent on one differentiable quantity, and the projections of intelligence gain a common quantitative footing.

---


### 53. [Surprise Forcing: What to Remember, When to Skip in Long Video Generation](https://arxiv.org/abs/2607.18436)

**<font color=#1a73e8>作者：</font>** Shuwei Shi, Zhen Li, Muyao Niu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Streaming autoregressive diffusion makes minute-scale video synthesis practical, but its bounded context and fixed denoising schedule allocate resources uniformly across a highly non-stationary sequence. A rolling key-value cache forgets distant visual evidence even when that evidence remains important, while every generated chunk receives the same number of denoising passes irrespective of its actual difficulty. We introduce Surprise Forcing, a training-free framework that treats both limitations as online resource-allocation problems. A Surprise-Gated Memory Bank summarizes evicted frames with value-token descriptors, evaluates them using complementary global-deviation and nearest-neighbor novelty signals, and regulates admission through a feedback-controlled budget in normalized score space. Priority-based replacement and relevance-aware routing then keep the external memory compact and useful. In parallel, Surprise-Aware Denoising estimates chunk difficulty from the maximum adjacent-frame cosine distance after the first denoising pass and uses a local percentile scheduler to skip intermediate steps for comparatively easy chunks. Experiments on VBench, VBench-Long, and VBench-2.0 show that the proposed allocation strategy improves long-horizon consistency and visual quality while retaining real-time streaming throughput.

---


### 54. [PathReportEval: A Systematic Benchmark for Pathology Report Generation](https://arxiv.org/abs/2607.18448)

**<font color=#1a73e8>作者：</font>** Suryakant Singh, Sejuti Majumder, Beatrice Knudsen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Pathology report generation from whole-slide images (WSIs) is a rapidly growing multimodal learning problem, yet progress is difficult to measure because existing studies use heterogeneous datasets, model settings, visual encoders, and evaluation protocols. Moreover, commonly used natural language generation metrics, including BLEU, ROUGE, and METEOR, primarily reward lexical similarity and often fail to detect clinically consequential errors such as omitted diagnoses, hallucinated findings, or discordant tumor attributes.
We present a standardized benchmark and evaluation framework for pathology report generation. The benchmark evaluates four representative methods across three datasets (TCGA, HistAI, and REG 2025) using three pathology foundation encoders (CONCHv1.5, UNI2-h, and H-Optimus-1). Our framework standardizes preprocessing, feature extraction, training, decoding, and evaluation, enabling fair comparison across models while providing a modular platform for integrating new methods, datasets, and encoders.
A central contribution is the Clinical Report Quality Score (CRQS), a clinically grounded metric for evaluating factual correctness. CRQS maps reference and generated reports into structured clinical attributes and measures four complementary dimensions: clinical fact coverage, key information recall, hallucination rate, and clinical discordance, producing both an overall score and interpretable sub-scores.
Experiments demonstrate that conventional language-generation metrics are weakly aligned with clinical correctness and frequently overestimate report quality. In contrast, CRQS reveals clinically meaningful differences between models and encoders that lexical metrics fail to capture. Together, the benchmark, public plug-and-play framework, and CRQS establish a reproducible foundation for rigorous evaluation of pathology report generation.

---


### 55. [CANDOR: Chance-Calibrated Discordance in Frozen Foundation Encoders](https://arxiv.org/abs/2607.18451)

**<font color=#1a73e8>作者：</font>** Soroosh Tayebi Arasteh, Sven Nebelung, Daniel Truhn  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Frozen encoders are chosen by how well a lightweight head reads a finding from their features, not whether the geometry separates it. Nearest-neighbor discordance does, but with unequal banks the opposite-label neighbor wins on density, not geometry, so prevalence alone makes an uninformed encoder look blind. We introduce CANDOR, a discordance measure whose equal-size banks are symmetric under a label swap, fixing its chance level at exactly one half. Across 22 encoders, 20 datasets from 7 domains, and 605,443 images, this correction reverses the conclusion. Collapse falls below chance almost everywhere, so no encoder is blind, yet all are weak: the best chest model reads pneumothorax at 84.5 AUROC and still places 18.4% of those positives nearer an opposite-label film than its own kind in the same hospital. The same encoder that resolves bird species at 4.5 leaves chest findings at 42.8 and glaucoma at 49.8, at chance and worse than random weights. Such a case caps the normalized margin of any Lipschitz head, yet some head among eleven is correct on all but 2.8% of cases where one head misses 35.9%: the deficit is selection, not information. Erasure retention is associated with collapse; we detect no association with the objective, scale, recency, or size of the finding. Because the chance level is fixed, CANDOR can be read before any head is trained, flagging which findings a frozen encoder supports poorly.

---


### 56. [0-Cyclic Equalizability of Binary Words Characterized by Hamming Weight](https://arxiv.org/abs/2607.18452)

**<font color=#1a73e8>作者：</font>** Sarunyu Thongjarast  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The random cut is one of the most fundamental shuffles in card-based cryptography: it rotates a sequence of face-down cards by a secret amount. Under this shuffle, two sequences of cards are indistinguishable if and only if they are cyclic shifts of each other. This motivates the question of whether, given two sequences of cards, inserting cards at matching positions can make them indistinguishable. A previous study shows that such an insertion is always possible when any cards may be inserted, as long as the two words are permutations of each other. This paper considers a stronger restriction: if the cards are binary, carrying only 0 or 1, can we insert only 0s to make the sequences indistinguishable? We call two words 0-cyclically equalizable if one can insert 0s into both sequences at matching positions so that the resulting words are cyclic shifts of each other. Our main result is that two binary words of equal length are 0-cyclically equalizable if and only if they have equal Hamming weight, that is, the same number of 1-bits. Since equal Hamming weight is clearly necessary, the content of the paper is to show that it is also sufficient. Our proof is constructive: we encode a pair of binary words as a single word over the four-letter alphabet {A, B, X, O}, reduce equalizability to a simpler condition in this encoding, and build the required insertion explicitly.

---


### 57. [AHEAD: Advancing Multi-Class Label Aggregation with Interpretable Cross-Annotator Modeling](https://arxiv.org/abs/2607.18465)

**<font color=#1a73e8>作者：</font>** Ju Chen, Sijia Xu, Jun Feng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Crowdsourced labeling provides valuable labeled data for domains across natural language processing, computer vision, and video. Label aggregation aims to infer latent true labels from noisy and biased annotations, with the key lying in annotator reliability estimation. Despite promising progress, existing approaches struggle with one real-world bottleneck: most individual annotators label only a small subset of tasks, making accurate annotator estimation highly intractable. In this paper, we focus on the considerably more challenging multi-class label aggregation and propose AHEAD (cross-Annotator learning and High-confidEnce Annotator-guideD label aggregation), a cross-annotator learning framework that advances annotator reliability estimation by leveraging the population-level data. Specifically, AHEAD first learns high-dimensional cross-annotator contexts via a graph neural network, deriving multi-view, complementary annotator embeddings by aggregating individual-level annotator features with contextual information. These embeddings are then decoded into interpretable annotator-specific confusion matrices to fit the observed labels. We formulate a composite objective incorporating high-confidence annotators to alleviate the unsupervised training issues faced by prior models. Experiments on 10 real-world datasets spanning NLP, CV, Video, and Audio show that AHEAD substantially improves label accuracy, increasing average accuracy from 68.75% to 73.23%, with gains of up to 14.9% in the best case. Meanwhile, scalability experiments on the largest dataset further demonstrate the overall superiority of our method.

---


### 58. [ECoNGS: Efficient Compressive Neural Gaussian Splats for Volume Visualization](https://arxiv.org/abs/2607.18466)

**<font color=#1a73e8>作者：</font>** Kaiyuan Tang, Chaoli Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in differentiable Gaussian splatting have highlighted the potential of primitive-based approaches as alternative scene representations for interactive, high-quality, volume visualization (VolVis) of large datasets. However, the explicit nature of current primitive-based methods, combined with isolated optimization for each VolVis scene, results in redundant, non-compact representations. We present ECoNGS, an efficient compressive neural Gaussian splatting framework for VolVis scene representation. ECoNGS employs lightweight neural networks to dynamically predict implicit, editable Gaussian splats from explicit anchor points, effectively combining model compactness and parameter efficiency of implicit representations with high-performance rendering of explicit primitives. We explore a joint learning strategy that clusters geometrically similar scenes and shares parameters across them, significantly reducing overall training time and model size while maintaining reconstruction fidelity. To achieve a more compact scene representation, we further compress the explicit anchor attributes using a neural entropy model that estimates their probability distributions, enabling compact storage via entropy coding. We systematically investigate Gaussian initialization strategies and propose a simple yet effective scheme tailored for VolVis scenes, improving reconstruction accuracy and accelerating convergence. We evaluate ECoNGS qualitatively and quantitatively across various univariate and multivariate VolVis scenes, highlighting its superior performance over prior methods in training time, reconstruction quality, and model size. In particular, compared with the prior method iVR-GS, ECoNGS improves reconstruction quality by up to 2.2 dB in PSNR while reducing the model size by up to 6.1x and the training time by up to 5.9x. The code is available at this https URL.

---


### 59. [Weak-to-Strong Learning in Decision Making](https://arxiv.org/abs/2607.18467)

**<font color=#1a73e8>作者：</font>** Jingwei Ji, Renyuan Xu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many operational decisions rely on predictive models that estimate uncertain outcomes conditional on observable contexts. Training such models, however, often faces a fundamental data asymmetry: labeled outcomes are scarce or costly to obtain, while contextual covariates are abundant. Motivated by this data asymmetry, we develop a decision-aware weak-to-strong (W2S) framework that leverages both labeled and unlabeled data to improve contextual stochastic optimization. Specifically, we first train a weak model using limited labeled data and then use it to generate predicted outcome distributions on unlabeled contexts. These distributions provide soft supervision for training a strong model. We establish a non-asymptotic upper bound on the excess decision risk of W2S and a complementary lower bound for a strong-only benchmark. Their comparison yields explicit sufficient conditions under which W2S improves downstream decision performance. The key quantity is the correlation dimension between the weak and strong feature representations: when it is small, abundant unlabeled data reduce the effect of teacher errors along non-overlapping directions. A synthetic newsvendor experiment and a comment moderation experiment based on real-world data provide empirical evidence consistent with the theory.

---


### 60. [RRPO: Reference-Relative Policy Optimization with Stratified Conditional Rollouts](https://arxiv.org/abs/2607.18470)

**<font color=#1a73e8>作者：</font>** Yuxin Xiong, Xunyi Jiang, Rohan Surana 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Group Relative Policy Optimization (GRPO) has shown strong effectiveness in reinforcement learning from verifiable feedback, where sampled rollouts can be compared within a group using task-provided correctness signals. However, extending group-relative optimization beyond verifiable settings is challenging because success in many tasks is not captured by a single correctness criterion. We propose \textbf{Reference-Relative Policy Optimization (RRPO)}, which generalizes GRPO by replacing direct correctness-based advantage construction with reference-relative contrastive comparisons. RRPO first uses \emph{stratified conditional rollouts} to construct positive and negative anchor sets, and then trains a metric projection head with a set-contrastive objective to compare candidate rollouts against these anchors. The resulting alignment scores directly define contrastive advantages: during policy optimization, the projection head is frozen, and the scores are centered within each rollout group in a standard group-relative objective. We evaluate RRPO using anchor-based contrastive advantages throughout policy optimization, without relying on task ground-truth verifiers. Across verifiable reasoning, open-ended generation, and post-SFT settings, RRPO remains competitive with verifier-based optimization, improves over weakly supervised baselines, and provides additional gains after supervised fine-tuning.

---


### 61. [Hybrid Latent-Structural Fusion (HLSF) for Cyber Anomaly Detection](https://arxiv.org/abs/2607.18479)

**<font color=#1a73e8>作者：</font>** Dorianis M. Perez, Maksim E. Eren, Bryan E. Kaiser  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Malicious anomalous activity detection is a fundamental challenge for cyber security systems. Both tensor decomposition under statistical framework with CANDECOMP-PARAFAC alternating Poisson regression (CP-APR) and normalizing flows have proven to be powerful unsupervised machine learning methods that model multi-dimensional data and capture complex and multi-faceted details of behavior profiles in cyber security applications. In this study, we propose Hybrid Latent-Structural Fusion (HLSF), a weighted anomaly fusion framework integrating CP-APR structural anomaly scores with latent-space density scores derived from normalizing flows. In our experiments, we show that the HLSF framework improves anomaly detection performance on a dataset of real-world compromised user credentials collected from the large enterprise network of Los Alamos National Laboratory (LANL) during a red-teaming exercise, compared with using CP-APR or normalizing flows alone.

---


### 62. [Attractor Geometry Determines the Identifiability Limits of System Discovery](https://arxiv.org/abs/2607.18490)

**<font color=#1a73e8>作者：</font>** Matteo Gallo, Fabio Anselmi, Paolo Lazzari  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Symbolic discovery of governing equations from data is limited not only by algorithm design and data volume, but by the geometry of the attractor: what the long-run dynamics allow to be recovered. Using a within-system design on Lorenz-84, where one forcing parameter drives fixed-point, limit-cycle, and chaotic regimes while the governing equations and library stay fixed, we show that a single number, $\lambda_{\min}(M)$, the smallest eigenvalue of the invariant-measure moment matrix, sets the identifiability ceiling for both sparse regression (SINDy) and evolutionary symbolic regression (PySR). Derived from the Birkhoff ergodic theorem and obtained from a short reference trajectory before any run, $\lambda_{\min}(M)$ measures how fully the attractor covers function space: where it vanishes, recovery is impossible for any algorithm, sparse or combinatorial alike; as it grows, both algorithms improve. Chaos raises $\lambda_{\min}(M)$ by spreading the attractor, but also enlarges it and amplifies noise; because noise enters SINDy's regression bottleneck linearly and PySR's discrimination channel superlinearly, the same transition can push the two methods in opposite directions, so deeper chaos is not uniformly better. Parameter-free mechanistic scores from this framework transfer without refitting to a held-out Lorenz-96 system, confirming mechanism rather than curve-fitting; a criterion read from the equations predicts when added chaos will not improve conditioning. We also introduce Soft F1, a coefficient-weighted structural metric that resolves performance differences invisible to binary-success and predictive scores. The first question of discovery is then not which algorithm, but what the attractor permits.

---


### 63. [Now We Know? A Systematic Comparison of TerraMind and THOR](https://arxiv.org/abs/2607.18504)

**<font color=#1a73e8>作者：</font>** Frederick Schindlegger, Kenzo Bounegta, Eva Gmelich Meijling 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Benchmarks for Geospatial Foundation Models (GFMs) increasingly rank models by aggregate score, but such rankings obscure why models differ: how much of the gap is architecture, how much is decoder capacity, and how much is a use-case-specific artefact? This study addresses that gap through a controlled comparison of two GFMs developed under European Space Agency's $\Phi$-lab with contrasting design philosophies: THOR, which introduces a compute-adaptive architecture supporting variable patch sizes and unifies Sentinel-1, -2, and -3 data at their native resolutions; and TerraMind, a multimodal generative GFM pretrained with a dual-scale token/pixel objective that enables any-to-any cross-modal generation (Thinking-in-Modalities) to infer missing sensors at inference time. Rather than reporting a single leaderboard, we investigate the axes along which the two architectures actually differ - patch size, decoder complexity, finetuning regime, input modality, and model scale - across ten use cases spanning segmentation and regression in diverse domains, including climate disaster response, methane leak detection, snow monitoring, or sea ice mapping. We find that architectural design choices - patch size and decoder type in particular - explain more performance variance than model identity itself, that the two models embody complementary investment strategies (pretraining-time scale for TerraMind versus inference-time tokenisation for THOR), and that correctly interpreting results requires dataset-level characterisation. The resulting picture is not a single winner but a set of hypotheses and a diagnostic ablation methodology that we expect to generalise to future GFMs beyond THOR and TerraMind.

---


### 64. [AInimation: Animating from Prompt to AI-Generated Responses](https://arxiv.org/abs/2607.18507)

**<font color=#1a73e8>作者：</font>** Jiaqi Wu, Damien Masson  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We explore the use of animated transitions between a prompt and an AI-generated response. After reviewing 800 examples of prompts and responses, we devise a taxonomy of animated transitions for multimodal text- and image-generative models. The proposed animations include translating and morphing elements of the prompt to their final location in the response; highlighting modifications such as fixed typos; overlaying structural requirements to verify them; and displaying how a model understands references. A study shows that adding animated transitions helps users review the response: participants performed 43% better at locating elements in the response; 153% better at identifying changes; and 20% better at verifying the prompt was correctly interpreted. Our work applies to all software that integrates AI and shows that well-crafted, slower animations are preferable to instant AI responses.

---


### 65. [Style over Substance: A Shortcut Audit of Emotion-Description Preference Evaluation](https://arxiv.org/abs/2607.18508)

**<font color=#1a73e8>作者：</font>** Jiabing Yang, Yixiang Chen, Yuan Xu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Preference over model-generated emotion descriptions is emerging as a standard evaluation metric for multimodal emotion understanding, exemplified by the MER2026 MER-Prefer track on EmoPrefer. Such benchmarks assume that predicting the preferred description requires grounded cross-modal understanding of the video. We conduct a systematic shortcut audit of EmoPrefer using content-blind probes. A simple logistic regression using only description length and generator identity, without processing the text, video, or audio, performs comparably to LoRA-finetuned 7B text and audio-visual judges (65.8 versus 66.8 WAF on EmoPrefer-V2). Generator identity is recoverable from description text with 99.5 percent accuracy, every candidate pair contrasts two distinct generators, and the human preference labels agree with a fold-exclusive per-generator win-rate prior on 66 percent of the evaluated pairs. When the human label conflicts with this prior, trained judges still follow the style prior on 63 to 80 percent of the pairs. On a length-matched subset that neutralizes verbosity bias, the tested media configurations yield no statistically significant improvement, while an ODIN-inspired diagnostic that decouples the style shortcut leaves its content head near chance. These results do not imply that human preferences are inherently stylistic or that the descriptions contain no emotional information. Instead, they show that the current scores can be reached without verifying either description against the video. We recommend source-balanced pairing, strict length control, counter-stereotypical sliced reporting, and multi-annotator consensus for future cross-generator evaluations. Code is available at this https URL.

---


### 66. [DuSPiT: Dual-Branch Sub-Patch Pixel Diffusion Transformer](https://arxiv.org/abs/2607.18510)

**<font color=#1a73e8>作者：</font>** Yunpeng Bai, Yossi Gandelsman, Michaël Gharbi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion Transformers achieve strong image generation performance, but most operate in compressed latent spaces. Pixel-space diffusion avoids this information loss, yet existing approaches map each raw image patch to a single token, forcing one representation to handle both global communication and fine-grained details. We address this issue by proposing a new architecture, \textbf{DuSPiT}, a \textbf{Du}al-branch \textbf{S}ub\textbf{P}atch \textbf{Pi}xel \textbf{T}ransformer. This model separates global structural reasoning from local appearance modeling. DuSPiT uses a compact base branch for efficient global reasoning and a parallel, high-capacity pixel branch, organized into subpatch groups, to preserve detailed appearance, with the two branches interacting through cross-attention. Our results show that DuSPiT generates images with richer details and stronger fine-grained structures, while also achieving a better quality--efficiency trade-off than prior pixel-space diffusion transformers.

---


### 67. [Automated Data Engineering and Feature Selection for the Case Study of Warpage Detection in Fused Deposition Modeling](https://arxiv.org/abs/2607.18515)

**<font color=#1a73e8>作者：</font>** Saleh Valizadeh Sotubadi, Nazanin Mahjourian, Vinh Nguyen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This study contributes toward development of an Automated Data Processing (ADP) framework designed to evaluate and reinforce optimal machine learning model-feature combinations for predictive tasks in fused deposition modeling (FDM) process datasets. The methodology is centered around a reinforcement learning-inspired policy updating mechanism, where multiple machine learning models are trained on both full feature sets and feature subsets selected through Shapley-based Explainable AI (SHAP XAI) across 217 datasets. At each episode, the framework assesses the predictive accuracy and F1-scores of each model-feature pair, computes a scalar reward, and updates $Q$ values to guide future model selection. SHAP XAI feature importance was employed to generate reduced yet informative feature subsets to enable the framework to explore performance with dimensionality. The policy was shown to evolve over multiple episodes, with reward distributions used to visualize performance stability. Overall, results indicate that leveraging the ADP framework through XAI algorithms successfully converges toward optimal model-feature configurations with improved accuracy and stability. Specifically, the proposed framework improves the test-set AUC from 0.9248 to 0.9731 and increases the mean reward value by more than fifty percent compared with the baseline full-feature configuration.

---


### 68. [Signed Rectified Flow: Negativity-Controlled Generation](https://arxiv.org/abs/2607.18516)

**<font color=#1a73e8>作者：</font>** Runlong Liao, Baiyu Su, Lizhang Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce Signed Rectified Flow (Signed RF), a generalization of Rectified Flow that targets the signed measure $\pi^{sign} = (1+\alpha)\pi^+ - \alpha\pi^-$, where $\alpha>0$, $\pi^+$ is the distribution to promote, and $\pi^-$ is the distribution to suppress. Although direct sampling from a signed measure is not well-defined, Signed RF induces a valid generative process that concentrates probability in regions where the signed measure is positive while provably excluding regions dominated by its negative component. It therefore provides a principled framework for incorporating negative information and exclusion constraints into generative modeling. We analyze the signed continuity equation underlying Signed RF and use a charged-particle interpretation to explain how negative mass forms exclusion barriers. This theory further motivates practical adaptive guidance algorithms. Across several applications, Signed RF improves the fidelity-diversity trade-off on ImageNet, reduces nearest-neighbor similarity in anti-memorization experiments, and reduces nudity induced by adversarial prompts in Stable Diffusion 3.5 while preserving CLIP and aesthetic scores.

---


### 69. [Adaptive Two-Stage Online Learning for Service-Affecting Failure Detection in Mobile Core Networks](https://arxiv.org/abs/2607.18522)

**<font color=#1a73e8>作者：</font>** J. du Toit, G. Fita, J. Salzwedel 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mobile network operators monitor aggregated traffic volumes to assess the operational health of core network infrastructure. Reliable failure detection is challenging due to strong temporal structure, non-stationarity, measurement artefacts, and extreme class imbalance, which limit static threshold-based monitoring. This paper proposes a two-stage online learning framework for traffic-based failure detection in mobile core networks. Stage I incrementally models normal traffic dynamics using lightweight regression with time-aware features. Stage II analyses prediction residuals together with contextual indicators to detect genuine service-affecting network failures. The framework operates fully online under a prequential evaluation protocol, enabling continuous adaptation with low computational overhead. Across linear and non-linear models, the proposed two-stage architecture achieves the best precision-recall trade-off, attaining the highest recall, F1-score, and AUC at acceptable false positive rates. These results demonstrate the importance of explicit residual decomposition for reliable failure detection in streaming mobile core network data.

---


### 70. [AniGS: Bridging Rendering and Diffusion Prior for 3D Scene Animation](https://arxiv.org/abs/2607.18539)

**<font color=#1a73e8>作者：</font>** Yen-Chi Cheng, Chen Gao, Chuhan Chen 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Novel view rendering of large and complex reconstructed scenes is becoming increasingly photorealistic. However, most reconstructions remain static and lack the ambient motion that makes environments immersive. We present AniGS, a method for scene-level animation of 3D Gaussian Splatting (3DGS) reconstructions that adds subtle, distributed dynamics, e.g., vegetation motion, while preserving rigid structures. Unlike existing 3D animation techniques which are limited to object-centric subjects or small regions, AniGS is designed for large, cluttered, navigable scenes. AniGS represents the scene with a canonical 3DGS and models motion using a time-conditioned deformation field. To animate the entire scene, we leverage a pretrained video diffusion model and introduce an iterative dataset--model update strategy that progressively expands viewpoint coverage and repeatedly updates camera-fixed training videos using a render-and-refine scheme. To prevent artifacts from unintended motion in static areas, we further introduce a composed video-to-video refinement scheme that restricts motion to desired regions. Experiments on five real-world, large-scale outdoor scenes demonstrate that AniGS produces natural ambient dynamics and high-quality novel view videos, enabling more immersive viewing experiences of reconstructed environments.

---


### 71. [Recti-Q: Feature-Space Rectification for Out-of-Distribution-Robust Quantized Perception in Edge Robotics](https://arxiv.org/abs/2607.18540)

**<font color=#1a73e8>作者：</font>** Hamidreza Yaghoubi Araghi, Parastoo Pilevar, Ming C. Lin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robotic perception pipelines increasingly rely on large vision backbones deployed on SWaP-constrained edge platforms, making post-training quantization (PTQ) attractive for real-time inference. However, while PTQ often preserves clean in-distribution accuracy, we show that it can substantially degrade reliability under deployment-relevant distribution shifts (e.g., sensor noise, severe weather, and novel operating environments), creating a Quantization-Induced Robustness Gap. Across foundational vision benchmarks (ImageNet-C and PACS), 4-bit PTQ models exhibit pronounced robustness degradation despite negligible ID accuracy loss. To address this, we propose Recti-Q, a lightweight feature-space rectification framework that freezes the quantized backbone and trains a small classifier-head LoRA adapter using only source data. Recti-Q is architecture-agnostic across CNNs and Transformers, supports efficient teacher-free training, and recovers a significant portion of the lost robustness, in some cases matching or exceeding FP32 performance. At less than 1% parameter overhead (as small as 6 KB), Recti-Q preserves over 99% of PTQ memory savings, adds negligible compute, and enables low-bandwidth Over-The-Air (OTA) resilience patching for deployed robotic fleets operating in unpredictable physical environments.

---


### 72. [Physics Closure Matters for Machine Olfaction: A Maxwell--Stefan Graph Solver for Identifiable Dynamic Gas Unmixing](https://arxiv.org/abs/2607.18544)

**<font color=#1a73e8>作者：</font>** Yue Shi, Liangxiu Han, Xin Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Machine olfaction for gas unmixing is an underconstrained inverse problem in which gas compositions must be inferred from low-dimensional, delayed, and entangled sensor responses produced by interacting chemical transport, surface adsorption, and sensor transduction. One of the key obstacles is physics closure misspecification, where a neural network is designed to fit sensor traces rather than infer a physically closed olfactory process. In this work, we formulate gas unmixing as a multi-physics-constrained inverse problem governed by Maxwell--Stefan multicomponent transport PDEs, competitive adsorption ODEs, and nonlinear sensor transduction ODEs. Directly solving such a high-dimensional coupled system is computationally expensive and often numerically unstable. To this end, we propose UnMixNet, a physics-closed graph neural solver that embeds this multi-physics forward process into end-to-end gas unmixing. UnMixNet discretizes Maxwell--Stefan cross-diffusion on spatial graphs and formulates the multicomponent flux on each edge. This design enables local, differentiable, and flux-conservative inference for multicomponent cross-diffusion. Evaluations on SmellNet show improved single-odor recognition, seen-mixture unmixing, and unseen-mixture generalization. In addition, an external validation on UCI Dynamic Gas Mixtures shows that the inferred concentration process agrees with ground truth concentration set points under dynamic transitions. Process-consistency diagnostics further show that the proposed model learns transferable dynamic physical fingerprints that better satisfies transport, conservation, adsorption, and readout closure.

---


### 73. [Scalable Policy Optimization for Networked Multi-Agent Reinforcement Learning with Continuous State-Action Spaces](https://arxiv.org/abs/2607.18554)

**<font color=#1a73e8>作者：</font>** Dongming Wang, Pengcheng Dai, Wenwu Yu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> We develop the Continuous Distributed Coupled Policy Gradient (CDCPG) algorithm for cooperative reinforcement learning in networked Markov decision processes with continuous state and action spaces. Each agent maintains a local actor over a bounded graph neighborhood, and a localized least-squares temporal-difference critic evaluates a truncated action-value function through a spectral random-feature representation of the local transition kernel. The analysis makes four contributions. First, the truncated action-value function is constructed as a conditional expectation over the neighborhood, yielding a well-posed localized Bellman theory that removes the continuation-kernel mismatch of naive truncation arguments. Second, we expose a dimensional obstruction to temporal-difference stability for normalized random features and prove an unconditional excitation bound that reduces stability to a symmetric persistence-of-excitation condition, monitorable through an online matrix-concentration certificate. Third, under exponential spatial decay of agent interactions, the excitation condition, and smoothness of the objective, CDCPG drives an averaged per-agent stationarity measure to within any excess $\epsilon$ of an explicitly characterized approximation floor using $\widetilde{\mathcal{O}}(\epsilon^{-2})$ shared-oracle samples, and the excess dependence matches the smooth nonconvex first-order rate; per-agent computation and communication are governed by the neighborhood size rather than the network size. Fourth, an adaptive-locality rule selects the radius that balances truncation and graph-decay residuals against the target accuracy. Experiments on a networked linear-quadratic benchmark corroborate the locality and feature-dimension predictions.

---


### 74. [ChatMuse: Supporting In-Person Small-Group Conversation Experience with a Proactive Assistive AI Agent in Mixed Reality](https://arxiv.org/abs/2607.18556)

**<font color=#1a73e8>作者：</font>** Shaoze Zhou, Joaquin Frangi, Diana Nelly Rivera Rodriguez 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> In-person small-group conversations occur across nearly every aspect of daily life and play a crucial role in social interaction. However, achieving effective in-person group conversations can be challenging and cognitively demanding. While recent Mixed Reality (MR) headsets show promise as a conversational support system by presenting relevant information through overlays, it remains unclear how such supporting information should be designed and generated for in-person group conversations. We propose ChatMuse, a novel MR-based proactive assistive system for in-person small-group conversation experience. ChatMuse analyzes verbal and non-verbal cues from all conversation participants and proactively provides real-time guidance on the user's verbal and non-verbal behaviors. The behavioral responses of the supported users are then used to improve ChatMuse's support capabilities in subsequent interactions. We conducted a within-subject study to evaluate and demonstrate the feasibility and effectiveness of ChatMuse in assisting users to engage in and contribute to in-person small-group conversations. Our research around ChatMuse represents a design exploration of a new interaction space that investigates the feasibility of supporting in-person small-group conversations through a proactive assistive AI agent in MR.

---


### 75. [Robust Multi-View Classification under Noisy Supervision via Global Anchor Consensus](https://arxiv.org/abs/2607.18561)

**<font color=#1a73e8>作者：</font>** Yuliang Yang, Hongzhe Zhang, Huiru Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In recent years, multi-view learning has attracted increasing attention, as it integrates the complementary information of heterogeneous views. Most existing multi-view classification methods rely on accurate annotations to guarantee performance. However, noisy labels are ubiquitous in practice due to imperfect annotation, and the refinement signals that existing methods derive from models trained on such noisy supervision can gradually lose their reliability. To deal with this problem, we propose a novel Global Anchor-based Label Auditing method (GALA) for multi-view classification to resist the negative impact of noisy labels. Specifically, we construct a global anchor for each class in every view, which aggregates the samples of the whole class and thus offers a stable reference insensitive to individual predictions. Then, each view measures how close an instance is to the anchor of its observed label relative to the nearest competing anchor, and the per-view evaluations are fused with the classifier confidence into a cross-view audit score. Based on the audit scores, suspicious samples are assigned small weights, and an adaptive correction strategy rewrites a label only when the anchor-based candidate agrees with the classifier prediction. Finally, the corrected labels in turn refine the anchors and supervise noise-robust representation learning. Extensive experiments on six datasets demonstrate that GALA outperforms eight state-of-the-art methods, especially under high noise rates.

---


### 76. [HALO: Interactive Co-abductive Reasoning in Scientific Hypothesis Generation](https://arxiv.org/abs/2607.18564)

**<font color=#1a73e8>作者：</font>** Youngseung Jeon, Kat Limqueco, JiaSyuan Chang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Scientific discovery is essential yet inefficient, primarily because generating hypotheses within a vast search space hinders breakthroughs. While current AI systems assist in generating new hypothesis candidates, they lack interactive support for the reasoning process by which users develop these outputs into promising hypotheses, resulting in surface-level hypotheses. To address this issue, we present co-abduction, a human-AI collaborative framework for abductive reasoning in scientific hypothesis generation. To operationalize co-abduction, we build HALO, a human-AI collaborative system for molecular hypothesis generation in drug discovery, enabling improved candidate clustering, strategy identification, and multi-strategy synthesis. In expert studies involving 10 medicinal chemists, HALO significantly facilitated abductive reasoning for hypothesis generation -- efficient candidate observation, systematic strategy identification, and coherent multi-strategy composition -- and enabled participants to produce higher-quality, more diverse candidate molecules.

---


### 77. [AMICA-Python: Adaptive Mixture Independent Component Analysis with Anderson Acceleration](https://arxiv.org/abs/2607.18568)

**<font color=#1a73e8>作者：</font>** Scott Huberty, Christian O'Reilly  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adaptive Mixture Independent Component Analysis (AMICA) is widely used in EEG research and has long been associated with strong empirical performance for blind source separation. Despite its impact, practical use has historically depended on a single Fortran implementation, accessed via the EEGLAB toolbox for MATLAB, limiting its accessibility for analytical pipelines not designed within the MATLAB ecosystem. Here we present AMICA-Python, a Python implementation of the AMICA algorithm, with a scikit-learn-conformant API designed for integration with existing scientific Python pipelines. The implementation follows the reference algorithm closely while adopting modern software engineering practices and an interface familiar to Python users. Additionally, we introduce an optional Anderson acceleration scheme that can dramatically reduce the time to convergence for this relatively slow algorithm. To evaluate numerical agreement and practical performance, we benchmarked AMICA-Python against the reference Fortran implementation on 14 open EEG recordings. After averaging 3 runs of each implementation on all 14 recordings, AMICA-Python closely matched the reference, with a median final normalized log-likelihoods of 11.572 for both the Fortran and Python implementations, and a negligible median relative absolute difference of only $1.07\times10^{-8}$ when normalized by the absolute Fortran value. Runtime was also competitive. Relative to the reference implementation, AMICA-Python was 17.7\% faster, while the Anderson-accelerated variant was 34.1\% faster. AMICA-Python reproduces the reference implementation to high numerical precision with competitive runtime, while making AMICA available through a more accessible and extensible Python interface.

---


### 78. [For What Reason? Interpreting Models' Encoding of Causation and Antithesis](https://arxiv.org/abs/2607.18570)

**<font color=#1a73e8>作者：</font>** Abhidip Bhattacharyya, Shira Wein  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Discourse relations provide document structure, critical to language understanding and enabling language model performance and ethicality. In this work, we investigate how instruction-tuned Transformer models (LLaMA and Mistral) encode discourse relations in English, with a particular focus on the contrasting relations of causation and antithesis. Framing the task as a next-token prediction task and applying a suite of interpretability techniques to test model internals, our findings show that certain early layers make predictive decisions at mid-sequence tokens, while some mid-level layers finalize their decisions closer to the last token. Most of the remaining layers primarily propagate earlier decisions rather than actively influencing them. Additionally, we observe that some layers exhibit a preference for one answer over alternatives, suggesting asymmetric representation of discourse-based reasoning.\footnote{Our code is available at this https URL}

---


### 79. [When Does Machine Learning Beat Value Sorting? A Three-Dataset Diagnostic of Exposure-Weighted Shipment Prioritization](https://arxiv.org/abs/2607.18573)

**<font color=#1a73e8>作者：</font>** Jize Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Delay-risk models are usually judged by predictive accuracy. What matters in practice is narrower: with capacity to review only a few shipments, which ones should a manager check first? We evaluate whether machine learning clears a demanding no-model baseline: inspect the highest-value shipments first. Across three real supply-chain contexts: SCMS procurement, DataCo logistics, and Olist e-commerce, we use leakage-controlled rolling-origin evaluation and 1000-sample paired bootstrap confidence intervals. Ranking by predicted delay severity times known value (M1) beats severity-only ranking in all three datasets, yet it does not generally beat value sorting. At a 10% review budget, M1 minus VALUE_ONLY is -5.5 percentage points (pp) for SCMS, +10.1 pp for DataCo, and -4.9 pp for Olist. The divide is consistent with severity learnability: DataCo has R^2 = 0.27 and calibration bias of +0.01 days, whereas SCMS and Olist have R^2 of approximately -0.02 and negative calibration bias. Nested-CV cost-sensitive retraining does not deliver a stable improvement over M1. Rather than proposing a new learning algorithm, this paper presents a deployment diagnostic and evaluation protocol. Value sorting should remain a permanent benchmark, and ML should be deployed only after severity learnability and calibration have been audited and the model clears that gate under leakage-controlled rolling-origin evaluation.

---


### 80. [Text-conditioned Segmentation for Tomato Phenotyping via Procedural Synthetic Data](https://arxiv.org/abs/2607.18576)

**<font color=#1a73e8>作者：</font>** Samy Mounir, Mikolaj Cieslak, Najmeddine Dhieb 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-based automation is an excellent candidate for reducing manual labor in greenhouse crop production and phenotyping. However, progress is constrained by the lack of annotated training data. Recent advances in vision-based foundational models have shown promising results in zero-shot generalization to novel domains, but their performance drops in complex agricultural environments. In this work, we present a sim-to-real framework for tomato plant segmentation that combines synthetic data generation with fine-tuning of a foundation model. We model a commercial cherry tomato greenhouse and use it to generate a large-scale synthetic dataset under diverse viewpoints, lighting conditions, and plant morphology. Subsequently, we fine-tune the Segment Anything Model 3 (SAM 3) on the synthetic dataset, specializing its text-conditioned segmentation behavior for greenhouse crop organs while retaining the general visual prior that makes zero-shot transfer possible. By evaluating our framework on multiple real-world greenhouse datasets, we demonstrate that combining synthetic data with SAM 3 fine-tuning significantly improves segmentation performance and model confidence. To support community benchmarking, we publicly release the procedural model, the generated synthetic dataset, and our fine-tuned SAM 3 weights.

---


### 81. [Attention Without Grounding: Causal Evaluation of Visual Explanations in Medical VLMs](https://arxiv.org/abs/2607.18577)

**<font color=#1a73e8>作者：</font>** Binesh Sadanandan, Vahid Behzadan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Attention and saliency heatmaps are widely used to explain medical Vision-Language Model (VLM) outputs on chest X-rays, yet whether they truly highlight the image evidence driving predictions has not been causally tested. We audit faithfulness via overlap with radiologist bounding boxes on PadChest (n=637), attribution mass within radiologist masks on CheXlocalize (n=643), and 16x16 patch-occlusion maps that record which regions, when hidden, change the answer. We study three MedGemma-4B variants, cross-family probes on LLaVA-RAD and Qwen3-VL-8B-Instruct, and the specialist CheXagent-2-3b, with two CXR-trained classifiers (DenseNet121, ResNet50) as positive controls. A heatmap is faithful only if the model uses the image and attention concentrates on regions whose occlusion alters the prediction. No evaluated VLM meets both criteria. MedGemma and Qwen3-VL use the image, but attention anti-correlates with patch-occlusion importance (rho < 0 with 95% bootstrap CIs below zero). LLaVA-RAD's attention correlates positively, but the model is almost text-only (99.1% text-only agreement, near-zero causal mass), so correlation ties two near-zero signals. Attention also misses annotated anatomy: overlap with true regions never beats shifted or random controls, and no method places more than 22% of its mass inside radiologist masks. The two CXR classifiers pass all metrics, indicating the failure is specific to VLM heatmaps, not the evaluation. These heatmaps are visually reassuring but not faithful; clinical explanations require controlled localization metrics and causal perturbation, not visual inspection alone.

---


### 82. [On the Diverse Dynamical Behaviors Arising in Deep Linear Transformers](https://arxiv.org/abs/2607.18584)

**<font color=#1a73e8>作者：</font>** Sixu Li, Thomas Jacob Maranzatto, Jan Peszek 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the inference-time behavior of deep linear encoder-only transformers through the lens of interacting particle systems. In this perspective, tokens are modeled as particles that interact dynamically through successive linear self-attention layers. We show that in embedding dimension two, for any key, query, and value matrices, the dynamics can be reformulated as a generalized Kuramoto-type model with pure second-harmonic coupling. This formulation is amenable to Watanabe--Strogatz theory which reveals the dynamics are intrinsically low-dimensional regardless of the parameter matrices. For a class of token initializations associated with the Ott--Antonsen (OA) manifold, we show that the parameter matrices induce a diverse variety of long-time behaviors in linear transformers, including clustering, oscillations, and bifurcations. The oscillations and bifurcations are characterized by uncovering a hidden Hamiltonian structure in the dynamics. By establishing a structural stability result, we further show that dynamics initialized near the OA manifold exhibit the same long-time behavior as those initialized exactly on the manifold. Motivated by our theory in dimension two, we conduct numerical experiments for analogous parameter regimes in higher-dimensional transformers. Our numerical experiments suggest that the long-time behaviors characterized in our theoretical results persist in higher dimensions.

---


### 83. [Planning as Emergent Behavior in Reinforcement Learning with Relational Hidden States](https://arxiv.org/abs/2607.18589)

**<font color=#1a73e8>作者：</font>** Armin Sommer  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning is conventionally divided into model-based and model-free methods. In this taxonomy, model-based methods perform lookahead planning over a learned world model, whereas model-free methods learn a reactive state-action mapping. Recent work, however, has shown that planning can emerge from model-free reinforcement learning alone. The conditions under which this behavior emerges from a pure reward-maximization objective have so far remained unclear. In this paper, we present evidence that, in the observed cases, the hidden-state structure of the neural architecture is the deciding factor. We find that a network of relational hidden states, each anchored to an environment state and exchanging messages along learned relations, acquires a planning mechanism. These hidden states recover the environment's transition structure in their learned relations, and improve the policy at decision time by planning over the learned graph. In a matched control agent that must additionally discover which cells represent which states, no such binding arises, and no planning follows from it. We argue that this explains the observed phenomenon of emergent planning in model-free reinforcement learning and raises the question of how common such emergent planning might be more generally. Finally, we hypothesize that the discovered mechanism could describe how planning emerges from pure reward maximization in the human brain through a neural architectural prior.

---


### 84. [A Self-Evolving Default Action for Cooperative Tasks with Continuous Action Space](https://arxiv.org/abs/2607.18597)

**<font color=#1a73e8>作者：</font>** Shuangyao Huang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Counterfactual credit assignment has proven effective in multi-agent reinforcement learning (MARL) for discrete action spaces, yet its extension to continuous-action cooperative tasks remains challenging. Existing methods that approximate the counterfactual baseline via Monte Carlo sampling often introduce bias into policy gradients and fail to guarantee convergence to local optima, as the sampled actions may not have been sufficiently trained. To address these limitations, we propose SAFE, a novel MARL framework that employs a counterfactual baseline conditioned on a self-evolving default action sampled from each agent's experience buffer. This design naturally extends to continuous action spaces without relying on additional simulations, reward models, or environment-specific prior knowledge. The baseline accurately quantifies each agent's contribution, and introduces no bias into the deterministic policy gradient, ensuring convergence to local optima. Extensive experiments on cooperative vehicular tasks demonstrate that SAFE consistently outperforms state-of-the-art models.

---


### 85. [Designing for What Cannot Be Seen: Supporting Embodied String Learning for Musicians with Blindness and Low-Vision](https://arxiv.org/abs/2607.18598)

**<font color=#1a73e8>作者：</font>** Shi Shi, Lingyun Chen, Zitao Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Bowed string instruments demand fine-grained bodily coordination that is typically taught through visual demonstration, creating persistent barriers for musicians with blindness and low-vision (BLV). To understand these challenges and explore new design opportunities, we conducted a design study with four advanced string musicians with BLV and three of their instructors. Our team, spanning violin performance and music education, disability studies in music, HCI design, and engineering employed a qualitative, multi-method approach including practice video analysis, lesson observation, expert interviews. Our analysis identifies recurring difficulties in right-hand bow control, left-hand coordination, score access, and memory-intensive practice. Building on these findings, we conducted an exploratory design ideation phase informed by empirical findings and feedback from one musician with BLV. We developed speculative design directions that could potentially address identified breakdowns, while acknowledging that these concepts require further evaluation with instructors and in deployed contexts.

---


### 86. [BRIDGE: Bottleneck-Aware Regulator-Set Inference and Diagnosis for Cooperative Gene Regulatory Recovery](https://arxiv.org/abs/2607.18602)

**<font color=#1a73e8>作者：</font>** Maryam Rahimimovassagh, Clayton Thomas Barham, Ivan Garibay 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cooperative gene regulation often depends on groups of regulators acting jointly, but most gene regulatory network (GRN) inference methods output pairwise regulator-target rankings. We introduce Bottleneck-Aware Regulator-Set Inference and Diagnosis (BRIDGE), a framework for complete regulator-set recovery, and Targeted Recovery Attribution for Cooperative Evaluation (TRACE), a diagnostic suite that attributes failures to retrieval, set-level scoring, decoding, and evaluation bottlenecks.
TRACE includes a leak-free mechanism-mismatch cooperativity stress test in which cooperative targets are generated by random nonlinear mechanisms rather than product interactions. This design avoids feature-mechanism circularity: Residual higher-order set scoring (Residual HOS2) operates on raw expression vectors without handcrafted product-correlation features. Across 30 matched seed-cooperativity settings, Residual HOS2 improves Jaccard similarity from 0.382 to 0.460, recall from 0.522 to 0.597, and exact recovery from 0.053 to 0.113 over a decomposable pairwise set scorer (PairS2), although exact recovery remains low.
On SERGIO DS3, oracle retrieval and TRACE show that candidate coverage is necessary but insufficient because set-level misranking remains the dominant source of exact-recovery failure. PairS2 proposal followed by Residual HOS2 reranking reduces HOS2-scored candidate sets by 94-97% while largely preserving exact-recovery behavior. These results distinguish edge ranking, candidate retrieval, set-level scoring, and exact cooperative regulator-set recovery as separate objectives.

---


### 87. [Understanding ADHD Productivity in Construction Work: Toward AI-enabled VR Interventions](https://arxiv.org/abs/2607.18605)

**<font color=#1a73e8>作者：</font>** Zinat Ara, Behzad Esmaeili, Lap-Fai Yu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Attention-Deficit/Hyperactivity Disorder (ADHD) is identified as the most prevalent neurodivergent condition in the construction industry. While the construction industry may broaden employment opportunities, little is known about how ADHD traits shape workers' performance, sustained attention, and situational awareness in dynamic job-site environments. This work presents an exploratory interview study aimed at understanding how ADHD traits influence construction-specific productivity and how future interventions can reduce challenges while amplifying strengths. We conducted semi-structured interviews with construction workers with ADHD, safety managers, and ADHD researchers to capture their perspectives on attentional demands, task coordination, and workplace adaptation. As part of these discussions, participants also reflected on the potential of combining artificial intelligence (AI) and virtual reality (VR) to support future ADHD workers. Our analysis identifies two overarching themes: (1) workplace challenges, capturing difficulties that arise from both the nature of construction work and the specific needs of ADHD workers, and (2) productivity support strategies, describing effective methods to sustain focus and task engagement. Further, we derive design requirements for AI and VR-enabled interventions that provide adaptive attentional scaffolding, mediated social presence, and motivational support. We conclude by discussing how these insights can inform the future development of ADHD productivity enhancement support.

---


### 88. [LatentMT: Machine Translation with Latent Reasoning](https://arxiv.org/abs/2607.18618)

**<font color=#1a73e8>作者：</font>** Wei-Rui Chen, Samar M. Magdy, Chiyu Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Latent-reasoning looped language models (LoopLMs) offer a different scaling path for machine translation (MT): instead of increasing parameter count or emitting explicit chain-of-thought tokens, they spend additional recurrent computation inside hidden states. We introduce LatentMT, the first systematic study of latent-reasoning LoopLMs for machine translation. LatentMT adapts a small 2.6B-parameter backbone model with lightweight training. Across 32 translation directions spanning high-, mid-, and low-resource languages, LatentMT achieves performance comparable to models three to five times larger. It is competitive in a high-resource language and achieves state-of-the-art performance on both mid-resource and low-resource languages. Studying the behavior of scaling the number of recurrent reasoning steps, we find that recurrent computation consistently improves translation quality in early steps, then saturates quickly afterwards. Our mechanistic analysis shows that hidden-representation differences shrink along the recurrent reasoning-step axis, supporting the observed saturation in performance. Finally, our efficiency analysis shows that LatentMT requires lower training and inference compute than much larger non-latent-reasoning models with similar performance, making latent recurrent computation a promising path toward compact, efficient, and strong machine translation.

---


### 89. [CPInj: Uncovering Prompt Injection Risks in Textual Collaborative Prompt Optimization](https://arxiv.org/abs/2607.18622)

**<font color=#1a73e8>作者：</font>** Xinting Liao, Behnoosh Zamanlooy, Masoumeh Shafieinejad 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Textual Collaborative Prompt Optimization (TCPO) extends Textgrad (Yuksekgonul et al., 2025) to a decentralized setting by allowing multiple clients to jointly improve prompts for large language models (LLMs) while keeping their data locally. Its reliance on free-form textual updating and aggregation introduces a new and largely unexplored attack surface, i.e., malicious instructions can be injected into local prompts and propagated through server-side prompt aggregation. Unlike conventional prompt injection attacks, attacking TCPO targets the collaborative optimization loop in TCPO. This setting is more challenging because malicious instructions must survive aggregation, persist through subsequent benign prompt optimization, and evade server-side defenses. To expose this risk, we propose CPInj, a collaborative prompt injection attack that contaminates the aggregated global prompt with malicious instructions, degrades downstream task performance, resists purification by prompt optimization on benign clients, and evades advanced detection-based defenses on the server. We find that current defense methods are ineffective against CPInj. To mitigate this attack, we further propose a defense-oriented aggregation method, i.e., APAgg, which purifies malicious instructions and partially recovers TCPO utility. We conduct extensive experiments across three LLM families and five reasoning tasks in math, logic, and medicine. The results demonstrate that our proposed attack reveals a critical vulnerability in TCPO. Although we take a first step toward mitigation, the attack remains highly effective and far from fully resolved, calling for more robust defense for TCPO.

---


### 90. [Norm or Direction? Decoding Vision Mambas for High-Resolution Vision](https://arxiv.org/abs/2607.18625)

**<font color=#1a73e8>作者：</font>** Jin Yu, Juyoun Park  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Mamba models replace quadratic self-attention with linear complexity selective state space models (SSMs), emerging as efficient visual backbones. However, MambaOut demonstrates that a Gated CNN block can match or exceed VMamba on image classification, questioning the necessity of SSMs for vision. This raises a fundamental question: do VMamba and MambaOut encode visual information differently at the representation level? To investigate, we apply cross model centered kernel alignment (CKA) analysis and find that VMamba's final stage blocks form representations distinctly different from both MambaOut and its own preceding blocks. We therefore focus on the final block features, decomposing each spatial token into magnitude and direction. MambaOut concentrates class-discriminative information in high-norm foreground tokens that align with Grad-CAM attribution. VMamba, by contrast, produces high-norm tokens predominantly in background regions, misaligned with Grad-CAM, yet preserves discriminative signals primarily in token directions. These observations reveal that the two models rely on different encoding strategies. We connect this difference to high-resolution classification and semantic segmentation. VMamba distributes logit support broadly across object regions, whereas MambaOut relies on sparse dominant tokens, a strategy that becomes less stable as token counts grow. Under full fine-tuning for segmentation, VMamba consistently outperforms MambaOut. These results suggest that VMamba's advantage in dense prediction stems not merely from the SSM mechanism or sequence length, but from how semantic evidence is organized across token magnitude, direction. Ultimately, we conclude that token magnitude and directional structure serve as critical axes for improving visual backbones, particularly under dense supervision.

---


### 91. [BlurDriving: Investigating How Personalized Blur Techniques Impact Drivers' Performance in Virtual Reality](https://arxiv.org/abs/2607.18628)

**<font color=#1a73e8>作者：</font>** Yuan Li, Mark Colley, Xinyue Gui 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Distracted driving remains a major safety concern, motivating approaches that aim to reduce visual overload before attention breaks down. However, visual overload varies across individuals, making it difficult to determine appropriate interventions for each driver. We investigate whether controllable visual blur can simplify the driving scene and mitigate distraction. To address this challenge, we propose BlurDriving, a target-selective, distance-aware blur system in a Virtual Reality (VR) urban driving simulator, and employ a Human-in-the-Loop Multi-Objective Bayesian Optimization (HITL-MOBO) framework to personalize blur configurations. Across two VR user studies, we evaluated driving under normal conditions in Study 1 and under cognitively demanding conditions in Study 2. We found that personalization revealed strong individual differences in blur preference but did not lead to significant improvements in objective driving performance compared to a no-blur baseline. Qualitative feedback revealed polarized responses: some drivers reported improved focus, while others experienced uncertainty, fatigue, or discomfort. These findings suggest that visual blur is not universally effective. Instead, its benefits depend on individual perceptual strategies and tolerance for visual uncertainty. This work highlights the limits of personalized visual simplification in safety-critical driving and informs adaptive in-vehicle interface design.

---


### 92. [Seeing Before Generating: Object Perception Enhances Single-View 3D Reconstruction](https://arxiv.org/abs/2607.18630)

**<font color=#1a73e8>作者：</font>** Y Huynh, Duc Thanh Nguyen, Mohamed Abdelrazek  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The relationship between object perception and reconstruction is well established in human vision, yet remains underexplored in computer vision. In this paper, we demonstrate that learnt object perception can significantly enhance 3D reconstruction. Focusing on the challenging task of single-view 3D object reconstruction, we propose a method that leverages perceptual signals extracted from pretrained perception models capturing semantic and geometric information to drive the reconstruction of an object from its single image. Our approach is model-agnostic and can be integrated into various reconstruction methods in a plug-and-play manner. Experiments with two state-of-the-art single-view 3D reconstruction pipelines in a benchmark dataset show consistent and substantial improvements achieved by our method, validating the effectiveness of incorporating perception into generation. We provide in-depth analysis of various aspects of our method and its application. Our project page is at this https URL.

---


### 93. [Graph Neural Network-based Algorithm Selection for the Traveling Salesman Problem: A Systematic Study of Cost and Rank Losses under Distinct Budget Regimes](https://arxiv.org/abs/2607.18632)

**<font color=#1a73e8>作者：</font>** Zhaoxuan Li, Jiale Yang, Yifei Lu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Automated Algorithm Selection (AS) aims to improve problem-solving performance by selecting, for each problem instance, the most suitable algorithm from a predefined portfolio. This is particularly relevant to the Traveling Salesman Problem (TSP), where solver performance is strongly instance-dependent. We introduce GNNAS-TSP, a Graph Neural Network (GNN)-based AS framework that learns TSP instance representations directly from raw graph data, avoiding manual feature engineering. GNNAS-TSP formulates AS as a joint cost-prediction and ranking task. We evaluate cost-based (mean squared error (MSE), mean absolute error (MAE), and Huber), rank-based (RankNet, ListNet, and LambdaRank), and hybrid learning objectives for a portfolio comprising Chained Lin-Kernighan, Edge Assembly Crossover, Lin-Kernighan-Helsgaun, Multiagent Optimization System, and Concorde. Experiments use fixed computational budgets of 10 and 60 seconds. On the held-out test set, the selected configurations improve on the Single Best Solver (SBS) in normalized solution cost at both budgets. For the 10s budget, AS achieves substantial and statistically significant cost improvement over SBS. Overall, the results suggest that GNNAS-TSP is a useful meta-solving strategy when exploitable variation exists across solver performance.

---


### 94. [Deep Learning Estimation of Sex, Age, Height, and Weight from CT-derived Digitally Reconstructed Radiographs](https://arxiv.org/abs/2607.18638)

**<font color=#1a73e8>作者：</font>** Tomohiro Kikuchi, Kohei Yamamoto, Yukihiro Nomura 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Purpose: To develop and validate a deep learning ensemble for estimating adult sex, age, height, and weight from coronal digitally reconstructed radiographs (DRRs) generated from diagnostic CT. Materials and Methods: This retrospective study included 128,621 CT examinations from 80,004 adults at nine institutions in Japan. Three multitask models-ConvNeXt-Base, ViT-Base/16, and MaxViT-Base-were fine-tuned using coronal DRRs and combined by weighted averaging. Data were split by institution into training (114,147 examinations; seven institutions), tuning (4,305; one institution), and test (10,169; one institution) sets; generalizability was assessed on two non-Japanese datasets. Accuracy and mean absolute error (MAE) were used to evaluate sex classification and age, height, and weight regression, respectively. Body surface area (BSA)-corrected heart and liver volume trends were compared using true versus estimated height and weight. Results: In the test set (median age, 69.9 years; 4,899 of 10,169 [48.2%] male), overall sex-classification accuracy was 0.997 (95% CI, 0.996-0.998), and MAEs were 3.57 years (3.51-3.63), 2.59 cm (2.54-2.64), and 3.40 kg (3.34-3.47) for age, height, and weight, respectively. In examinations covering the chest through pelvis, accuracy was 1.000, and MAEs were 3.15 years, 2.28 cm, and 3.18 kg, respectively. BSA calculated from estimated values reproduced age-related heart and liver volume trends obtained using true values. On non-Japanese datasets, height error increased but was reduced by continued fine-tuning. Conclusion: The ensemble estimated adult sex, age, height, and weight from CT-derived DRRs, with generally lower errors in examinations with broader anatomical coverage.

---


### 95. [Spaghetti Architect: A Contamination-Resistant, By-Construction-Labelled, Multi-Language Code Dataset Generator](https://arxiv.org/abs/2607.18642)

**<font color=#1a73e8>作者：</font>** Yuxiang Ji  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mined code corpora are abundant but uncontrolled: a snippet's semantics, surface "messiness," and difficulty are whatever the wild contained; there is no known-optimal reference to grade against; and any public sample may already sit in a model's training set. We present Spaghetti Architect, a tool that mints code datasets with the control such corpora lack. An anti-optimization transpiler maps a clean, language-agnostic JSON intermediate representation to deliberately redundant, fully-flattened programs in five languages (Python, JavaScript, Go, Java, C++); every program is compiled, run, and checked against a reference oracle, so each instance is correct by construction. The clean IR is a known-optimal reference, messiness is dialed by strictly-nested anti-pattern profiles, each instance is labelled along two orthogonal difficulty axes, intrinsic (problem size) and incidental (presentation at fixed semantics), and contamination is resisted by minting fresh variants from a private held-out seed. We give construct-validity evidence that the quality order moves established complexity and readability metrics, and report baselines on a four-model open ladder: exact match rises with scale, and the intrinsic knob collapses arithmetic-aggregation accuracy of even the strongest model to zero. Further, development-set scores equal freshly re-minted held-out counterparts within $|\Delta|\le 0.012$ (comprehension) and $\le 0.011$ (refactoring); on identical programs, refactoring equivalence ($0.73 \rightarrow 0.99$) is scale-invariant while output prediction collapses; and ablating the generator's self-annotations shows they inflate the weakest model an order of magnitude more than the strongest ($-0.173$ vs $-0.017$): the annotated ladder resolves one of three adjacent pairs where the unannotated resolves all three. Open source (MIT), dependency-free, archived under a persistent DOI.

---


### 96. [Fluid-SDF: Ultra-Lightweight and Editable Implicit Shape Representation via Differentiable Primitives](https://arxiv.org/abs/2607.18646)

**<font color=#1a73e8>作者：</font>** Pradyumna Sripada, Chinmay Nadgir, Ksheer Agrawal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Implicit Neural Representations (INRs) have become the standard for continuous 2D shape modeling, but they suffer from black-box uneditability, vulnerability to noise, and high parameter counts that severely hinder deployment on edge devices. We introduce Fluid-SDF, a highly compressed, differentiable Constructive Solid Geometry (CSG) framework that models shapes using explicit geometric primitives blended via a smooth minimum function. By replacing traditional multi-layer perceptrons (MLPs) with a parameterized primitive engine, Fluid-SDF reconstructs complex, non-convex topologies using strictly under 100 parameters, achieving comparable or superior intersection-over-union (mIoU) to standard neural baselines. Furthermore, we demonstrate that Fluid-SDF acts as a powerful geometric prior, inherently resisting high-frequency dataset noise where capacity-matched neural networks catastrophically overfit. Finally, unlike standard INRs, Fluid-SDF's explicit parameter space allows for direct, zero-shot user editing of local and global shape features without retraining. By bypassing expensive on-device gradient updates entirely, Fluid-SDF is uniquely suited for mobile AI, augmented reality, and resource-constrained embedded environments

---


### 97. [DeforM: Reasoning-Guided Physics-Aware Video Generation via Spatial-Temporal Masking](https://arxiv.org/abs/2607.18664)

**<font color=#1a73e8>作者：</font>** Yunyi Li, Yu Qiao, Yaohui Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video generation models achieve high visual quality but often struggle to generate physics-aware videos. Unlike rigid-body motion, which can be described by explicit trajectories or formulas, complex deformation dynamics remain challenging to synthesize. We observe that a lack of physical reasoning for localizing dynamic areas allows irrelevant regions to dilute the model's attention, leading to generation failure. In this paper, we propose DeforM, a reasoning-guided image-to-video generation framework that directs the model's focus toward physics-critical regions. To reason about and localize these critical regions, we introduce a VLM-guided physical reasoning module, DeforM-Reason, to identify target objects and generate spatial-temporal masks. For physical guidance, we develop two alternative strategies: DeforM-Free for training-free mechanism analysis and DeforM-Injection as a powerful training-based generator. Experimental results demonstrate that DeforM improves the realism of generated deformation scenarios, outperforming baseline models in both visual quality and physical consistency.

---


### 98. [SciHazard: A Benchmark for Measuring Scientific Safety Risks with Decomposed Harm Scoring](https://arxiv.org/abs/2607.18665)

**<font color=#1a73e8>作者：</font>** Chunxiao Li, Yuan Xiong, Lijun Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) increasingly support science, but they can also convert hazardous scientific knowledge into actionable misuse guidance. Existing benchmarks often rely on templated queries disconnected from real-world hazards, and employ LLM-as-a-Judge paradigms without domain grounding. To address this, we introduce SciHazard, a real-world-grounded benchmark for scientific risks and a dataset agnostic evaluation framework for measuring harmfulness. SciHazard contains 2400 hazardous questions and 600 oversafety questions across 12 disciplines, with both queries grounded in regulated entities and documented failure scenarios. To compute \textsc{DeHarm-Score} , we develop a decomposed evaluating procedure that combines query hazard severity, refusal behavior, and response-level risk. For non-refused responses, it further decomposes response-level harm into \textsc{Executability}, quantified via dynamic checklists with importance weighting, and \textsc{Net-new risk}, assessed through retrieval-augmented claim extraction and synthesis-barrier verification. An expert-validation study shows that \textsc{DeHarm-Score} improves agreement with expert annotations by 90.17\% over the strongest baseline. We benchmark 31 frontier LLMs and deep research agents in an extensive scientific safety evaluation. Notably, deep research agents yield 32.3\% higher mean \textsc{DeHarm-Score} than standard LLMs, exposing autonomous agents as a critical blind spot in current safety defenses. Code and dataset are available at this https URL.

---


### 99. [Fusion Embedding: A Unified Embedding Space for Text, Image, Video, and Audio](https://arxiv.org/abs/2607.18666)

**<font color=#1a73e8>作者：</font>** Abdul Basit Tonmoy, Kazi Fardinul Hoque, Md. Shahrier Islam Arham 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A single embedding space that covers text, images, video, and audio lets one index serve every query a user can pose. Embedding models built on vision-language backbones now lead text/image/video retrieval benchmarks but lack audio entirely, while audio-text retrieval is led by specialist systems that serve no other modality. We present the Fusion Embedding family, which adds audio to a frozen vision-language embedding base whose parameters are never updated: generation 1 (fusion-embedding-1) trains only a 16.4M-parameter connector between a frozen audio tower and the frozen base, and generation 2 (fusion-embedding-2) adds modality-gated deep adapters (44.2M parameters) whose branch never executes on text, image, or video inputs: their outputs are bit-for-bit those of the released base, verified after every training run. Because the base already binds text, images, and video, aligning audio to text alone makes audio-image retrieval emerge, with zero paired audio-visual training data. Alongside the recipe we map its design space with controlled negative results (rewriting training captions with an LLM, substituting a leaderboard-stronger audio tower, and widening the connector each reduce retrieval) and with training-protocol findings that we expect to transfer to any frozen decoder-LM embedding backbone. Both generations train in hours on a single GPU. Weights, code, and the evaluation harness are openly released.

---


### 100. [PeakFlow: Peak-Guided Coarse-to-Refined Modeling for EEG-Based Dynamic Affective Trajectory Prediction](https://arxiv.org/abs/2607.18671)

**<font color=#1a73e8>作者：</font>** Hao Tang, Songyun Xie, Xinzhou Xie 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Most existing EEG-based emotion recognition studies formulate affective decoding as static category prediction, although emotions elicited by continuous stimulation evolve over time, accumulate, reach peak intensity, and then recover. This motivates EEG-based dynamic affective trajectory prediction, which estimates continuous affective intensity curves from sequential EEG observations. Existing temporal regression models can capture coarse intensity trends but often fail to preserve peak-centered structure, leading to inaccurate peak timing and terminal-peak bias, where the predicted maximum is shifted toward the end of a trial. To address this issue, we propose PeakFlow, a peak-guided coarse-to-refined framework for EEG-based dynamic affective trajectory prediction. PeakFlow first learns a coarse affective flow through EEG temporal tokenization and masked temporal modeling, then applies a lightweight residual refiner for peak-guided bounded calibration. The refiner uses trajectory-aware cues and a peak-centered objective combining global trajectory consistency, peak-zone emphasis, peak-probability localization, terminal suppression, and residual regularization. This design preserves the global affective trend while correcting peak misalignment, peak-value deviation, and false-terminal predictions. Leave-one-subject-out experiments on SEED-VII show that PeakFlow improves both global trajectory fitting and peak-centered temporal reliability over strong dynamic modeling baselines. Auxiliary evaluation on FIRMED further suggests its potential for sparse peak-centered ordinal intensity analysis. These results highlight the importance of peak-aware modeling for temporally faithful EEG-based dynamic emotion prediction. Code is available at this https URL.

---


> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-241](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
