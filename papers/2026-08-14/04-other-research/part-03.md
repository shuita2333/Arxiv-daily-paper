# 📦 其他研究 | 2026年08月14日

> 本类共 **202** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-202](./part-05.md)

---

### 101. [EGM-Det: Entropy-Guided Multimodal Adaptive Fusion for UAV RGB-IR Object Detection](https://arxiv.org/abs/2608.11685)

**<font color=#1a73e8>作者：</font>** Cunzheng Fan, Dawei Yan, Guanlin Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Joint use of RGB and infrared (IR) imagery can improve UAV-view object detection, but most existing methods fuse multimodal features with static or fixed weights and therefore overlook spatially varying modality reliability. We propose EGM-Det, an entropy-guided multimodal adaptive fusion framework for RGB-IR object detection. EGM-Det employs a dual-stream architecture to preserve modality-specific representations and introduces an Entropy Offset Gate Fusion module for adaptive multi-scale fusion. The module derives shallow entropy priors from input intensity, local entropy, and cross-modal discrepancy, and uses them to guide local offset alignment and spatial-channel gated fusion. It therefore selectively aggregates reliable RGB and infrared cues instead of uniformly combining heterogeneous features. We further introduce cross-modal distillation to regularize the learned fusion gates and reduce fusion degradation. Each student branch extracts complementary knowledge from the cross-modality teacher branch matched to the main branch, while entropy-adaptive supervision emphasizes uncertain modality decisions. Experiments on DroneVehicle, LLVIP, and VEDAI demonstrate state-of-the-art performance across all three benchmarks; in particular, EGM-Det outperforms prior approaches by more than 10 percentage points on VEDAI.

---


### 102. [Drift and Dependence: Layer-wise Information-Theoretic Bounds for Replay-Based Continual Learning](https://arxiv.org/abs/2608.11690)

**<font color=#1a73e8>作者：</font>** Tieliang Gong, Zhongbo Zhang, Wen Wen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continual learning must absorb new tasks without erasing old ones, and replay---mixing a small buffer of past examples into current training---is among the most effective remedies for catastrophic forgetting. Yet its generalization behavior is shaped by two coupled effects that existing analyses fold into a single hypothesis-level quantity: finite memory replaces each past distribution with an empirical proxy, and repeated reuse couples the buffer, the current data, and the final hypothesis through a shared optimization trajectory. We develop a layer-wise information-theoretic framework that separates these effects at every depth. Our main result decomposes the expected generalization gap into a replay-induced representation drift and an optimization-dependence term, the latter further resolved into stability, plasticity, interaction, and residual-coupling components. Two refinements make the framework operational. A Wasserstein relaxation of the drift term, valid under support mismatch, yields a depth-dependent drift--sensitivity trade-off whose minimizer identifies which interior layer to stabilize. An SGLD instantiation of the optimization term reduces it to a trajectory-level log-determinant budget, exposing a curvature-aware gradient-alignment statistic that serves as an online diagnostic of task-wise forgetting. Controlled and benchmark experiments confirm the predicted memory scaling, the interior funnel, and the alignment signal's link to forgetting.

---


### 103. [Boundary-Enhanced Segmentation of Pig Point Clouds in Commercial Housing Environments](https://arxiv.org/abs/2608.11697)

**<font color=#1a73e8>作者：</font>** Zhankang Xu, Fei Shi, Xiangyu Qi 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In real pigsty environments, pig point clouds often come into close contact with background structures, resulting in blurred target boundaries, local adhesion, and background mis-segmentation. This reduces the accuracy of subsequent point cloud completion and body size measurement. To address these challenges, this study proposes a pig point cloud segmentation method based on boundary feature analysis. The proposed method adopts Octree Transformer as the backbone network and integrates local geometric details with global semantic context through octree convolution, self-attention encoding, and multi-scale feature fusion. Furthermore, soft-distance boundary pseudo-labels are generated to provide continuous boundary supervision, and a bidirectional cross-boundary semantic module is designed to enable explicit interaction between boundary and semantic features. Experiments conducted on a comprehensive dataset demonstrate that the proposed method significantly outperforms various state-of-the-art models in terms of segmentation accuracy, mean intersection over union, and boundary delineation. The results indicate that the method effectively alleviates boundary adhesion, providing reliable point cloud inputs for downstream precision livestock farming tasks.

---


### 104. [Robust and Efficient Noisy-Label Time-Series Classification via Dynamic Time Warping Based Granular Ball Computing](https://arxiv.org/abs/2608.11704)

**<font color=#1a73e8>作者：</font>** Ziqiang Li, Yun Liu, Gouhei Tanaka  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dynamic Time Warping (DTW)-based Nearest-Neighbor (NN) classifiers are effective for time-series classification but are vulnerable to mislabeled training samples and require numerous DTW computations during inference. We propose DTW-based Granular Ball Computing (DTW-GBC), which organizes temporally similar training samples into granular balls and performs classification at the granule level. We further develop two granular-ball construction strategies for DTW-GBC. Experiments on four benchmark datasets with symmetric label noise show that the two DTW-GBC variants generally mitigate the performance degradation caused by label noise while requiring substantially fewer comparisons than DTW-based 1-NN during inference. These findings suggest that DTW-GBC provides a favorable balance between classification robustness and inference efficiency.

---


### 105. [A Browser-Based Gesture-Driven Avatar Interaction Framework for Metaverse Onboarding Environments](https://arxiv.org/abs/2608.11708)

**<font color=#1a73e8>作者：</font>** Deepti Parachuri, Chhayank Sahu, Sameer Singh Choudhary  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Avatar interaction shapes how engaging and immersive a metaverse experience feels, and for that interaction to feel natural, avatars need to respond to users without forcing them through a controller-based interface first. This paper describes a gesture-driven interaction layer built for a browser-based metaverse onboarding environment, where users explore a set of virtual rooms as an avatar and interact with embedded video, document, and quiz content using hand, arm, and head gestures instead of a keyboard or controller. The system combines real-time gesture recognition (Google MediaPipe) with two alternative locomotion techniques - hand-raise navigation and in-place walking - so users can trade off precision against physical immersion depending on the task. The contribution is the integration, deployment, and evaluation of these techniques as a single lightweight, web-deployable, controller-free interaction model, assessed through a structured internal onboarding session with five participants. We report what worked, what didn't, and the design trade-offs that came out of combining these techniques in one deployed system.

---


### 106. [High-dimensional Multi-objective Bayesian Optimization with Learned Variable Interactions](https://arxiv.org/abs/2608.11713)

**<font color=#1a73e8>作者：</font>** Hongyan Wang, Jiayu Huang, Haotian Zheng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-objective Bayesian optimization (MOBO) is effective in identifying the Pareto fronts for expensive black-box problems. However, most current MOBO approaches are limited to low-dimensional decision space due to its exponential sampling complexity. This paper presents decision variable interaction analysis-based MOBO, ViaMOBO, a generic framework for expensive multi-objective problems with high-dimensional decision space. The key idea of ViaMOBO is that it utilizes a variable interaction analysis model to determine whether the decision space can be completely or partially divided, and then performs local Bayesian optimization in the divided decision subspaces. Through the variable analysis model, it can be derived whether the objectives in black-box problems are separable, partially separable, or non-separable based on the potential independent or interdependent relationships among decision variables without any strong assumptions. We compare ViaMOBO with the state-of-the-art MOBO methods on both synthetic and real-world benchmarks. The experimental results demonstrate that ViaMOBO outperforms other related MOBO baselines in approximating the Pareto front of high-dimensional expensive multi-objective problems.

---


### 107. [Proportional Analogies on Probability Distributions via Bayesian Updating](https://arxiv.org/abs/2608.11724)

**<font color=#1a73e8>作者：</font>** Pierre-Alexandre Murena  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Analogies are quaternary relations of the form "A is to B as C is to D". Among the various formalizations of analogical reasoning, proportional analogies provide an important axiomatic framework by characterizing valid analogies through a set of postulates. While proportional analogies have been extensively studied over Boolean, symbolic, and real-valued domains, their extension to probability distributions remains largely unexplored. In this paper, we introduce a notion of proportional analogy for probability distributions based on Bayesian updating. Our approach builds upon the idea that two distributions are related whenever one can be transformed into the other through Bayesian updating induced by a suitable set of observations. We investigate this framework for several standard members of the exponential family and discuss how it naturally extends to arbitrary probability distributions through Gaussian mixture approximations.

---


### 108. [Plaintext Recovery Against Post-Filtering Access Control](https://arxiv.org/abs/2608.11730)

