# 📦 其他研究 | 2026年05月01日

> 本类共 **173** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-173**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-173**

---

### 151. [Semi-supervised learning with max-margin graph cuts](https://arxiv.org/abs/2604.26818)

**<font color=#1a73e8>作者：</font>** Branislav Kveton, Michal Valko, Ali Rahimi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper proposes a novel algorithm for semisupervised learning. This algorithm learns graph cuts that maximize the margin with respect to the labels induced by the harmonic function solution. We motivate the approach, compare it to existing work, and prove a bound on its generalization error. The quality of our solutions is evaluated on a synthetic problem and three UCI ML repository datasets. In most cases, we outperform manifold regularization of support vector machines, which is a state-of-the-art approach to semi-supervised max-margin learning.

---


### 152. [Bridge: Basis-Driven Causal Inference Marries VFMs for Domain Generalization](https://arxiv.org/abs/2604.26820)

**<font color=#1a73e8>作者：</font>** Mingbo Hong, Feng Liu, Caroline Gevaert 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Detectors often suffer from degraded performance, primarily due to the distributional gap between the source and target domains. This issue is especially evident in single-source domains with limited data, as models tend to rely on confounders (e.g., illumination, co-occurrence, and style) from the source domain, leading to spurious correlations that hinder generalization. To this end, this paper proposes a novel Basis-driven framework for domain generalization, namely \textbf{\textit{Bridge}}, that incorporates causal inference into object detection. By learning the low-rank bases for front-door adjustment, \textbf{\textit{Bridge}} blocks confounders' effects to mitigate spurious correlations, while simultaneously refining representations by filtering redundant and task-irrelevant components. \textbf{\textit{Bridge}} can be seamlessly integrated with both discriminative (e.g., DINOv2/3, SAM) and generative (e.g., Stable Diffusion) Vision Foundation Models (VFMs). Extensive experiments across multiple domain generalization object detection datasets, i.e., Cross-Camera, Adverse Weather, Real-to-Artistic, Diverse Weather Datasets, and Diverse Weather DroneVehicle (our newly augmented real-world UAV-based benchmark), underscore the superiority of our proposed method over previous state-of-the-art approaches. The project page is available at: this https URL.

---


### 153. [Random Cloud: Finding Minimal Neural Architectures Without Training](https://arxiv.org/abs/2604.26830)

**<font color=#1a73e8>作者：</font>** Javier Gil Blázquez  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> I propose the \emph{Random Cloud} method, a training-free approach to neural architecture search that discovers minimal feedforward network topologies through stochastic exploration and progressive structural reduction. Unlike post-training pruning methods that require a full train-prune-retrain cycle, this method evaluates randomly initialized networks without backpropagation, progressively reduces their topology, and only trains the best minimal candidate at the end. I evaluate on 7 classification benchmarks against magnitude pruning and random pruning baselines. The Random Cloud matches or outperforms both baselines in 6 of 7 datasets, achieving statistically significant improvements on Sonar ($+4.9$pp accuracy, $p{=}0.017$ vs magnitude pruning) with 87\% parameter reduction. Crucially, the method is faster than both pruning baselines in 4 of 5 datasets (0.67--0.94$\times$ the cost of full training), since it avoids training the full-size network entirely.

---


### 154. [HalluCiteChecker: A Lightweight Toolkit for Hallucinated Citation Detection and Verification in the Era of AI Scientists](https://arxiv.org/abs/2604.26835)

**<font color=#1a73e8>作者：</font>** Yusuke Sakai, Hidetaka Kamigaito, Taro Watanabe  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce HalluCiteChecker, a toolkit for detecting and verifying hallucinated citations in scientific papers. While AI assistant technologies have transformed the academic writing process, including citation recommendation, they have also led to the emergence of hallucinated citations that do not correspond to any existing work. Such citations not only undermine the credibility of scientific papers but also impose an additional burden on reviewers and authors, who must manually verify their validity during the review process. In this study, we formalize hallucinated citation detection as an NLP task and provide a corresponding toolkit as a practical foundation for addressing this problem. Our package is lightweight and can perform verification in seconds on a standard laptop. It can also be executed entirely offline and runs efficiently using only CPUs. We hope that HalluCiteChecker will help reduce reviewer workload and support organizers by enabling systematic pre-review and publication checks. Our code is released under the Apache 2.0 license on GitHub and is distributed as an installable package via PyPI. A demonstration video is available on YouTube.

