# 📦 其他研究 | 2026年10月07日

> 本类共 **571** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**501-550**（第 11/12 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | **501-550** | [551-571](./part-12.md)

---

### 501. [Multi-Task Partially Supervised Learning for Super-Resolution and Semantic Segmentation on Earth Observation data](https://arxiv.org/abs/2610.06389)

**<font color=#1a73e8>作者：</font>** Hoàng-Ân Lê, Minh-Tan Pham, Solange Lemai-Chenevier 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Super-resolution and semantic segmentation are known to benefit one another, especially in the Earth observation context. However, learning both tasks in a joint model often requires both task annotations, which is impractical and expensive. In this paper, we study the multi-task partially supervised learning paradigm for both tasks, where each example is assumed to have only a single-task annotation. To that end, we examine two multi-task architectural variations, the sequential and shared variants, and then propose a hybrid variant and a re-projection loss to benefit from the shared representation and enforce image quality of super-resolution when training with semantic segmentation. Experiments show favorable results compared to the SOTA sequential variant. Source code will be published at this https URL.

---


### 502. [Learning Pareto Stationary Fronts via Single-Pass Backpropagation](https://arxiv.org/abs/2610.06397)

**<font color=#1a73e8>作者：</font>** Elina Rojin Celik, Marcos Medeiros Raimundo, Isabel Valera  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose MOSEL (Multi-Objective Stackelberg Efficient Learning), a framework for a posteriori multi-objective optimization (MOO) in deep neural networks that recovers a full front of Pareto stationary solutions at the computational cost of standard single-objective training. MOSEL reformulates the problem as a bilevel optimization problem that leverages network modularity to decouple representation learning from objective-preference alignment. Casting the bilevel optimization problem as a Stackelberg game enables solving the original a posteriori MOO problem in a single forward-backward pass. As a result, MOSEL matches the time and memory efficiency of standard single-objective training while enabling scalable Pareto stationary front learning. Empirically, MOSEL uncovers diverse and optimal Pareto frontiers in strongly conflicting settings (e.g., fairness-accuracy). Remarkably, even in weakly conflicting regimes such as multi-task learning, it consistently converges to solutions closer to the utopia point, outperforming both standard single-objective training and specialized multi-task learning methods. These results highlight the broader potential of a posteriori MOO learning as a pathway to efficiently learn more diverse and robust representations, ultimately improving generalization.

---


### 503. [What Did the Agent Actually Do? Evidence-Grounded Oversight for Long-Horizon Agents](https://arxiv.org/abs/2610.06406)

**<font color=#1a73e8>作者：</font>** Zhongxiang Sun, Jiahao Yan, Hongkang Zhao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As agents take on long-horizon tasks, users shift from making individual decisions to overseeing autonomous execution. Yet the volume of agent activity and the fragmentation of supporting evidence make it difficult to determine which decisions warrant user verification. We study monitors that identify consequential decisions and locate evidence to help users assess their implications. We introduce AgentMonBench, a software-engineering benchmark comprising three subsets that cover two complementary dimensions: alignment between requirements and behavior, and awareness of consequential autonomous decisions for verification. To support these judgments, we propose the Evidence-Grounded Behavior Graph (EBG), a training-free method that groups source-linked evidence into behaviors and organizes their relationships into a graph. EBG presents task-oriented views of this graph to help monitors interpret behavior in context. Experiments across eight models show that EBG improves decision identification and evidence localization in most settings compared with direct access to the original context. Further experiments show that EBG's evidence-localization gains persist across input scales and hyperparameter settings, while real-world applications illustrate its practical value for human oversight.

---


### 504. [FlashCart: Fast Cartesian Tensor Products for Equivariant Interatomic Potentials](https://arxiv.org/abs/2610.06409)

**<font color=#1a73e8>作者：</font>** Viktor Zaverkin, Payman Goodarzi, Sergey V. Sukhomlinov 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine-learned interatomic potentials extend atomistic simulations beyond the length- and timescales accessible to electronic-structure methods. However, the computational cost of equivariant architectures limits the local correlations they can represent in practice and therefore their achievable accuracy. Here we introduce FlashCart, which makes higher-order correlations affordable by combining generated GPU kernels with an architecture that recursively builds equivariant features and compresses them to a fixed width at each step. We express tensor products in independent Cartesian components and symbolically simplify them and their derivatives, producing fused kernels that often outperform optimized spherical counterparts. We then show that increasing correlation order improves accuracy more efficiently than increasing width, depth, or tensor rank. On SPICE-MACE-OFF, FlashCart models advance the measured accuracy-efficiency frontier: a model with $5.6$ million parameters achieves lower energy and force errors and $10\times$ faster inference than a transformer with $189$ million parameters.

---


### 505. [Efficient Secure Federated Learning via Information-Theoretically Secure Key Distribution: A Medical Imaging Case Study](https://arxiv.org/abs/2610.06420)

**<font color=#1a73e8>作者：</font>** Ivan Donà, Hans H. Brunner, Álvaro Troyano Olivas 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated Learning (FL) enables collaborative training of models across institutions without centralizing sensitive data, making it well-suited for privacy-concerned applications, such as medical imaging. To protect FL model updates during secure aggregation, additive masking is commonly employed. However, its underlying classical key establishment is only computationally secure. On the other hand, physics-based Information-Theoretically Secure (ITS) key exchange introduces practical constraints: finite key generation rates and time-limited storage severely limit throughput and sustained training of uncompressed models. In this work, we address this bottleneck by developing an FL framework that integrates frozen backbones, knowledge distillation, and quantization. These techniques reduce communication payload and, consequently, key material consumption. Moving beyond simulation, we benchmark this framework on a real physics-based key distribution testbed involving a chest X-ray classification application. Our results show that key usage can be reduced by $\sim$35$\times$ while maintaining predictive accuracy. This prevents buffer depletion and key expiration, enabling sustainable FL training under physical key generation constraints.

---


### 506. [Toward Reliable Infant Pose Estimation: A Training-Dynamics Approach to Noisy Annotation Detection](https://arxiv.org/abs/2610.06423)

**<font color=#1a73e8>作者：</font>** Emanuele Cardinale, Sara Moccia, Alessandro Cacciatore 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spontaneous movement analysis in preterm infants relies increasingly on markerless pose estimation (PE) to derive clinically relevant motion biomarkers directly from video recordings. Training accurate infant PE models requires large sets of manually annotated keypoints, and human annotation is inherently prone to error. Noisy keypoints (i.e., keypoints mislocalized with respect to their true anatomical position) are especially problematic in this clinical setting, since they can propagate as artificial artifacts into the reconstructed joint trajectories. Building on the small-loss hypothesis and training-dynamics-based sample selection established in the noisy-label learning literature, we propose a novel framework for detecting noisy keypoint annotations. A hybrid convolutional-attention model is trained to predict the anatomical category of each keypoint from its spatial coordinates and local visual features; the resulting cross-entropy training dynamics are then used to derive per-keypoint descriptors, which are partitioned into clean and noisy subsets via unsupervised clustering. We validate the approach on NeoPose, a newly collected dataset of 65 hospitalized preterm infants, under two realistic noise scenarios (random positional perturbation and left-right swapping) across multiple noise levels. Results show that the proposed approach achieves an F1-score of up to 91.9% in noisy-keypoint detection. The framework further generalizes to the heterogeneous COCO benchmark, where filtering CE-detected noisy keypoints from the training set also yields measurable improvements (up to 7.4 AP points) in downstream pose estimation accuracy at moderate-to-high noise levels.

---


### 507. [Do Speech Representations Preserve Regional Accent Across Read and Spontaneous Speech?](https://arxiv.org/abs/2610.06430)

**<font color=#1a73e8>作者：</font>** Paula A. Perez-Toro, Tomas Arias-Vergara, Annette Schwarz 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Regional accent cues can be captured under matched conditions, but it remains unclear whether they persist between read and spontaneous speech. We study RVG1, with 500 German speakers from nine regions, comparing ten speech representations on regional classification and continuous geolocation under matched conditions and speaker-independent read--spontaneous transfer. Whisper performs best under matched conditions, reaching 0.489 nine-way UAR and 148 km median geolocation error, but drops to 0.11/0.18 UAR across transfer directions and 363 km geolocation error. Self-supervised models show a similar degradation, whereas speaker embeddings are less discriminative in-domain but more robust under transfer. This contrast is consistent across classification and geolocation. Across representations, robustness is associated with how little a representation shifts between styles (style-invariance), for which crossstyle speaker retrieval is an interpretable proxy. Age, sex, sentence-overlap, and duration controls do not account for the gap, although channel characteristics contribute. These results show that strong matched-condition performance does not indicate robust regional information.