**<font color=#1a73e8>作者：</font>** Zachary Espiritu, David Cash  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Fine-grained access control (FGAC) mechanisms such as row-level security (RLS) and document-level security (DLS) are widely deployed in databases to restrict access to data stored in physical indexing structures shared by multiple users (e.g., in multi-tenant databases, or in the implementation of least-privilege within an organization). FGAC implementations often use post-filtering where untrusted queries run over all data and private results are redacted afterwards. Prior work shows this approach can lead to side-channels that enable attackers to test if a chosen value exists in unseen data. While damaging, prior attacks do not enable the efficient recovery of rich, high-entropy data like full records or text documents.
We show these side-channels are more damaging than previously thought. Using rich query interfaces (e.g., range, prefix, and conjunctive predicates), we amplify existence leakage into reconstruction attacks. We do this in two settings:
- PostgreSQL (RLS timing). We exploit a timing side-channel and expressive SQL queries (e.g., ranges, conjunctions) to enumerate unknown attribute values and, in turn, full records via binary search over large domains.
- Elasticsearch/OpenSearch (DLS scoring). We exploit scoring and prefix-expansion side-channels to recover indexed terms from documents. In some cases, we can extract $n$-grams in the corpus to recover approximate text.
Our results show that FGAC side-channels must be evaluated in the presence of rich predicates, which can turn membership tests into scalable reconstruction of high-entropy records.

---


### 109. [Fingerprinting Text-to-Image Diffusion Models via Collapsed Generation](https://arxiv.org/abs/2608.11732)

**<font color=#1a73e8>作者：</font>** Yuanmin Huang, Chen Chen, Geng Hong 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Proprietary text-to-image diffusion models are increasingly distributed as hosted services and downloadable checkpoints, making their intellectual property (IP) protection an increasingly critical concern when model leakage, copying, or unauthorized fine-tuning is disputed. In this work, we present a non-invasive model fingerprinting framework based on \emph{collapsed generation}, a phenomenon where certain input conditions produce highly consistent images across multiple stochastic seeds. We show that collapsed generation is an intrinsic, model-dependent property of the learned generation process. These collapse-prone conditions therefore expose model-specific behavioral signatures, enabling reliable ownership verification without embedding invasive watermarks. After preparing conditions on the source model, the framework verifies a suspect model under two access settings: (1) white-box pipeline access, where optimized continuous embeddings can be injected into the generation process, and (2) black-box API-only access, where natural language prompts are queried through the service interface. In both cases, ownership evidence is measured by whether the suspect model reproduces the source model's collapse behavior across stochastic samplings. Extensive experiments across UNet- and transformer-based diffusion models show that collapsed generation fingerprints can distinguish different source models with low confusion. These fingerprints remain verifiable in fine-tuned derivatives and under common and adaptive model- or query-level obfuscations, while requiring only a modest verification query budget. Together, these results establish collapsed generation as a reliable intrinsic evidence source for non-invasive diffusion model ownership verification.

---


### 110. [Epiplexity Guided Data Selection and Generation for Out-of-Distribution Generalization](https://arxiv.org/abs/2608.11746)

**<font color=#1a73e8>作者：</font>** Ellen Su, Andres Potapczynski, Shikai Qiu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern systems are increasingly expected to transfer across tasks not specified during training. What data facilitates generalization in these new, unanticipated settings? One hypothesis is that data with more structural information could contain shared circuits and subprograms that could be recycled in a wider array of downstream settings. Epiplexity, a recently proposed measure of the structural information a compute-bounded learner can extract from data, provides a mechanism to reason about this relationship. In this paper, we show how to operationalize epiplexity as an online training signal for data selection and synthetic data generation. For selection, we fit scaling laws to the training loss curves of natural data domains to predict the expected epiplexity gain as a function of training tokens, and use this signal to adaptively determine the sampling weights over domains during training. For synthetic data generation, we define a generator's reward as the change in learner epiplexity over a buffer of previously generated data and use REINFORCE policy gradients to guide the generator toward an epiplexity-maximizing distribution. In both cases, higher epiplexity predicts improved downstream performance on zero-shot and fine-tuning based tasks, supporting the hypothesis that data rich in structural information yield representations that transfer across domains.

---


### 111. [Making Every Step Count: Spatio-Temporal Information Allocation for Imaging Inverse Problems](https://arxiv.org/abs/2608.11747)

**<font color=#1a73e8>作者：</font>** Yi Cao, Xiangyong Cao, Pei Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Flow-based generative models have emerged as powerful image priors for training-free inverse problem solving, capturing coherent semantics and fine-grained structure. Despite these strengths, existing flow-based inverse solvers primarily focus on the design of individual updates, largely overlooking spatio-temporal information allocation under a fixed number of function evaluations (NFEs). Temporally, insufficient early exploration can trap the flow trajectory in an incorrect semantic basin, whereas excessive allocation of NFEs to early stages leaves little budget for late-stage refinement. Spatially, data consistency provides direct constraints only within observed regions, whereas the recovery of missing regions relies mainly on the generative prior. To address these two issues, we introduce two complementary and training-free components, i.e., Spectrum-Adaptive Scheduling (SAS) and Measurement-Prioritized Attention (MPA). For temporal allocation, SAS distributes the available NFEs over flow time according to the degradation spectrum and logSNR geometry, thus better balancing semantic exploration and detail refinement. For spatial propagation, MPA exploits data-prior conflicts to guide information toward weakly constrained regions, thereby enhancing semantic and structural fidelity. Extensive experiments on standard image inverse problems, e.g., super-resolution, motion deblurring, and inpainting, demonstrate that the proposed components can be integrated into existing flow-based inverse solvers in a plug-and-play manner without retraining or additional flow-model evaluations, and can also significantly improve the restoration quality of existing solvers.

---


### 112. [Dual Modality Prompted Diffusion Priors for Zero Shot Hyperspectral Pansharpening](https://arxiv.org/abs/2608.11748)

**<font color=#1a73e8>作者：</font>** Pengwei Xie, Fei Zhu, Jiajun Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hyperspectral pansharpening aims to reconstruct a high resolution hyperspectral (HRHS) image from a panchromatic (PAN) image and a low resolution hyperspectral (LRHS) image while preserving both spatial details and spectral fidelity. Recent diffusion based methods exploit pretrained image priors by generating a low dimensional representation and subsequently mapping it to the hyperspectral domain. However, the observed panchromatic and hyperspectral images are typically imposed only through external reconstruction objectives, limiting their direct interaction with the diffusion prior. To address this issue, we propose dual-modality image-prompted diffusion model (DIDM) for zero shot hyperspectral pansharpening. DIDM encodes the low resolution hyperspectral and panchromatic observations into spectral and spatial prompt tokens, respectively, and injects them into intermediate features of a frozen remote sensing diffusion model through cross attention, allowing complementary spectral and spatial information to directly guide diffusion feature evolution. In addition, we introduce a panchromatic guided weighted pixel aware total variation regularizer that combines low resolution hyperspectral degradation fidelity and panchromatic response fidelity with gradient adaptive structural regularization, thereby preserving structural discontinuities while suppressing spurious variations in homogeneous regions. Extensive experiments on Pavia, Chikusei, and Houston under reduced resolution protocols show that DIDM achieves the best performance across all evaluated metrics, while full resolution evaluation on FR1 yields the highest HQNR among the compared methods. These results demonstrate that internal dual modality prompting and panchromatic guided structural regularization provide an effective balance between spatial detail enhancement and spectral preservation.

---


### 113. [MOON: Multi-Objective OrthoNormalized Updates for Multitask Learning](https://arxiv.org/abs/2608.11749)

**<font color=#1a73e8>作者：</font>** Shiji Zhou, Kunlin Lyu, Lei Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-objective optimization (MOO) has demonstrated significant success in multi-task learning by mitigating task conflicts through gradient manipulation. However, most existing methods flatten model parameters into vectors and perform gradient manipulation under Euclidean geometry, thereby overlooking the matrix structure prevalent in modern architectures such as Transformers. In this paper, we show that gradient manipulation in Euclidean space does not generally yield the steepest descent direction under matrix geometry, potentially limiting optimization efficiency. Drawing from the theory of steepest descent for matrix-valued parameters, we propose MOON (Multi-Objective OrthoNormalized Updates), which performs gradient manipulation under spectral--nuclear norm geometry and uses the orthonormalized manipulated gradient for parameter updates. Theoretically, for smooth non-convex objectives, we establish convergence of the averaged Pareto-stationarity measure at rates of $\mathcal{O}(T^{-1/2})$ in the deterministic setting and $\mathcal{O}(T^{-1/4})$ under stochastic gradients. Empirical results across various benchmarks show that MOON consistently improves both optimization efficiency and final multi-task performance. Our code is available at this https URL.

---


### 114. [UniSwap: Streaming Audio-Visual Identity Swapping for Talking Videos](https://arxiv.org/abs/2608.11752)

