# 📦 其他研究 | 2026年11月06日

> 本类共 **236** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-236](./part-05.md)

---

### 51. [Toward an Optimal Configuration for Tree Species Classification from Bark Images: A Leakage-Safe Ablation Study](https://arxiv.org/abs/2611.05680)

**<font color=#1a73e8>作者：</font>** Maeve Côté  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Background: The automatic identification of tree species from bark photographs is of practical interest for forestry inventory and the wood-processing industry, yet the design choices that govern the accuracy of deep-learning approaches have not been studied systematically, and some prior results may be inflated by leakage of images of the same trunk across training and test partitions. Methods: A systematic ablation study is conducted on the public BarkNet 1.0 dataset (20 species) under the established tree-level, leakage-safe partitioning scheme. Using ConvNeXt-V2 backbones, the following factors are varied in turn and evaluated by five-fold cross-validation: patch size, the strategy by which per-patch predictions are aggregated into an image-level decision, the training regime (single- versus two-stage), backbone capacity, the whole-image baseline, and the number of patches available at inference. Results: Per-patch accuracy rises monotonically with patch size (from 75.6% at 160 px to 89.6% at 512 px), and image-level accuracy rises in step, plateauing near 94.9% around 512 px. Learned aggregation exceeds majority voting by at most 0.7 pp, an advantage that shrinks as patches grow and attention becomes near-uniform. Backbone capacity (pico to tiny) alters accuracy by less than a point, and two-stage training offers no advantage over one-stage. Whole-image classification (91.9%) trails patch-based aggregation, since it admits no bag to average over; accuracy increases with the number of patches at inference, saturating around 64. Conclusions: The study yields a simple recommended configuration: patches as large as possible while leaving enough to average over (around 512 px here), with a nano backbone. It also quantifies the second-order role of learned aggregation and model capacity, providing a reproducible reference point for practitioners and future research

---


### 52. [TRUST-Stereo: Teacher-Assisted Robust Uncertainty-Guided Search and Transfer for Fast Stereo Matching](https://arxiv.org/abs/2611.05689)

**<font color=#1a73e8>作者：</font>** Pouya Sohrabipour, Yihong Feng, Chaitanya Kumar Reddy Pallerla 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Coarse-to-fine stereo matching enables efficient disparity estimation but remains sensitive to errors in propagated disparity, which may place ground-truth correspondences outside subsequent local search ranges. We propose TRUST-Stereo (Teacher-Assisted Robust Uncertainty-Guided Search and Transfer for Fast Stereo Matching), which addresses this limitation through an Uncertainty-Guided Residual Search Module (UGRSM). UGRSM estimates the reliability of propagated disparity and predicts residual offsets to adaptively relocate local cost-volume centers. Additionally, we introduce a two-stage Senior-Junior Teacher Assistant knowledge distillation strategy to transfer rich monocular representations from a large foundation model to a lightweight backbone to achieve fast stereo matching performance. Experiments on KITTI 2012, KITTI 2015, ETH3D, and Middlebury demonstrate strong zero-shot generalization. Using only 1.4M synthetic stereo pairs, TRUST-Stereo achieves state-of-the-art results on several benchmark metrics, outperforming competing efficient methods trained with substantially larger datasets, including real-world pseudo-labeled samples. Specifically, it achieves a KITTI 2015 EPE of 0.93, ETH3D Bad 1.0 of 2.13% and Middlebury Bad 2.0 of 6.79% while maintaining inference at approximately 50 ms per stereo pair.

---


### 53. [Anchored Slice Propagation with Boundary Transport for 3D CT Segmentation from Three Orthogonal Annotated Slices](https://arxiv.org/abs/2611.05693)

**<font color=#1a73e8>作者：</font>** Tushar Kataria, Md Rakibul Haque, Shireen Y. Elhabian  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sli2Vol propagates a binary mask through affinities between adjacent slices, but an error can persist because each prediction becomes the input to the next step. Three orthogonal annotations reduce dependence on any one chain, yet they offer more than three starting masks: where a chain crosses another annotated plane, the correct label is already known. Those labels could correct drift during propagation and indicate how much to trust each chain at fusion. Between annotated planes, the information carried by the chain may matter as well. A binary mask records foreground membership but discards distance to the boundary, a cue that could help follow gradual shape changes between this http URL address these two sources of error with a fixed pretrained affinity backbone. We anchor each chain by correcting its prediction where it crosses another annotated plane, then use its agreement with those labels to weight fusion. We compare this anchored mask with two ways of transporting boundary geometry: a truncated signed-distance field (SDF) propagated by dense affinity averaging, and a contour whose vertices follow motion cues from the same affinity. The contour tracker starts from a hand-crafted rule and learns a motion correction from supervoxel pseudo-objects in 506 CT volumes, without manual organ labels. On 2,091 held-out structure instances from approximately 403 CT scans spanning 17 abdominal structures, anchoring raises mean Dice from 0.737 with orthogonal mask propagation to 0.769 and improves every structure. Beyond the anchored mask, learned contour tracking improves Dice by 5.7\% for the esophagus and 5.9\% for the postcava, while SDF transport improves right-adrenal Dice by 2.8\%. The anchored methods have similar mean Dice (0.769--0.772); contour tracking performs worse on the kidneys, stomach, and hepatic vessel tree.

---


### 54. [From Type to Token: Petri Nets, Individual Token Philosophy, and Individualized Causal Effects](https://arxiv.org/abs/2611.05703)

**<font color=#1a73e8>作者：</font>** Fernando Delbianco, Fernando Tohmé, Gustavo Bodanza  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Structural Causal Models and Bayesian Networks are the dominant framework for representing causal relations. They are fundamentally type-level formalisms since their estimands, Average Treatment Effects and Conditional Average Treatment Effects, are properties of distributions over populations, not of individual units. When treatment effects exhibit unbounded heterogeneity, these estimands collapse. What persists is the structural, token-level core of causation.
We argue that Petri Nets under the Individual Token Philosophy are the natural representation of these token-level causal structures. We develop a formal translation from Bayesian Networks to Petri Nets, providing a two-layer account of individualized causality. The PN layer provides a structural representation of causal mechanisms that does not rest on distributional assumptions. In turn, a conformal prediction layer quantifies causal effects with finite-sample coverage guarantees. Together they constitute a complete account of individual causal effects.

---


### 55. [Self-Supervised Pretraining for Label-Efficient Facial Expression Recognition using Smart Glasses](https://arxiv.org/abs/2611.05711)

**<font color=#1a73e8>作者：</font>** Zhengtao Gao, Francesco Bombassei De Bona, Leonardo Alchieri 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Facial Expression Recognition (FER) on optomyographic (OMG) smart glasses such as OCOsense enables privacy-preserving, camera-free affect sensing for health and well-being. Most FER systems are fully supervised, i.e., they rely either on hand-crafted expert features with classical machine learning, or on end-to-end deep models trained from labelled data. Both depend on large quantities of labelled expressions, which are costly to collect and limit deployment in real-world, personalized settings. We investigate Self-Supervised Learning (SSL) as a route to label-efficient FER on these glasses. We pretrain a Vision Transformer with a masked-autoencoder objective on unlabelled OCOsense recordings and finetune it for five-class FER under person-independent cross-validation. Across label budgets from 5% to 100%, pretraining consistently improves performance; with only 5% of the labels, the pretrained model outperforms the from-scratch model trained with all labels. Our results show that SSL pretraining is a practical way to reduce labelling cost for smart eyewear FER, and we discuss the implications for future personalization and continual adaptation.

---


### 56. [CoReFlow: Consistency-Relaxed Flow Maps for Probabilistic Traffic Forecasting](https://arxiv.org/abs/2611.05715)

**<font color=#1a73e8>作者：</font>** Pengnan Chi, Zhiguo Zhang, Xiaoliang Ma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Probabilistic traffic forecasting is essential for reliable Intelligent Transportation Systems (ITS), as it captures uncertainties in complex road networks. Recent diffusion- and flow-based generative models have facilitated uncertainty modeling through a multi-step sampling process. However, beyond slow inference, this process is designed to capture complex multimodal distributions, which misaligns with the limited complexity of the conditional traffic data distribution, causing models to underperform deterministic baselines. To address this, we introduce the \underline{Co}nsistency-\underline{Re}laxed \underline{Flow} Map (CoReFlow) model, presenting the first effort to leverage the one-step generation capability of flow maps, known as solution operators of probability-flow ordinary differential equations. Besides, we improve accuracy using a concise training objective that supervises the model via interpolation endpoints over finite time intervals. Unlike existing methods (e.g., self-distillation and MeanFlow Identity) that maintain trajectory consistency to model multimodal distributions, our objective leverages conditional mean to restrict the consistency, thereby achieving higher accuracy in the probabilistic traffic forecasting task. Extensive experiments on four real-world datasets show CoReFlow achieves state-of-the-art forecasting accuracy. It surpasses recent baselines, provides competitive uncertainty modeling, and reduces inference costs compared to existing generative baselines.

---


### 57. [RESHPart: Feedback-Reshaped Spectral Embedding for Hypergraph Partitioning](https://arxiv.org/abs/2611.05729)