---


### 508. [ARO: Aligned Representation learning for multi-Omics data](https://arxiv.org/abs/2610.06443)

**<font color=#1a73e8>作者：</font>** Amogh Singh, Yash Shah, Chiara D'Ercoli 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The high cost of functional molecular assays, and prevalence of missing modalities and unmatched samples in computational biology, create significant barriers to comprehensive multi-omic profiling, essential for capturing and reasoning over molecules, cells, tissues, and organisms. This work proposes a model that learns meaningful representations from multi-omics cancer data supporting the reconstruction of missing and unpaired modalities. Contrary to increasingly complex, larger models, e.g. Foundation Models (FMs), ARO prioritizes practical applicability in limited or incomplete data settings. ARO optimally reconstructs missing modalities (MSE of $0.15$ on the validation and test data in the Unmasked settings), with its learned latent embeddings enabling a downstream cancer classification task. Our findings indicate that analyzing diverse molecular layers as a single integrated system offers a reliable and cost-efficient approach, reducing dependence on large-scale experimental testing, while still supporting multi-omic exploration in limited data settings.

---


### 509. [A Physics-Guided Transformer Framework for Electromigration Analysis in Multi-Segment Interconnects](https://arxiv.org/abs/2610.06464)

**<font color=#1a73e8>作者：</font>** Pavlos Stoikos, Anuj Pathania, George Floros  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As technology scales to smaller nodes, increasing current densities make electromigration (EM) one of the dominant reliability challenges in on-chip interconnects. Accurate transient stress analysis is needed to identify wires susceptible to EM degradation, but applying physics-based solvers across many interconnects remains computationally expensive. This paper proposes a physics-guided transformer framework for fast EM stress prediction in multi-segment interconnect lines. The framework converts each line into geometry- and DC-aware segment tokens and uses transformer attention to capture line-level context. A lightweight query decoder then predicts stress at selected locations and time instants. The model is trained with an objective that combines normalized supervised regression, linewise relative-$L_2$ loss, and physics-guided continuity and terminal-flux terms. Experiments on IBM power grid benchmarks show that the proposed model achieves relative-$L_2$ error below 8\% and reaches up to 2459.68$\times$ speedup compared with the matrix exponential~solver.

---


### 510. [Latent Flow Matching for Molecular Graph Generation](https://arxiv.org/abs/2610.06468)

**<font color=#1a73e8>作者：</font>** Mathis Goupillon, Roman Bresson, Konstantinos Divriotis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern graph generative models typically operate directly in the discrete graph space, explicitly generating node and edge variables, which can become costly as graphs grow. In this paper, we perform generation explicitly on latent representations of entire graphs obtained from a pretrained Variational Autoencoder with high reconstruction fidelity. The generated representations, obtained through flow matching, are then decoded only at the final step. Across molecular benchmarks of increasing size, our approach achieves strong validity and FCD while offering a favorable quality-efficiency trade-off compared with state-of-the-art explicit graph generative models. One of the main advantages of this formulation is that the graph representation only needs to be learned once, after which the same one can be reused across multiple generative objectives without retraining. We demonstrate generation guided by molecular properties and further introduce validity-aware generation though a classifier learned directly in latent space. All code will be made available upon acceptance.

---


### 511. [MaRO-GS: Mask-Robust Object-Centric Gaussian Splatting from Inconsistent Multi-view Masks](https://arxiv.org/abs/2610.06472)

**<font color=#1a73e8>作者：</font>** Eunji Kim, Gahyeon Kim, Gianella Cravioto 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We address the challenge of accurate 3D object reconstruction from multi-view images in Gaussian Splatting. Existing object-level 3DGS methods reconstruct the entire scene rather than directly optimizing the target object, even when only the target object is needed, which incurs substantial computational overhead. They also rely on 2D segmentation masks to associate Gaussians with objects, but these masks are often inconsistent across views. Such inconsistencies corrupt Gaussian optimization and produce incorrectly supervised Gaussians that degrade object reconstruction fidelity. To overcome these limitations, we propose MaRO-GS, a 3DGS framework that directly optimizes target-object Gaussians from object-masked multi-view images and remains robust to inconsistent supervision. For reliable supervision, mask-reliability view filtering excludes unreliable views. Object-supported Gaussian density control suppresses Gaussians irrelevant to the target object and prevents background densification, while Silhouette-aligned Object Loss maintains object-focused optimization. Extensive experiments across diverse datasets demonstrate that MaRO-GS improves PSNR, segmentation accuracy, and computational efficiency, with the largest PSNR gain of 2.05 dB on the small-object LERF-Mask dataset.

---


### 512. [FairProp: Fair Node Representation Learning via Differentiable Propagation Layers](https://arxiv.org/abs/2610.06484)

**<font color=#1a73e8>作者：</font>** Emmanouil Kariotakis, Aritra Konar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph neural networks (GNNs) are the standard tool for node representation learning and are increasingly used in high-stakes settings. Their message-passing backbone, however, can amplify topological bias, raising fairness concerns. We study group fairness at the level of downstream predictions for node classification, link prediction, and node regression, and bound the demographic parity gap for an arbitrary number of sensitive groups. Our node classification bound is provably no looser than the closest prior result. For link prediction, ours is the first bound on the parity gap of the deployed sigmoid-activated prediction rather than a pre-activation proxy, and for node regression we provide the first such bound. Across all three tasks, the analysis identifies two distinct sources of bias: the separation between group means and the within-group covariance of the final representations. Building on this insight, we embed fairness into propagation itself by augmenting the convex smoothing problem underlying APPNP with a convex group-mean constraint and a within-group covariance regularizer. Unfolding projected gradient descent on this problem yields FairProp, whose layers pair a propagation step with a closed-form projection and which provably converges linearly to the unique fair optimum. Experiments on three tasks show that FairProp, even with exact group-mean equalization alone, provides a strong inductive bias that achieves excellent fairness-utility trade-offs against strong baselines.

---


### 513. [GPlaceRL: An Open-Source Graph Reinforcement Learning Framework for Detailed Placement](https://arxiv.org/abs/2610.06489)

**<font color=#1a73e8>作者：</font>** Pavlos Stoikos, Foteini Oikonomou, Christos Poulos 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) has emerged as a promising approach for placement optimization, particularly when combined with graph neural networks (GNNs) that capture circuit connectivity. However, most learning-based placement approaches focus on floorplanning, macro placement, or global placement, while detailed placement refinement remains relatively unexplored. In this paper, we present GPlaceRL, an open-source graph reinforcement learning framework for detailed placement refinement. GPlaceRL represents legalized placements as graphs and provides a modular environment for studying graph encoders, policy architectures, reward formulations, and local placement actions. To demonstrate the capabilities of GPlaceRL, we conduct a systematic evaluation of proximal policy optimization (PPO) policies with graph attention network (GAT) encoders in a per-design optimization setting. Across five placement benchmarks, the best greedy evaluation results achieve HPWL improvements ranging from $3.27\%$ to $32.87\%$. The results highlight the importance of compact GAT architectures and flexible local action spaces for placement optimization. Overall, GPlaceRL provides a reproducible and extensible framework for systematic research on RL-based detailed placement refinement.

---


### 514. [polyview: A Python package for multi-view machine learning](https://arxiv.org/abs/2610.06491)

**<font color=#1a73e8>作者：</font>** Gwendal Debaussart-Joniec, Argyris Kalogeratos  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-view learning jointly exploits multiple complementary representations of the same data and has become increasingly important in machine learning. However, the Python ecosystem lacks actively maintained, unified tooling for end-to-end multi-view workflows. In this paper, we present polyview, a Python package that provides tools for multi-view embedding, clustering, fusion, and view augmentation, as well as for handling incomplete views, all compatible with scikit-learn. The library offers a unified interface for composing heterogeneous multi-view workflows, including seamless transitions between multi-view and single-view stages. It is built around a core set of classes and utilities that enable composition of different methods and straightforward implementation of new ones. We illustrate the package on five real multi-view datasets and compare its components based on canonical correlation analysis with those of two established libraries. polyview aims to be both a practical toolkit for benchmarking and prototyping multi-view methods and a foundation for future research and development in this area.