**<font color=#1a73e8>作者：</font>** Yuxuan Zhang, Haozhong Xiong, Jiayi Song 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Talking-video character replacement requires coordinated transfer of appearance and voice while preserving the source motion, scene, linguistic content, and audio-video timing. Existing methods use separately optimized models for the two modalities, making audio-visual consistency difficult to enforce. We present UniSwap, the first framework for streaming joint audio-visual identity replacement in talking videos. Given a source video, a reference image, and a reference voice clip, UniSwap transfers the reference appearance and vocal timbre within a single audio-visual diffusion transformer while preserving the source content and dynamics. To address the scarcity of aligned cross-identity training pairs, we introduce a swap-and-reconstruct pipeline that removes visual and vocal identity from real clips and uses the original clips as reconstruction targets. Starting from a bidirectional backbone, we progressively adapt the model through In-context Pretraining for joint replacement, Conditional Streaming Adaptation for block-causal KV-cached generation, and Efficient Self-forcing DMD for mitigating exposure bias and reducing sampling from 30 to 3 denoising steps per block. Efficient Multi-LoRA Switching enables the three DMD roles to share a single frozen backbone. Feature-RoPE Decomposition keeps cached positions within the training range, supporting stable long-form inference. Experiments demonstrate strong audio-visual synchronization, competitive identity preservation, efficient streaming, and stable long-form generation.

---


### 115. [Automated binary classification of hazelnut X-ray images: A deep-learning benchmark for quality assessment](https://arxiv.org/abs/2608.11759)

**<font color=#1a73e8>作者：</font>** Giancarlo Sportelli, Nicola Belcari, Roberta Pace 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Non-destructive X-ray imaging can reveal internal hazelnut defects that are difficult to detect by external inspection alone; however, automated interpretation remains challenging because of subtle radiographic differences among classes, marked class imbalance, and limited annotated data. Here, we present a benchmark for binary hazelnut quality classification (healthy versus defective) based on 799 segmented single-kernel X-ray images (224 x 224 pixels, grayscale), grouped into 101 acquisition units. Seven single-model configurations and ten probability-aggregation ensembles were evaluated using a group-wise split-rotation protocol across five data splits generated using different random seeds. Decision thresholds were selected on the validation set, and performance was assessed deterministically on validation and test sets. Under the expert-reassessed annotation condition, the average-probability ensemble of the binary cross-entropy-trained convolutional neural network and frozen Swin Transformer achieved the highest mean balanced accuracy (86.3% +/- 1.8%, five seeds), with several other ensembles providing comparable performance. Across methods, substantial split-to-split variability was observed, indicating that multi-split evaluation is essential for reliable model comparison at this dataset scale. Expert reassessment of ambiguous samples improved the performance of all 17 evaluated methods by 2.8-8.1 percentage points, while having only a limited effect on cross-split variance. The results highlight both the potential of deep learning for automated X-ray-based hazelnut quality assessment and the importance of rigorous evaluation and label curation in small, imbalanced agricultural imaging datasets.

---


### 116. [ProBAG: Prototype-Guided Boundary-Aware Graph Diffusion for Weakly Supervised Histopathology Segmentation](https://arxiv.org/abs/2608.11765)

**<font color=#1a73e8>作者：</font>** Duy-Dong Nguyen, Le-Van Thai, Hoai Nhan Pham 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Weakly supervised semantic segmentation enables histopathology tissue segmentation from image-level annotations, avoiding costly pixel-level labeling by expert pathologists. However, CAM-based methods often localize only highly discriminative regions and remain unreliable near tissue interfaces. We propose ProBAG, a stage-1 pseudo-mask generator that combines dataset-specific visual prototypes with pathology-aligned CONCH text prototypes over multi-scale frozen UNI features. ProBAG introduces two complementary mechanisms: class-wise power recalibration that reshapes inter-class competition while preserving the total foreground activation mass at each pixel, and one-step graph diffusion in which feature affinities are penalized by a late-transformer attention-context discrepancy used as a soft structural boundary cue. The resulting stage-1 pseudo-masks require neither CRF nor an external segmentation model; for complete two-stage comparison, they additionally supervise a downstream Phikon-FPN segmenter. Experiments on BCSS-WSSS and LUAD-HistoSeg show consistent gains over recent WSSS approaches, while ablations indicate that pathology-aligned text semantics provide the largest improvement and graph refinement provides a smaller complementary gain. The code is available at: this https URL

---


### 117. [HyperANFIS: Enhancing Rule Representation and Interpretability in Adaptive Neuro-Fuzzy Systems via Hyperbolic Geometry](https://arxiv.org/abs/2608.11768)

**<font color=#1a73e8>作者：</font>** Haoran Pei, Zhao Su, Zetao Lin 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The adaptive neuro-fuzzy inference system (ANFIS) is an interpretable reasoning framework capable of generating explicit IF-THEN fuzzy rules, making it suitable for tasks requiring transparent reasoning. However, existing ANFIS models generally construct rule antecedents and perform inference in Euclidean space, limiting their representational capacity and predictive performance. To address this issue, we propose Hyperbolic ANFIS (HyperANFIS), a hyperbolic extension of ANFIS. HyperANFIS preserves the fuzzy semantics and core architecture of conventional ANFIS while performing rule-prototype learning, rule activation, and consequent aggregation in hyperbolic space. It also retains the ability to generate interpretable IF-THEN rules. By exploiting the representational properties of hyperbolic geometry, HyperANFIS strengthens the fuzzy inference process, thereby improving predictive accuracy, inter-rule collaboration, and the credibility of its interpretable rules. Experimental results show that HyperANFIS consistently outperforms the standard ANFIS baseline and various ANFIS variants across all datasets, while also generating higher-quality fuzzy rules.

---


### 118. [Achieving Near-Zero-Overhead Multi-Model Hierarchical Classification in Real-Time Detection Pipelines](https://arxiv.org/abs/2608.11770)

**<font color=#1a73e8>作者：</font>** Vaishnav Raju  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Edge-deployed vision systems in target recognition, surveillance, autonomous vehicles, and drone domains require hierarchical inference pipelines where a detection model identifies objects of interest and downstream classifiers provide fine-grained attribute analysis. Running all models on the GPU creates a serial bottleneck that limits real-time throughput as pipeline stages grow. Modern edge SoCs pair GPUs with dedicated neural accelerators (NPUs, DLAs) capable of concurrent execution, yet deploying custom models on these accelerators remains impractical due to strict operator constraints, quantization incompatibilities, and an undocumented end-to-end pipeline. We target NVIDIA Jetson DLA cores as the representative platform. We present a five-step methodology for zero GPU fallback DLA INT8 deployment of classification backbones, comprising architecture adaptation, manual dynamic range workaround to rescue TensorRT's implicit quantization (recovering 94.0% accuracy from implicit quantization's 75%) for rapid pipeline validation before explicit quantization, quantization-aware training, ONNX graph surgery for DLA compilation, and a concurrent GPU-detection/DLA-classification inference pipeline. We document nine engineering constraints with root-cause analysis and generalizable solutions. Validation on a dual-head person attribute classifier running on DLA alongside a GPU object detector on a Jetson Orin NX demonstrates near-zero pipeline overhead (12.5 vs. 13.3~FPS detector-only at 1080p), with dual-DLA scaling at no additional cost. The methodology is backbone-agnostic and generalizes to any detection-classification edge pipeline.

---


### 119. [Anti-Shortcut Distillation via Temporal Negative Knowledge Transfer](https://arxiv.org/abs/2608.11789)

**<font color=#1a73e8>作者：</font>** Syed Muhammad Raza, Omer Tariq, Jeongbae Son  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Knowledge distillation (KD) trains a compact student by attracting it towards a converged teacher. It is silent about which directions the teacher itself learned to suppress: repulsive and bias-aware objectives exist, but none exploits the teacher's own trajectory to identify what the student should avoid. We observe that the missing signal is already encoded in the teacher's optimization trajectory: features that an early-stage teacher emphasizes but that a converged teacher attenuates are precisely the shortcut directions worth pushing the student away from. We instantiate this observation as \textbf{A}nti-\textbf{S}hortcut \textbf{D}istillation (ASD), a push--pull KD framework that treats the converged teacher $\Tfinal$ as a positive semantic anchor and an early-checkpoint teacher $\Tearly$ as a temporal negative reference. ASD couples two losses: a temporal contrastive loss ($\Ltc$) that places the early-teacher feature as a same-sample negative against in-batch and memory-bank final-teacher features in an InfoNCE objective; and a shortcut suppression loss ($\Lss$) that penalizes student projection onto the top eigenvectors of $\E[\Dh\Dh^{\top}]$, the uncentered second-moment matrix of early-to-final feature displacements. Across 13 teacher--student pairs on CIFAR-100, ImageNet-100, and TinyImageNet, ASD attains the highest clean top-1 accuracy on more than 10 pairs and outperforms standard KD on 12. On CIFAR-100-C corruption robustness, ASD obtains the lowest mean Corruption Error ($86.1$\,mCE) on the most challenging cross-architecture pair (WRN-40-2$\to$ShuffleNet-V2). Mechanistic diagnostics confirm the intended geometry: the ASD student is systematically anti-aligned with the shortcut direction, while its projection onto the robust subspace is substantially larger ($0.45$ vs.\ $0.12$).