---


### 155. [Uncertainty-Aware Predictive Safety Filters for Probabilistic Neural Network Dynamics](https://arxiv.org/abs/2604.26836)

**<font color=#1a73e8>作者：</font>** Bernd Frauenknecht, Lukas Kesper, Daniel Mayfrank 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predictive safety filters (PSFs) leverage model predictive control to enforce constraint satisfaction during deep reinforcement learning (RL) exploration, yet their reliance on first-principles models or Gaussian processes limits scalability and broader applicability. Meanwhile, model-based RL (MBRL) methods routinely employ probabilistic ensemble (PE) neural networks to capture complex, high-dimensional dynamics from data with minimal prior knowledge. However, existing attempts to integrate PEs into PSFs lack rigorous uncertainty quantification. We introduce the Uncertainty-Aware Predictive Safety Filter (UPSi), a PSF that provides rigorous safety predictions using PE dynamics models by formulating future outcomes as reachable sets. UPSi introduces an explicit certainty constraint that prevents model exploitation and integrates seamlessly into common MBRL frameworks. We evaluate UPSi within Dyna-style MBRL on standard safe RL benchmarks and report substantial improvements in exploration safety over prior neural network PSFs while maintaining performance on par with standard MBRL. UPSi bridges the gap between the scalability and generality of modern MBRL and the safety guarantees of predictive safety filters.

---


### 156. [Language Diffusion Models are Associative Memories Capable of Retrieving Unseen Data](https://arxiv.org/abs/2604.26841)

**<font color=#1a73e8>作者：</font>** Bao Pham, Mohammed J. Zaki, Luca Ambrogioni 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When do language diffusion models memorize their training data, and how to quantitatively assess their true generative regime? We address these questions by showing that Uniform-based Discrete Diffusion Models (UDDMs) fundamentally behave as Associative Memories (AMs) $\textit{with emergent creative capabilities}$. The core idea of an AM is to reliably recover stored data points as $\textit{memories}$ by establishing distinct basins of attraction around them. Historically, models like Hopfield networks use an explicit energy function to guarantee these stable attractors. We broaden this perspective by leveraging the observation that energy is not strictly necessary, as basins of attraction can also be formed via conditional likelihood maximization. By evaluating token recovery of $\textit{training}$ and $\textit{test}$ examples, we identify in UDDMs a sharp memorization-to-generalization transition governed by the size of the training dataset: as it increases, basins around training examples shrink and basins around unseen test examples expand, until both later converge to the same level. Crucially, we can detect this transition using only the conditional entropy of predicted token sequences: memorization is characterized by vanishing conditional entropy, while in the generalization regime the conditional entropy of most tokens remains finite. Thus, conditional entropy offers a practical probe for the memorization-to-generalization transition in deployed models.

---


### 157. [What Kind of Language is Easy to Language-Model Under Curriculum Learning?](https://arxiv.org/abs/2604.26844)

**<font color=#1a73e8>作者：</font>** Nadine El-Naggar, Tatsuki Kuribayashi, Ted Briscoe  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Many of the thousands of attested languages share common configurations of features, creating a spectrum from typologically very rare (e.g., object-verb-subject word order) or impossible languages to very common combinations of features (e.g., subject-object-verb word order). One central question is under what conditions such typological tendencies can be predicted, and specifically whether the learning bias of language models (LMs) is sufficient to reproduce such patterns. In this study, we add one dimensionality to such analysis -- the learning scenario for LMs -- to explore its interaction with the inductive bias of LMs. Specifically, as a first study, we examine the effect of curriculum learning (CL), as a developmentally motivated learning scenario, i.e., starting with simpler sentences rather than randomly-ordered input. We expand existing LM-based exploration (El-Naggar et al., 2025a,b) with a simple CL variant and find that CL substantially impacts the apparent inductive bias of LMs.

---


### 158. [Edge AI for Automotive Vulnerable Road User Safety: Deployable Detection via Knowledge Distillation](https://arxiv.org/abs/2604.26857)