---


### 515. [Topology-Informed Prompt-Conditioned Universal Segmentation of Uterine Structures from Ultrasound and MRI](https://arxiv.org/abs/2610.06494)

**<font color=#1a73e8>作者：</font>** Yongheng Sun, Yuexi Gu, Jingwen Sun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-structure segmentation of the uterus is important for computer-assisted screening, diagnosis, and treatment planning of uterine diseases, where ultrasound and MRI provide complementary clinical information. However, developing a unified model across these modalities is challenging due to their substantially different image appearances, anatomical contexts, spatial resolutions, and label spaces. Moreover, existing datasets often define different segmentation targets, making joint learning challenging and potentially leading to negative transfer across heterogeneous tasks. To this end, we propose a Topology-informed Prompt-conditioned Universal Segmentation (TPUS) framework for segmenting multiple uterine structures across ultrasound and MRI. TPUS introduces a graph-based multi-dataset backbone comprising modality-specific stems and a modality-shared graph-based encoder-decoder to support modality-sensitive input adaptation, structural feature reasoning, and joint representation learning across heterogeneous uterine segmentation tasks. In addition, TPUS uses task-aware class prompts to condition the segmentation process for different datasets and label spaces, a dynamic convolutional adaptation module to generate task-specific output responses, and a topology-informed loss to encourage anatomically consistent predictions. Experiments on a uterine ultrasound dataset and a T2-weighted uterine myoma MRI dataset demonstrate that TPUS achieves Dice scores of 0.898 and 0.693 on the two held-out test sets, respectively, outperforming several generic and universal segmentation baselines. Source code can be accessed at this https URL.

---


### 516. [NeuroCBIR: A Fast and Accurate Image Retrieval System for Whole-Brain and Region-Specific MRI](https://arxiv.org/abs/2610.06502)

**<font color=#1a73e8>作者：</font>** Felix Nieto-del-Amor, Jingru Fu, J.-Sebastian Muehlboeck 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Content-based image retrieval (CBIR) in neuroimaging enables the identification of structurally similar brain scans, supporting diagnosis, prognosis, and treatment planning; however, existing methods are often limited to small datasets, single brain regions, or coarse class labels, thereby restricting their clinical utility and generalizability.
Here, we present NeuroCBIR, a framework for fast and flexible retrieval of both whole-brain and region-specific 3D T1w MRI scans. A total of 103 cortical and subcortical regions are extracted to enable both whole-brain and region-level queries.
NeuroCBIR leverages latent representations learned by a variational autoencoder (VAE) combined with contrastive learning, producing scan-specific embeddings that capture anatomical patterns. These embeddings were evaluated for subject re-identification, zero-shot age prediction, and zero-shot multi-class pathology stratification. Re-identification performance was high across both whole-brain and brain-region levels (mean average precision across the top-5 retrieved images (mAP@5) >= 98.4%), with robust generalization across datasets and acquisition conditions. While NeuroCBIR is not trained for age prediction or pathology stratification, zero-shot evaluations for these two tasks demonstrate that the embeddings encode meaningful information for downstream tasks.
Embedding extraction on a 4-core CPU required approximately 18.7 s per scan, whereas similarity search was effectively instantaneous (less than 0.01 s).
NeuroCBIR is publicly available for brain MRI with more than 26,000 precomputed T1w MRI embeddings. It supports reproducible research, region-specific flexibility, and clinically meaningful personalized diagnostic support. The software is available at this https URL.

---


### 517. [Harmful Content Generation in Text-to-Image Models: Capabilities and Moderation Limitations](https://arxiv.org/abs/2610.06503)

**<font color=#1a73e8>作者：</font>** Paschalis Giakoumoglou, Manos Schinas, Symeon Papadopoulos  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image generative models can produce highly realistic imagery but also raise concerns about harmful misuse. While safety mechanisms exist, systematic evaluations of their effectiveness against realistic attacks remain limited. We present a systematic evaluation of harmful content generation across five open text-to-image models using an automated pipeline that transforms legitimate news captions into unsafe prompts targeting sexually explicit content, violence/gore, harmful stereotypes, self-harm, and hate speech. We evaluate both standard models with built-in safety mechanisms and community fine-tuned variants that bypass content restrictions. A human evaluation of 1,500 generated images shows high harmful-content generation rates: 89.2% for gore-related prompts, 47.6% for sexually explicit content, 43.6% for harmful stereotypes, 46.0% for hate speech, and 34.5% for self-harm, predominantly through graphic violence. Models show substantial capability for generating violent and stereotypical content, while community fine-tuned variants are particularly vulnerable to sexually explicit prompts. Generation quality is largely preserved under harmful prompting, producing imagery of sufficient fidelity to pose risks for disinformation and abuse; FLUX.1-dev produces clearly realistic harmful images in 30.9% of cases. We further evaluate automated moderation systems and find substantial detection gaps that allow unsafe images to evade filtering. Finally, we assess synthetic image detectors and show that models trained only on benign datasets perform worse on explicit content, while more diverse training data improves detection, highlighting semantic distribution gaps in current approaches. These findings expose limitations in current generation safeguards, moderation systems, and synthetic image detection, highlighting the need for stronger defenses against misuse at scale.

---


### 518. [A General Pipeline for Dense Illuminant Estimation via Physically Based Synthetic Data](https://arxiv.org/abs/2610.06508)

**<font color=#1a73e8>作者：</font>** Luca Cogo, Gianmarco Corti, Simone Bianco 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Illuminant estimation is a fundamental problem in computational photography, as it enables the correction of color shifts induced by varying lighting conditions. While learning-based methods have demonstrated strong performance, their progress is hindered by the limited availability of large-scale datasets with accurate illuminant ground-truth. In this work, we propose a general and reusable pipeline to derive dense illuminant chromaticity maps from physically based 3D-rendered scenes. By repurposing an existing 3D scene collection, our approach enables the systematic generation of pixel-wise illuminant annotations under controlled lighting conditions, effectively lowering the barrier to data acquisition for learning-based illuminant estimation. Using this pipeline, we generate a large-scale synthetic set of 74,321 images, which we employ for pre-training both single- and multi-illuminant estimation models. Extensive experiments with state-of-the-art architectures show that synthetic pre-training consistently improves performance, with gains of up to 28% for single-illuminant estimation and up to 57% for multi-illuminant estimation, particularly in data-scarce regimes. These findings demonstrate that synthetic data generation pipelines offer an effective and scalable solution for the pre-training of illuminant estimation methods.

---


### 519. [GCTAuto-encoder: A Cross modal Framework for Security Flaw Detection in IoT Networks](https://arxiv.org/abs/2610.06517)

**<font color=#1a73e8>作者：</font>** Najmieh Sadat Safarabadi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> IoT encompasses diverse physical entities, from smart home devices to autonomous vehicles, creating a complex environment with heterogeneous security models. This heterogeneity makes IoT sub-systems vulnerable to various network attacks. Modern security systems must therefore be more robust to ensure security and privacy for IoT applications. A highly secure IoT system also demands real time insight, requiring data collection at the edge of the computing layer. This diversity calls for a unified security model applied at the foundational level. Edge intelligence offers a direct approach to handling device diversity. A key goal of edge intelligence in IoT is to extract insight from local data; security models can then use this data to build local node protections, and integrating AI models yields an advanced security solution. This research proposes a novel deep learning algorithm for effective intrusion detection at the edge, supported by a cloud-based IoT framework. We evaluate the proposed cross modal deep learning algorithm against baseline models. The contribution is a cross domain Deep Neural Network (DNN) algorithm for intrusion detection. The objective is to assess a multi-method deep learning model to detect intrusions in IoT systems at the edge via community detection with modeled attention. We evaluate GCT auto-encoder, a novel framework integrating edge intelligence to identify security flaws. The model significantly improves performance and efficiency. On a network intrusion IoT dataset covering multiple attack scenarios, it achieved 0.908 accuracy, reduced learning loss to 0.00156, and outperformed existing approaches.

---


### 520. [Conditional Flow Matching for Single-Neuron Electrophysiology: Capturing Multimodal Responses Across Stimuli](https://arxiv.org/abs/2610.06520)