**<font color=#1a73e8>作者：</font>** Rongjian Liang, Zhuo Feng, Brucek Khailany  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> With scalable Laplacian solvers now available, the next frontier is to exploit them more effectively for high-quality hypergraph partitioning. In this work, we revisit spectral hypergraph partitioning from the perspective of spectral embedding geometry. Through a systematic analysis of circuit hypergraphs and controlled synthetic (hyper)graphs, we identify a ray-like embedding structure that helps explain the effectiveness of projection-based partitioning. We further show that the geometry of spectral embeddings can be systematically influenced through Laplacian design and hyperedge reweighting. Guided by these insights, we propose FRESHPart, a feedback-reshaped spectral partitioning framework that refines the spectral embedding through Geometry Feedback and Search Feedback, producing embeddings that are better aligned with projection-based partitioning. On the Titan23 benchmark, FRESHPart achieves average cut reductions over hMETIS of 13.09% at $\epsilon=2\%$ and 25.21% at $\epsilon=20\%$, surpassing the strongest previously reported results (12.16% and 22.53%, respectively), while completing every benchmark in under 120 s on a single GPU.

---


### 58. [Mitigating Spurious Invariance in Contrastive Learning: A Probabilistic Self-Supervised Learning Framework for Medical Image Analysis](https://arxiv.org/abs/2611.05734)

**<font color=#1a73e8>作者：</font>** Wei Wei, Yading Yuan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Owing to the prohibitive cost of manual annotation for enormous medical images, self-supervised learning (SSL) has gained substantial attention and shown promise in various medical imaging tasks. Among SSL approaches, contrastive learning has emerged as a prominent one, encouraging models to encode semantic information that remains invariant between different augmented views. However, this invariance can be spurious for medical images, as subtle but critical medical features can be suppressed during augmentations. In this paper, we mitigate this issue by encoding the learned feature embeddings as probability distributions rather than fixed vectors, thus capturing a richer and more nuanced spectrum of information. Furthermore, we propose a unified probabilistic framework that seamlessly integrates multiple SSL approaches. Our method achieves superior performance over the state-of-the-art SSL methods on various downstream tasks across multiple datasets, including medical image segmentation and classification. We further validate the method through additional analyses of robustness to stronger augmentations, label efficiency under limited fine-tuning labels, and computational trade-offs. The code is released at this https URL.

---


### 59. [Self-Supervised Learning of Universal Latent Spaces for Operator Learning](https://arxiv.org/abs/2611.05735)

**<font color=#1a73e8>作者：</font>** Sepehr Mousavi, Levi Lingsch, Siddhartha Mishra 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural operators fit their representation of functions to the task they are trained on, so every new task rebuilds a reduced space from labeled data. Following the self-supervised pre-training that made representations shareable in natural language processing and computer vision, we decouple representation learning from operator learning. A functional autoencoder is pre-trained on analytic functions synthesized on the fly, with no solver and no labels, to represent functions on arbitrary point clouds, and the latent space it induces is frozen and reused across tasks. The representation is exactly equivariant to translation, dilation, and amplitude, and reconstructs solutions of partial differential equations (PDEs) and natural images on geometries it never saw. Being task-agnostic, the latent space can be interpreted in its own right. The whole space is used and decodes to valid fields, it preserves the ordering of distances between physical fields, its geodesics interpolate physical evolutions, and edit directions transfer across fields. With frozen representation maps, a dataset is encoded once and a neural operator is trained entirely on cached embeddings, which saves memory and training time. On 28 tasks in fluid dynamics, solid mechanics, acoustics, and the Helmholtz and Poisson equations, this paradigm can exceed the accuracy of state-of-the-art end-to-end architectures, with up to an order of magnitude higher throughput and memory savings that fit models nearly two orders of magnitude larger on consumer-grade GPUs. At inference, latent rollouts run up to an order of magnitude faster than regular rollouts, and chunked inference processes functions of over half a billion points on a single consumer-grade GPU.

---


### 60. [C-WFDM: A ControlNet-Guided Wavelet-Fusion Diffusion Model for Multimodal Brain MRI Completion](https://arxiv.org/abs/2611.05737)

**<font color=#1a73e8>作者：</font>** Muhammad Nabi Yasinzai, Remika Mito, Mangor Pedersen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal brain MRI provides complementary anatomical, tissue, and pathological information to support downstream artificial intelligence (AI) applications. However, modality availability is uneven across public and pooled neuroimaging datasets: T1-weighted (T1w) MRI is widely represented, T2-weighted (T2w) and fluid-attenuated inversion recovery (FLAIR) MRI are less consistently available, and gadolinium-enhanced T1-weighted (T1Gd) MRI is relatively scarce. Pooled datasets therefore contain participants with different combinations of acquired MRI contrasts, reflecting variation in the study designs, acquisition protocols, and clinical or research objectives of the contributing studies. Many missing-modality benchmarks simulate incomplete MRI by withholding contrasts from complete four-modality cases, which may not represent the observed availability patterns in pooled datasets. To address this gap, we introduce C-WFDM, a ControlNet extension of our Wavelet-Fusion Diffusion Model (WFDM), for subject-specific missing-modality completion. C-WFDM is built on an earlier BrainScape snapshot comprising 157 public MRI datasets and 45,880 preprocessed scans. The pretrained WFDM backbone retains target-modality and metadata conditioning, while target-specific ControlNet adapters use MRI contrasts from the same participant to guide synthesis. C-WFDM synthesizes T2w from T1w, FLAIR from T1w and T2w, and T1Gd from T1w, T2w, and FLAIR. Acquired conditioning contrasts are used when available, and generated intermediate contrasts are used only when required. We compare C-WFDM with ALDM, cWDM, and Pix2Pix using paired structural similarity index (SSIM), peak signal-to-noise ratio (PSNR), and mean absolute error (MAE). In the BrainScape completion experiment, C-WFDM achieves the best T2w and FLAIR results among the evaluated models, with SSIM values of 0.9232 and 0.8904, respectively.

---


### 61. [Learning Hierarchical Patch Splitting Policies for Faster Vision Transformers](https://arxiv.org/abs/2611.05742)

**<font color=#1a73e8>作者：</font>** Aditya Gupta, Jean Sebastien Dandurand, Kai Qiu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Transformers (ViTs) are bottlenecked by the length of their input token sequence. Standard patchification fixes this length with a single patch size applied across the image, regardless of regional content. Prior work on adaptive patch sizing reduces token count by assigning coarser patches to visually simple regions, but relies on noisy pixel-level heuristics such as local entropy to make patchification decisions. We argue that this compute allocation should be grounded in the model's interpretation of task relevant information, not in raw pixel statistics. We introduce Split Policy Learned Image Tokenization which learns to allocate token resolution based on what the model finds meaningful, producing shorter token sequences that are better matched to task-relevant content. SPLIT matches the accuracy of full-resolution ViT classification baselines while using 30% fewer tokens. The same gains hold on dense prediction: SPLIT achieves competitive accuracy on COCO and ADE20K, demonstrating that semantically aligned patchification generalises well beyond classification.

---


### 62. [Constraint-Aware Evaluation of Reinforcement Learning and Unsupervised Anomaly Detection for Security Operations Alert Triage](https://arxiv.org/abs/2611.05746)

**<font color=#1a73e8>作者：</font>** Radityo Ghifiardi, Rifny Rachman  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Security Operations Centers (SOCs) must identify real threats from large alert streams, but limited analyst capacity means that unnecessary escalations can delay more serious investigations. Existing studies often frame SOC alert triage as classification or anomaly detection, but both views are incomplete for production SOCs, where the central problem is selecting alerts worth escalating under limited capacity, asymmetric error costs, and workload constraints. This paper addresses that gap by formalizing alert triage as a constrained decision problem and evaluating three approaches: an offline reinforcement learning policy trained on alert embeddings, an Isolation Forest model built on operational features, and an autoencoder trained on historical benign alerts. These methods represent different triage assumptions: learning actions from reward, isolating unusual operational patterns, and detecting deviations from benign behavior. We evaluate all methods on 74,909 analyst-labeled production alerts under a strict temporal split and benign-escalation constraint. Because the test set contains 503 unique feature patterns, we primarily rank clusters of similar alerts. At the main operating point, all three methods satisfy the constraint, with the reinforcement learning policy achieving the lowest benign-escalation fraction at 0.000, compared with 0.007 for the autoencoder and 0.041 for Isolation Forest. The methods also prioritize largely different alert clusters, showing complementary rather than redundant coverage. These results suggest that production SOC triage can benefit from constraint-aware evaluation and combined or adaptive deployment of different model families.

---


### 63. [Decompose the Distillation: Interpretable Single-Pass Guidance for Diffusion Models](https://arxiv.org/abs/2611.05755)