**<font color=#1a73e8>作者：</font>** Akshay Karjol, Darrin M. Hanna  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deploying accurate object detection for Vulnerable Road User (VRU) safety on edge hardware requires balancing model capacity against computational constraints. Large models achieve high accuracy but fail under INT8 quantization required for edge deployment, while small models sacrifice detection performance. This paper presents a knowledge distillation (KD) framework that trains a compact YOLOv8-S student (11.2M parameters) to mimic a YOLOv8-L teacher (43.7M parameters), achieving 3.9x compression while preserving quantization robustness. We evaluate on full-scale BDD100K (70K training images) with Post-Training Quantization to INT8. The teacher suffers catastrophic degradation under INT8 (-23% mAP), while the KD student retains accuracy (-5.6% mAP). Analysis reveals that KD transfers precision calibration rather than raw detection capacity: the KD student achieves 0.748 precision versus 0.653 for direct training at INT8, a 14.5% gain at equivalent recall, reducing false alarms by 44% versus the collapsed teacher. At INT8, the KD student exceeds the teacher's FP32 precision (0.748 vs. 0.718) in a model 3.9x smaller. These findings establish knowledge distillation as a requirement for deploying accurate, safety-critical VRU detection on edge hardware.

---


### 159. [Breaking the Rigid Prior: Towards Articulated 3D Anomaly Detection](https://arxiv.org/abs/2604.26868)

**<font color=#1a73e8>作者：</font>** Jinye Gan, Bozhong Zheng, Xiaohao Xu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing 3D anomaly detection methods are built on a rigid prior: normal geometry is pose-invariant and can be canonicalized through registration or alignment. This prior does not hold for articulated objects with hinge or sliding joints, where valid pose changes induce structured geometric variations that cannot be collapsed to a single canonical template, causing pose-induced deformations to be misidentified as anomalies while true structural defects are obscured. No existing benchmark addresses this challenge. We introduce ArtiAD, the first large-scale benchmark for articulated 3D anomaly detection, comprising 15,229 point clouds across 39 object categories with dense joint-angle variations and six structural anomaly types. Each sample is annotated with its joint configuration and part-level motion labels, enabling explicit disentanglement of pose-induced geometry from structural defects. ArtiAD also provides a seen/unseen articulation split to evaluate both interpolation and extrapolation to novel joint configurations. We propose Shape-Pose-Aware Signed Distance Field (SPA-SDF), a baseline that replaces the rigid prior with a continuous pose-conditioned implicit field, factorized into an articulation-independent structural prior and a Fourier-encoded joint embedding. At inference, the articulation state is recovered by minimizing reconstruction energy, and anomalies are identified as point-wise deviations from the learned manifold. SPA-SDF achieves 0.884 object-level AUROC on seen configurations and 0.874 on unseen configurations, substantially outperforming all rigid-based baselines. Our code and benchmark will be publicly released to facilitate future research.

---


### 160. [KAYRA: A Microservice Architecture for AI-Assisted Karyotyping with Cloud and On-Premise Deployment](https://arxiv.org/abs/2604.26869)

**<font color=#1a73e8>作者：</font>** Attila Pintér, Javier Rico, Attila Répai 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present KAYRA, an end-to-end karyotyping system that operates inside the operational constraints of a clinical cytogenetic laboratory. KAYRA is architected as a containerized microservice pipeline whose ML stack combines an EfficientNet-B5 + U-Net semantic segmenter, a Mask R-CNN (ResNet-50 + FPN) instance detector, and a ResNet-18 classifier, orchestrated through a cascaded ROI-narrowing strategy that focuses each downstream model on the chromosome-bearing region. The same container images are deployed both as a cloud service and as an on-premise installation, supporting clinical environments where patient-data egress is not permitted as well as those where it is. A pilot clinical evaluation against two commercial reference karyotyping systems on 459 chromosomes from 10 metaphase spreads shows segmentation accuracy of 98.91 % (vs. 78.21 % / 40.52 %), classification accuracy of 89.1 % (vs. 86.9 % / 54.5 %), and rotation accuracy of 89.76 % (vs. 94.55 % / 78.43 %). KAYRA improves over the older density-thresholding reference on all three axes (p < 0.0001 for segmentation and classification by Fisher's exact test on chromosome-level counts), and on segmentation also against the modern AI- supported reference (p < 0.0001); on classification the difference vs. the modern AI reference is not statistically significant at the present test-set size (p = 0.34). The system reaches TRL 6 maturity and integrates the human-in-the-loop expert-review workflow that diagnostic cytogenetic practice requires. The thesis of this paper is that a multi-model cytogenetic AI service can be packaged as a microservice architecture supporting flexible deployment - cloud-hosted or on-premise - while delivering strong empirical performance on a pilot clinical evaluation.