---


### 120. [High-Order Liquid Evidence Encoding for Gradual GNSS Spoofing Detection in Autonomous Driving](https://arxiv.org/abs/2608.11790)

**<font color=#1a73e8>作者：</font>** Muhammad Ayub Sabir, Junbiao Pang, Fatima Ashraf  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate Global Navigation Satellite System (GNSS)-based localization is essential for safe and reliable autonomous driving. However, spoofing attacks can manipulate vehicle position estimates. Continuous and subtle attacks are particularly difficult to detect because individual GNSS observations may remain plausible while the inconsistency between GNSS-implied displacement and onboard vehicle motion gradually increases. Existing methods often rely on static vehicle-behavior features or a single residual signal and do not explicitly model this evolution. To address this problem, we propose a causal high-order liquid evidence framework for GNSS spoofing detection. The method first constructs a physics-guided GNSS--motion inconsistency residual by comparing GNSS-implied displacement with onboard-motion-derived displacement. It then forms separate evidence streams for the residual level and its first- and second-order discrete variations, with relevant contextual cues selected according to the evidence order. Each stream is processed by a separate adaptive liquid encoder, and the resulting temporal states are hierarchically coupled to predict spoofing at the window endpoint using only current and past observations. Experiments on three subsets of the real-world AV-GPS dataset show that the proposed method achieves the highest F1-scores among the evaluated temporal models on Dataset~1 and Dataset~3, reaching 0.9535 and 0.9777, respectively. On Dataset~3, it detects both labeled normal-to-attack transitions within four sampling steps. Code and datasets are publicly available at: this https URL.

---


### 121. [PolarSym: Polar Geometry-aware Attention for CAD Floorplan Parsing](https://arxiv.org/abs/2608.11793)

**<font color=#1a73e8>作者：</font>** Kerui Chen, Yiqing Wang, Kangzhou Xin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> CAD plan parsing is a fundamental task in Building Information Modeling (BIM), aiming to automatically extract architectural elements including walls, doors, windows, and furniture from 2D engineering drawings. Existing Transformer-based methods capture global semantic dependencies via self-attention, yet they infer spatial relationships merely from semantic features without explicitly characterizing the intrinsic geometric symmetry of building layouts. Such methods tend to produce mismatched correspondences in long-range matching and complex symmetric spatial layouts. To tackle this limitation, we propose PolarSym, a polar-coordinate geometry-aware attention framework for CAD plan parsing. The framework decouples geometric relationships of buildings into two complementary components, direction and distance, which are modeled independently. Structural consistency is strengthened by directional constraints, while long-range symmetric correspondences are built with distance constraints. A dynamic gating mechanism is adopted to synergistically fuse the two geometric information branches while maintaining the vanilla Transformer architecture. This design boosts geometric modeling capacity with negligible extra computation. Experiments on a public CAD plan parsing dataset show that PolarSym surpasses the reproduced SymPoint V2 baseline by 1.73% PQ, 1.54% RQ and 4.31% mIoU under identical training settings. PolarSym also converges faster and yields more stable optimization. Ablation experiments verify the complementary effects of direction and distance modeling. Our results reveal that PolarSym improves the geometric awareness of Transformers at low computational cost, offering an effective geometric modeling paradigm for CAD plan parsing.

---


### 122. [AmbSentry: Mitigating Sensing Eavesdropping in ISAC Systems by Harnessing Ambient IoT Devices](https://arxiv.org/abs/2608.11799)

**<font color=#1a73e8>作者：</font>** Yifan Zhang, Yu Bai, Riku Jantti 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Integrated sensing and communication (ISAC) has emerged as a pivotal paradigm for 6G networks, enabling the synergistic convergence of spectral and hardware resources to maximize system efficiency. However, the inherent openness of wireless transmission exposes ISAC systems to critical security risks, particularly regarding the privacy of the sensing information. Unauthorized sensing eavesdroppers can extract sensitive target parameters (e.g., range and velocity) by directly estimating open sensing echo channels, rendering traditional data-based protection techniques ineffective. To mitigate this threat, this paper proposes AmbSentry, an ISAC system that prevents the leakage of sensing information to sensing eavesdroppers by harnessing naturally distributed passive ambient IoT (AIoT) devices. Specifically, these AIoT devices are strategically configured to act as cooperative jammers and ghost targets, introducing controllable interference into the sensing environment. Based on the proposed system, we formulate a joint optimization problem to maximize the integrated sidelobe level at the eavesdropper under quality-of-service (QoS) constraints, thereby degrading sensing eavesdropping performance while maintaining sensing and communication performance for legitimate receivers. Since the problem is non-convex, we further develop an efficient iterative algorithm to cooperatively design the transmit beamforming at the base station and the reflection modulations of the AIoT devices based on Dinkelbach transformation and block coordinate descent methods. The detailed results also demonstrate that AmbSentry significantly enhances sensing security, allowing the legitimate sensing receiver to achieve a 14-dB SNR advantage in detection probability and a hundred times lower estimation error compared to the eavesdropper.

---


### 123. [JAPE: Joint Anomaly Prediction and Intrinsic Explanation in Multivariate Time Series](https://arxiv.org/abs/2608.11801)

**<font color=#1a73e8>作者：</font>** Yian Wei, Yuanyuan Yao, Lu Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multivariate time-series anomaly prediction aims to identify whether and when anomalies will occur over a future horizon from historical observations. Existing methods primarily characterize anomalies as deviations in future numerical values, which may overlook subtle dependency changes induced by weak anomaly precursors and provide no native variable-level explanation together with the alert. To bridge these gaps, we propose JAPE, a Joint Anomaly Prediction and Explanation framework that lifts anomaly prediction from numerical-deviation modeling to dependency-structure modeling. JAPE is the first anomaly prediction framework to explicitly model evolving dependency structures for both point-wise alerting and native variable-level explanation. Specifically, JAPE (i) proposes a Decoupled Spatio-Temporal Representation (DSTR) backbone that decouples temporal and spatial modeling and captures lag-aware dependencies via learnable lag aggregation, thereby perceiving structural precursors before numerical deviations emerge; (ii) designs a dual-view alerting mechanism that fuses numerical forecasts with evolving dependency graphs for point-wise anomaly prediction, capturing structural evidence even under subtle numerical deviations; and (iii) presents Native Predictive Explanation (NPE), which directly reuses the predicted dependency graphs to rank variables by structural deviations without additional models or training. Extensive experiments on five real-world benchmarks across three prediction horizons demonstrate that JAPE improves average F1 and AUC-PR by 19.7% and 41.3%, respectively, while improving explainability with 26.6% gain in MRR.

---


### 124. [Towards Model-based Run-time Cybersecurity: On Control-Flow Anomaly Detection, Attack Identification, and Hardware Monitoring](https://arxiv.org/abs/2608.11802)

**<font color=#1a73e8>作者：</font>** Martin Sachenbacher, Martin Leucker, Alexander Weiss 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Methods to increase the resilience of systems to cyber-attacks become increasingly important. Control-flow monitoring provides a principled basis to ensure integrity and detect possible anomalies at run-time. Once anomalies have been detected, so-called attack trees can be used to identify possible types of attacks. However, this approach is vulnerable to camouflage, by which attackers try to evade detection (and correct identification) by deliberately manipulating also the system's observed control flow. In this paper, we outline a model-based approach that provides more robust intrusion detection and attack identification through an architecture that combines software- with hardware-based monitoring. In this approach, software-level observation indicates suspicious activities, while hardware-level monitoring checks them separately in more detail, making it much harder for attacks to camouflage themselves and go undetected. We illustrate the approach with an authentication-service example that captures a realistic failure mode: a software-level observer sees an anomalous but apparently harmless control-flow deviation, maps it to a benign root cause in an attack tree, but misses the true intrusion. A second, independent hardware control-flow monitor observes the actual transition sequence and thereby changes the attack-tree diagnosis from a low-severity configuration or maintenance issue to a high-confidence code-injection or control-flow hijack. In this scenario, the proposed combination of control-flow anomaly detection, attack-tree based intrusion identification, and hardware-based monitoring can improve not only anomaly detection, but also the diagnostic precision of attack-tree-based cyber-attack identification.

---


### 125. [Hybrid Gated Attention](https://arxiv.org/abs/2608.11805)