**<font color=#1a73e8>作者：</font>** Wuyang Zhang, Xiaolin Xu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Classifier-Free Guidance is a widely used inference-time guidance rule for conditional image generation with diffusion models, which exposes a guidance scale that adjusts conditioning strength after training. This flexibility requires conditional and unconditional model evaluations at every sampling step, so an N-step trajectory takes 2N forward passes. Single-pass alternatives reduce such cost, yet most collapse CFG's two components into one opaque guided prediction, losing the separable base flow and guidance direction that support per-step control and diagnostics, even when the scale remains adjustable. This work introduces CtrlFlow, a single-pass guidance method that preserves CFG's separable base-flow and guidance-direction interface. To preserve both components at one-pass cost, CtrlFlow attaches two lightweight LoRA adapters to a frozen backbone, each adding 2.5% parameters, and predicts the base flow and guidance direction from one pass of the shared frozen backbone. Because the guidance scale multiplies the guidance direction only after the forward pass, one evaluation yields the guided velocity at any scale, so a single trained checkpoint remains adjustable at inference without retraining. Preserving two outputs introduces a training mismatch: inference amplifies guidance-direction errors by the chosen scale, while naive component-wise losses weight both outputs equally. To align training with this composed inference-time error, CtrlFlow uses a unified multi-scale distillation loss. Residual guidance errors can still persist at extreme scales, where even small guidance-direction errors are amplified by the guidance scale. To reduce this inference-time error, CtrlFlow applies scale-adaptive modulation to damp velocity-field errors and time-grid warping to concentrate solver evaluations where the trajectory changes most rapidly.

---


### 64. [ME^2FDiff: Multiscale Expert Enhancing Feature Diffusion in Residual Network for Brain Tumor Segmentation](https://arxiv.org/abs/2611.05766)

**<font color=#1a73e8>作者：</font>** Afrida Rahman, Bijoy Kundu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated segmentation of post-treatment glioma from MRI is essential for accurate diagnosis and treatment planning, yet remains difficult. Surgery and chemoradiotherapy cause structural changes in brain like resection cavities, edema, and fibrosis, that alter imaging appearance and mimic tumor recurrence. Contemporary segmentation architectures attain high accuracy with two limitations. First, the bottleneck originates from the deepest encoder stage, so one representation must serve sub-regions that differ widely in size and appearance. Second, they produce the segmentation in a single forward pass with no mechanism for refinement. We propose ME^2FDiff, a single-model architecture, addressing both. An attention-conditioned spectral diffusion block refines the bottleneck. It uses the image-conditioned latent diffusion process with two processes: a spatial pre-attention gate and a spectral fusion block whose timestep-adaptive bandpass filter selects the informative frequency band at each noise level. A multiscale expert-enhanced feature block fuses the intermediate encoder scales into the bottleneck through expert-selected shared tokens, guaranteeing balanced utilization without an auxiliary loss. On the BraTS 2024 post-treatment glioma dataset, ME^2FDiff achieves the best results on every tumor sub-region among all single-model baselines (91.23% Dice, 84.52% IOU, 2.13 mm HD95 on whole-tumor) and surpasses a three-expert ensemble on both overlap metrics at roughly one-third of its inference cost. Against recent state-of-the-art methods retrained under identical conditions, it maintains the strongest performance with the fewest parameters of any competing model. These findings demonstrate that a single, compact network can absorb the specialization, usually sought through ensembling or larger architectures.

---


### 65. [Optimizing Recourse Under Predictive Multiplicity](https://arxiv.org/abs/2611.05774)

**<font color=#1a73e8>作者：</font>** Shahin Jabbari  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Algorithmic recourse identifies modifications that can change an unfavorable model prediction into a favorable one. Under predictive multiplicity, similarly performing models can disagree on individual predictions, so recourse valid for one model may fail for another. We formulate robust recourse under predictive multiplicity as a budget-constrained minimization of the worst-case validity loss across a competing set of models, which can include models with different architectures or from different hypothesis classes. We propose an oracle-efficient algorithm called ORPM and prove sufficient conditions for its convergence. We evaluate ORPM on one synthetic and five real datasets, and competing sets consist of linear, neural, mixed, and decision-tree models. Our experiments show decreasing optimization-gap bounds and high validity in many tested settings, with favorable performance against baselines designed for specific model classes or architectures. We also quantify how requiring a common action across competing models changes recourse success at a given budget and examine disparities in this success across demographic groups.

---


### 66. [Private Vulnerability Testing for User Oversharing](https://arxiv.org/abs/2611.05779)

**<font color=#1a73e8>作者：</font>** Alexander Boyd, Daniel Gardham, Nishanth Sastry 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Users can inadvertently increase their vulnerability to privacy attacks by oversharing personal information. In particular, the combination of individually innocuous attributes can place a user in a sufficiently small population to enable linkage or re-identification attacks. We present a privacy-preserving mechanism that allows users to determine whether the information they disclose places them below a predefined population threshold, without revealing their query or the data of other users. Our setting presents several practical challenges: users contributing data may be offline when queries are made, queries may select arbitrary subsets of attributes, and neither server should learn the queried population or its size. We address these challenges using secret-shared data and queries, private equality testing, and secure threshold computation. Our protocol provides computational privacy against a malicious client and semi-honest, non-colluding servers, while supporting arbitrary queries and dynamic database updates. We define reactive $f$-privacy for a dynamically evolving database and prove that our construction satisfies it, with the sequence of permitted threshold outputs defining the information available to the adversary across an execution. We optimise the protocol using oblivious-transfer extensions and pre-computation, achieving sub-second online query times for 96-bit queries on datasets of up to one million records.

---


### 67. [WayPOP: A Panoramic Open-Set Panoptic Tracking Benchmark](https://arxiv.org/abs/2611.05801)

**<font color=#1a73e8>作者：</font>** Rohit Mohan, Maximilian Luz, Swarnava Chowdhury 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Holistic perception for autonomous agents requires reliably segmenting and associating scene elements across time and camera views, including objects outside a fixed semantic taxonomy. Existing open-set panoptic benchmarks focus on individual images or views, while panoramic tracking benchmarks assume closed-set taxonomies. Consequently, these benchmarks do not evaluate whether unknown objects can be consistently segmented and tracked across synchronized multi-camera sequences. We introduce WayPOP, a panoramic open-set panoptic tracking benchmark built on real Waymo PVPS sequences augmented with diverse out-of-taxonomy 3D assets from Objaverse. Inserted objects are placed at fixed locations in the 3D scene and rendered using calibrated vehicle-mounted cameras as the ego vehicle and surrounding traffic move, providing temporally and cross-view consistent panoptic annotations and auxiliary LiDAR range observations. WayPOP contains approximately 670 curated assets instantiated as 980 unique unknown-object tracks, yielding 53,452 unknown-object mask annotations across 21,300 camera images. Our evaluation protocol defines a hierarchy of tasks from view-independent open-set panoptic segmentation to full panoramic open-set panoptic tracking, using known/unknown PQ and (w)STQ metrics. We benchmark representative open-set and open-vocabulary segmentation methods with temporal and cross-camera association. Our results reveal substantial limitations of current methods in truly open-set scenarios, highlighting robust unknown-object localization and identity association across time and views as major open challenges.

---


### 68. [Matching the Training-Time Weight Rule in Inference-Time Expert Deactivation](https://arxiv.org/abs/2611.05804)

**<font color=#1a73e8>作者：</font>** Hao Cheng, Zhiyu Yang, Bo Ma 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Expert deactivation at inference time changes both token routing and expert weights, and its effect on performance depends on how these changes are implemented. We compare removal, freezing, remaining-expert renormalization, and unnormalized re-routing on identical disabled sets across five instruction-tuned checkpoints from four model families, with a base OLMoE checkpoint as an additional comparison. We develop a weight-sum model that relates the loss of expert contributions and changes in branch scale to the weight rule used during training. With half of the experts deactivated according to activation-based rankings, remaining-expert renormalization yields the highest perplexity in models trained with raw router probabilities, whereas unnormalized re-routing yields the highest perplexity in models trained with normalized weights. Perplexity ranges from 1.4 to 73 times the intact baseline when the training rule is retained, and from 14 to 28,740 times the baseline under a rule mismatch. Task outcomes vary across evaluation types: on OLMoE, GSM8K strict-match accuracy falls to zero under all four implementations. Extending the model to changes in the number of active experts yields a further prediction, supported by the OLMoE experiments: the perplexity penalty from additional renormalization increases as fewer experts are activated.

---


### 69. [ReTailor: A Residual Feature Tailoring Framework for Real-Time Cross-Sensor Pansharpening Adaptation](https://arxiv.org/abs/2611.05811)