---


### 161. [Uncertainty-Aware Pedestrian Attribute Recognition via Evidential Deep Learning](https://arxiv.org/abs/2604.26873)

**<font color=#1a73e8>作者：</font>** Zhuofan Lou, Shihang Zhang, Fangle Zhu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose UAPAR, an Uncertainty-Aware Pedestrian Attribute Recognition framework. To the best of our knowledge, this is the first EDL-based uncertainty-aware framework for pedestrian attribute recognition (PAR). Unlike conventional deterministic methods, which fail to assess prediction reliability on low-quality samples, UAPAR effectively identifies unreliable predictions and thus enhances system robustness in complex real-world scenarios. To achieve this, UAPAR incorporates Evidential Deep Learning (EDL) into a CLIP-based architecture. Specifically, a Region-Aware Evidence Reasoning module employs cross-attention and spatial prior masks to capture fine-grained local features, which are further processed by an evidence head to estimate attribute-wise epistemic uncertainty. To further enhance training robustness, we develop an uncertainty-guided dual-stage curriculum learning strategy to alleviate the adverse effects of severe label noise during training. Extensive experiments on the PA100K, PETA, RAPv1, and RAPv2 datasets demonstrate that UAPAR achieves competitive or superior performance. Furthermore, qualitative results confirm that the proposed framework generates uncertainty estimates that are predictive of challenging or erroneous samples.

---


### 162. [SEAL: Semantic-aware Single-image Sticker Personalization with a Large-scale Sticker-tag Dataset](https://arxiv.org/abs/2604.26883)

**<font color=#1a73e8>作者：</font>** Changhyun Roh, Yonghyun Jeong, Jonghyun Lee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Synthesizing a target concept from a single reference image is challenging in diffusion-based personalized text-to-image generation, particularly for sticker personalization where prompts often require explicit attribute edits. With only one reference, test-time fine-tuning (TTF) methods tend to overfit, producing \textit{visual entanglement}, where background artifacts are absorbed into the learned concept, and \textit{structural rigidity}, where the model memorizes reference-specific spatial configurations and loses contextual controllability. To address these issues, we introduce \textbf{SE}mantic-aware single-image sticker person\textbf{AL}ization (\textbf{SEAL}), a plug-and-play, architecture-agnostic adaptation module that integrates into existing personalization pipelines without modifying their U-Net-based diffusion backbones. SEAL applies three components during embedding adaptation: (1) a Semantic-guided Spatial Attention Loss, (2) a Split-merge Token Strategy, and (3) Structure-aware Layer Restriction. To support sticker-domain personalization with attribute-level control, we present StickerBench, a large-scale sticker image dataset with structured tags under a six-attribute schema (Appearance, Emotion, Action, Camera Composition, Style, Background). These annotations provide a consistent interface for varying context while keeping target identity fixed, enabling systematic evaluation of identity disentanglement and contextual controllability. Experiments show that SEAL consistently improves identity preservation while maintaining contextual controllability, highlighting the importance of explicit spatial and structural constraints during test-time adaptation. The code, StickerBench, and project page will be publicly released.

---


### 163. [Multiple Additive Neural Networks for Structured and Unstructured Data](https://arxiv.org/abs/2604.26888)

**<font color=#1a73e8>作者：</font>** Janis Mohr, Jörg Frochte  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper extends and explains the Multiple Additive Neural Networks (MANN) methodology, an enhancement to the traditional Gradient Boosting framework, utilizing nearly shallow neural networks instead of decision trees as base learners. This innovative approach leverages neural network architectures, notably Convolutional Neural Networks (CNNs) and Capsule Neural Networks, to extend its application to both structured data and unstructured data such as images and audio. For structured data the advantages of capsule neural networks as feature extractors are used and combined with MANN as a classifier. MANN's unique architecture promotes continuous learning and integrates advanced heuristics to combat overfitting, ensuring robustness and reducing sensitivity to hyperparameter settings like learning rate and iterations. Our empirical studies reveal that MANN surpasses traditional methods such as Extreme Gradient Boosting (XGB) in accuracy across well-known datasets. This research demonstrates MANN's superior precision and generalizability, making it a versatile tool for diverse data types and complex learning environments.