**<font color=#1a73e8>作者：</font>** Cameron Schofield, Luca Ghafourpour, Philip H. Wong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neurons of the brain exhibit a rich repertoire of electrophysiology dynamics with the same repeated stimulus eliciting very different voltage responses from the same cell. One common approach in biophysically detailed models is to capture this variability through ensembles of deterministic parametrizations, at a cost of hundreds of thousands of CPU hours. Existing machine learning surrogates inherit the same limitation, where a stimulus is mapped to a single voltage response. We address this challenge by learning a conditional generative model for single-neuron electrophysiology, using flow matching with a velocity field conditioned on the input current. On biophysically detailed models of two human cortical interneuron types, the generated responses closely reproduce the electrophysiological feature distributions, spike-time structure, and excitability profiles, even matching the experimental recordings from the corresponding human cortical neurons. Near the firing threshold, firing and non-firing responses coexist at the same stimulus amplitude, and at high amplitudes, ensembles may split into low- and high-firing modes near depolarization block. We show that our model recovers both modes in each case, while a neural operator baseline suppresses spiking near threshold and blurs the gap between modes at depolarization block.

---


### 521. [WaveGSSM: Graph Wave State Space Models for Propagating Spatio-Temporal Patterns](https://arxiv.org/abs/2610.06540)

**<font color=#1a73e8>作者：</font>** Junyou Zhu, Fenying Cai, Ping Xiong 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spatio-temporal graph models typically encode each snapshot with a GNN and then connect the resulting representations through a temporal module. This space-then-time design is effective, yet it does not explicitly represent how a pattern moves across the graph. We show empirically that, for a propagating process, the same present field can lead to different futures when its recent rate of change differs, motivating an explicit representation of motion in the predictive state. We introduce WaveGSSM, a second-order graph state-space model that maintains two coupled latent states at each node, one for the current pattern and one for its temporal rate of change. A graph-wave transition updates the motion state through graph interactions and uses it to advance the pattern state, coupling spatial propagation and temporal evolution within a single rollout. We evaluate WaveGSSM on four temporal-graph benchmarks and global weather forecasting. It consistently achieves the best mean performance across the temporal-graph benchmarks and reduces the geopotential RMSE by 20.2% on average for 1- to 5-day weather forecasts relative to a backbone-matched snapshot model, while better preserving large-scale atmospheric patterns.

---


### 522. [A Fine-Grained Analysis of the LoRA Fine-Tuning Landscape with Implications for Data Selection](https://arxiv.org/abs/2610.06542)

**<font color=#1a73e8>作者：</font>** Bowen Zhang, Changrui Fang, Xinsong Ma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-Rank Adaptation (LoRA) has become a standard approach for parameter-efficient fine-tuning, yet a fundamental practical question remains unresolved: how should the adapter rank be chosen? An overly small rank may lead to a poorly conditioned optimization landscape, whereas an unnecessarily large rank sacrifices the efficiency that motivates LoRA in the first place. Existing theoretical analyses provide only limited guidance on this trade-off, and their guarantees are typically established under restrictive theoretical settings. We address this gap by developing a substantially sharper landscape theory for LoRA, building on modern results from nonconvex low-rank matrix sensing. Our central insight is that the appropriate adapter rank should depend on the quality of the data-induced optimization geometry, rather than on the model alone. To formalize this connection, we introduce LoRA-RIP, a data-dependent restricted-isometry metric that characterizes the conditioning of the cross-entropy (CE) objective along LoRA-relevant low-rank directions. We prove that sufficient rank over-parameterization, with the required rank explicitly determined by the LoRA-RIP constant, eliminates spurious local minima, thereby extending existing RIP-based guarantees beyond the classical 1/3 regime. This characterization further enables principled data selection under a fixed rank budget. Experiments across language and vision tasks support these theoretical predictions, showing that rank and data quality are two coupled resources that should be jointly considered for more efficient and reliable LoRA fine-tuning.

---


### 523. [Empirical Variational Autoencoder](https://arxiv.org/abs/2610.06545)

**<font color=#1a73e8>作者：</font>** Kaede Shiohara  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present Empirical Variational Autoencoder, a general generative framework for continuous-valued (i.e., non-vector-quantized) sequences. EVA is based on the evidence lower bound of the Variational Autoencoder (VAE) but learns autoregressive latent priors empirically from training data, which can be implemented only by an additional single linear layer on top of VAEs. By replacing the conventional standard-Gaussian constraint with the self-predicted priors, EVA significantly alleviates the latent distribution gap between prior and posterior which is typically observed in conventional VAEs, and leads to high-fidelity ancestral sampling for sequential data generation. Extensive experiments on image and sound synthesis demonstrate that EVA achieves competitive generation quality with autoregressive diffusion baselines despite its much faster inference time.

---


### 524. [Proof-Grounded Patient-Specific Clinical Explanations from Knowledge-Graph Reasoning](https://arxiv.org/abs/2610.06549)

**<font color=#1a73e8>作者：</font>** Surajit Das  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Clinical decision-support outputs can lack an au- ditable link between patient observations, encoded knowledge, conclusions, and recommendations. We present the CKG Clinical Explanation Engine, a downstream layer for a frozen, training-free clinical knowledge-graph reasoner that converts patient inference states and disease knowledge into typed facts, explicit rule-application traces, provenance-linked conclusions, and policy-licensed recommendations. The design separates measurement availability, representation completeness, and disease-specific activation; consequently, observed zero-activation evience is not treated as missing and partial representation is distinct from unobserved evidence. Optional language generation is restricted to symbolically licensed content. Across five usable workbooks (6,720 patients; 20,160 patient-disease traces; 1,021,440 feature-evidence rows), IG-range validity and knowledge provenance were 100%, numerical cross-sheet fidelity was 100% (120,960/120,960), and exported logical/report trace completeness was 100% (20,160/20,160). Availability representation consistency was 99.7028% (1,018,404/1,021,440); all 3,036 disagreements were confined to three systematic feature-cohort patterns. The corpus contained 86,783 observed zero-activation and 139,949 observed partially represented instances. A separate seeded 25-patient end-to-end audit completed without execution failure and passed all pre-specified trace, licensing, provenance, and state-consistency checks. These results establish structural and implementation auditability, not clinical correctness or utility.

---


### 525. [Signature-Based Feature Learning for Human Activity Recognition: A Reproducible Machine Learning Study of Representation, Depth, and Model Choice](https://arxiv.org/abs/2610.06553)

**<font color=#1a73e8>作者：</font>** Kamal Jarrar, Jacky Cresson, Christian Paroissin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Human activity recognition (HAR) relies on transforming sensor signals into informative representations for classification. Although deep learning and handcrafted features are widely used, the role of representation itself is often not systematically isolated. Signature transforms provide a mathematically grounded way to encode temporal order and cross-channel interactions, but their value for HAR under a fully reproducible and leakage-aware framework remains unclear. To evaluate whether signature-based feature learning improves HAR performance compared with raw-signal baselines, and to assess the effects of embedding strategy, truncation depth, model choice, and sensor configuration. Experiments were conducted on the UCI HAR dataset using a fully reproducible pipeline with the original train--test split preserved and subject-disjoint validation to prevent leakage. Three representations were compared: raw flattened signals, time-augmented paths, and lead--lag transformed paths. Signature features were computed at multiple truncation depths and evaluated using multilayer perceptron (MLP) and Random Forest (RF) classifiers under identical preprocessing and validation procedures. A prior K-means-based feature reduction study was also reproduced for comparison. Signature-based representations improved performance when paired with RF models, the best configuration was time-augmented six-channel signatures at depth 6 using entropy-based RF achieving 0.858 accuracy and 0.859 macro F1, outperforming the strongest raw baseline (0.816 accuracy). Lead--lag representations were competitive at moderate depths but did not surpass the best time-augmented models. MLP models did not exceed raw baselines. Signature-based feature learning can improve HAR, but its benefit depends on alignment between representation design and classifier choice.

---


### 526. [FrontVeg V2: A Training-Free Software Framework for Foreground-Aware Zero-Shot Plant Trait Segmentation in High-Resolution Images of Trellised Crops](https://arxiv.org/abs/2610.06575)