**<font color=#1a73e8>作者：</font>** Zekun Zhou, Ruobing Xie, Lanrui Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Gated attention is an effective approach to mitigate attention sinks and enhance the representational capacity of attention. To further extend its effectiveness-efficiency Pareto frontier, we propose a Hybrid Gated Attention (HyGA) framework that contains three types of gating strategies. Specifically, these gates leverage diverse information from multiple stages of attention, and collaboratively build element-wise/head-wise gating from multiple perspectives, capturing intra-head and cross-head information interactions. Through our hybrid gating components, HyGA could provide multi-source modulation signals, enabling more comprehensive control over information flow and improving the representational capacity of attention. We also introduce low-rank matrix decomposition and learnable attention sink to further enhance training efficiency and stability. In experiments, we evaluate HyGA on widely-used benchmarks based on different backbones. The experimental results show that our HyGA comprehensively improves both training loss and various downstream performances compared with Gated attention. HyGA has also been verified to achieve the best performance at different computation costs, with comprehensive model analyses for better understanding. The proposed HyGA sheds light on a more effective, efficient, and stable attention mechanism.

---


### 126. [CoDiR: Confidence-Guided Diffusion Refinement for Semi-Supervised Histopathology Segmentation](https://arxiv.org/abs/2608.11807)

**<font color=#1a73e8>作者：</font>** Hoai Nhan Pham, Dang-Nguyen Bui, Le-Van Thai 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Semi-supervised histopathology segmentation is challenging due to scarce annotations and unreliable pseudo-labels in ambiguous gland regions. To address this problem, we propose Confidence-Guided Diffusion Refinement (CoDiR), a semi-supervised framework that combines a Mean Teacher segmentation model with diffusion-based pseudo-label refinement. Given an unlabeled image, the teacher first produces a soft prediction, and only low-confidence regions are refined by a conditional diffusion model trained to capture plausible mask structures from labeled data. The refined mask is then fused with reliable teacher predictions and used to train the student with confidence weighting and consistency regularization. On the GlaS and CRAG datasets CoDiR reaches 88.09\% and 89.83\% mDice with 10\% labeled data, and 89.19\% and 90.29\% mDice with 20\%, matching or exceeding the strongest published method on seven of the eight benchmark metrics. Ablations attribute the largest single contribution to the refinement module, which adds +6.36\% mDice over the Mean Teacher baseline. The implementation code is publicly available at: this https URL

---


### 127. [Can Vision Models Read the Radar Display? On the Feasibility of Radar Imagery for Air Traffic Complexity Estimation](https://arxiv.org/abs/2608.11810)

**<font color=#1a73e8>作者：</font>** Hyewook Kim, Byul Kang, Seokbin Yoon 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Air traffic controllers perceive traffic complexity through the radar display, suggesting that a computer vision model operating on the same imagery may provide a natural architecture for modeling controller-perceived complexity; however, whether radar imagery is a viable input format for deep learning vision models remains unclear. Unlike natural images, radar images are extremely sparse and self-similar, consisting primarily of a black background and a few visually identical aircraft blobs, while small changes in aircraft positions can substantially alter sector-level complexity. To test whether a vision model can capture these operationally important differences, we encode each traffic situation as a position image supplemented by five channels representing aircraft state variables, including heading, speed, and altitude, and train a Vision Transformer (ViT) to regress four intrinsic complexity components derived from pairwise geometric relations among aircraft. The model achieves $R^2 > 0.96$ for all four components, and a one-aircraft-removal perturbation study shows that its response changes proportionally to how much the removed aircraft contributed to sector complexity rather than treating every removal as equivalent. These results demonstrate that, despite its atypical visual characteristics, radar imagery is a viable input format for air traffic complexity modeling.

---


### 128. [Learning with Bilevel-Minimax Optimization for Efficient and Reliable Transfer Attacks](https://arxiv.org/abs/2608.11815)

**<font color=#1a73e8>作者：</font>** Yaohua Liu, Yifan Guo, Jiaxin Gao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transfer-based adversarial attacks craft adversarial examples using surrogate models to mislead black-box victim models. Beyond perturbation generation, transferability is fundamentally governed by the coupling of initialization, surrogate adaptation, and gradient dynamics. We revisit this challenge from a bilevel-minimax perspective and propose BMAT (Bilevel-Minimax Adversarial Transfer). The bilevel formulation captures the dependency between initialization and perturbation, while the inner minimax problem promotes surrogate robustness for cross-architecture generalization. Algorithmically, we develop an integrated bottom-up solver that combines a Soft Weight Modulator and an Implicit Gradient Approximator to enable ternary coupling among initialization, surrogate adaptation, and perturbation optimization. We further provide theoretical insights into the optimization dynamics of the proposed bilevel-minimax framework. Extensive experiments on classification and segmentation benchmarks show that BMAT outperforms more than 10 strong baselines across more than 30 victim models, improving both intra- and cross-architecture transfer and yielding up to a 2x reduction in mIoU. Code is available at this https URL.

---


### 129. [Kernel Methods for Learning Operators with Multiple Inputs and Outputs](https://arxiv.org/abs/2608.11831)

**<font color=#1a73e8>作者：</font>** Adrien Weihs, Chunyang Liao, Jingmin Sun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning mappings between infinite-dimensional objects is a central challenge in scientific machine learning. We introduce a general kernel-based encoder-decoder framework for operator learning that separates observation, representation, learning, and reconstruction. We develop this framework for multi-input, multi-output operator learning, where operators map between products of potentially distinct function spaces. Our approximation theory shows that, although the number of inputs and outputs can increase, the convergence rate is governed by the most challenging constituent approximation problem rather than the overall problem dimension. The framework leads to practical kernel methods with closed-form training and inference, combining mathematical tractability with computational efficiency. We further specialize the approach to multiple operator learning by introducing KernelMO, a family of kernel methods with complementary operator-valued and product-space formulations. Across five families of parametric partial differential equations, the proposed methods achieve competitive or state-of-the-art predictive accuracy while reducing training and inference costs relative to neural operator architectures and deep learning based models, offering an efficient and lightweight alternative.

---


### 130. [Distractor-Aware Video Object Segmentation](https://arxiv.org/abs/2608.11835)

**<font color=#1a73e8>作者：</font>** Andreas Robinson, Abdelrahman Eldesokey, Michael Felsberg  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Semi-supervised video object segmentation is a challenging task that aims to segment a target throughout a video sequence given an initial mask at the first frame. Discriminative approaches have demonstrated competitive performance on this task at a sensible complexity. These approaches typically formulate the problem as a one-versus-one classification between the target and the background. However, in reality, a video sequence usually encompasses a target, background, and possibly other distracting objects. Those objects increase the risk of introducing false positives, especially if they share visual similarities with the target. Therefore, it is more effective to separate distractors from the background, and handle them independently.
We propose a one-versus-many scheme to address this situation by separating distractors into their own class. This separation allows imposing special attention to challenging regions that are most likely to degrade the performance. We demonstrate the prominence of this formulation by modifying the learning-what-to-learn (LWL) method to be distractor-aware. Our proposed approach sets a new state-of-the-art on the DAVIS 2017 val dataset, and improves over the baseline on the DAVIS 2017 test-dev benchmark by 4.6 percentage points.

---


### 131. [Air Quality Station Simulation via LSTM and Attention-Based Modelling](https://arxiv.org/abs/2608.11839)

**<font color=#1a73e8>作者：</font>** Alexander Kostadinov, Petar O. Hristov, Dessislava Petrova-Antonova  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Poor air quality in urban areas is driven by a complex chain of processes and presents a significant public health concern. To better understand and control the mechanisms that determine air quality, cities deploy networks of measurement stations, and launch initiatives for collecting denser data about the concentration of pollutants in the atmosphere. Extracting insights from the stations relies on their reliable and uninterrupted operation. However, hardware is susceptible to faults and black- outs that may result in data unavailability, which affects the overall quality of analyses. In this paper, we present a deep-learning model, called SATADL, which can infer complex relations and output multiple-hour-ahead air-quality forecasts. The goal of the model is to simulate the mea- surements of an unresponsive station until its operation is restored. The architecture of the model, which allows it to extract information from different aspects of the data, is described in detail and a careful examination of all of its components is provided. We demonstrate the performance of SATADL on four sets of air quality stations from around the world, by using it to simulate the concentration of PM10 for periods of hypothetical failures of one of the measurement stations, lasting for as long as 48 hours. A selection of baseline and published deep learning models were trained and used as a benchmark. The results show that SATADL per- forms better across different prediction windows, for both coefficient of determination and root mean squared error, demonstrating its suitability as a virtual proxy station.

---


### 132. [When the Knowledge Base Becomes the Gold Standard: Measuring Resource-Shared Evaluation Loops in Entity-Level Machine Translation](https://arxiv.org/abs/2608.11843)