**<font color=#1a73e8>作者：</font>** Jing-Ze Liang, Wei-Jie Xiao, Zi-Han Cao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent pansharpening models achieve strong fusion performance on trained sensors, yet often generalize poorly to unseen sensors. Existing cross-sensor adaptation is limited by target-sensor retraining, which requires target-sensor training pairs and a dedicated training stage, and by per-image zero-shot adaptation, which is computationally expensive due to whole-network optimization for each test image. To address these problems, we propose ReTailor, a real-time sequential cross-sensor adaptation framework. Only a lightweight residual Feature Tailor is rapidly optimized under self-supervised, physics-aware constraints to correct cross-sensor shifts without modifying the well-learned fusion prior. For efficient and effective deployment, ReTailor combines content-aware patch selection, which identifies a few informative patches per image for optimization at negligible cost to improve both quality and efficiency, with rolling residual bootstrap, which inherits sensor-related knowledge across the image stream to further improve quality. Extensive experiments on cross-sensor adaptation settings show that ReTailor mitigates cross-sensor degradation both effectively and efficiently. Moreover, we compare ReTailor with Low-Rank Adaptation (LoRA), a widely used method for fine-tuning, to demonstrate the advantages of our approach. We further evaluate the core principle of ReTailor on two additional remote sensing tasks: super-resolution pansharpening and image segmentation, where it consistently improves performance. In general, ReTailor provides a highly effective and efficient strategy for deploying pansharpening models under real-world cross-sensor degradation, while also offering useful insights into managing cross-sensor degradation in other remote sensing tasks. Code will be released at this https URL .

---


### 70. [GRIDSHIELD: Verifiable Grid Feasibility and Manipulation Resistance in Privacy-Preserving Peer-to-Peer Energy Trading](https://arxiv.org/abs/2611.05816)

**<font color=#1a73e8>作者：</font>** Abdullahil Kafi, Md Zahidul Islam, Alvi Ataur Khalil  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Blockchain-based peer-to-peer (P2P) energy markets let neighbors trade directly, but concentrate unchecked power in the clearing operator. Most prior work addresses only part of this: network-aware clearing respects grid constraints but operates on plaintext allocations, while privacy-preserving designs hide bids yet either drop the network constraint, enforce it only inside an unauditable computation, or recover it at the cost of a per-circuit trusted setup. Neither considers what happens if an adversary captures the operator's clearing privilege to reorder trades for profit or curtail a rival. We present GRIDSHIELD, a P2P energy-trading system that clears sealed bids with an order-independent batch program, removing the welfare a compromised operator can extract by reordering trades, and proves the result grid-feasible via an aggregated congestion-feasibility proof (ACFP). Exploiting the additive homomorphism of Pedersen commitments, ACFP reconstructs each grid constraint directly from per-bus commitments, reducing feeder-wide feasibility verification over any public grid constraints to a single aggregated range proof over the hidden allocation, with a reveal-and-recompute challenge that catches feasible yet unfair clearings. We introduce congestion-responsibility fairness (CRF), a metric scoring curtailment against each party's physical responsibility for congestion rather than consumption. We evaluate GRIDSHIELD against three prior P2P energy-trading designs across four feeders, including a 240-node Midwest feeder with real hourly loads, on a live Hyperledger Fabric network benchmarked with Hyperledger Caliper. GRIDSHIELD proves an entire round feasible with a few-kilobyte proof and no trusted setup, rejects infeasible allocations two of the three compared designs accept, and sustains $\approx$1064 tx/s.

---


### 71. [Navigational Safety of Marine Surface Vehicles in Restricted Visibility: From Intelligent Vision to Vision-Centered Multi-Sensor Fusion](https://arxiv.org/abs/2611.05818)

**<font color=#1a73e8>作者：</font>** Ryan Wen Liu, Fengchuan Song, Tianxiang Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Marine surface vehicles (MSVs) have attracted considerable attention for their commercial, scientific, and military applications. Owing to their favorable performance-to-cost ratio, shipboard cameras are widely used to detect and recognize potentially hazardous situations across diverse operational scenarios. However, visual perception is inevitably degraded by restricted conditions, including irregular motion of the imaging platform, adverse weather, and long imaging distances. To improve situational awareness and navigation capabilities, complementary sensors, such as the automatic identification system (AIS), radar, and light detection and ranging (LiDAR), etc., have become essential shipboard equipment. Multi-sensor fusion can provide richer perceptual information and help ensure navigational safety of MSVs in restricted visibility. This article reviews recent progress from intelligent vision to vision-centered multi-sensor fusion for newcomers and researchers in intelligent ship navigation and intelligent waterborne transportation system (IWTS). After introducing the generation of quality-degraded images in restricted visibility, we will review intelligent vision methods for four key issues, i.e., shipboard video stabilization, visual perception enhancement, object detection and tracking, and navigable area segmentation. We then examine vision-centered multi-sensor fusion methods, including infrared-visible image fusion, radar-vision fusion, LiDAR-vision fusion, AIS-vision fusion, and other multi-sensor fusion scenarios. Open-source datasets and safety-critical applications are also summarized and discussed. Finally, we highlight open challenges and future research directions. The collected maritime datasets are available at this https URL and will be regularly updated.

---


### 72. [DualCast: Dual-Image Conditioned Diffusion Transformers for Digital Human E-Commerce Video Generation](https://arxiv.org/abs/2611.05825)

**<font color=#1a73e8>作者：</font>** Lifan Jiang, Yibo Zhao, Senlin Cheng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Digital human e-commerce video generation requires preserving product appearance, human identity, and overall video style during dynamic demonstrations. Although recent models support multiple reference images, their general conditioning schemes do not explicitly distinguish the asymmetric roles of "what is presented" and "who presents it." Consequently, generated videos may favor a single reference, resulting in product distortion, identity drift, or single-reference collapse. To address this issue, we propose DualCast, a role-addressed dual-image conditioning framework for video generation. By explicitly modeling the distinct roles of product and human conditions, DualCast reduces role ambiguity and feature competition between references. First, a dual-spatiotemporal slot injection mechanism VAE-encodes the product and human images separately and places their latent features at the front and rear boundaries of the DiT sequence, enabling sequence-level condition separation and directed injection. Second, a mask-guided region-weighted loss strengthens supervision over product, face, and product-face overlap regions, improving generation fidelity in critical areas. Third, image condition dropout enables a single model to support dual-image, product-only, and human-only generation. In addition, we construct a curated dataset of 10K e-commerce videos for model training. Experimental results demonstrate the strong performance of DualCast.

---


### 73. [Autonomy and Coordination in Intelligent Manufacturing: A Recursive Autonomous Agent Framework](https://arxiv.org/abs/2611.05828)

**<font color=#1a73e8>作者：</font>** Yuning Chen, Hongda Zhang, Linqiang Hu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Intelligent production requires systems to make decisions and organize work according to production goals and operating conditions. It also requires continuous adjustment through feedback. This paper analyzes intelligence in human production organizations from a complex adaptive systems (CAS) perspective. The analysis identifies two coupled mechanisms: individual autonomy and collective coordination. Individual autonomy enables actors to form local decisions using available information. Collective coordination aligns these decisions with shared goals and joint constraints. Learning and adaptation improve both mechanisms over time. A production-system model formalizes how local decision rules and coordination jointly form system decisions. On this basis, we propose the Recursive Autonomous Agent (RAA) framework, which combines goal-driven autonomous agents with a recursive organizational structure. Goal contracts define local objectives and operating boundaries, while capability contracts support the selection and composition of production units. Common interfaces allow coordinated groups to participate as units in larger organizations, connecting equipment, production lines, and factories. RAA thus provides an engineering approach to next-generation intelligent manufacturing, translating the requirements of intelligence, openness, and system-wide integration into mechanisms for autonomous and coordinated production.

---


### 74. [Sure Enough to Share? Overconfidence in GenAI Video Discernment is Associated with Sharing Intentions](https://arxiv.org/abs/2611.05844)

**<font color=#1a73e8>作者：</font>** Haoning Xue, Sijia Qian, Christopher Calabrese 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative Artificial Intelligence (GenAI) is blurring the line between synthesized and recorded videos, but less is known about people's awareness of their discernment abilities and the consequences of miscalibration. This study examines three forms of overconfidence in GenAI video discernment (i.e., overestimation, overplacement, and overprecision) and their associations with source judgments and sharing intentions in an online study (N = 973). Participants evaluated videos depicting everyday scenes and achieved 62.5% accuracy. Three forms of overconfidence showed distinct patterns: participants overplaced themselves by 12.8 percentile points, but overprecision showed consistent positive associations with sharing intentions and the tendency to classify videos as human-made. Age, GenAI usage, and AI literacy showed consistent positive associations with all three forms of overconfidence. These findings highlight the importance of distinguishing the three forms of overconfidence to better understand GenAI engagement and incorporating metacognition into interventions to support informed media consumption.

---


### 75. [Risk Control Certifies Rates, Not Magnitudes: An Audit of Selective Fetal Biometry](https://arxiv.org/abs/2611.05851)