---


### 164. [Graph-based Semantic Calibration Network for Unaligned UAV RGBT Image Semantic Segmentation and A Large-scale Benchmark](https://arxiv.org/abs/2604.26893)

**<font color=#1a73e8>作者：</font>** Fangqiang Fan, Zhicheng Zhao, Xiaoliang Ma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fine-grained RGBT image semantic segmentation is crucial for all-weather unmanned aerial vehicle (UAV) scene understanding. However, UAV RGBT semantic segmentation faces two coupled challenges: cross-modal spatial misalignment caused by sensor parallax and platform vibration, and severe semantic confusion among fine-grained ground objects under top-down aerial views. To address these issues, we propose a Graph-based Semantic Calibration Network (GSCNet) for unaligned UAV RGBT image semantic segmentation. Specifically, we design a Feature Decoupling and Alignment Module (FDAM) that decouples each modality into shared structural and private perceptual components and performs deformable alignment in the shared subspace, enabling robust spatial correction with reduced modality appearance interference. Moreover, we propose a Semantic Graph Calibration Module (SGCM) that explicitly encodes the hierarchical taxonomy and co-occurrence regularities among ground-object categories in UAV scenes into a structured category graph, and incorporates these priors into graph-attention reasoning to calibrate predictions of visually similar and rare this http URL addition, we construct the Unaligned RGB-Thermal Fine-grained (URTF) benchmark, to the best of our knowledge, the largest and most fine-grained benchmark for unaligned UAV RGBT image semantic segmentation, containing over 25,000 image pairs across 61 categories with realistic cross-modal misalignment. Extensive experiments on URTF demonstrate that GSCNet significantly outperforms state-of-the-art methods, with notable gains on fine-grained categories. The dataset is available at this https URL.

---


### 165. [ClawGym: A Scalable Framework for Building Effective Claw Agents](https://arxiv.org/abs/2604.26904)

**<font color=#1a73e8>作者：</font>** Fei Bai, Huatong Song, Shuang Sun 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Claw-style environments support multi-step workflows over local files, tools, and persistent workspace states. However, scalable development around these environments remains constrained by the absence of a systematic framework, especially one for synthesizing verifiable training data and integrating it with agent training and diagnostic evaluation. To address this challenge, we present ClawGym, a scalable framework that supports the full lifecycle of Claw-style personal agent development. Concretely, we construct ClawGym-SynData, a diverse dataset of 13.5K filtered tasks synthesized from persona-driven intents and skill-grounded operations, paired with realistic mock workspaces and hybrid verification mechanisms. We then train a family of capable Claw-style models, termed ClawGym-Agents, through supervised fine-tuning on black-box rollout trajectories, and further explore reinforcement learning via a lightweight pipeline that parallelizes rollouts across per-task this http URL support reliable evaluation, we further construct ClawGym-Bench, a benchmark of 200 instances calibrated through automated filtering and human-LLM review. Relevant resources will be soon released at this https URL.

---


### 166. [Causal Learning with Neural Assemblies](https://arxiv.org/abs/2604.26919)

**<font color=#1a73e8>作者：</font>** Evangelia Kopadi, Dimitris Kalles  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Can Neural Assemblies -- groups of neurons that fire together and strengthen through co-activation -- learn the direction of causal influence between variables? While established as a computationally general substrate for classification, parsing, and planning, neural assemblies have not yet been shown to internalize causal directionality. We demonstrate that the inherent operations of neural assemblies -- projection, local plasticity control, and sparse winner selection -- are sufficient for directional learning. We introduce DIRECT (DIRectional Edge Coupling/Training), a mechanism that co-activates source and target assemblies under an adaptive gain schedule to internalize directed relations. Unlike backpropagation-based methods, DIRECT relies solely on local plasticity, making the resulting causal claims auditable at the mechanism level. Our findings are verified through a dual-readout validation strategy: (i) synaptic-strength asymmetry, measuring the emergent weight gap between forward and reverse links, and (ii) functional propagation overlap, quantifying the reliability of directional signal flow. Across multiple domains, the framework achieves perfect structural recovery under a supervised, known-structure setting. These results establish neural assemblies as an auditable bridge between biologically plausible dynamics and formal causal models, offering an "explainable by design" framework where causal claims are traceable to specific neural winners and synaptic asymmetries.