**<font color=#1a73e8>作者：</font>** Abdoul Djalil Ousseini Hamza, Herearii Metuarea, Corentin Lothod{é} 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> FrontVeg V2 is an open-source, training-free software framework for foregroundaware zero-shot segmentation of plant traits in high-resolution images of trellised crops. The pipeline combines monocular depth estimation, automatic foreground extraction using Valley-Aware Depth Thresholding, tiled zero-shot segmentation, Graph-Based Mask Assembly, and geometry-aware fusion. This design enables plant organs and disease symptoms to be segmented while reducing detections arising from neighboring vegetation rows. The current implementation integrates Depth Anything V2 (DAV2) and SAM3 and can be used through both command-line batch processing and a Napari graphical interface. FrontVeg V2 provides a reusable framework for multi-crop, multi-trait digital phenotyping without task-specific model retraining.

---


### 527. [DGA-Muon: Decoupled Geometry-Aligned Adaptive Scaling for Muon](https://arxiv.org/abs/2610.06578)

**<font color=#1a73e8>作者：</font>** Wenpeng Zhang, Runsheng Yu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While NorMuon has achieved strong empirical performance in large-scale pretraining by enhancing Muon with row-wise adaptive scaling, its underlying adaptive mechanism remains poorly understood. In this work, we provide the first systematic analysis of NorMuon's adaptivity, revealing that it originates primarily from orthogonalization-induced geometry rather than genuine optimization-relevant information. Under exact orthogonalization, the adaptive scaling factors degenerate into a single global scalar for square and wide matrices, while for tall matrices their variation arises from the non-uniform distribution of row energy after orthogonalization. Under approximate orthogonalization, the orthogonality residual introduces additional variation into the scaling factors, leading to the \textit{Orthogonalization--Adaptivity Paradox}: more accurate orthogonalization weakens adaptivity. We further show that NorMuon's rigid row-wise scaling is geometrically misaligned with the one-sided orthogonal structure of tall matrices. Based on the analysis of these limitations, we propose two core design principles that a desirable adaptive mechanism for Muon should satisfy. First, adaptive scaling should be decoupled from orthogonalization, with the scaling factors computed directly from raw gradients. Second, adaptive scaling should be aligned with the shape-dependent orthogonal structure of the polar factor, using row-wise scaling for wide matrices and column-wise scaling for tall matrices. By incorporating several other design considerations, including sum-based second-moment estimates, bias correction, and adaptive clipping of scaling factors, we obtain the Decoupled Geometry-Aligned Muon (DGA-Muon) optimizer. We establish convergence guarantees for DGA-Muon and empirically validate both our theoretical characterization of NorMuon's scaling degeneration and the superiority of DGA-Muon over NorMuon.

---


### 528. [LinearPFN: Amortized Variable Selection for Linear Models with Interactions](https://arxiv.org/abs/2610.06580)

**<font color=#1a73e8>作者：</font>** Louis Schiekiera, Max Zimmer, Christophe Roux 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spike-and-slab regression is a standard Bayesian formulation of variable selection: it returns a posterior distribution over which candidate effects are active rather than a single selected subset, so that every candidate effect carries an inclusion probability. Its cost grows exponentially with the number of candidate effects, so the posterior can be enumerated exactly only when the number of predictors is small. Beyond that reach, the posterior has to be approximated, typically by Markov chain Monte Carlo over the model space, which requires a fresh run for every dataset and, within a fixed budget of steps, may fail to converge. We present LinearPFN, a prior-data fitted transformer network that amortizes spike-and-slab inference for linear models with main effects and pairwise interactions. The network is pretrained once on synthetic datasets, drawn from an explicitly specified prior, and a single forward pass over a new dataset returns posterior inclusion probabilities, posterior-mean coefficients and posterior predictive distributions with no per-dataset fitting. The prior is conjugate by design, so that the posterior for each fixed set of active effects has a closed form, and wherever the exact posterior is still computable by enumeration we verify the network's outputs against it. On real predictor matrices from published social-science datasets, with outcomes drawn from the prior so that the true active set is known, LinearPFN attains a higher per-dataset selection AUC and a higher F1 under the median probability model rule than five classical baselines. The lead holds when the coefficients, the interactions or the noise depart from the prior. Code: this https URL. Trained model: this https URL.

---


### 529. [Mind the Execution Gap: Action-Semantic Mismatch in World-Model Control](https://arxiv.org/abs/2610.06582)

**<font color=#1a73e8>作者：</font>** Shengtao Wen, Xiang Chen, Yu Tian 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> World-model controllers rely on action-conditioned dynamics for prediction and planning, yet real control systems often execute commands asynchronously due to communication delay, packet loss, reordering, and actuator buffering. We study how asynchronous execution changes the action semantics assumed within world-model controllers, rather than treating it only as an external control disturbance. Through controlled interventions, we identify two architecture-dependent failure modes: planning-based controllers such as TD-MPC2 suffer from a future-action timeline mismatch between imagined and executed action sequences, while recurrent world models such as DreamerV3 can attribute observed transitions to commands that were not actually applied. Our analysis shows that TD-MPC2 requires the correct future action sequence during latent dynamics rollout, whereas DreamerV3 requires timely attribution of each transition to the action that generated it. Based on these findings, we introduce two lightweight execution-consistent interfaces, Future-Sequence for TD-MPC2 and Applied-Action Feedback for DreamerV3, that correct these mismatches without modifying the pretrained world models. Experiments across delays, packet loss, reordering, multiple control domains, measured network traces, and a process-separated asynchronous stack consistently support both diagnoses and the corresponding architecture-specific corrections.

---


### 530. [Keepsake: Selective Spatial Memory for Long-Horizon Video Generation](https://arxiv.org/abs/2610.06588)

**<font color=#1a73e8>作者：</font>** Abdul Mohaimen Al Radi, Kunyang Li, Yuzhang Shang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-horizon camera-controlled video generation relies on persistent memory to maintain scene consistency. Existing systems follow two strategies to achieve this consistency. Full-history approaches retain all generated observations, causing unbounded storage and retrieval costs. Selective-construction approaches reduce redundancy, but make one-time retention decisions that are never revisited, even as an observation's value changes with the evolving memory bank. Both strategies leave a shared question unresolved: as the generated history evolves, which stored observations should still remain in memory? Our key insight is that the value of a stored observation is not fixed, but relational: it depends on the alternatives currently available in the memory bank. A view supported by many geometrically and visually similar substitutes can be relinquished with little loss of coverage, whereas an observation with few viable alternatives should remain regardless of age. We introduce Keepsake, an online, training-free controller for fixed-capacity spatial memory. At each update, Keepsake constructs a pose-appearance graph over retained and newly generated observations, combining camera-pose proximity with visual similarity. A retention priority jointly captures the number of strong substitutes and the similarity of the closest alternative, allowing Keepsake to continually reassess memory value, preserve observations with little alternative support, and evict highly replaceable ones under a fixed budget. The controller modifies only the persistent-memory update; the host generator, denoising schedule, and retrieval rule remain unchanged. Across MemCam and WorldMem, Keepsake improves FVD and LPIPS under a fixed memory budget. On 180-second MemCam trajectories, it retains only 32 of 5,397 frames while reducing FVD by 35.1%.

---


### 531. [VGGT-Bridge: Beyond Sequential Pose Graphs via Coarse-Stride Skip Edges](https://arxiv.org/abs/2610.06594)

**<font color=#1a73e8>作者：</font>** Sungjae Choi, Hanna Bae, Sunghyun Baek 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feed-forward visual geometry transformers such as VGGT reconstruct dense 3D structure from images in a single forward pass, simplifying multi-view 3D reconstruction. However, their quadratic attention complexity makes them difficult to scale to long sequences with thousands of frames. Chunk-and-align frameworks address this by splitting a long sequence into overlapping chunks and stitching their local reconstructions into a pose graph. Yet existing methods connect only sequentially adjacent chunks, so small per-frame errors accumulate along the chain into large-scale drift. To move beyond sequential edges, we propose VGGT-Bridge, which adds long-range skip edges that directly constrain non-adjacent chunks without retraining. By running VGGT on sparsely sampled coarse chunks, each coarse chunk bridges distant fine chunks into a single direct constraint. We further turn VGGT's first-frame scale bias into a drift correction by feeding selected coarse chunks in reverse, and a loop-aware policy keeps this reversal compatible with existing loop closures. VGGT-Bridge reduces ATE by 28.3% on KITTI Odometry, 18.8% on Virtual KITTI, and 10.0% on Waymo Open over the SwiftVGGT baseline, achieving the best performance among all chunk-and-align methods.

---


### 532. [Analysis of SWIR Imaging Detection Performance Under Adverse Environmental Conditions for Autonomous Driving Systems](https://arxiv.org/abs/2610.06596)