**<font color=#1a73e8>作者：</font>** Zhengshuai Yang, Linna Jiang, Changyun Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Prenatal ultrasound biometry must return a head circumference (HC) and refuse when the image cannot support one. Selective prediction trades coverage against error, but its finite-sample guarantees bound the rate of gross errors, not their magnitude. We audit a tool-grounded biometry pipeline on two separately pre-registered four-way splits of the 999 labelled HC18 images, retraining the segmenter three times on each. Calibrating the contour-completeness threshold by exact Clopper-Pearson risk control returns a certificate indistinguishable from a hand-set floor, yet the pipeline still emits a 271.3 mm error: a small, geometrically complete ring fitted to an image whose true HC is 324.6 mm. The accepted candidate scores 0.94 completeness, so the score cannot see the failure, and one outlier among $\approx 150$ answers leaves the certified risk bound ($\alpha = 0.10$) intact. A second, untouched split reproduces the mechanism on a different image (233.3 mm). Constraining the admissibility region---the anatomical range in which the measurand is defined---removes the family instead: raising the lower bound from 50 to 55 mm costs 0.4 coverage points and cuts the worst-case error on both splits to 11.4 and 11.1 mm, whereas suppressing it through the completeness threshold costs 19.0 and 12.1 points. At an anatomically defined 70 mm the frozen tests give 1.91 and 1.81 mm MAE.

---


### 76. [On Convergence of Gradient Temporal-Difference Learning with Regularized Corrections and Eligibility Traces](https://arxiv.org/abs/2611.05869)

**<font color=#1a73e8>作者：</font>** Jingyi Jin, Martha White, Hao Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Temporal-difference (TD) learning underlies many prediction and control algorithms, but can diverge when combined with off-policy learning, bootstrapping, and function approximation. TD with Regularized Corrections (TDRC) is theoretically sound and practically simple, but existing convergence theory covers only the one-step case under i.i.d. sampling, while the Huber Bellman-error formulation has not been extended to TDRC or eligibility traces. In this work, we establish convergence of constrained TDRC($\lambda$) with diminishing stepsizes and non-i.i.d. off-policy data, for state-dependent and history-dependent $\lambda$-parameters. We also propose TDRC($\lambda$)-Huber, which preserves the TDRC($\lambda$) fixed point while reducing sensitivity to large Bellman errors. For both algorithms, we apply an ODE-based weak-convergence method from stochastic approximation theory. For the nonlinear mean dynamics of TDRC($\lambda$)-Huber, we give an integral small-gain condition that guarantees uniqueness and global asymptotic stability of the target equilibrium. We then establish convergence of the constrained algorithm, derive computable sufficient conditions for convergence, and identify a regularization-based convergence mechanism shared by linear TDRC($\lambda$) and TDRC($\lambda$)-Huber. When the mean TD matrix is positive stable, both constrained algorithms converge under sufficiently strong regularization without requiring positive definiteness.

---


### 77. [Feature Puzzles: Single-Image Supervision for Multi-View 3D-Aware Segmentation](https://arxiv.org/abs/2611.05874)

**<font color=#1a73e8>作者：</font>** Jiahao Ma, Qiang Zhang, Miaomiao Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Humans can easily recognize the same objects across different viewpoints of a 3D scene, whereas teaching models such multi-view-consistent perception typically requires videos or calibrated multi-view captures, which are considerably more expensive and less diverse than large-scale monocular data.~In this paper, we introduce Feature Puzzles, a novel framework for learning multi-view-consistent segmentation using only single-image semantic segmentation supervision. Specifically, we propose a simple yet effective pipeline that constructs multi-view-consistent segmentation pseudo-labels through image cropping and geometric transformations. We further introduce a lightweight, plug-and-play network that leverages the multi-view-consistent image features learned by existing pretrained 3D foundation models and the generated pseudo-labels to perform multi-view-consistent segmentation. Importantly, our flexible framework supports various types of prompts provided from one or multiple views and can be readily extended to open-vocabulary 3D segmentation. Under this single-image supervision, our feed-forward model achieves the best mIoU on NVOS, remains competitive on SPIn-NeRF and ScanNet++ against baselines using per-scene optimization or in-domain multi-view training, and demonstrates zero-shot transfer to open-vocabulary 3D segmentation. Visual comparisons are available on our project page: this https URL

---


### 78. [MIGONet: a multiple-input graph neural operator with solver-free discrete manufactured-solution training](https://arxiv.org/abs/2611.05876)

**<font color=#1a73e8>作者：</font>** Muhammad Hasnain, N. K. Anand, Arun Srinivasa  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Surrogate modeling of transport requires operators that capture the combined influence of spatially distributed sources and Dirichlet and Neumann boundary conditions, together with training datasets that can be generated at low computational cost. This work presents MIGONet, a multiple-input graph neural operator, and a discrete method of manufactured solutions (MMS) that trains it without solving a partial differential equation, using steady heat conduction as the model problem. In the discrete MMS procedure, temperature fields are prescribed a priori, and the source terms and Dirichlet or Neumann boundary data are evaluated with the same discrete operators as the reference finite-difference method (FDM), so every training sample satisfies the discrete governing equations by construction. Because the boundary data are derived from each field, a Dirichlet or Neumann condition can be assigned to every boundary segment of every sample, and the boundary specification becomes an operator input. MIGONet supplies representations of the complete source field and boundary data to every node before local message passing. On the rectangular domain, it is compared with a version without the complete-source encoder (MIGONet-local) and with the multiple-input operator network MIONet, using the same training data. MIGONet achieves mean relative temperature errors of 10.31% and 10.64% for curved-wire and Gaussian-spot heating, compared with 45.97% and 48.34% for MIONet and 72.25% and 67.82% for MIGONet-local. For 10,000 samples, discrete MMS reduces data-generation time from 486.65 s to 3.15 s relative to matched iterative FDM labeling. Separately trained MIGONet models are also evaluated on L-shaped, disc-shaped, and ring-shaped domains.

---


### 79. [Compiling, Validating, and Using Human Reference Atlas Cell Type Annotation Crosswalks](https://arxiv.org/abs/2611.05888)

**<font color=#1a73e8>作者：</font>** Nicole Vasilevsky, Aleix Puig-Barbe, Andreas Bueckle 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The Human Reference Atlas (HRA) v2.5 includes 4,807 anatomical structures, 1,347 cell types, and 2,215 biomarkers (genes, proteins, lipids); 81 organs with 1,392 anatomical structures modeled in three dimensions (3D). Mapping new data into the HRA requires 3D spatial registration and/or cell type annotation (CTann). Many CTann tools exist but few use cell type names linked to Cell Ontology (CL), making comparisons across tools, tissues, and organs difficult. The HRA supports five transcriptomics CTann tools (Azimuth, CellTypist, popV, FR-Match, Pan-Human Azimuth), four sc-proteomics CTann tools (DeepCell Types, DeepCell Types-HuBMAP, Robust Image-Based Cell Annotator [RIBCA], and SpaTial cELl LeARning [STELLAR]), plus a Cell Distance Explorer (CDE) Spatial Omics collection covering previously published annotations across 12 tissue types with 47,349,496 cells. Assigned cell types differ in number, resolution, and coverage. This paper details how 10 crosswalks were constructed, validated, and used to compile a "Supertree" that can be used to compare CTann across organs and technologies in support of reference atlas constitution and usage. All data and code can be accessed at this https URL.

---


### 80. [Chronos: Sequential Identity-Preserving Video Generation by Temporal Anchoring](https://arxiv.org/abs/2611.05893)

**<font color=#1a73e8>作者：</font>** Mengqi Huang, Wenchuan Wang, Zhendong Mao 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Identity-preserving video generation aims to synthesize high-quality and visually realistic videos from textual and visual conditions while faithfully maintaining the subject's identity across diverse motions. Prior methods have extensively introduced reference-guided control signals and identity-aware conditioning to improve facial alignment from reference images. However, improving static identity alignment alone creates a fundamental tension between identity fidelity and temporal controllability, which frequently causes identity drift or motion suppression under large pose variations and multi-segment sequential actions. To address this, we propose Chronos, a framework that unifies single-segment facial identity preservation and multi-segment sequential action generation under a common temporal formulation. Specifically, Chronos integrates Semantic Prompt Anchoring to adaptively refine the user prompt, Visual Frame Anchoring to transform conditions into visually grounded keyframe anchors for visual guidance, and Metric-Guided Candidate Routing to select the highest-quality videos from heterogeneous generators via multi-dimensional evaluation. Extensive evaluations demonstrate the superiority of our approach, which achieved first place in both Track 1 and Track 2 of the ACM MM 2026 Identity-Preserving Video Generation Challenge, demonstrating its effectiveness across both facial identity preservation and sequential action generation settings.

---


### 81. [Information-Matched Auditing of Conversational Emotion-Shift Forecasting: A Leakage-Safe Evaluation Protocol](https://arxiv.org/abs/2611.05895)

**<font color=#1a73e8>作者：</font>** Bin Wen, Dai-Qiao Zhang, Tien-Ping Tan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Comparisons in conversational emotion-shift forecasting are easily distorted when a learned model receives rich features but its transition baseline is given a noisy or unavailable current-emotion label, when hyperparameter budgets differ, or when target-turn information enters the representation. We present an information-matched, leakage-safe auditing protocol that closes these gaps with an explicit commitment point, executable causality tests, equal four-configuration validation searches, and seed-dialogue-aware inference. Applying it to six causal model families on four text corpora and two feature-source sensitivity configurations shows that a deployable train-only current-emotion classifier feeding the transition baseline yields a different verdict than an oracle diagnostic where both sides receive gold current emotion. Under the deployable condition, learned models improve over the predicted-label baseline on all four primary corpora; DailyDialog gains are large and survive a 72-comparison Holm correction (best ROC-AUC gain = +0.167, adjusted p=.0144). Under matched gold information, the baseline remains competitive on IEMOCAP and stronger on MELD, while every model retains a large DailyDialog advantage. We additionally report precision-recall AUC, calibration, a strictly utterance-local feature control, same-person self-shift forecasting, and a future-access dose-response test. An eight-item leakage checklist accompanies the protocol. Code, raw seed predictions, and reporting artifacts are available from the corresponding author upon request.