---


### 167. [Color-Encoded Illumination for High-Speed Volumetric Scene Reconstruction](https://arxiv.org/abs/2604.26920)

**<font color=#1a73e8>作者：</font>** David Novikov, Eilon Vaknin, Narek Tumanyan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The task of capturing and rendering 3D dynamic scenes from 2D images has become increasingly popular in recent years. However, most conventional cameras are bandwidth-limited to 30-60 FPS, restricting these methods to static or slowly evolving scenes. While overcoming bandwidth limitations is difficult for general scenes, recent years have seen a flurry of computational imaging methods that yield high-speed videos using conventional cameras for specific applications (e.g., motion capture and particle image velocimetry). However, most of these methods require modifications to a camera's optics or the addition of mechanically moving components, limiting them to a single-view high-speed capture. Consequently, these methods cannot be readily used to capture a 3D representation of rapid scene motion. In this paper, we propose a novel method to capture and reconstruct a volumetric representation of a high-speed scene using only unaugmented low-speed cameras. Instead of modifying the hardware or optics of each individual camera, we encode high-speed scene dynamics by illuminating the scene with a rapid, sequential color-coded sequence. This results in simultaneous multi-view capture of the scene, where high-speed temporal information is encoded in the spatial intensity and color variations of the captured images. To construct a high-speed volumetric representation of the dynamic scene, we develop a novel dynamic Gaussian Splatting-based approach that decodes the temporal information from the images. We evaluate our approach on simulated scenes and real-world experiments using a multi-camera imaging setup, showing first-of-a-kind high-speed volumetric scene reconstructions.

---


### 168. [On the Learning Curves of Revenue Maximization](https://arxiv.org/abs/2604.26922)

**<font color=#1a73e8>作者：</font>** Steve Hanneke, Alkis Kalavasis, Shay Moran 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning curves are a fundamental primitive in supervised learning, describing how an algorithm's performance improves with more data and providing a quantitative measure of its generalization ability. Formally, a learning curve plots the decay of an algorithm's error for a fixed underlying distribution as a function of the number of training samples. Prior work on revenue-maximizing learning algorithms, starting with the seminal work of Cole and Roughgarden [STOC, 2014], adopts a distribution-free perspective, which parallels the PAC learning framework in learning theory. This approach evaluates performance against the hardest possible sequence of valuation distributions, one for each sample size, effectively defining the upper envelope of learning curves over all possible distributions, thus leading to error bounds that do not capture the shape of the learning curves.
In this work we initiate the study of learning curves for revenue maximization and provide a near-complete characterization of their rate of decay in the basic setting of a single item and a single buyer. In the absence of any restriction on the valuation distribution, we show that there exists a Bayes-consistent algorithm, meaning that its learning curve converges to zero for any arbitrary valuation distribution as the number of samples $n \to \infty$. However, this convergence must be arbitrarily slow, even if the optimal revenue is finite. In contrast, if the optimal revenue is achieved by a finite price, then the optimal rate of decay is roughly $1/\sqrt{n}$. Finally, for distributions supported on discrete sets of values, we show that learning curves decay almost exponentially fast, a rate unattainable under the PAC framework.

---


### 169. [A Note on How to Remove the $\ln\ln T$ Term from the Squint Bound](https://arxiv.org/abs/2604.26926)

**<font color=#1a73e8>作者：</font>** Francesco Orabona  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In Orabona and Pál [2016], we introduced the shifted KT potentials, to remove the $\ln \ln T$ factor in the parameter-free learning with expert bound. In this short technical note, I show that this is equivalent to changing the prior in the Krichevsky--Trofimov algorithm. Then, I show how to use the same idea to remove the $\ln \ln T$ factor in the data-independent bound for the Squint algorithm.

---


### 170. [Artistic Practice Opportunities in CST Evaluations: A Longitudinal Group Deployment of ArtKrit](https://arxiv.org/abs/2604.26935)