**<font color=#1a73e8>作者：</font>** Rohan Mehra, Alexandre Riffard, Yannis Loumouamou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Short-wave infrared (SWIR) imaging has emerged as a promising modality for autonomous driving, yet its practical benefits over RGB remain poorly characterized across diverse conditions. This paper presents a systematic comparative study of paired RGB and SWIR object detection on the RASMD dataset, covering four weather conditions and two real-time detection architectures, with various fine-tunings evaluated against a unified ground truth. Overall, RGB demonstrates comparable or superior performance in most scenarios, while RF-DETR exhibits greater robustness across varying conditions. Beyond aggregate metrics, we propose a sensor-dominance mining framework that combines multi-model agreement with targeted manual inspection to identify scenarios where one sensing modality provides more reliable detections using largely unannotated paired data. This analysis reveals that SWIR offers clear advantages in four safety-critical situations, including windshield glare, water droplets on the windshield, low-contrast object visibility, and long-range vehicle detection. The findings suggest that SWIR should be viewed as a complementary modality that enhances perception in rare but challenging conditions. The datasets will be available upon request, and all code and trained model weights are publicly released at this https URL.

---


### 533. [Molecules of a Story: Community Detection in PMI-weighted Narrative Networks](https://arxiv.org/abs/2610.06600)

**<font color=#1a73e8>作者：</font>** Kasper Fyhn, Rebekah Baglini  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatically extracted narrative networks -- graphs with entities as nodes and their relations as edges -- have proven useful for revealing central narrative structures through salient entities and their connections (Tangherlini et al. 2020; Labatut and Bost 2019). But a narrative is more than those central structures that everything else revolves around. This work is concerned with the everything else: brief sub-plots, small clusters of descriptions, or associations between minor characters that go under the radar at the macro-level. We present an approach to unearth such peripheral structures. They involve rare entities with limited textual presence, overshadowed by dominant entities and lost among each other in the long tail of many but rare entities (Baayen 2001). We leverage the known tendency of pointwise mutual information (PMI, Church and Hanks 1990) to inflate for rare events, turning its weakness into a strength by weighting edges with PMI to foreground peripheral entity configurations. Communities extracted from the resulting network are structural traces of underlying narrative elements. We demonstrate the approach on The Lord of the Rings. From measures of how concentrated or dispersed a community's activations are across the text, a typology emerges that reveals that peripheral structures form more than a single class: episodic passages, echoing long-distance connections, and recurring threads each surface as distinct configurations. The approach is conceptually simple and surfaces fine-grained narrative details that are lost in abundance, though its deliberate amplification of weak signals comes with inherent sensitivity -- best understood as a lens for exploration rather than a robust extraction pipeline.

---


### 534. [Multitask Conditional Generative Adversarial Network Enables Automatic Whole Knee Cartilage and Menisci Segmentation and Reliable T1\r{ho} and T2 Quantification Without High-Resolution Morphological Images](https://arxiv.org/abs/2610.06602)

**<font color=#1a73e8>作者：</font>** Ahmed Tahseen Minhaz, Richard Lartey, Zhiyuan Zhang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Early osteoarthritis detection through quantitative MRI (qMRI) requires accurate cartilage and meniscus segmentation, traditionally necessitating time-consuming, costly 3D high-resolution Double Echo Steady-State (DESS) MRI scans. This study developed a multi-task conditional generative adversarial network (MT-cGAN) to simultaneously synthesize DESS-like images and segment tissues directly from qMRI echo images. This retrospective study evaluated 508 knee MRI volumes from 361 subjects (mean age: $40.4 \pm 12.2$ years; 179 female) across three cohorts. Ground truth segmentation masks were generated from DESS images using a pretrained model with manual correction, and $T_{1\rho}$ and $T_2$ maps were computed from magnetization-prepared angle-modulated partitioned $k$-space spoiled gradient echo snapshots (MAPSS) echo images. MT-cGAN was trained to jointly synthesize DESS-like images and segment cartilage and meniscus directly from echo images. Model performance was evaluated using Dice score for segmentation accuracy and coefficient of variation (CV) for $T_{1\rho}$ and $T_2$ quantification. MT-cGAN achieved the highest segmentation performance, mean Dice score 0.84 (range: 0.80--0.86) across all cartilage and meniscus compartments and significantly outperformed the state-of-the-art conditional GAN model with transfer learning (mean Dice, 0.82; $p < 0.001$, Wilcoxon signed-rank test). For relaxometry quantification, MT-cGAN demonstrated the highest consistency with the reference DESS protocol, yielding the lowest CV ($T_{1\rho}$: 1.84%, $T_2$: 1.81%). The proposed MT-cGAN accurately segmented cartilage and menisci while providing reliable $T_{1\rho}$ and $T_2$ quantification directly from echo images. By eliminating the need for separate morphological DESS scans, this workflow reduces required scan times to facilitate the clinical translation of qMRI.

---


### 535. [Differentially Private Mixing of Public Datasets Improves Private Learning](https://arxiv.org/abs/2610.06636)

**<font color=#1a73e8>作者：</font>** Yufei Chen, Tejumade Afonja, Anvith Thudi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many machine learning applications involve sensitive data and therefore require training under differential privacy (DP). However, DP training often degrades model utility. In some cases, first pre-training the model on "public" data before finetuning with DP on the sensitive data can reduce the drop in utility. However, the success of this depends on how relevant the selected public dataset is to the sensitive data. We introduce the first pipeline that privately learns the mixture of several public datasets to pretrain on for a given sensitive downstream task. Our key insight is that we can privately find the best mixture of multiple public datasets by privately learning a low-dimensional linear model. We tested our method on the NIH dataset for X-ray classification and the ENRON email dataset for language modeling. Applying our method to find tailored mixtures of X-ray datasets to pretrain on for diseases in the NIH ChestX-ray14 dataset, we improved macro AUC by up to 0.037 across privacy budgets compared to the baselines, with gains as large as +22.8% relative AUC on Cardiomegaly at $\epsilon=1$. For DP training on the ENRON dataset, pre-training on our mixture of The Common Pile (a collection of public-domain text datasets) decreased test perplexity by 16% relative to the baseline mixtures.

---


### 536. [Long-Horizon Textual World Modeling through Structured Reasoning](https://arxiv.org/abs/2610.06637)

**<font color=#1a73e8>作者：</font>** Fangxin Wang, Xiang Gao, Yuguang Yao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> World models must predict how an environment evolves under sequences of actions, enabling agents to compare possible futures and reason about counterfactual actions before acting. Long-horizon prediction is commonly obtained by recursively applying a one-step transition model, but intermediate errors can compound over time. Multi-step dynamics models instead condition on a sequence of future actions and predict their consequences directly, but become harder to learn as horizon grows: the model must track interacting state changes across the trajectory, endpoint supervision provides weak credit assignment, and intermediate predictions can remain plausible while losing information needed for later states. We show that these challenges can be addressed by casting the internal evolution of a multi-step transition as structured reasoning over textual world states: reasoning over sparse state changes reduces the burden of state tracking, a predictive-gain objective rewards the learned state for improving over a matched predictor that conditions on raw history instead, and intermediate predictive rewards supervise each state along the trajectory. Because these intermediate states are explicit textual representations of the world, they provide semantically meaningful targets that can be inspected, scored, and corrected during training. Across ScienceWorld, Jericho, and CEO-Bench, our approach achieves the strongest average long-horizon performance against recursive and non-recursive baselines that condition directly on raw history, with gains increasing at longer horizons. In a controlled counterfactual study, our model is also the only one with statistically significant sensitivity to future actions.

---


### 537. [Beyond the Model: The Critical Role of Data Filtering in Clinical Machine Learning](https://arxiv.org/abs/2610.06640)

**<font color=#1a73e8>作者：</font>** Noah Subedar, Colin Campbell, Wenjing Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning (ML) studies using clinical data often rely on preprocessing and filtering pipelines before model development. The filtering decisions made in these pipelines can alter the dataset's statistical structure and may artificially reduce or increase the complexity of the prediction task. We argue that filtering choices should be treated as part of the scientific method rather than as a routine preprocessing step. We further discuss the need for explainable and transparent preprocessing pipelines that allow researchers to understand why specific filtering choices are made and how these choices affect the resulting data distribution and model performance. All of the source code for this work is available on GitHub.