---


### 82. [Do Saliency Maps Fail Dense Breasts? A Chance-Normalized, Confounder-Aware Audit of Explanation Fairness in Mammography](https://arxiv.org/abs/2611.05909)

**<font color=#1a73e8>作者：</font>** Ahmed Jaheen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Saliency maps, offered as evidence that mammography classifiers use the cancer, are untested in dense breasts, which can hide cancers. We tested whether they locate cancers worse there, and why. On 1,345 malignant CBIS-DDSM views, we scored three CNNs' Grad-CAM, Integrated Gradients and occlusion maps by whether their peak hits the lesion and a chance-normalized lesion-to-background saliency ratio (bits; +1 doubles it). Unadjusted gaps were large: Grad-CAM peaks hit 44% of dense vs. 58% of non-dense lesions. Case mix, chiefly more calcifications in dense breasts, explained about half or more of each gap. Occlusion kept a significant average of -0.56 bit gap. Controls also implicate the classifiers: unadjusted gaps exceeded an image-only conspicuity map's, and models relied less on dense-breast lesions. We recommend reporting density gaps before and after case-mix adjustment, per classifier, with conspicuity and lesion-reliance controls.

---


### 83. [Autonomous agents for electricity-system planning](https://arxiv.org/abs/2611.05911)

**<font color=#1a73e8>作者：</font>** Yoon Pyo Lee, Samrendra Roy, Jay Phil Yoo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Planning electricity systems requires repeated decisions that connect regional resources, investment, operation and network constraints. Here we present an autonomous planning framework that carries prepared regional scenarios through proposal, numerical evaluation, feedback interpretation, redesign and final plan selection. Agents propose investment bounds, storage operating conditions and feeder interventions, interpret numerical feedback, and decide how to revise designs and when to stop. The framework automatically executes annual investment-and-dispatch optimization and representative-feeder verification, applies fixed acceptance criteria and retains the lowest-cost accepted candidate. We evaluate forty carbon-constrained trajectories across ten system-year scenarios in five electricity systems and four countries, using two model deployments and single- and multi-agent architectures. All forty retain candidates satisfying the implemented physical and fixed annual operational carbon-budget checks. Twenty-eight of forty matched reference designs exceed the new scenario ceilings. A separate archive of ninety-six trajectories under a common 1,000 Mt annual ceiling provides matched references and broader regional coverage. The results demonstrate autonomous planning under explicit emissions constraints using public regional data and published institutional demand outlooks.

---


### 84. [DecoupAttn: Decoupled Sparse Attention for Training-Free Acceleration of Video Diffusion](https://arxiv.org/abs/2611.05917)

**<font color=#1a73e8>作者：</font>** Yanjin Li, Bingbing Qiu, Qiang Huang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sparse attention accelerates few-step video diffusion transformers by computing a few key blocks exactly and compensating for the rest. However, existing sparse attention still faces key challenges, including identification overhead from finding critical blocks at every denoising step, suboptimal budget allocation that sets sparsity budgets uniformly or by local metrics, and cross-step error accumulation as reused masks or clusters go stale. Observing that the errors left on skipped blocks cancel each other once every key is compensated, we propose DecoupAttn, a new paradigm of decoupled sparse attention: semantic clusters compensate every key, and exact attention corrects their error on a few blocks fixed once offline by position. To support this paradigm, we introduce Distortion Budget, a rate-distortion objective for budget allocation that places exact computation across timesteps, layers, and heads where it removes the most distortion that compensation leaves in the final latent. Built on this budget, we further propose Reassign Cache, in which each step reassigns the drifting keys to cached centroids and refreshes compensation while the budgeted blocks stay fixed. Moreover, DecoupAttn is training-free: a few calibration clips compile one plan offline, and inference runs standard block-sparse kernels with one fused compensation kernel. Our code will be released after submission.

---


### 85. [3D Banff Glomerulitis Scoring for Kidney Transplant Pathology: Feasibility Study for Volumetric Quantification](https://arxiv.org/abs/2611.05925)

**<font color=#1a73e8>作者：</font>** Yanfan Zhu, Junchao Zhu, Ruining Deng 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Quantifying glomerular inflammation in kidney-transplant biopsies is traditionally performed on single whole-slide sections using the Banff "most-severe section" rule, despite the inherently three-dimensional nature of lesion distribution. This 2D based assessment might lead to instability when inflammation varies across slices. This paper reports a feasibility study examining the technical feasibility and clinical relevance of extending Banff scoring into three dimensions. To this end, we propose a 3D Banff lesion-scoring framework that aligns serial sections, reconstructs glomerular identities across depth, and integrates inflammatory-cell counts in 3D under three scoring strategies: Compatible, Volumetric, and Deduplicated Volumetric. In the experiments, glomerulitis (g-scores) was used as an example Banff metric and applied to multi-section renal allograft biopsies. Our findings indicate that 3D Banff g-scores are more consistent across sections and, under the semi-automatic setting, the Volumetric strategy correlates more strongly with clinical biomarkers than traditional 2D scores. These results show that 3D volumetric quantification offers promising added value, underscoring the potential benefit of 3D-aware Banff scoring for kidney transplant pathology.

---


### 86. [Split-KV: Efficient Context Parallelism for Training Diffusion Drafters](https://arxiv.org/abs/2611.05926)

**<font color=#1a73e8>作者：</font>** Geng Zhang, Fangzhao Zhang, Cong Xie 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Diffusion drafters accelerate speculative decoding by denoising multiple draft tokens in parallel. Their training uses anchor sampling to construct compact draft queries and performs cross-attention with a block-sparse mask over a much longer context. We empirically show that acceptance length remains stable as context scales with a fixed query budget, while increasing the query budget yields diminishing quality gains, jointly establishing a practical regime with queries far shorter than the context. No existing context parallelism (CP) method jointly exploits this query--context asymmetry and meets the nonlinear, sample-dependent load-balancing requirement created by anchor sampling. We present Split-KV, an exact CP method that keeps key/value shards local and limits per-layer attention communication to query-sized tensors, making this communication independent of context length. Its global query view further enables a cost-aware longest-processing-time-first (LPT) strategy that balances context key/value chunks by their realized attention cost. At a CP size of 64, Split-KV retains 85--91\% weak-scaling efficiency and achieves up to $3.67\times$ speedup over the fastest available CP baseline. LPT achieves $<$1\% imbalance and plans three orders of magnitude faster than the best load-balancing baseline. Code is available at this https URL.

---


### 87. [Deep Meets Classical: A CPU-Efficient Decision-Fusion Model for Automatic Modulation Classification](https://arxiv.org/abs/2611.05937)

**<font color=#1a73e8>作者：</font>** Zhiyi Yin, Zhizhao Wen, Ruoxin Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Automatic modulation classification (AMC) underpins spectrum sensing and non-cooperative signal identification in cognitive radio, yet the two standard CPU-feasible approaches to it, a compact convolutional neural network (CNN) on raw in-phase and quadrature (I/Q) samples and a classical higher-order-cumulant feature classifier, are rarely compared against each other conditioned on signal-to-noise ratio (SNR). We show that they are, in fact, complementary: the CNN is markedly more robust at low SNR, where hand-crafted statistics collapse toward chance, while the cumulant classifier is more accurate at high SNR, where higher-order statistics cleanly separate dense constellations. We exploit this complementarity with FuseAMC, a lightweight decision-fusion model that trains a logistic-regression meta-combiner over the concatenated class-posteriors of an approximately 198k-parameter residual CNN and a gradient-boosted-tree cumulant classifier, on a validation split disjoint from test. On RadioML 2016.10a (5 seeds, 44k-frame held-out test set), FuseAMC reaches 55.8% overall accuracy, improving on the best cumulant-feature baseline by 5.1 points and on the CNN alone by 3.2 points (paired-bootstrap 95% confidence-interval lower bounds of 5.0 and 3.1 points, both positive), while matching the best classical baseline in its own strong high-SNR regime and the CNN in its strong low-SNR regime. With about 0.2 million parameters, a model footprint of a few megabytes, and roughly 3 MFLOPs per frame, the whole pipeline trains and runs on one CPU core, targeting general-purpose and embedded processors without hardware acceleration.

---


### 88. [BAM: Bivariate Additive Models for Interpretable Tabular Prediction](https://arxiv.org/abs/2611.05940)