**<font color=#1a73e8>作者：</font>** Catherine Liu, Tao Long, Asya Vaisberg 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Creativity support tools (CSTs) aim to elevate the quality of artists' creative processes and artifacts. Yet most current CST evaluations overlook temporal and social aspects of tool use. To address this gap, we present a longitudinal, group-based CST evaluation through a three-week deployment of ArtKrit, a computational drawing tool that supports disciplined drawing. Nine digital artists, organized into three communities of practice, completed weekly "master studies" alongside a researcher-artist. Our results show users' evolving relationships with ArtKrit over time - from early experimentation to selective incorporation or misuse - alongside changes in their ways of artistic seeing. These changes unfolded within artist support networks that fostered confidence and creative safety, and validated individual expression. Overall, our findings suggest that CST evaluations can - and should - be designed as opportunities for meaningful artistic engagement rather than purely extractive measurement exercises. We contribute this longitudinal, group-based approach as one CST evaluation method.

---


### 171. [Select to Think: Unlocking SLM Potential with Local Sufficiency](https://arxiv.org/abs/2604.26940)

**<font color=#1a73e8>作者：</font>** Wenxuan Ye, Yangyang Zhang, Xueli An 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Small language models (SLMs) offer computational efficiency for scalable deployment, yet they often fall short of the reasoning power exhibited by their larger counterparts (LLMs). To mitigate this gap, current approaches invoke an LLM to generate tokens at points of reasoning divergence, but these external calls introduce substantial latency and costs. Alternatively, standard distillation is often hindered by the capacity limitation, as SLMs struggle to accurately mimic the LLM's complex generative distribution. We address this dilemma by identifying local sufficiency: at divergence points, the LLM's preferred token consistently resides within the SLM's top-K next-token predictions, even when failing to emerge as the SLM top-1 choice. We therefore propose SELECT TO THINK (S2T), which reframes the LLM's role from open-ended generation to selection among the SLM's proposals, simplifying the supervision signal to discrete candidate rankings. Leveraging this, we introduce S2T-LOCAL, which distills the selection logic into the SLM, empowering it to perform autonomous re-ranking without inference-time LLM dependency. Empirically, we demonstrate that a 1.5B SLM's top-8 candidates capture the 32B LLM's choice with 95% hit rate. Translating this potential into performance, S2T-LOCAL improves greedy decoding by 24.1% on average across benchmarks, effectively matching the efficacy of 8-path self-consistency while operating with single-trajectory efficiency.

---


### 172. [Hyper Input Convex Neural Networks for Shape Constrained Learning and Optimal Transport](https://arxiv.org/abs/2604.26942)

**<font color=#1a73e8>作者：</font>** Shayan Hundrieser, Insung Kong, Johannes Schmidt-Hieber  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce Hyper Input Convex Neural Networks (HyCNNs), a novel neural network architecture designed for learning convex functions. HyCNNs combine the principles of Maxout networks with input convex neural networks (ICNNs) to create a neural network that is always convex in the input, theoretically capable of leveraging depth, and performs reliable when trained at scale compared to ICNNs. Concretely, we prove that HyCNNs require exponentially fewer parameters than ICNNs to approximate quadratic functions up to a given precision. Throughout a series of synthetic experiments, we demonstrate that HyCNNs outperform existing ICNNs and MLPs in terms of predictive performance for convex regression and interpolation tasks. We further apply HyCNNs to learn high-dimensional optimal transport maps for synthetic examples and for single-cell RNA sequencing data, where they oftentimes outperform ICNN-based neural optimal transport methods and other baselines across a wide range of settings.

---


### 173. [ProcFunc: Function-Oriented Abstractions for Procedural 3D Generation in Python](https://arxiv.org/abs/2604.26943)

**<font color=#1a73e8>作者：</font>** Alexander Raistrick, Karhan Kayan, Jack Nugent 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce ProcFunc, a library for Blender-based procedural 3D generation in Python. ProcFunc provides a library of easy-to-use Python functions, which streamline creating, combining, analyzing, and executing procedural generation code. ProcFunc makes it easy to create large-scale diverse training data, by combinatorial compositions of semantic components. VLMs can use ProcFunc to edit procedural material and geometry code and can create new procedural code with significantly fewer coding errors. Finally, as an example use case, we use ProcFunc to develop a new procedural generator of indoor rooms, which includes a collection of new compositional procedural materials. We demonstrate the detail, runtime efficiency, and diversity of this room generator, as well as its use for 3D synthetic data generation. Please visit this https URL for source code.

---


> [!TIP]
> 当前位于：**151-173**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-173**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