**<font color=#1a73e8>作者：</font>** Jinhyung Bae, Dain Kil, Seongmin Oh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The Seungjeongwon Ilgi, a UNESCO Memory of the World record, is only 37.4% translated, and the most conspicuous failure mode in automatic translation is the person name -- a misread name corrupts the historical fact rather than merely the surface. Low-resource historical domains have no expert gold standard for entity translation, so practitioners substitute a knowledge base (KB) for the gold. That KB is the same resource injected into the system: scoring becomes self-referential and the metric measures instruction compliance rather than translation quality.
We measure this loop. Using expert person-name annotations from the National Institute of Korean History as a gold independent of the injection pipeline, we hold the entity set fixed and vary only the provenance of the correct reading. Of 527 expert-annotated mentions, only 31.1% lie outside the injection pipeline, and the residual loop is not uniform -- in the overlapping segment the injected reading agrees with the human translation 97.8% of the time against 70.1% in the independent one, so the segment that looks healthiest is the one the loop is holding up.
Across four models, a difference-in-differences analysis shows the gain from KB injection is confined to the segment whose gold shares the injected resource; in the independent segment it is at or below zero. Post-injection preservation clusters in a narrow 0.910-0.996 band even though baseline capability differs fivefold, so the reported gain is the complement of prior performance and weaker models appear to improve more dramatically. On an independent sample built by removing the construction filter, the measure replicates within model (overlapping intervals) while discriminating between models (non-overlapping intervals) -- it reflects a property of the model, not of the sample.

---


### 133. [BoltNet: An Ultra-Lightweight Convolutional Network for On-Device Plant Species Identification](https://arxiv.org/abs/2608.11844)

**<font color=#1a73e8>作者：</font>** Daniel Rossi, Guido Borghi, Roberto Vezzani  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated plant species identification from citizen-science imagery is an established, demanding fine-grained recognition problem: large taxonomic label spaces, visually similar species, and long-tailed observations require real model capacity, while field use constrains memory, latency, and power. Model size is only part of the deployment cost: intermediate activations held in memory during inference and platformdependent execution behavior matter too, so compact recognition must be assessed on target hardware rather than through complexity metrics alone. We present BoltNet, an ultra-lightweight fully convolutional architecture combining a Spatial Redistribution Bottleneck and Logit PreSampling to improve the tradeoff between predictive performance and model size in high-cardinality classification, and report the AccuracyCompression Tradeoff as a complementary diagnostic. On Pl@ntNet300K, BoltNet reaches 0.682 F1-score with 341K parameters (1.37 MB), the highest F1-score among evaluated models below 2 MB and close to substantially larger convolutional backbones. Model-only measurements on a Raspberry Pi 5, Jetson Orin Nano, and Hailo-8 characterize execution across CPU, GPU, and NPU platforms, where BoltNet is the most consistently efficient model, with the best FPS/W on the GPU and NPU and second-best on the CPU. Results on AIDERv2 and CLRS provide secondary evidence of transfer across environmental image-classification tasks. Code available at: this https URL

---


### 134. [Small-Scale Experiments: Are We There Yet?](https://arxiv.org/abs/2608.11859)

**<font color=#1a73e8>作者：</font>** Nicholas Lourie, Kyunghyun Cho, Karen Ullrich 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scaling laws promised cost-effective experiments; six years later, they have yet to fully deliver. Instead, researchers have found them unreliable at small scales (starting at 4M parameters) and concluded that sizable models cannot be avoided. We show this is not the case: the confounding factor is hyperparameters. Small models are highly sensitive, but hyperparameter sensitivity fades with scale. This small-scale sensitivity makes scaling laws easy to miss because they only emerge on the fully tuned frontier, and reaching that frontier requires an extensive search far beyond what most ever run. By ablating the basic scaling law recipe, we show well-tuned hyperparameters matter more than any other ingredient. Further, we reveal why those hyperparameters become easier to find: as scale increases, the hyperparameter loss surface becomes lower dimensional. Nevertheless while scaling laws exist in small models, extrapolation hits statistical limitations. A holistic approach is required. Synthesizing our insights with the recent literature, we develop a new methodology for model-centric research and demonstrate it on a question that once took the field years to settle: where to place normalization layers in the transformer architecture. From small-scale experiments, we recover the large scale result: pre-normalization works better as models grow in size. With the right tools and a better understanding, small-scale experiments can deliver on scaling laws' long-awaited promise.

---


### 135. [Forward and Inverse Virtual Metrology for Phototransistor Gain: A Hierarchical, Uncertainty-Aware Approach for Small Production Datasets](https://arxiv.org/abs/2608.11868)

**<font color=#1a73e8>作者：</font>** Mahshid Amirabgir, Lorenza Ferrario, Paolo Conci 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The customization, optimization and stabilization of the process flow of a silicon bipolar phototransistor commits months of cleanroom time before a finished device can be measured, so a model that predicts device gain from process parameters before a run has value out of proportion to its accuracy. We study this problem on a real fabrication history, thirteen to fourteen process runs of a single device: a small-sample, hierarchically structured setting unlike the large-corpus regime of conventional virtual metrology. Decomposing the variance of device gain, we find that roughly half of it lies between process runs rather than within them, so recipe-only prediction is bounded by construction. Building on these findings we provide a forward gain predictor with a relative, uncertainty-aware signal, an inverse search that returns recipes for a target gain, and, as the foundation for all of it, a multi-level data-quality assessment tailored to the nested physical entities of fabrication (batch, wafer, die) with an explicit cross-level linkage score. The normalized dataset and analysis code are released for full reproducibility.

---


### 136. [ATOM: Geometry-Aware Microgesture towards Object-Agnostic Tangible Interaction](https://arxiv.org/abs/2608.11871)

**<font color=#1a73e8>作者：</font>** Yinqiao Wang, Hao Xu, Qixuan Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This paper presents ATOM, an integrated framework towards agnostic and tangible object interactions with microgestures. Our goal is to support microgesture interactions across different everyday objects, with the capability to automatically leverage the geometric affordance of each object. We formulate a fingertip-aware detection pipeline to leverage generative 2D and 3D models for geometry enhancement and refinement. We then introduce a usability-based method to prioritize the detected elements based on their ergonomic suitability for interactions. Building on this foundation, we further develop an AR system to transform everyday handheld objects into tangible user interfaces with 0D, 1D, and 2D microgesture interactions. Across transitions among everyday cooking objects of varying shapes and sizes, ATOM outperformed ablation baselines in task completion, usability (SUS), and workload (NASA-TLX). A further study with 10 objects demonstrates ATOM's generalizability across objects and grasps, highlighting its potential towards fluid, object-agnostic tangible interaction in real-world AR scenarios.

---


### 137. [DCM Bandits: Multiplayer Information Asymmetric Cascading Bandits for Multiple Clicks](https://arxiv.org/abs/2608.11873)

**<font color=#1a73e8>作者：</font>** Andy Wang, Charlton Shih, William Chang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this work, we extend the Dependent Click Model (DCM) Bandits to a multiplayer information-asymmetric setting, where multiple agents interact with a shared ranked list and may observe multiple clicks per session, introducing new challenges for selection strategies. We study asymmetry in (1) actions and (2) rewards, providing sublinear regret guarantees for three settings where at least one asymmetry is present. Establishing matching information-theoretic lower bounds for these settings is left as an open problem. We further show that for small termination probabilities, the termination ranking need not be known, improving on prior single-agent results. Experiments confirm that our algorithms perform well across asymmetric environments and highlight the critical role of feedback structure, specifically the distinction between full versus first-click feedback, in coordinating exploration and minimizing regret.

---


### 138. [Total Recall at What Cost? Benchmarking the Serving Cost of Agentic Memory Systems](https://arxiv.org/abs/2608.11879)

**<font color=#1a73e8>作者：</font>** Natchanon Pollertlam, Witchayut Kornsuwannawit  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-running conversational agents increasingly rely on a memory system to avoid resending the whole conversation each turn, yet how much that costs to serve has received little systematic benchmarking. We compare three memory systems (Mem0, Hindsight, and Mastra Observational Memory) against two reference strategies -- a fixed-size rolling window and resubmitting the full transcript -- across two backbones and conversations of up to 400 turns, pairing every cost measurement with answer accuracy on 665 LoCoMo questions. First, a memory system's serving cost cannot be predicted from conversation length and message size alone: a regression that tracks the two reference strategies closely misses the memory systems by 18-69%, their cost driven instead by internal memory behavior. Second, a break-even analysis shows that whether -- and when -- a memory system becomes cheaper to serve than the full transcript is highly sensitive to the system and the backbone, from the first tens of turns for the cheapest to never within 400 turns for the most expensive. Third, no system wins on both axes: accuracy spans 21-54%, and the backbone choice drives cost as much as the memory system does.

---


### 139. [Warping Earth Observations for better ice labeling in the Marginal Marginal Ice Zone](https://arxiv.org/abs/2608.11883)