**<font color=#1a73e8>作者：</font>** Atsushi Koike  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generalized Additive Models with pairwise interactions (GA$^2$Ms) are regarded as glass-box models, since each pairwise shape function can be visualized as a contour plot. In practice, the shape functions learned by methods such as EBM or NODE-GAM are so complex (irregular contours and sharp local fluctuations) that a practitioner cannot meaningfully interpret them or check them against domain knowledge. Auditability in this stronger sense requires substantially simpler shape functions. We argue that such simplification can match the accuracy of standard GAMs if the right feature pairs are captured. We propose Bivariate Additive Models (BAMs), a class of GA$^2$Ms in which every pairwise shape function is constrained to a simple parametric form, instantiated as an asymmetric bivariate Gaussian. Each component is visualizable as a unimodal contour map, and its feature pair is selected automatically during training. Experiments on six tabular benchmarks show that BAM attains predictive accuracy comparable to standard GAMs and approaches that of GA$^2$Ms. We also show the trade-off between accuracy and the number of components to inspect.

---


### 89. [FLINT: Coupling Proximal Initialization and Bounded Stochasticity for Flow-Matching Inverse Problems](https://arxiv.org/abs/2611.05945)

**<font color=#1a73e8>作者：</font>** Junseo Bang, Daewon Choi, Dong Ju Mun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Flow matching models have emerged as a dominant paradigm for generative posterior sampling in imaging inverse problems. Existing solvers follow two distinct lines of work: trajectory-space methods, which refine sampling dynamics from random initial noise, and source-space methods, which optimize the initial noise itself. While most prior work treats these as independent design choices, we show that they are inherently coupled. We derive a unified stability bound that links initialization proximity and cumulative sampling stochasticity through a multiplicative envelope, complemented by two empirical observations. First, we identify a sufficiency regime in which a moderately optimized proximal source initialization is enough to attain the performance plateau, rendering exhaustive source-space optimization unnecessary. Second, this initial advantage is fragile: it is eroded by excessive stochasticity accumulation during guided sampling, necessitating a mechanism that bounds the cumulative noise injection. These findings motivate FLINT, a two-stage framework that operationalizes this coupling. FLINT establishes a high-fidelity starting point via a manifold-constrained proximal objective in only a few iterations, then performs guided sampling under a bounded stochasticity schedule that helps prevent erasure of the initialization advantage. Across diverse inverse problems, FLINT delivers state of the art perceptual quality and competitive distortion metrics while maintaining superior computational efficiency.

---


### 90. [CLEAR: Color-Texture Latent Alignment for Single Image Reflection Removal](https://arxiv.org/abs/2611.05969)

**<font color=#1a73e8>作者：</font>** Tu Vo, Sheir A. Zaheer, Chan Y. Park  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Single Image Reflection Removal (SIRR) seeks to recover the transmitted scene from a photograph captured through glass. Recent latent restoration methods use pretrained generative priors, but many recover detail by feeding high-frequency features from the degraded input back into the decoder. This works for degradations such as blur, noise, or haze, where input detail mostly belongs to the scene. It is less suitable for SIRR, where reflections add a second structured layer: directly reusing the input's skip connections can sharpen the image while also bringing reflection edges back. Latent compression also introduces color drift and fine-detail loss.
We propose CLEAR (Color-Texture LatEnt Alignment for Single Image Reflection Removal), a deterministic, single-timestep, non-iterative latent framework that uses a pretrained latent diffusion backbone as a natural-image prior. A physics-guided separator organizes the prediction around the transmission, reflection, and residue formation model and outputs coarse layer latents in one forward pass. The Hybrid Feature Alignment Module (HFAM) then treats input-derived skips as contaminated layer-mixture features. It rectifies their high-frequency content with a clean-transmission-aligned color query, learned from the input features themselves under ground-truth feature supervision, keeping transmission-consistent texture while attenuating reflection-colored detail. CLEAR achieves the best average across fidelity and perceptual metrics on six real-world benchmarks and the lowest LPIPS on every dataset, with the largest gains on the hardest benchmarks.

---


### 91. [PathoS2VD: From 2D Histopathology to Pseudo Z-Stack Representations](https://arxiv.org/abs/2611.05974)

**<font color=#1a73e8>作者：</font>** Jiamu Wang, Keunho Byeon, Ji-Uk Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> For decades, diagnostic pathology has relied on thin two-dimensional (2D) tissue sections, despite biological tissues exhibiting inherently three-dimensional (3D) morphological organization. Because a single section captures only one focal plane, important morphological cues along the z-axis are inevitably discarded, limiting tissue representation for both human interpretation and computational analysis. In this work, we propose a generative framework that learns z-axis morphological priors from pathology z-stack data, offering a cost-effective alternative to dedicated volumetric imaging, and transfers this knowledge to conventional single-plane histopathology. Specifically, an image-to-video (I2V) latent diffusion model (LDM) is trained to synthesize a pseudo z-stack from a single 2D image, capturing plausible morphological variations across adjacent focal planes rather than reconstructing physical tissue volumes. To enable deployment on large-scale clinical datasets without native z-stack acquisition, we further introduce a prior-preserving mixture fine-tuning strategy that adapts the model to new domains while retaining the learned z-axis morphological prior. Extensive experiments demonstrate that the synthesized pseudo z-stacks exhibit realistic cross-plane morphological continuity and consistently improve downstream prostate cancer classification compared with conventional 2D representations. Our results suggest that learning transferable z-axis priors from limited z-stack data provides a practical way to enrich routine pathology images with complementary morphological information. Code: this https URL.

---


### 92. [A Comparative Study of Importance Attribution to Columns in Deep Learning over Relational Databases](https://arxiv.org/abs/2611.05986)

**<font color=#1a73e8>作者：</font>** Hila Levi-Yosefi, Shunit Agmon, Ester Livshits 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning over relational databases has led to increasingly effective prediction models, motivating a growing need to explain their behavior. We study explanation methods that assign importance scores to individual database attributes, focusing on a fundamental question: to what extent does the choice of importance-attribution method matter? We develop a methodology to systematically compare importance-attribution methods and analyze their similarities and differences. In particular, we study two aspects of the explanations: which attributes they deem important, captured by differences in attribute rankings, and how importance scores vary across attributes, captured by differences in score distributions. We further investigate whether these differences are reflected in the conventional measure of explanation quality, fidelity.
We apply our methodology in an extensive empirical study of four methods: Monte Carlo Shapley, Kernel SHAP, single-attribute impact, and mask learning. We experiment with multiple datasets and tasks using two RDL architectures: heterogeneous GraphSAGE and Relational Graph Transformers. Our experiments show that explanation methods behave differently depending on the prediction type: regression or classification. In regression, most methods exhibit high agreement in attribute rankings, whereas classification yields considerably less consensus. Notably, while mask learning frequently diverges in its importance distributions, Shapley-based methods and single-attribute impact often converge to similar explanations. This suggests that, in many settings, single-attribute impact can replace Shapley at substantially lower computational cost. Overall, our study provides methodological tools for comparing importance-attribution methods, and empirical evidence that their choice has important consequences for interpreting relational deep learning models.

---


### 93. [From Waste to Discovery: Recycling High-Scored Unexposed Candidates in Taobao Feed Recommendation](https://arxiv.org/abs/2611.05997)

**<font color=#1a73e8>作者：</font>** Ge Fan, Kai Meng, Huiping Chu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Helping users discover new interests is vital to the long-term health of industrial recommender systems, yet the usual remedy, boosting exposure of under-explored (discovery) content, often backfires in production. We report URED (Unexposed Recycling for Efficient Discovery), a training-free recall-stage system serving Taobao feed recommendation at Alibaba for over six months to tens of millions of daily active users. It rests on a production-validated insight: naive boosting fails because it injects cold, information-poor candidates that rankers systematically over-estimate, buying no discovery gain while risking engagement. Items scored highly but never exposed (signals industrial pipelines routinely discard) form a pool that is both relevant and reliably predictable. Over a 30-day horizon URED aggregates them and re-injects at recall time through a lightweight pipeline spanning offline storage, distributed aggregation, and low-latency online serving, adding under 1% latency via a single O(1) lookup per request with no model retraining. Online A/B tests show +3.47% discovered categories and +8.47% content richness with engagement preserved: completion video views rise significantly (+2.62%) and total views move positive (+0.36%, not significant). Ablations confirm both design pillars are necessary: a one-day window collapses the discovery gain to +0.55% (not significant), and random injection without score filtering yields no gain while trending negative on engagement (-0.17%). Across production recall channels, URED reaches 13.9x the platform-average discovery rate (6.3x the strongest nearline baseline) at engagement quality on par with the platform average. We share deployment details and lessons for practitioners facing the exploration-exploitation dilemma under tight resource constraints.

---


### 94. [Familiar letters, not related languages, let unseen languages into a shared space of meaning](https://arxiv.org/abs/2611.06006)

**<font color=#1a73e8>作者：</font>** Yuliang Liu, Xinyu Wang, Xiang Bai  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Hundreds of languages have written text but almost no translations, and whether a model learning one from untranslated text builds on a related language or familiar letters is unclear: they usually coincide. Here we show that familiar letters, not a related language, let an unseen language into a shared space of meaning. GlyphMind, a tokenizer-free vision transformer that reads text as pixels and lets any sentence be shown in any script, was pretrained to align translations across 27 writing systems. Adapted on untranslated Lao, a language and script it had never seen, it retrieved English translations seven times as often as the strongest simple baseline. Rewritten in unfamiliar letters, Lao did not enter although its close relative Thai was in pretraining; Santali, which had none, entered in Devanagari, familiar from Hindi, but not in its own script. Transliteration into familiar scripts may thus open multilingual models to languages without translations.