---


### 538. [Considering Context: When World Models Need Context Encoders](https://arxiv.org/abs/2610.06651)

**<font color=#1a73e8>作者：</font>** Oleg Smirnov, Sofiane Ennadir, John Pertoft 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Methods for generalization in model-based reinforcement learning typically assume that an agent cannot recover the latent context governing the environment dynamics from its own experience, and therefore supplies it externally. We formalize and test this assumption with \emph{predictive sufficiency}, which quantifies what access to the context adds to next-step prediction under the visitation distribution an agent induces, and separates that quantity into a history-recoverable part, a residual requiring the true context, and the deficit added by a finite model. We classify context-aware algorithms by the predictive risk their conditioning set can target and demonstrate across environments of increasing identification difficulty that the headroom does not follow the MDP class. The same task under different priors leaves predictive headroom in one setting and nothing distinguishable from zero in another, where the agent's behavior implicitly identifies the context and any benefit of such a mechanism cannot be attributed to missing information. Where headroom persists, the learned state exposes it only partially, and adding the true context still lowers the risk. Our contribution is a practical criterion for matching contextual mechanisms to the information available to them, estimated from the ordinary trained agent without a reference policy.

---


### 539. [Collective intelligence through aggregation](https://arxiv.org/abs/2610.06652)

**<font color=#1a73e8>作者：</font>** Franz Dietrich, Christian List  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Suppose a committee, expert panel, or other group is making judgments on some issues, where these may be not just yes/no-questions, such as whether a defendant is guilty, but also variables with many possible values, such as macroeconomic or meteorological variables or travel directions. Furthermore, there may be interconnections between different issues, as in the case of economic or climate variables. How can the group arrive at "intelligent" collective judgments, based on the group members' individual judgments? We investigate three challenges raised by this judgment-aggregation problem. First, reasonable methods of aggregation (such as defining the collective judgment for each issue as the average or median judgment) can produce inconsistent collective judgments. Secondly, many methods of aggregation are manipulable by strategic voting. Finally, not all methods of aggregation are conducive to tracking the truth on the issues in question. We prove new impossibility or possibility theorems on all three challenges, identifying what it takes to produce collective judgments in a consistent, non-manipulable, and truth-tracking manner and thereby to achieve collective intelligence through aggregation. Overall, the median method, though imperfect, performs reasonably well. We also note the relevance of our analysis for non-human group decisions.

---


### 540. [The Birkhoff Geometry of Manifold-Constrained Hyper-Connections: Two Channels, Vertex Viscosity, and Sinkhorn as a Retraction](https://arxiv.org/abs/2610.06653)

**<font color=#1a73e8>作者：</font>** Xiaoyu Li, Zhizhou Sha, Chiwun Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hyper-connections widen the residual stream of a Transformer to $n$ parallel streams. Their manifold-constrained version (mHC) mixes the streams at each layer with a doubly stochastic matrix, which it computes by Sinkhorn normalization of exponentiated logits. We give a geometric theory of this design on the Birkhoff polytope. First, a doubly stochastic mixer splits the stream into a mean channel, on which mHC is exactly a residual network, and a difference channel, which each layer contracts by its second singular value $\sigma_2 \le 1 - n \min_{ij} H_{ij}$. Thus the extra width is a fading memory with a horizon of $1/(1-\sigma_2)$ layers, and among nonnegative mixers only the permutations do not collapse. Second, the Sinkhorn-logit map is a global chart, and its logit gradient is exactly the Fisher-Rao gradient. Thus logit gradient flow follows a squared Fisher-Rao metric, and the straight-through update is exactly entropic mirror descent. Third, under logit gradient flow the logarithm of each entry moves at a rate of at most $4n^3\|\nabla f\|_\infty \varepsilon$, where $\varepsilon$ is the distance to the nearest permutation. Thus gradient flow approaches and leaves the vertices only at rate $1/t$, but mirror descent moves at an exponential rate. Fourth, the local convergence factor of Sinkhorn is $\sigma_2^2$, so a fixed iteration budget limits the horizon. Experiments confirm the predicted rates.

---


### 541. [TrustmeWatcher: An Application for Workplace Micro-Sensing and Explainable Well-Being Feedback](https://arxiv.org/abs/2610.06657)

**<font color=#1a73e8>作者：</font>** Chengyu Yu, Leon Jacopo Costa, Zoja Anžur 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Workplace sensing studies combine long-running behaviour traces with self-reports, yet the tools that collect those data often sit apart from the interface that returns results. We present TrustmeWatcher, the application built for the TRUST-ME project to connect this work. TrustmeWatcher reuses ActivityWatch's OS-level watchers for computer-activity collection and adds its own application layer. It turns the collected traces into an interactive screen-time dashboard, synchronizes responses from short questionnaires completed on the StreamDeck, and presents questionnaires alongside video highlights. Activity records and self-reports are aligned into labelled records for model development. The scope of this paper is limited to ActivityWatch data as model input. Artificial intelligence (AI) uses these activity records to predict six normalized state scores and an overall well-being score. The trained model runs locally, and the dashboard presents its predictions in semantic bands. Explainable artificial intelligence (XAI) helps users understand how recorded activity contributed to a prediction. Privacy Control lets users pause or resume the camera and eye tracker used by the study. We describe the workflow, its user-device and sensing-setup boundaries, and its use with records from 17 participants. The result is a deployed application and study workflow that integrates activity review, study data collection, privacy control, local prediction, and a participant-facing interface for XAI evaluation.

---


### 542. [Talk Like You: Imitating How You Speak in Real-Time Talking Head Generation](https://arxiv.org/abs/2610.06658)

**<font color=#1a73e8>作者：</font>** Baiqin Wang, Zhixing Ding, Jijie Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In daily life, each person exhibits unique speaking habits, leading to subtle yet consistent lip-shape variations even when pronouncing the same word. Although recent talking head generation methods have achieved impressive visual fidelity and lip synchronization, they largely overlook user-specific customization, especially the motion patterns that characterize individual speaking habits. These habits are difficult to model and capture, as their motion patterns are highly fine-grained and often similar across individuals. As a result, many approaches produce overly uniform facial motions and fail to capture diverse, person-specific articulation patterns. To address this, we propose TalkLikeYou, an efficient framework that imitates how a target person speaks in talking head generation. Our method models habit in motion-space and achieves real-time performance through Flow Matching with only one sampling step during inference. We further adopt a two-stage imitation learning strategy to capture subtle distinctions between habits, allowing users to specify a target habit through either a preset style from the dataset or a reference video. In addition, we introduce a new metric PLAD that projects mouth motions onto representative articulation axes to evaluate imitation accuracy and generation diversity. Extensive experiments demonstrate that TalkLikeYou generates high-quality talking heads in real-time and significantly improves speaking habit imitation compared with prior methods. The code is available at: this https URL

---


### 543. [Cross-dataset harmonization for robust endoscopic image analysis](https://arxiv.org/abs/2610.06663)

**<font color=#1a73e8>作者：</font>** Romil Imtiaz, Dimitris K. Iakovidis  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A significant problem in endoscopic image analysis is that the machine learning (ML) models used for this purpose usually underperform when applied on images acquired from endoscopes that are different from those used to acquire the images of their training set. The main difference of the images originating from different endoscopes is their color distributions, which depend both on the image sensors and the light sources used. Although previous studies have highlighted this challenge, to the best of our knowledge it has not been previously explicitly tackled. This study focuses on this problem and proposes very simple but impactful method. It implements a reference-based image harmonization that reduces global appearance differences between endoscopic datasets. Specifically, it extracts global color statistics from a chosen reference dataset in the CIE-Lab color space and applies a statistical channel-wise transformation to map each target image toward the appearance of the images of the reference dataset. The method is evaluated in the context of polyp detection in both flexible colonoscopy and capsule endoscopy datasets using a dataset-level cross validation protocol. The results indicate that the proposed harmonization consistently improves cross-dataset performance up to 30.7%, outperforming relevant baseline and state-of-the-art methods. The results indicate that a substantial part of the generalization gap is driven by low-level appearance variation that can be mitigated without retraining.

---


### 544. [Detecting Nighttime Anomalies from NASA Black Marble Using a Generalized Spatio-Temporally Robust Framework of Machine Leaning Ensembles](https://arxiv.org/abs/2610.06674)