**<font color=#1a73e8>作者：</font>** Tom Kelly, Martin S. J. Rogers  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal satellite imagery provides complementary information for Earth Observation, but accurately combining heterogeneous sensors remains challenging in dynamic environments. Fast-changing regions, such as the Antarctic marginal ice zone, cannot fully exploit multimodal information from different satellite sensors because surface features move between image acquisitions. This spatial and temporal mismatch challenges effective perceptual grounding, violating the assumption of pixel-level correspondence that underpins most multimodal reasoning and downstream classification pipelines. Antarctic sea ice provides a challenging benchmark due to the rapid, heterogeneous drift of individual ice floes and the differing responses of sea ice to radar, visible and thermal sensing modalities. Accurate, dense supervision of sea ice remains scarce because generating pixel-wise labels requires time-consuming expert interpretation of noisy data, leading to historical reliance on coarse-resolution maritime ice charts for model training. This paper presents a novel architecture based on mutual information warping to align multi-satellite (Sentinel-1 and MODIS platforms) multimodal (visible, thermal, radar) satellite scenes. To demonstrate the approach, we introduce a sparse expert-labeled dataset of 2,088 pixel-wise annotations (7,046 expert point classifications) located at the ice-water margin interface across 43 scenes. Our results demonstrate that spatially grounding and aligning modalities prior to segmentation improves classification accuracy, and enables accurate, dense sea ice segmentation from sparse point-wise supervision.

---


### 140. [Disentangling the Expressivity of RoPE](https://arxiv.org/abs/2608.11909)

**<font color=#1a73e8>作者：</font>** Selim Jerad, Anej Svete, Jiaoda Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Two accounts recur in explanations of the success of rotary position embeddings (RoPE). Expressivity studies associate periodic position information with modular predicates, whereas mechanistic and long-context studies emphasize positional anchors and local offsets. We formalize both accounts for fully uniform, finite-precision soft-attention transformers. We find that, if every rotary component is periodic, RoPE transformers recognize exactly the languages definable in past temporal logic with modular predicates. Conventional RoPE is different: The rotations it computes never repeat. This yields a precision-dependent bounded simulation of fixed-offset look-back operators, rather than an all-length modular characterization. Controlled experiments match this separation: Constructed periodic schedules length-generalize on modular languages, while conventional RoPE behaves more like a bounded locality bias and can impair tasks requiring position-invariant access to distant context. Altogether, our findings shed light on RoPE transformers, bringing theoretical expressivity characterizations closer to models used in practice.

---


### 141. [A Factor Graph Approach to Scalable Multi-Output Gaussian Process Regression](https://arxiv.org/abs/2608.11917)

**<font color=#1a73e8>作者：</font>** Wouter W. L. Nuijten, Esther G. van Pelt, Albert Podusenko 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-output Gaussian process regression scales cubically in the number of observations times outputs, and dense kernel-matrix methods need bespoke handling whenever different outputs are observed at different inputs. We express multi-output Gaussian process regression as a Forney-style factor graph in which a nearest-neighbor chain orders a fixed candidate set of $C$ inputs into a one-dimensional sequence. Along this chain, latent Matérn processes evolve through linear-Gaussian transition factors, while the linear model of coregionalization mixes $L$ latent processes into $D$ outputs through a deterministic mixing factor and per-output scalar observation factors. Posterior computation reduces to exact Gaussian message passing on the chain at cost $\mathcal{O}(C(DL^2 + L^3))$ after chain construction, and missing observations omit their local factor without any covariance-matrix restructuring. The formulation therefore scales in the number of data samples and in the rate of missing observations, while remaining best suited to candidate sets in low input this http URL compare the factor-graph formulation against an exact kernel-matrix baseline, a sparse-variational inducing-point baseline, and a nearest-neighbor baseline on a synthetic input-dimension sweep and on electricity time series forecasting. At low input dimension the factor-graph posterior tracks the exact kernel-matrix posterior closely, and the gap grows gradually as input dimension increases while staying competitive with both approximate baselines. On the electricity time series our factor-graph formulation matches all three baselines in forecast accuracy while scaling linearly in the number of data points, where the exact kernel-matrix method becomes infeasible and the inducing-point baseline remains substantially slower.

---


### 142. [Spark-to-Paper: End-to-End Research Paper Generation as a Composable Skill](https://arxiv.org/abs/2608.11924)

**<font color=#1a73e8>作者：</font>** Zhuoyang Qian, Biao Wu, Yiran Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Turning a research idea into a complete paper requires more than text generation: the system must retrieve literature, design and execute experiments, revise claims according to evidence, produce publication-ready figures, and maintain consistency across a long generation process. We present Spark-to-Paper, an end-to-end research paper generation system implemented as thirteen composable skills inside an existing coding assistant, without requiring a separate agent platform or orchestration service. Spark-to-Paper separates model-based judgment from deterministic operations that can be directly executed and checked. It further separates experiment planning from reporting, so that required evidence is specified before results are observed and manuscript claims are revised according to measured outcomes. To improve reliability over long research trajectories, the system combines deterministic integrity checks with self-critique and bounds a failure mode we call the Self-Refutation Loop, in which repeated experiments continue to reject the original research objective. Spark-to-Paper also produces editable vector figures through programmatic plotting for experimental results and code-based reconstruction for generated method diagrams. Across eight controlled research topics, Spark-to-Paper achieves 99.5% citation validity and 96.4% figure editability. A controlled ablation increases fabrication detection from 14% for a single-pass draft to 92% with the full integrity and review stack, while adversarial review achieves 74% precision. The full system uses 11.9M tokens, costs $8.1 per manuscript, and requires 3.2 hours on average. These results show that end-to-end research paper generation can be implemented as a lightweight, composable workflow inside existing coding assistants while keeping experimental evidence central to how claims are accepted, revised, or abandoned.

---


### 143. [Seed2GS: Camera-Free, Training-Free Object Extraction from 3D Gaussian Scenes via a Single Reference-View Grounding](https://arxiv.org/abs/2608.11928)

**<font color=#1a73e8>作者：</font>** Zongjian Ding, Yudong Gao, Jiale Liu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Extracting a target object from a pre-built 3D Gaussian Splatting (3DGS) scene enables interactive 3D editing. Existing methods either train for tens of minutes per scene, sacrifice accuracy, or require original reconstruction cameras that pre-built assets may not include. We present Seed2GS, which achieves the highest reported LERF-MASK accuracy without original reconstruction cameras or scene-specific representation training. Its key insight is to separate target identity from 3D coverage. QD-SAM3 selects one reliable reference mask from several open-vocabulary candidates, fixing identity once. Seed lift and visibility-adaptive virtual orbits then expose the object from new viewpoints, while tracking propagates the seed without repeated detection. Because the scene remains frozen, these masks supervise only one temporary foreground logit per Gaussian. On LERF-MASK, Seed2GS reaches 92.1% mean intersection over union (mIoU) with a measured compute-only latency of 9.3 seconds, 3.7 points above the strongest scene-trained baseline and 7.6 points above the closest camera-free baseline. With one fixed test reference per scene, the complete pipeline retains 91.1% mIoU; replacing its predicted seed with a ground-truth mask improves mIoU by only 0.72 points. On 3D-OVS, Seed2GS reaches 95.7% mIoU.

---


### 144. [Dual Anchors, Do It Better: Hierarchical Group Merging for Zero-Shot Anomaly Detection](https://arxiv.org/abs/2608.11933)

**<font color=#1a73e8>作者：</font>** Jimin Roh, DongKyu Kim, Suk-Ju Kang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Zero-shot anomaly detection (ZSAD) aims to identify anomalies in unseen domains, a setting that is particularly critical for industrial and medical applications where domain shifts are prevalent. However, most CLIP-based ZSAD methods anchor semantics solely on the text modality, making performance highly sensitive to prompt design and leading to weak visual grounding. To mitigate these limitations, we propose a Dual-Anchor framework that complements conventional text anchors with hierarchical image anchors constructed via a top-down grouping mechanism. This mechanism progressively aggregates local-to-global image features to form normal and abnormal group tokens, which serve as image anchors and act as gating signals in a Group-Gated Token Refiner to enhance the global representation. The refined image anchors are then fused with text prompts to construct dynamic state prompts. By jointly reinforcing visual and textual semantics, our framework stabilizes image-text alignment, reduces prompt dependency, and achieves strong generalization across 8 industrial and 6 medical benchmarks.

---


### 145. [Surfsvr: 2D Surface Priors as 3D Geometric Regularizers for Sparse Voxel Reconstruction](https://arxiv.org/abs/2608.11938)