---


### 95. [Holistic Parallel Supervision for Expressive Speech to Speech Translation](https://arxiv.org/abs/2611.06010)

**<font color=#1a73e8>作者：</font>** Hao Zhang, Ismail Rasim Ulgen, Bismarck Bamfo Odoom 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Expressiveness is central to speech-to-speech translation (S2ST), yet existing datasets rarely align source and target speech jointly in content, prosody, timing, and speaker identity. Consequently, current systems often rely on indirect conditioning or transfer mechanisms. To obtain this supervision, we introduce a training-data construction strategy that combines professional dubbing, which provides human-performed correspondence in content, prosody, and timing, with multilingual voice conversion to reduce speaker mismatch. We evaluate this supervision using existing expressive S2ST systems and DirectS2ST, an end-to-end method developed in this work that predicts the complete target-speech representation directly from source speech. Experiments on English-German and English-Spanish show that holistic parallel supervision improves expressive realization across all evaluated systems. DirectS2ST exhibits the largest gains in content, prosody, timing, speaker similarity, and human-rated expressiveness. To our knowledge, this work provides the first systematic investigation of holistic parallel supervision for expressive S2ST.

---


### 96. [ChanSFormer: A Channel Agnostic Vision Transformer for Multi-Channel Cell Painting Images](https://arxiv.org/abs/2611.06015)

**<font color=#1a73e8>作者：</font>** Jingwei Zhang, Srinivasan Sivanandan, Dimitris Samaras  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-content multi-channel imaging, from Cell Painting assays to remote sensing, is central to modern scientific pipelines. Because these channels are highly heterogeneous and experimental configurations frequently evolve, a practical vision backbone must be fundamentally channel-agnostic. Current channel-adaptive vision transformers rely on global self-attention with learnable channel embeddings, which can be computed only for previously known channels. Attempts to overcome this limitation of new channels either discard the embeddings, losing channel identity, or process each channel independently, thereby eliminating critical cross-channel interactions. To address this, we introduce ChanSFormer, an efficient Vision Transformer that replaces rigid embeddings with disentangled spatial-channel attention and individual channel CLS tokens. This architecture natively preserves both distinct channel identities and cross-channel information flow. Furthermore, the individual channel class token design unlocks more informative feature representations for self-supervised learning and enables representation-based channel sampling while remaining channel-agnostic. We evaluate ChanSFormer on two biology multi-channel datasets, CHAMMI, JUMP-CP and a satellite dataset, So2Sat. Experimental results show that ChanSFormer outperforms state-of-the-art methods by 3.93%-4.27% on JUMP-CP in classification accuracy. It also demonstrates exceptional cross-dataset transferability under a self-supervised setting, outperforming previous methods by up to 2.72% in accuracy in the same classification tasks. Furthermore, the disentangled attention reduces the quadratic complexity of channel-by-spatial sequence length of the global attention baseline, thus improving throughput by 55%-313%. Code is available at this https URL.

---


### 97. [METRIC-GS: Selective Metric-Scale Estimation for 3D Gaussian Splatting](https://arxiv.org/abs/2611.06020)

**<font color=#1a73e8>作者：</font>** Sooyeun Yang, Jongseong Brad Choi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A 3D Gaussian Splatting (3DGS) reconstruction inherits arbitrary units from structure-from-motion, so it cannot be measured or used to place AR content until someone supplies a scale. Both standard recipes are fragile on real captures: on five indoor scenes with tape-measured ceilings, a quantile floor-to-ceiling heuristic errs by 27% and metric-depth alignment by 35-71% across three networks. We present METRIC-GS, a selective scale estimator for real indoor photographs: it reads the scale off the reconstruction's own semantic content and, just as importantly, refuses when the evidence is thin. A frozen 2D teacher labels Gaussians by visibility-aware voting; instance-level size priors for architectural and furniture classes (doors, tables, the floor-to-ceiling gap) are fused by a robust maximum-likelihood step; and an inlier-mass test turns thin evidence into an explicit abstention that doubles as a router to a heavyweight metric model. On 47 ScanNet++ scenes with laser ground truth, with a configuration frozen before public evaluation, the estimator alone cuts the heuristic's mean error from 21.1% to 16.6% (9.3% on the 28 scenes it acts on) at ~11 s per scene. MASt3R remains the more accurate standalone estimator (9.9%), but routing only our refusals to it matches running it everywhere with 60% fewer invocations; this selective hybrid is the configuration we advocate. Visibility-aware voting raises the scenes the estimator can act on from 16 to 28 at unchanged deployed accuracy. Applied unchanged to 13 phone and drone captures of our own, on which MASt3R fails its own registration gate 12 times, the system improves all five captures it acts on and degrades none. We also report that a current feed-forward metric model scores 2.3% on a benchmark inside its training mixture and 28-35% on captures it has never seen: a published metric-scale number is a best case, not a deployment estimate.

---


### 98. [Attraction-Ranking Mismatch in Out-of-Distribution Detection: Theory and Evidence from Hamiltonian Feature Dynamics](https://arxiv.org/abs/2611.06021)

**<font color=#1a73e8>作者：</font>** Zilin Wang, Lianghai Xiao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Attracting features toward learned in-distribution (ID) regions is an intuitive strategy for out-of-distribution (OOD) detection, but does such attraction improve detection? We investigate this question using class-conditioned Hamiltonian dynamics as a controlled testbed and identify an attraction-ranking mismatch: improving individual class-affinity scores need not improve the relative ordering of ID and OOD samples. Our analysis separates misalignment between the driving field and the detection score from ranking failure that persists even when they are aligned. An exact AUROC decomposition and a local boundary analysis identify relative score changes at the ID-OOD ranking boundary as the source of first-order AUROC change under regularity conditions. Experiments demonstrate that a score-aligned rule can improve performance on a held-out source validation split yet consistently degrade it after transfer, even without a single winning-class change. A separate perturbation study finds that near-boundary relative score changes track the direction of small AUROC changes in the tested settings. Finally, centroid approximation and shared scales connect the zero-step score to a static centroid family that includes the existing CTM detector. Together, these results explain why class attraction is insufficient to justify feature refinement and motivate evaluating its effect on the ranking boundary.

---


### 99. [Practical Estimation of the Bayes Optimal Fairness-Accuracy Tradeoff with Soft Labels](https://arxiv.org/abs/2611.06027)

**<font color=#1a73e8>作者：</font>** Mohit Sharma, Okan Koç, Amit Deshpande 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> There is a fundamental limit to the best prediction error of any model for a given data distribution. In classification, the Bayes error quantifies this limit and serves as both a benchmark for trained models and a criterion to detect overfitting. The state-of-the-art Bayes error estimation techniques for binary classification use only soft labels (positive class probabilities) and require no input features or auxiliary training. We extend such notions to constrained classification problems, such as fairness. Fair classification is an important case of constrained or multi-objective classification. It requires a model not only to be accurate but also to yield fair outcomes (equal or near-equal true positive rates) across different demographic groups (e.g., race and gender). This leads to an inherent fairness-accuracy tradeoff or a Pareto frontier that is used to compare fair classifiers against each other. The focus of our work is to estimate the fundamental limit for this fairness-accuracy tradeoff. We derive an explicit expression for the fair Bayes error rate (i.e., best achievable error rate subject to given fairness constraints), and construct consistent, instance-free estimators for it using only soft labels and group information. We provably bound the bias and the sample complexity of our estimators. Empirically, our method produces a robust, low-variance estimate of the optimal fairness-accuracy tradeoff curve, even when the soft labels are noisy and derived from a classification model on hard labels.

---


### 100. [CoordX Protocol: Peer to Peer Cryptographically Verified Shared Records](https://arxiv.org/abs/2611.06034)

**<font color=#1a73e8>作者：</font>** David Hyland-Wood, Rob Ewin  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> People, companies and software agents often must work on shared records even when they do not trust each other. Today they usually give those records to a central server. The server keeps the canonical copy, authenticates users, and decides who has permissions to act on the record. The CoordX Protocol removes the need for that central server.
In the CoordX protocol the author of a record holds full permission over it. Permission for any other party to create, read or update the record is assigned by explicit grants and keys. An invitation only starts contact between two parties. It gives no permission. Each record is a causal tree of signed entries, and each entry is immutable. Each entry names the permission that allowed it. Any party can get the proof of that permission and check it without help from anyone. Two honest parties that check the same bytes, with the same keys and local settings, always get the same answer. The content is encrypted, so the relays that may carry it in transit see only sealed bytes. To exclude a party from future content, the other parties move to new keys. The protocol does not choose a winning version, does not put entries in time order, and does not need global agreement. Applications decide what the entries mean above the level of the protocol.

---


> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-236](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