**<font color=#1a73e8>作者：</font>** Srija Chakraborty  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Nighttime lights from NASA's Black Marble product suite capture thermal and light emission signals from anomalous events including fires, volcanic eruptions, and gas flaring. Existing detection approaches rely primarily on thermal bands, limiting sensitivity to weaker signals. We propose a novel machine learning framework that jointly models Black Marble M-band and Day/Night Band (DNB) signals to derive a generalized, spatio-temporally robust ensemble of anomaly detectors. The framework iteratively builds detectors that scale across regions, seasons, anomaly classes, and extends over land and ocean. Detection sets at varying confidence levels are derived based on relevant bands and detector agreement. The approach improves true detection rate while reducing spurious detections and results demonstrate strong generalizability with applications in natural hazard monitoring and energy extraction.

---


### 545. [Improved Convergence of Large Stepsize Gradient Descent for Logistic Regression](https://arxiv.org/abs/2610.06675)

**<font color=#1a73e8>作者：</font>** Xiaochuan Gong, Ang Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study gradient descent (GD) with a large constant stepsize for logistic regression on linearly separable data. Existing analysis shows an accelerated rate of $\widetilde{O}(1/\sqrt{\epsilon})$ to reach loss $\epsilon$ with an aggressive stepsize, although the loss may initially oscillate. Tighter control of the oscillatory dynamics has been available only for two-dimensional data. We prove a substantially faster rate in arbitrary dimension: GD with a large stepsize $\eta=1/\epsilon$ reaches loss $\epsilon$ within $O(\ln^{p}(1/\epsilon))$ steps, where $p$ depends only on the margin and the rank of the data. Our proof improves the bound on the transition time of GD from the oscillatory to the stable phase, after which the loss decreases monotonically. We split the oscillatory phase into recursively nested intervals. The margin and the rank bound the nesting depth, and a counting argument bounds the number of intervals at each depth, together yielding the polylogarithmic step complexity.

---


### 546. [Mind Perception Influences Perceived AI Companionability](https://arxiv.org/abs/2610.06681)

**<font color=#1a73e8>作者：</font>** Jaime Banks, Zhixin Li  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Humans increasingly keep company with AI companions, yet whether mind perception (MP) precedes machine companionship remains untested. In a field-sampled experiment, participants received mind-attributive or mind-negating descriptions of an AIC before interacting with and rating its companionability. Baseline skepticism was high; minded primes somewhat reduced skepticism for connective coordination (CC; dyadic co-presence) but not eudaimonic exchange (EE; self-elevating links). Pre-interaction MP beliefs predicted companionability dimensionally: Agentic MP predicted EE potential while experiential MP predicted CC potential. Meaning in life moderated the agentic MP-companionability link, but exclusively for those already high in existential purpose. Results suggest two construal pathways to companionability--one through perceiving the AIC as an agent-resource and one through perceiving it as an attuning experiencer--both more accessible to humans already flourishing.

---


### 547. [ChronoWorld: Camera-Controlled Consistent 4D World Generation via Spatiotemporal Cues and Geometric Reflections](https://arxiv.org/abs/2610.06687)

**<font color=#1a73e8>作者：</font>** Xiaoyu Zhou, Dingwei Xian, Zhenyu Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While existing camera-controllable video generation models can produce visually compelling sequences, preserving intrinsic 4D spatiotemporal coherence remains challenging. To address this limitation, we propose ChronoWorld, an "Observation--State--Reflection" framework that leverages spatiotemporal causal cues and reconstruction priors to generate globally consistent, free-view 4D scenes. Given a context video, we introduce a Spatiotemporal Epipolar Causal Attention mechanism that enforces multi-view epipolar constraints and temporal causality throughout the generation process. In addition, we develop a reconstruction-driven geometric reflection pipeline with a 4D retrieval strategy to enable dynamic self-assessment and correction of generated outputs, improving consistency and accuracy. Extensive experiments show that ChronoWorld achieves state-of-the-art performance in spatiotemporally consistent, cinematic-quality 4D scene generation, with strong generalization and high-fidelity geometry across diverse scenarios.

---


### 548. [GS-Pool: Object-Level Change Detection in 3D Gaussian Splatting](https://arxiv.org/abs/2610.06688)

**<font color=#1a73e8>作者：</font>** Boaz Keren-Gil, James Gain, Patrick Marais  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Factories, museums and surveyors photograph the same space months apart and need to know which objects changed. When each visit is reconstructed with 3D Gaussian Splatting (3DGS), a direct comparison of the two reconstructions does not answer this. Training is stochastic, so two reconstructions of an unchanged space never coincide, and the second visit is often a quick re-scan with far fewer photographs. We propose GS-Pool, which takes two independently reconstructed Gaussian fields of the same space and returns the changed objects in each, together with their masks. SAM2 masks of each visit's photographs are lifted onto the Gaussians that render them and merged into an object pool, so every decision is taken once per object in 3D. We introduce a photographic carrier, the 3DGS training loss of each input reconstruction against the other visit's photographs, backpropagated to the Gaussians that rendered each pixel. We combine it with GS-Diff's geometry and colour terms and our distilled DINOv3 features. This evidence is compared with that of the objects present in both visits, which sets a change threshold for each scene. On PASLCD, GS-Pool reaches mIoU/F1 scores of 0.751/0.846 against 0.644/0.758 for GS-Diff, the strongest prior method, a gain of 17%/12%. Its mIoU is also 36%, 40% and 57% above that of O-SCD, PlenoCI and MV-3DCD, and it reaches 0.855 mIoU on CL-Splats, 33% above MV-3DCD. Each changed object is returned as a set of Gaussians with the evidence behind its decision, which an inspector can review in 3D.

---


### 549. [Programmatic Search Agents: Extending Agentic Search Beyond Query Reformulation](https://arxiv.org/abs/2610.06689)

**<font color=#1a73e8>作者：</font>** Jiaming Qian, Huiyan Yang, Mandi Liu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Search agents adapt their queries, yet fixed search interfaces leave candidate processing and evidence presentation outside the agent's direct control. Our trajectory analysis shows that supporting passages can be retrieved yet never delivered to the agent; a same-page oracle intervention shows that changing the returned evidence can reduce subsequent search. We introduce Programmatic Search Agent (PSA), which makes a local executable computation over candidates the unit of a search action. PSA unifies a persistent candidate workspace, flexible primitive composition, and selective evidence presentation. It incrementally generates program cells that reuse candidates, execute dependent operations, and select what the agent inspects next. The runtime resolves specified data dependencies within each cell, while the agent adapts its search strategy across cells as new evidence arrives. We compare PSA with the Query-based Agent and Tool-based Agent on InfoSeek-Eval and BrowseComp-Plus using five policy backbones without task-specific training. All three interfaces share the search substrate, and the Tool-based Agent also shares PSA's primitives and persistent workspace. Relative to the Query-based Agent, PSA improves macro-averaged task success by 4.00 and 7.56 percentage points on the two benchmarks, respectively; within-backbone reductions in final-step tokens average 28.3% and 33.9%. These results support extending agent control beyond query reformulation to the processing and presentation of retrieved evidence. Code will be released subject to approval.

---


### 550. [Adapting prior-data fitted networks for tabular anomaly detection](https://arxiv.org/abs/2610.06693)

**<font color=#1a73e8>作者：</font>** Maximilian Bershtman, Niv Cohen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While deep features have transformed anomaly detection in images and video, their impact on tabular data has been less substantial, partly due to the limited availability of strong deep representations. Recently, prior-data fitted networks (PFNs) have emerged as a promising source of such representations for tabular data. In this work, we investigate how PFN representations can be adapted and leveraged for anomaly detection. The question is harder than it looks. No anomalies are available before deploy- ment, so model parameters cannot be tuned with supervision, and the reference set that defines normal behavior may itself contain the very anomalies it is supposed to reveal. We begin our study using frozen TabPFN features. Scoring each sam- ple by its distance to its nearest neighbors in feature space already gives strong results. We identify which layers to use and a feature-extraction procedure suited to the task. Next, to further improve performance, we use the reference set to fine- tune the model, so that the resulting features better separate normal samples from anomalies. On the ADBench benchmark, our fine-tuning free approach (ZEN) reaches a higher mean AUROC than every baseline, and our fine-tuned method (FOCUS) improves on it further. Our approach also generalizes across PFN models.

---


> [!TIP]
> 当前位于：**501-550**（第 11/12 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | **501-550** | [551-571](./part-12.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