**<font color=#1a73e8>作者：</font>** Yan Di, Chengxi Li, Yaoxing Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sparse voxel reconstruction offers an efficient representation for high-fidelity 3D modeling, yet its geometry is commonly optimized from local photometric evidence and discrete visibility statistics. This often leads to fragmented surfaces, excessive subdivision, and floating artifacts, particularly in weakly textured or sparsely observed regions. We introduce SurfSVR, a novel sparse voxel reconstruction paradigm that treats 2D surface priors as explicit 3D geometric regularizers. Instead of directly lifting noisy pixel-wise depth predictions, SurfSVR first organizes each image into coherent surface regions by jointly reasoning over appearance, monocular depth, normals and cross-view geometry. Each region is then represented by an adaptively selected planar or quadratic surface model based on fitting reliability and geometric complexity, while cross-model agreement distinguishes reliable geometry from ambiguous predictions. These structured 2D priors are lifted into 3D and integrated throughout the reconstruction pipeline. They guide surface-adaptive voxel subdivision, provide region-level depth and normal supervision during optimization, enhance geometrically reliable sparse-observed surfaces in voxel pruning, and suppress off-surface floaters during post-refinement training. This unified design converts semantic and geometric coherence in image space into persistent structural constraints in 3D. Extensive experiments on 3 public benchmarks demonstrate that SurfSVR consistently improves sparse voxel reconstruction across scenes with substantially different visibility and geometry characteristics, achieving state-of-the-art reconstruction quality. Codes and models will be released soon.

---


### 146. [Rank-Two Frobenius-Linearized Normal Forms and Orthoderivative Dual Coordinates in Quadratic APN Maps](https://arxiv.org/abs/2608.11939)

**<font color=#1a73e8>作者：</font>** Jingchuan Ma, Yanhua Liu, Qiaoyun Huang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We classify binary-linear two-term Frobenius-linearized operators $L(Y)=AY^\sigma+BY$ on $K^3$, where $K$ is a finite extension of $\mathbb{F}_2$ and $\sigma$ is a fixed nontrivial Frobenius automorphism of $K$ with fixed field $\mathbb{F}_2$. Under a coefficient-rank and binary-kernel condition, if $A$ and $B$ both have $K$-rank two and $L$ has a one-dimensional kernel over $\mathbb{F}_2$, then invertible $K$-linear input and output changes reduce $L$, for this fixed $\sigma$, to the canonical model $(\alpha,\beta,\gamma)\mapsto(\alpha^\sigma+\alpha,\beta^\sigma,\gamma)$. The proof constructs the coordinate frames from the two coefficient-kernel directions and the binary kernel. In these coordinates, the first dual output row is exactly the unique nonzero trace-adjoint normal, with an exact $K$-valued normalization. For pure $\sigma$-quadratic almost perfect nonlinear maps, this identifies the orthoderivative by $\pi_F(X)^T F(X)=1$; in odd extension degree it also yields permutation behavior and a bijection from the projective plane to its dual. The triprojective construction of Gologlu and Kolsch and the cubic norm-twist construction of Li, Zhou, Li, and Qu provide two realizations arising from different algebraic constructions. The triprojective case further admits a determinant factorization and a complete dual frame, whereas the norm-twist realization shows that the pure-map consequences do not follow from the operator theorem alone. A natural Gold representation has coefficient-rank pair $(3,3)$, delimiting the rank-two subclass. The normal form also supplies exact extension-field labels for known component-radical and Walsh-support relations.

---


### 147. [Evaluating and Calibrating Diffusion Model-derived Uncertainty for Quantitative MRI Mapping](https://arxiv.org/abs/2608.11942)

**<font color=#1a73e8>作者：</font>** Shishuai Wang, Stefan Klein, Juan A. Hernandez-Tamames 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Quantitative MRI (qMRI) provides standardised tissue parameter maps, but the reliability of deep learning-based qMRI mapping methods is often not explicitly characterised. In this work we systematically evaluate uncertainty maps for quantitative MRI derived from multiple inferences of a data-consistent diffusion model-based qMRI framework. Evaluation on synthetic test data assessed error-awareness, high-error detection, selective prediction, and Gaussian interval calibration. Diffusion model-derived uncertainty was positively associated with the mapping error, while risk-coverage analysis showed that excluding high-uncertainty voxels reduced the retained error. However, the raw uncertainty was poorly calibrated for quantitative interval interpretation. Calibration was substantially improved using a post-hoc procedure combining prediction-value-dependent bias correction with scalar uncertainty scaling. Qualitative evaluation on a healthy volunteer showed spatially meaningful uncertainty patterns. These results indicate that diffusion model-derived uncertainty is informative for reliability assessment and selective prediction, but requires calibration for quantitative interval interpretation.

---


### 148. [TailBooster: A Dual-Layer Generative Framework for Extreme Value Augmentation with Operational Validity Enforcement](https://arxiv.org/abs/2608.11951)

**<font color=#1a73e8>作者：</font>** Karim Aly, Alexei Sharpanskykh, Jacco Hoekstra  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Extreme events in air transport, such as severe arrival delays and abnormal air times, cause cascading network disruptions with substantial operational, economic, and safety costs. Such events are rare in historical records, leaving insufficient training signal for machine learning models. Synthetic data augmentation offers a principled solution, but conventional generative models under-represent distributional tails and give no guarantee against operationally infeasible instances, such as a short air time paired with a long flight distance. No existing approach addresses both limitations for mixed-type tabular records. We propose TailBooster, a dual-layer generative framework combining generative modelling with two anomaly detection layers. A statistical layer extracts extremes via the interquartile range, supplying tail-concentrated training signal to dedicated generative models, here a Tabular Variational Autoencoder. A deep learning layer then applies autoencoder-based cleaning, discarding synthetic records that violate the operational envelope learned from historical data. The framework was evaluated on US flight records across five dimensions: diversity, statistical similarity, fidelity, operational validity, and utility, the latter two being the primary improvement targets. Data-driven cleaning markedly improved operational validity, while targeted augmentation enhanced utility for extreme-event prediction. Across six regression algorithms, training on the framework's records reduced Mean Absolute Error by 47-49% on extreme air time and 29-57% on extreme arrival delay prediction relative to conventional synthetic data, with comparable gains when real records were enriched with synthetic extremes. Being fully data-driven and model-agnostic, TailBooster extends to domains where extreme-event prediction is critical and domain-specific rules are unavailable.

---


### 149. [Synchronized AMG and EMG Dataset of Lower-limb Muscle Activities in Everyday Training](https://arxiv.org/abs/2608.11958)

**<font color=#1a73e8>作者：</font>** Dongxu Tang, Shih Ying-Lei, Zhuoyi Ren 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Understanding how lower-limb muscle groups coordinate is important for studying movement impairment, rehabilitation, and physical performance. Reproducible analysis of this coordination requires multimodal recordings that relate local muscle-related signals with body-level kinematics. Complementing neural-level electrical activation captured by EMG, AMG provides a valuable mechanical approach to monitoring muscle activity. Here, we introduce a synchronized, multimodal dataset for healthy-adult lower-limb activities. For data collection on the left leg, 16 triaxial accelerometers were evenly divided into four muscle-site clusters for AMG recording, complemented by four surface EMG channels. A 15-marker optical motion-capture (MoCap) system captured lower-body kinematics, with the resulting marker trajectories used to compute bilateral knee and ankle joint angles. Our dataset contains 1,918 trials from 30 subjects across 16 task conditions. We benchmark the dataset by estimating four joint angles from 300 ms windows of the 5-100 Hz band-pass-filtered AMG data and assess matched EMG features in a separate modality ablation. In the primary cross subject benchmark, the four reference models achieved mean absolute errors of 8.840$^\circ$-9.591$^\circ$. The benchmark and ablation results characterize performance across subjects, tasks, and joint angles and examine the effects of sensor configuration, modality, the number of training subjects, and frequency representation. The release includes documented timing definitions, processed data, and reproducible benchmark resources. this https URL

---


### 150. [TESLA: Taylor Expansion of Sinusoidal Learnable Activations](https://arxiv.org/abs/2608.11970)

**<font color=#1a73e8>作者：</font>** Daehwa Ko, Jaehyeon Kim, Seunghyun Ham 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The parity problem--deciding whether the number of ones in a binary vector is odd or even--remains challenging for standard neural networks due to linear inseparability and the need for global interactions. We propose TESLA, an activation defined as a learnable combination of sine and cosine terms, enabling explicit control over polynomial degree and selective amplification of high-order components. Theoretically, we show that constraining TESLA's coefficients yields Lipschitz/Rademacher complexity bounds and shapes the training dynamics to emphasize higher-frequency structure. Empirically, on parity with input length n = 32, TESLA attains strong generalization with 100K training samples (approximately 0.002% of the 2^32 input space) and remains robust under heavy corruption, retaining high accuracy with up to 30% label noise. We also compare against periodic and frequency-based baselines (SIREN, SNAKE, and Fourier feature embeddings) on parity and Forrelation. Beyond synthetic structure, TESLA delivers comparable performance on ImageNet-100, indicating that activation-level degree control transfers to more general vision workloads. Code: this https URL

---


> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-202](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
