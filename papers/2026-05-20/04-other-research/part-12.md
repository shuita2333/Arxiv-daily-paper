# 📦 其他研究 | 2026年05月20日

> 本类共 **619** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**551-600**（第 12/13 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | **551-600** | [601-619](./part-13.md)

---

### 551. [Scheduling That Speaks: An Interpretable Programmatic Reinforcement Learning Framework](https://arxiv.org/abs/2605.18454)

**<font color=#1a73e8>作者：</font>** Chengpeng Hu, Yingqian Zhang, Hendrik Baier  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep reinforcement learning (DRL) has recently emerged as a promising approach to solve combinatorial optimization problems such as job shop scheduling. However, the policies learned by DRL are typically represented by deep neural networks (DNNs), whose opaque neural architectures and non-interpretable policy decisions can lead to critical trust and usability concerns for human decision makers. In addition, the computational requirements of DNNs can further hinder practical deployment in resource constrained environments. In this work, we propose ProRL, a novel interpretable programmatic reinforcement learning framework that achieves high-performance scheduling with human-readable and editable programmatic policies (i.e., programs). We first introduce a domain-specific language for scheduling (DSL-S) to represent scheduling strategies as structured programs. ProRL then explores the program space defined by DSL-S using local search to identify incomplete programs, which are subsequently completed by learning their parameters via Bayesian optimization. ProRL learns which scheduling heuristic rules to select, and hence, it naturally incorporates existing heuristics already used in industrial scenarios. Experiments on widely used benchmark instances demonstrate the strong performance of ProRL against existing heuristics and DRL baselines. Furthermore, ProRL performs well under strongly constrained computational resources, such as training with only 100 episodes. Our code is available at this https URL.

---


### 552. [OrganicHAR: Towards Activity Discovery in Organic Settings for Privacy Preserving Sensors Using Efficient Video Analysis](https://arxiv.org/abs/2605.18455)

**<font color=#1a73e8>作者：</font>** Prasoon Patidar, Riku Arakawa, Ricardo Graça 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Deploying human activity recognition (HAR) at home is still rare because sensor signals vary wildly across houses, people, and time, essentially requiring in-situ data collection and training. Prior approaches use cameras to generate training labels for privacy-preserving sensors (LiDAR, RADAR, Thermal), but this forces sensors to detect predefined activities that cameras can see yet the sensors themselves cannot reliably distinguish. In this work, we introduce OrganicHAR, an activity discovery framework that inverts this relationship by placing sensor capabilities at the center of activity discovery. Our approach identifies naturally occurring signal patterns using privacy-preserving sensors, leverages Vision Language Models (VLMs) only during these key moments for scene understanding, and discovers discrete activity labels at granularities that these sensors can reliably detect. Our evaluation with 12 participants demonstrates OrganicHAR's effectiveness: it achieves 79% accuracy for coarse (4-5) activities using only basic ambient sensors (radar, lidar, thermal arrays), and 73% accuracy for fine-grained (8-9) activities when a wearable IMU, depth, and pose sensor are added. OrganicHAR maintains 77% accuracy on average across configurations while discovering 4-8 categories per user (15 across all users) tailored to each environment and sensor capabilities. By triggering video processing only at key moments identified by local sensors, we reduce queries to VLM by 90%, enabling practical and privacy-preserving activity recognition in natural settings.

---


### 553. [Adaptive Experimentation for Censored Survival Outcomes](https://arxiv.org/abs/2605.18459)

**<font color=#1a73e8>作者：</font>** Yuxin Wang, Dennis Frauen, Jonas Schweisthal 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adaptive experimentation enables efficient estimation of causal effects, but existing methods are not designed for survival data with censoring, where event times are only partially observed (e.g., overall survival in cancer trials but with dropout). In this paper, we develop a novel framework for adaptive experimentation to estimate causal effects under right censoring. For this, we derive the semiparametric efficiency bound for the average survival effect curve as a function of the treatment allocation policy and thereby obtain a closed-form efficiency-optimal allocation policy. The policy generalizes classical Neyman allocation to survival settings by prioritizing patient strata where both event and censoring dynamics induce high uncertainty. Building on this, we propose the Adaptive Survival Estimator (ASE), an adaptive framework that learns the allocation policy and estimates the average survival effect curve sequentially. Our framework has three main benefits: (i) it accommodates arbitrary machine learning models for nuisance estimation; (ii) it is guided by a closed-form efficiency-optimal allocation policy; and (iii) it admits strong theoretical guarantees, including asymptotic normality via a martingale central limit theorem. We demonstrate our framework across various numerical experiments to show consistent efficiency gains over uniform randomization and censoring-agnostic baselines.

---


### 554. [When Fireflies Cluster; Enhancing Automatic Clustering via Centroid-Guided Firefly Optimization](https://arxiv.org/abs/2605.18460)

**<font color=#1a73e8>作者：</font>** MKA Ariyaratne, Azwirman Gusrialdi, Yury Nikulin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This work presents a novel variant of the Firefly Algorithm (FA) for data clustering, addressing limitations of traditional methods like K-Means that struggle with non-uniform cluster shapes, densities, and the need for pre-defining the number of clusters. The proposed algorithm introduces a centroid movement strategy and a multi-objective fitness function that balances compactness, separation, and a novel TSP-based navigation penalty. It automatically estimates the optimal number of clusters and dynamically adjusts cluster boundaries. Application to robotic sensor networks highlights its practical value, with experiments showing improved clustering quality and reduced intra-cluster path distances compared to K-Means. These results confirm the algorithm's robustness in complex spatial clustering tasks, with potential for future extensions to higher-dimensional and adaptive scenarios.

---


### 555. [From BERT to T5: A Study of Named Entity Recognition](https://arxiv.org/abs/2605.18462)

**<font color=#1a73e8>作者：</font>** Mei Jia  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Named entity recognition (NER) has been one of the essential preliminary steps in modern NLP applications. This report focuses on implementing the NER task on finetuning two pretrained models: (i) an encoder-only model (BERT) with a simple classification head, and (ii) a sequence-to-sequence model (T5) with few-shot prompts. Under the original 7-class tag and 3-class simplified tag schemes, BERT is applied a weighted cross-entropy for training loss, and T5 is fine-tuned with two validation strategies. It also conducted an ablation study with different hyperparameters. Moreover, the related analysis provides valuable insights into common errors in BERT and the two models' performance. Based on a bunch of performance metrics, this report aims to compare the above two architectures and explore their abilities in the sequence labelling task, laying the groundwork for further practical use cases.

---


### 556. [PERL: Parameter Efficient Reasoning in CLIP Latent Space](https://arxiv.org/abs/2605.18464)

**<font color=#1a73e8>作者：</font>** Simone Carnemolla, Salvatore Calcagno, Daniela Giordano 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Contrastively trained vision-language models such as CLIP provide strong zero-shot transfer by aligning images and text in a shared embedding space. However, adapting these models to downstream tasks without degrading their open-vocabulary generalization remains challenging. Existing parameter-efficient adaptation methods typically improve task specialization through learned prompts, adapters, or multimodal transformations, where adaptation capacity is primarily expressed through additional trainable parameters. Inspired by recent latent reasoning methods in language models, we investigate a complementary perspective: can adaptation emerge from iterative reasoning on latent representations rather than from increasing parameter count alone? We introduce PERL (Parameter-Efficient Reasoning in CLIP Latent Space), a lightweight adaptation framework that augments a frozen CLIP model with a compact shared reasoning module applied recurrently across refinement steps. At each step, PERL generates a latent reasoning token conditioned on the current representation and injects it into an intermediate encoder layer, progressively refining higher-level semantic representations while preserving CLIP's pretrained multimodal structure. Across 15 benchmarks spanning base-to-novel generalization, cross-dataset transfer, and out-of-distribution ImageNet variants, PERL achieves the best parameter-performance trade-off among the compared methods under a fast-adaptation few-shot setting, combining strong novel-class accuracy and competitive transfer performance with only about 6K trainable parameters, up to 817x fewer than the largest compared approach. Overall, our results suggest that iterative latent reasoning provides a complementary adaptation mechanism to parameter scaling in discriminative vision-language models.

---


### 557. [InstructAV2AV: Instruction-Guided Audio-Video Joint Editing](https://arxiv.org/abs/2605.18467)

**<font color=#1a73e8>作者：</font>** Haojie Zheng, Yixin Yang, Siqi Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent diffusion-based methods have achieved impressive progress in video content manipulation. However, they typically ignore the accompanying audio, leaving the audio disjointed from the edited results. In this paper, we propose InstructAV2AV, the first end-to-end framework for instruction-guided audio-video joint editing. We first develop a scalable data synthesis pipeline and construct InsAVE-80K, the first large-scale audio-video editing dataset with high-quality source-to-target pairs. With this data foundation, we adapt an audio-video generation backbone to leverage its robust priors. We concatenate the audio-video input with noisy latent codes to anchor the source context, propose the source-instruction gated attention to improve instruction following and content preservation, and introduce a two-stage training strategy to effectively transfer these pre-trained priors. Extensive experiments demonstrate that InstructAV2AV outperforms state-of-the-art methods across 11 metrics spanning three aspects on two evaluation sets, highlighting its potential for controllable content creation. Project page: this https URL.

---


### 558. [OCCAM: Open-set Causal Concept explAnation and Ontology induction for black-box vision Models](https://arxiv.org/abs/2605.18481)

**<font color=#1a73e8>作者：</font>** Chiara Maria Russo, Simone Carnemolla, Simone Palazzo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Interpreting the decisions of deep image classifiers remains challenging, particularly in black-box settings where model internals are inaccessible. We introduce OCCAM, a framework for open-set causal concept explanation and ontology induction in vision models. OCCAM discovers visual concepts in an open-set manner, localizes them via text-guided segmentation, and performs object-level interventions by removing concepts to measure changes in class confidence, estimating each concept's causal contribution. Beyond local explanations, OCCAM aggregates interventional evidence across a dataset to induce a structured concept ontology that captures how classifiers globally organize visual concepts. Reasoning over this ontology reveals consistent dependencies between concepts, exposes latent causal relations, and uncovers systematic model biases. Experiments on Broden and ImageNet-S across multiple classifiers show that OCCAM improves explanation quality in open-set black-box settings while providing richer global insight than per-image attribution methods.

---


### 559. [Modality vs. Morphology: A Framework for Time Series Classification for Biological Signals](https://arxiv.org/abs/2605.18483)

**<font color=#1a73e8>作者：</font>** Jordan Tschida, Matthew Yohe, Edward Kane 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series classification (TSC) of biological signals has progressed from handcrafted, modality-specific approaches to deep architectures capable of representing the diverse waveform structures of underlying physiological processes (i.e., morphology). This review introduces a unified morphology--modality framework that connects waveform structure to a methodological design, revealing how spikes, bursts, oscillations, slow drift, and hierarchical rhythms inform model design. By analyzing electroencephalography, electromyography, electrocardiography, photoplethysmography, and ocular modalities (electrooculography, pupillometry, eye-tracking), the review demonstrates how morphology determines preprocessing and modeling strategies. Integrating evidence across these biological signals, the framework reveals that morphology, not model class, most strongly determines performance and interpretability. This provides insight into why deep models succeed when their inductive biases align with underlying waveform dynamics. This review also identifies future work including morphological data augmentation and evaluation metrics to improve generalization. Together, these insights position morphology-aware modeling as a unifying principle for developing generalizable, interpretable, and physiologically meaningful TSC models across biological signals.

---


### 560. [Bridging the Cybersecurity Gap Between Web2 and Web3 - An Incident-Based Analysis of Organizational and Application-Level Security Failures](https://arxiv.org/abs/2605.18484)

**<font color=#1a73e8>作者：</font>** Tarkan Yavas, Arslan Brömme  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The rapid adoption of Web3 infrastructures has led to a growing number of security incidents affecting cryptocurrency exchanges, custody services and blockchain-based platforms. While existing research predominantly focuses on vulnerabilities in smart contracts and blockchain protocols, a substantial portion of real-world losses originates from off-chain systems, organizational processes and human-centered operational workflows.
This paper presents a qualitative, incident-based analysis of publicly documented, high-impact security breaches in the Web3 ecosystem, including the Bybit exchange incident (2025), the Ronin Network bridge compromise (2022), and the DMM Bitcoin exchange breach (2024). The selected cases are systematically analysed and mapped to established Web2 security reference frameworks, including OWASP-based vulnerability categories and organizational security control domains.
The results indicate that dominant failure patterns in Web3 environments are insufficiently addressed by generic security control catalogues, particularly with respect to cryptographic key management, transaction approval governance, signer and validator infrastructure, third-party tooling dependencies, and human-in-the-loop processes.
Based on these findings, this paper argues for the adoption of established information security management systems (ISMS) in Web3 organizations and derives a structured set of blockchain-specific cybersecurity control categories to operationalize existing ISMS frameworks for blockchain-based systems. The proposed categories aim to bridge the gap between generic security governance frameworks and domain-specific risks inherent to Web3 infrastructures.

---


### 561. [Benchmarking transferability of SSL pretraining to same and different modality segmentation tasks](https://arxiv.org/abs/2605.18491)

**<font color=#1a73e8>作者：</font>** Jue Jiang, Harini Veeraraghavan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Methods: Nine SSL methods spanning four pretext-task families were pretrained from scratch using the same 10{,}412 3D CT scans (1.89~M 2D axial slices) covering varied disease sites. The pretrained Swin Transformer encoder from each method was integrated into a SwinUNETR-style segmentation network (Swin encoder with a 3D CNN decoder and skip connections) and fine-tuned on nine public segmentation tasks of varying complexity, including large abdominal organs, head-and-neck structures, and tumors from CT and MRI. Performance was assessed using Dice similarity coefficient (DSC). Fine-tuning convergence speed, transferability across modalities (CT-to-MRI), and feature-reuse patterns between few- and many-shot fine tuning were further analyzed using centered kernel alignment.
Results: Self-distilled masked image transformer (SMIT), which combines masked image modeling (MIM) with local and global self-distillation, achieved the highest overall segmentation accuracy across the nine tasks, the fastest fine-tuning convergence, and the smallest few-shot-to-many-shot performance gap, indicating the strongest data efficiency. SMIT also showed the most consistent feature-reuse patterns between few- and many-shot fine tuning. MIM-based SimMIM and self-distillation methods (DINO, iBOT) outperformed contrastive learning and rotation prediction, which rely on image-level global representations. Differences between SSL methods were largest in the few-shot setting and narrowed as the size of the labeled fine-tuning dataset increased, indicating that the choice of SSL pretraining matters most under limited annotation budgets.

---


### 562. [Weakly Supervised Cross-Modal Learning for 4D Radar Scene Flow Estimation](https://arxiv.org/abs/2605.18507)

**<font color=#1a73e8>作者：</font>** Jingyun Fu, Zhiyu Xiang, Na Zhao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Due to the difficulty of obtaining ground-truth data for 4D radar scene flow estimation, previous methods typically rely on either self-supervised losses or cross-modal supervision using 3D LiDAR data, 2D images, and odometry. However, self-supervised approaches often yield suboptimal results due to radar's inherently low-fidelity measurements, while existing cross-modal supervised methods introduce complex multi-task architecture and require costly LiDAR sensors to generate pseudo radar scene flow labels from pretrained 3D tracking models. To overcome these limitations, we propose a task-specific iterative framework for weakly supervised radar scene flow learning, using only images and odometry for auxiliary supervision during training. Specially, we establish two novel instance-aware self-supervised losses by exploiting off-the-shelf 2D tracking and segmentation algorithms to obtain tracked instance masks, which are back-projected into 3D space to provide instance-level semantic guidance; for static regions, we integrate vehicle odometry with radar's intrinsic motion cues to construct a rigid static loss. Extensive experiments on the real-world View-of-Delft (VoD) dataset demonstrate that our method not only surpasses state-of-the-art cross-modal supervised approaches that rely on 3D multi-object tracking on dense LiDAR point clouds but also outperforms existing fully supervised scene flow estimation methods. The code is open-sourced at \href{this https URL}{this https URL}.

---


### 563. [DiPRL: Learning Discrete Programmatic Policies via Architecture Entropy Regularization](https://arxiv.org/abs/2605.18508)

**<font color=#1a73e8>作者：</font>** Chengpeng Hu, Yingqian Zhang, Hendrik Baier  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Programmatic reinforcement learning (PRL) offers an interpretable alternative to deep reinforcement learning by representing policies as human-readable and -editable programs. While gradient-based methods have been developed to optimize continuous relaxations of programs, they face a significant performance drop when converting the continuous relaxations back into discrete programs. Post-hoc discretization can discard optimized branches and parameters in a program, which results in a collapse of policy expressivity and lowered task performance, leading in turn to a need for additional fine-tuning. To overcome these limitations, we propose Differentiable Discrete Programmatic Reinforcement Learning (DiPRL), a method that learns programmatic policies that become nearly discrete during training, avoiding a separate post-hoc fine-tuning stage. We first analyze the inherent risks of performance drop introduced by post-hoc discretization of gradient-based methods. Then, we introduce programmatic architecture entropy regularization, which enables smooth, differentiable training that encourages convergence toward a discrete program. DiPRL maintains the efficiency of gradient-based optimization while mitigating the risks of post-hoc discretization. Our experiments across multiple discrete and continuous RL tasks demonstrate that DiPRL can achieve strong performance via interpretable programmatic policies.

---


### 564. [Offline Contextual Bandits in the Presence of New Actions](https://arxiv.org/abs/2605.18509)

**<font color=#1a73e8>作者：</font>** Ren Kishimoto, Tatsuhiro Shimizu, Kazuki Kawamura 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Automated decision-making algorithms drive applications such as recommendation systems and search engines. These algorithms often rely on off-policy contextual bandits or off-policy learning (OPL). Conventionally, OPL selects actions that maximize the expected reward from an existing action set. However, in many real-world scenarios, actions, such as news articles or video content, change continuously, and the action space evolves over time after data collection. We define actions introduced after deploying the logging policy as new actions and focus on OPL with new actions. Existing OPL methods identify optimal actions from the existing set effectively but cannot learn and select new actions because no relevant data are logged. To address this limitation, we propose a new OPL method that leverages action features. We first introduce the Local Combination PseudoInverse (LCPI) estimator for the policy gradient, generalizing the PseudoInverse estimator initially proposed for off-policy evaluation of slate bandits. LCPI controls the trade-off between reward-modeling condition and the condition for data collection regarding the action features, capturing the interaction effects among different dimensions of action features. Furthermore, we propose a generalized algorithm called Policy Optimization for Effective New Actions (PONA), which integrates LCPI, a component specialized for new action selection, with Doubly Robust (DR), which excels at learning within existing actions. We define PONA as a weighted sum of the LCPI and DR estimators, optimizing both the selection of existing and new actions, and allowing the proportion of new action selections to be adjusted by the weight parameter. Through extensive experiments, we demonstrate that PONA efficiently selects new actions while maintaining the overall policy performance as opposed to most existing methods that cannot select new actions.

---


### 565. [A Practical Noise2Noise Denoising Pipeline for High-Throughput Raman Spectroscopy](https://arxiv.org/abs/2605.18511)

**<font color=#1a73e8>作者：</font>** David Martin-Calle, Cesar Alvarez Llamas, Vincent Motto- Ros 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A lightweight and reproducible denoising pipeline for high-throughput Raman spectroscopy is presented. The approach relies on a one-dimensional convolutional autoencoder trained using a Noise2Noise strategy, requiring neither external spectral libraries nor high signal-to-noise reference spectra for training. From a reduced training subset composed of repeated short-exposure acquisitions, the model learns to reconstruct Raman spectra while efficiently suppressing stochastic noise. The method is evaluated on a heterogeneous mineral sample, using both quantitative spectral fidelity metrics (RMSE, SNR, SSIM) and task-oriented criteria based on unsupervised K-means classification. Results demonstrate that integration times as short as 5 ms per spectrum, which are typically insufficient for reliable interpretation, yield denoised spectra with high fidelity to the reference data while preserving chemically coherent maps. This work provides a practical trade-off between spectral quality and acquisition speed, enabling fast, adaptable Raman workflows compatible with routine laboratory use. It also offers a transferable framework for other one-dimensional spectroscopic modalities.

---


### 566. [Beyond Morphology: Quantifying the Diagnostic Power of Color Features in Cancer Classification](https://arxiv.org/abs/2605.18522)

**<font color=#1a73e8>作者：</font>** Farnaz Kheiri, Shahryar Rahnamayan, Masoud Makrehchi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In histopathology, human experts primarily rely on color as a means of enhancing contrast to interpret tissue morphology, whereas machine vision models process color as raw statistical information. This distinction raises a fundamental question: to what extent can pixel intensity alone, independent of structural and morphological cues, support cancer classification? To address this question, we systematically evaluated the standalone discriminative power of global color features while deliberately excluding all morphological information. Specifically, we extracted statistical color moments and discretized RGB and HSV color histograms, and assessed their performance across ten diverse experimental settings using classical machine learning classifiers. Our results demonstrate that color features alone can achieve strong performance in binary diagnostic tasks (e.g., benign versus malignant), with classification accuracies reaching up to 89%. This performance is likely attributable to global chromatic shifts associated with malignancy. Importantly, these simple color-based representations consistently outperformed random baselines by a substantial margin, indicating that raw color distributions encode a non-random and diagnostically relevant signal for cancer detection. Consequently, this study suggests that simple, computationally efficient color features can serve as an effective pre-screening tool. By identifying samples with strong chromatic indicators of malignancy, these lightweight models could function as a first-pass triage system, reducing the computational burden on complex deep learning architectures.

---


### 567. [Continuous Diffusion Scales Competitively with Discrete Diffusion for Language](https://arxiv.org/abs/2605.18530)

**<font color=#1a73e8>作者：</font>** Zhihan Yang, Wei Guo, Shuibai Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While diffusion has drawn considerable recent attention from the language modeling community, continuous diffusion has appeared less scalable than discrete approaches. To challenge this belief we revisit Plaid, a likelihood-based continuous diffusion language model (DLM), and construct RePlaid by aligning the architecture of Plaid with modern discrete DLMs. In this unified setting, we establish the first scaling law for continuous DLMs that rivals discrete DLMs: RePlaid exhibits a compute gap of only $20\times$ compared to autoregressive models, outperforms Duo while using fewer parameters, and outperforms MDLM in the over-trained regime. We benchmark RePlaid against recent continuous DLMs: on OpenWebText, RePlaid achieves a new state-of-the-art PPL bound of $22.1$ among continuous DLMs and superior generation quality. These results suggest that continuous diffusion, when trained via likelihood, is a highly competitive and scalable alternative to discrete DLMs. Moreover, we offer theoretical insights to understand the advantage of likelihood-based training. We show that optimizing the noise schedule to minimize the ELBO's variance naturally yields linear cross-entropy (information loss) over time. This evenly distributes denoising difficulty without any case-specific time reparameterization. In addition, we find that optimizing embeddings via likelihood creates structured geometries and drives the most significant likelihood gain.

---


### 568. [Beyond Scaling: Agents Are Heading to the Edge](https://arxiv.org/abs/2605.18535)

**<font color=#1a73e8>作者：</font>** Chunlin Tian, Dongqi Cai, Wanru Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The bottleneck of useful agentic intelligence has shifted from compressing world knowledge into a single model to executing a coordinated system. This position paper argues that personal-agent architecture must move to the edge because the core properties of agentic intelligence tasks, particularly their structural coupling with high-fidelity local context and the need for zero-latency execution loops, do not sit well with cloud-centric designs. We develop this claim through three structural shifts. First, the Prefrontal Turn: the main marginal lever of capability has moved from pre-training scale to framework-level executive control. Such control must remain physically close to the environment of action if the agent is to preserve cognitive alignment. Second, the Data-Geography Paradox, the ``dark matter'' of agentic data (local file hierarchies, real-time sensor streams, and transient OS states) degrades, disappears, or loses meaning once prepared for cloud transmission, thereby cutting the agent off from ground-truth context. Third, the interaction-alignment loop, the only economically and ecologically sustainable source of agentic refinement data is the high-fidelity implicit preference signal produced through real-time local interaction. Third, the interaction-alignment loop, the only economically and ecologically sustainable source of agentic refinement data is the high-fidelity implicit preference signal produced through real-time local interaction. We conclude with falsifiable predictions for the next deployment cycle of personal agents.

---


### 569. [Probing for Representation Manifolds in Superposition](https://arxiv.org/abs/2605.18537)

**<font color=#1a73e8>作者：</font>** Alexander Modell  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper introduces the Manifold Probe, a supervised method for discovering representation manifolds in superposition. The method generalizes linear regression probes by learning the space of features of a concept that can be linearly predicted from the representations, and then learning the directions used to encode them. We demonstrate the probe on representations of time and space in Llama 2-7b, finding manifolds which linearly represent an interpretable set of features in each case. In the case of time, we show that by steering along the manifold, we can influence the model's completions about the years in which famous songs, movies and books were released, providing evidence that the Manifold Probe can discover manifolds which are causally involved in model behaviour.

---


### 570. [LESSViT: Robust Hyperspectral Representation Learning under Spectral Configuration Shift](https://arxiv.org/abs/2605.18541)

**<font color=#1a73e8>作者：</font>** Haozhe Si, Yuxuan Wan, Yuqing Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modeling hyperspectral imagery (HSI) across different sensors presents a fundamental challenge due to variations in wavelength coverage, band sampling, and channel dimensionality. As a result, models trained under a fixed spectral configuration often fail to generalize to other sensors. Existing Vision Transformer (ViT) approaches either rely on implicit spectral modeling with fixed channel assumptions or adopt explicit spatial-spectral attention with prohibitive computational cost, leading to a fundamental trade-off between efficiency and expressiveness. In this work, we introduce Low-rank Efficient Spatial-Spectral ViT (LESSViT), a sensor-flexible architecture for cross-spectral generalization. LESSViT is built on LESS Attention, a structured low-rank factorization that models joint spatial-spectral interactions through separable spatial and spectral components, reducing the complexity of full spatial-spectral attention from $O(N^2 C^2)$ to $O(rNC)$, where $N$ is the number of spatial tokens, $C$ is the number of spectral channels, and $r$ is the rank of the low-rank approximation. We further incorporate channel-agnostic patch embedding and wavelength-aware positional encoding to support flexible spectral inputs. To enable efficient and robust pretraining, we introduce a hyperspectral masked autoencoder (HyperMAE) with decoupled spatial-spectral masking and hierarchical channel sampling. We evaluate LESSViT under a cross-spectral generalization setting that simulates cross-sensor variability. Experiments on the SpectralEarth benchmark demonstrate that LESSViT improves robustness under spectral shifts while remaining competitive in-distribution, and explicit and efficient spatial-spectral modeling is essential for scalable and generalizable hyperspectral representation learning.

---


### 571. [Monitoring the Internal Monologue: Probe Trajectories Reveal Reasoning Dynamics](https://arxiv.org/abs/2605.18549)

**<font color=#1a73e8>作者：</font>** Maciej Chrabąszcz, Aleksander Szymczyk, Marcin Sendera 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Reasoning Models (LRMs) introduce new opportunities for safety monitoring through their Chain of Thought (CoT) reasoning. However, CoT is not always faithful to the model's final output, undermining its reliability as a monitoring tool. To address this, we investigate the hidden representations of LRMs to determine whether future behavior can be predicted from prompt and CoT representations. By evaluating a probe at each generated token, we construct a probe trajectory, the continuous evolution of a concept's probability across the reasoning process. We find that future model behavior is more distinguishable when examined over the full trajectory than from a single static prediction. To characterize these temporal dynamics, we extract signal-processing features that capture volatility, trend, and steady-state behavior, significantly improving the separation of future model states. We also present two methodological insights. First, template-based training data achieves near-parity with dynamically generated model responses, eliminating the need for a costly initial inference and labeling. Second, the choice of pooling operation is critical: average-pooling and last-token methods collapse to near-random performance, while max-pooling achieves up to 95% AUROC and yields stable probe trajectories. Using four datasets and four reasoning models across the domains of safety and mathematics, we demonstrate that trajectory features encode task-specific dynamics that improve outcome separability. These findings establish probe trajectories as a complementary framework for monitoring LRM behavior.
Warning: This article contains potentially harmful content.

---


### 572. [Protein Fold Classification at Scale: Benchmarking and Pretraining](https://arxiv.org/abs/2605.18552)

**<font color=#1a73e8>作者：</font>** Dexiong Chen, Andrei Manolache, Mathias Niepert 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Classifying protein topology is essential for deciphering biological function, but progress is held back by the lack of large-scale benchmarks that avoid duplicates and by models that do not scale well. We introduce TEDBench, a large-scale, non-redundant benchmark for protein fold classification constructed from the Encyclopedia of Domains (TED) and Foldseek-clustered AlphaFold structures. We show that on TEDBench, current protein representation learning methods either require very large models or fail to deliver strong performance. To address this challenge, we propose Masked Invariant Autoencoders (MiAE), a self-supervised framework for protein structure representation learning. MiAE uses an extremely high masking ratio of up to 90% with an $\mathrm{SE(3)}$-invariant encoder and a lightweight decoder that reconstructs backbone coordinates from the latent representation and mask tokens. MiAE scales well and outperforms supervised counterparts and state-of-the-art baselines on TEDBench, establishing a strong recipe for protein fold classification. To test transfer beyond AlphaFold structures, we further benchmark on a curated dataset from experimental structures of CATH v4.4. TEDBench is available at this https URL.

---


### 573. [StableHand: Quality-Aware Flow Matching for World-Space Dual-Hand Motion Estimation from Egocentric Video](https://arxiv.org/abs/2605.18553)

**<font color=#1a73e8>作者：</font>** Huajian Zeng, Chaohua Yao, Yuantai Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recovering world space 4D motion of two interacting hands from egocentric video is a fundamental capability for supervising robot policy learning, where wrist trajectories track the end-effector and finger articulations specify the grasp pose. Two major challenges arise in this setting: hands frequently leave the camera view for extended periods due to head motion, and persistent hand-object interactions cause severe occlusions of one or both hands. Existing methods uniformly condition on noisy hand motion observations without accounting for their per-frame reliability, leading to substantial performance degradation. Our key insight is that accurate world space hand motion estimation is tightly coupled with the quality of per-frame hand observations. To this end, we decompose the quality of hand motion observations extracted from an off-the-shelf hand pose estimator into four channels: wrist global translation and finger articulations for both hands. We propose StableHand, a quality-aware flow-matching framework conditioned on these four-channel quality signals, which are predicted by a learned quality network. We naturally incorporate the quality signals into the flow-matching process through a per-channel forward schedule, a quality-adjusted velocity target, AdaLN modulation of the DiT denoiser, and a quality-aware ODE initialization. This unified generative process preserves high-quality observations while reconstructing unreliable ones using a learned bimanual motion prior. Experiments on HOT3D and ARCTIC, two egocentric benchmarks featuring long missing-hand spans and persistent hand-object occlusions, show that StableHand achieves state-of-the-art performance across all reported metrics, reducing W-MPJPE by 20-25% compared to the strongest baseline, with the largest gains on heavily occluded ARCTIC sequences.

---


### 574. [Federated Martingale Posterior Samping](https://arxiv.org/abs/2605.18554)

**<font color=#1a73e8>作者：</font>** Boning Zhang, Matteo Zecchin, Mingzhao Guo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated Bayesian neural networks require fixing a prior on the model parameters together with a likelihood. Eliciting meaningful priors on the weight space of modern overparameterized models is notoriously difficult, and misspecification of either component can severely degrade accuracy and calibration. Motivated by the rapid progress of predictive models such as large language models, the martingale posterior, also known as predictive Bayes, replaces the prior--likelihood pair with a predictive distribution and recovers parameter uncertainty by repeatedly drawing predictive samples and refitting the model. A direct federated implementation, however, would require clients to share the local data sets. This letter proposes {federated martingale posterior} (FMP) sampling, a one-shot embarrassingly parallel protocol in which each client uploads a small set of trainable data embeddings and the server runs the predictive sampler centrally. Experiments on MNIST, CIFAR-10, and CIFAR-100 show that FMP closely matches the centralized counterpart and significantly improves calibration over consensus-style baselines.

---


### 575. [Self-supervised local learning rules learn the hidden hierarchical structure of high-dimensional data](https://arxiv.org/abs/2605.18557)

**<font color=#1a73e8>作者：</font>** Ariane Delrocq, Wu S. Zihan, Guillaume Bellec 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The brain learns abstract representations of high-dimensional sensory input, but the plasticity rules that enable such learning are unknown. We study biologically plausible algorithms on the Random Hierarchy Model (RHM), an artificial dataset designed to investigate how deep neural networks learn the intrinsic hierarchical structure of high-dimensional data. We focus on two types of local learning rules that avoid both a long convergence time and the use of a symmetric error network. The first type uses direct feedback signals to approximate error propagation from the output layer. The second type uses layerwise self-supervised contrastive or non-contrastive loss functions that do not explicitly approximate errors at the output layer. We show that all rules of the first type fail to solve the tasks of the RHM and trace this failure back to input-specific nonlinearities (`masking') that are implemented in full backpropagation and are essential for learning complex tasks. However, algorithms of the second type are able to learn the hierarchical hidden structure of the RHM tasks and are as data-efficient as supervised backpropagation training, while being compatible with known rules of synaptic plasticity in cortex.

---


### 576. [Readers make targeted regressions to plausible errors in reanalysis of "noisy-channel garden-path" sentences](https://arxiv.org/abs/2605.18563)

**<font color=#1a73e8>作者：</font>** Thomas Hikaru Clark, Roger Levy, Edward Gibson  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A key question in psycholinguistics is how inferences about the meaning of linguistic input unfold incrementally a comprehender's mind. In this work, we study reading dynamics for ``noisy-channel garden-path'' sentences, which temporarily appear well-formed but feature late-appearing violations of expectation that can be resolved not by inferring an alternative syntactic structure, but by inferring the presence of an error. We find evidence for targeted regressions -- eye movements towards regions that are promising loci of possible errors in light of later-arriving information, showing patterns consistent with the posterior inferences of a model of noisy-channel processing with reanalysis. We discuss the implications of these findings for theories of noisy-channel language comprehension and information-theoretic explanations of reading dynamics.

---


### 577. [LongMINT: Evaluating Memory under Multi-Target Interference in Long-Horizon Agent Systems](https://arxiv.org/abs/2605.18565)

**<font color=#1a73e8>作者：</font>** Hyunji Lee, Justin Chih-Yao Chen, Joykirat Singh 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Real-world agents operate over long and evolving horizons, where information is repeatedly updated and may interfere across memories, requiring accurate recall and aggregated reasoning over multiple pieces of information. However, existing benchmarks focus on static, independent recall and fail to capture these dynamic interactions between evolving memories. In this paper, we study how current memory-augmented agents perform in realistic, interference-heavy, long-horizon settings across diverse domains and question types. We introduce LongMINT (Long-Horizon Memory under INTerference), a benchmark featuring (1) long, highly interconnected contexts with frequently updated information that induces substantial interference, (2) diverse domains (state tracking, multi-turn dialogue, Wikipedia revisions, and GitHub commits), enabling evaluation of domain generalization, and (3) diverse question types that assess robustness to interference, including (i) single-target recall tasks requiring retrieval of a specific target from long contexts, and (ii) multi-target aggregation tasks requiring reasoning over multiple relevant pieces of information. Overall, LongMINT has 15.6k question-answering pairs over long-horizon contexts averaging 138.8k tokens and extending up to 1.8M tokens per instance. We evaluate 7 representative systems, including vanilla long-context LLMs, RAG, and memory-augmented agent frameworks. Across all systems, we observe consistently low performance (avg. 27.9% accuracy), especially on questions requiring aggregated reasoning over multiple pieces of evidence. Our analysis shows that performance is primarily limited by retrieval and memory construction. Furthermore, current memory systems struggle to recall and reason over earlier facts that are later revised or interfered with by subsequent context, with performance degrading as the number of intervening updates increases.

---


### 578. [GUT-IS: A Data-Driven Approach to Integrating Constructs and Their Relations in Information Systems](https://arxiv.org/abs/2605.18567)

**<font color=#1a73e8>作者：</font>** Maximilian Reinhardt, Jonas Scharfenberger, Burkhardt Funk  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Structural equation modeling is widely used in IS research. However, inconsistent construct definitions impede the cumulative development of knowledge. In this work, we present an approach that aims at the integration of structural equation models into a unified model: We use a combination of task-adapted text embeddings and clustering to produce a candidate set of construct groupings. Subsequently, we select the optimal solution using a loss function that explicitly trades off semantic purity and parsimony in the number of clusters. By making this trade-off explicit, our approach allows to analyze how construct groupings and their relations change as one shifts the priority from purity to parsimony. Empirically, we evaluate and explore the proposed methodology on two datasets from the IS domain.

---


### 579. [scHelix: Asymmetric Dual-Stream Integration via Explicit Gene-Level Disentanglement](https://arxiv.org/abs/2605.18576)

**<font color=#1a73e8>作者：</font>** Xichen Yan, Zelin Zang, Changxi Chi 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A critical challenge in single-cell RNA sequencing (scRNA-seq) integration is resolving the tension between eliminating batch effects and maintaining biological fidelity. While recent evidence indicates that batch effects manifest heterogeneously across genes, most existing methods process the transcriptome uniformly, frequently resulting in over-correction and loss of subtle biological signals. To address this, we present scHelix, a dataset-adaptive framework that fundamentally changes how features are processed by explicitly partitioning genes into domain-invariant Anchors and domain-sensitive Variants at the input level. scHelix utilizes a dual-stream sparse diffusion encoder equipped with stop-gradient graph caching to efficiently learn multi-scale structural representations. The core of our approach is a novel asymmetric Align-Refine-Fuse protocol: the unstable Variant stream is first aligned to the robust topology of the Anchor stream, followed by a conservative refinement phase where the Anchor stream absorbs denoised details via bounded residual gating. This divide-and-conquer architecture prevents shortcut learning and ensures robust batch removal without compromising the integrity of biological clusters. Extensive benchmarking demonstrates that scHelix outperforms state-of-the-art methods.

---


### 580. [OmniPro: A Comprehensive Benchmark for Omni-Proactive Streaming Video Understanding](https://arxiv.org/abs/2605.18577)

**<font color=#1a73e8>作者：</font>** Ruixiang Zhao, Jie Yang, Zijie Xin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Omni-proactive streaming video understanding, i.e., autonomously deciding when to speak and what to say from continuous audio-visual streams, is an emerging capability of omni-modal large language models. Existing benchmarks fall short in three key aspects: they rely primarily on visual signals, adopt polling or fixed-timestamp protocols instead of true proactive evaluation, and cover only a limited range of tasks, preventing reliable assessment and differentiation of omni-proactive streaming models. We present OmniPro, the first benchmark to jointly evaluate omni-modal perception, proactive responding, and diverse video understanding tasks. It comprises 2,700 human-verified samples spanning 9 sub-tasks and 3 cognitive levels, covering 6 basic video understanding capabilities. Notably, 84% of samples require audio signals (speech or non-speech), and each sample is annotated with modality-isolation labels to enable fine-grained multimodal analysis. We further introduce a dual-mode evaluation protocol: Probe mode assesses content understanding by querying the model before and after each ground-truth trigger, while Online mode evaluates full proactive ability by requiring models to autonomously decide when to respond in streaming input. Evaluating 11 representative models reveals three key findings: (1) audio provides consistent gains but with highly variable utilization across models, (2) performance degrades significantly over time, indicating limited long-horizon robustness, and (3) non-speech audio perception remains the weakest dimension.

---


### 581. [When Outcome Looks Right But Discipline Fails: Trace-Based Evaluation Under Hidden Competitor State](https://arxiv.org/abs/2605.18580)

**<font color=#1a73e8>作者：</font>** Peiying Zhu, Sidi Chang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Outcome-only evaluation can certify economically unsafe agents: a policy can hit a business KPI while violating deployable behavioral discipline. In hotel pricing with hidden competitor state, a learner can achieve plausible revenue per available room while failing to preserve the rate discipline of a rule-based revenue-management competitor.
We introduce discipline stability, a trace-based evaluation paradigm: define the benchmark behavior, restrict observations to the deployment regime, induce trace diagnostics from failure, separate mechanisms with ablations, and test transfer and deployment. Across a two-hotel benchmark and a compact hidden-budget bidding task, reward-only PPO variants miss trace alignment; revealing hidden state reduces label uncertainty; deterministic copy collapses uncertainty; and trace-prior or corrected history policies better preserve price or bid distributions. Pure behavior cloning is nearly enough for symmetric imitation, while Trace-Prior RL adds bounded adaptation under capacity asymmetry. The contribution is an evaluation and benchmark paradigm, not a new optimizer or a universal claim about MARL

---


### 582. [Randomized Advantage Transformation (RAT): Computing Natural Policy Gradients via Direct Backpropagation](https://arxiv.org/abs/2605.18591)

**<font color=#1a73e8>作者：</font>** Mingfei Sun  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Natural policy gradients improve optimization by accounting for the geometry of distribution space, but their practical use is limited by the cost of estimating and inverting the Fisher matrix. We present Randomized Advantage Transformation (RAT), a method for estimating Tikhonov-regularized natural policy gradients via direct backpropagation. By applying the Woodbury formula, we reformulate the regularized natural policy gradients as vanilla policy gradients with a transformed advantage. RAT computes this transformation efficiently via randomized block Kaczmarz iterations on on-policy mini-batches, avoiding explicit Fisher construction, conjugate-gradient solvers, and architecture-specific approximations. We provide convergence guarantees for RAT and demonstrate empirically that it matches or exceeds established natural-gradient methods across continuous and visual control benchmarks, while remaining simple to implement and compatible with various architectures.

---


### 583. [AMARIS: A Memory-Augmented Rubric Improvement System for Rubric-Based Reinforcement Learning](https://arxiv.org/abs/2605.18592)

**<font color=#1a73e8>作者：</font>** Peilin Wu, Xinlu Zhang, Kun Wan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Rubric-based reward shaping is an effective method for fine-tuning LLMs via RL, where structured rubrics decompose standard outcome rewards into multiple dimensions to provide richer reward signals. Recent works make the rubrics adaptive based on local signals such as the rollouts from the current step or pairwise comparisons. However, these methods discard the diagnostics produced during evaluation after immediate use and prevent the long-term accumulation and strategic reuse of evaluation knowledge. This forces the system to re-derive evaluation principles from scratch, limits its ability to detect recurring suboptimal behaviors, and forfeits the curriculum-like progression that a persistent training history would naturally support. To address these limitations, we introduce AMARIS, which grounds rubric modifications in long-term training history. At each training step, AMARIS analyzes individual rollouts, aggregates findings into step-level summaries, retrieves relevant historical context from a persistent evaluation memory through both static (recent steps) and dynamic (semantically matched) retrieval, and updates rubrics based on these accumulated analyses. This procedure runs asynchronously alongside the normal RL loop with minimal overhead. Experiments across both closed and open-ended domains show that AMARIS consistently outperforms the baselines. Ablation studies show that static and dynamic memory retrieval contributes to the performance gain and their combination provides the strongest results with moderate retrieval budgets sufficient to provide most of the gain, and that the entire pipeline adds only ~5\% time overhead through asynchronous execution. These results show that persistent evaluation memory can transform rubric-based reward shaping from a stateless, per-step heuristic into an evidence-driven loop for RL training.

---


### 584. [Not What You Asked For: Typographic Attacks in Household Robot Manipulation](https://arxiv.org/abs/2605.18593)

**<font color=#1a73e8>作者：</font>** Ali Iranmanesh, Peng Liu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Open-vocabulary embodied AI agents increasingly rely on vision-language models such as CLIP for object perception and task grounding. However, the shared embedding space that enables this flexibility introduces a structural vulnerability to typographic attacks, where printed text in a physical scene semantically overrides visual judgment. While prior work has quantified this threat in static 2D benchmarks and 3D navigation tasks, its impact on the full Sense-Plan-Act pipeline of household robot manipulation remains unexplored.
This work evaluates typographic attacks in a Habitat-based simulation using the HomeRobot benchmark. We introduce a decoupled perception architecture that exposes a frozen CLIP encoder to adversarial stickers while maintaining geometric grounding via DETIC. In a controlled evaluation pool of 59 attributable episodes, the attack achieves an overall Attack Success Rate (ASR) of 67.8%, rising to 70.0% among fully successful episodes, under uncontrolled viewing angles and occlusion with no perceptual optimization.
Critically, we find that perceptual errors propagate through the persistent 3D semantic map to produce kinetic failures, defined here as physically executed grasping and transport of the wrong object driven by an adversarially poisoned semantic state. In these cases, the robot physically grasps and delivers the wrong object to a target receptacle. These results establish typographic misclassification as a real, measurable, and physically consequential threat to the safety of modular manipulation pipelines that prior typographic attack research has left unexamined.

---


### 585. [Pointwise Generalization in Deep Neural Networks](https://arxiv.org/abs/2605.18598)

**<font color=#1a73e8>作者：</font>** Shaojie Li, Yunbei Xu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We address the fundamental question of why deep neural networks generalize by establishing a pointwise generalization theory for fully connected networks. This framework resolves long-standing barriers to characterizing the rich nonlinear feature-learning regime and builds a new statistical foundation for representation learning. For each trained model, we characterize the hypothesis via a pointwise Riemannian Dimension, derived from the eigenvalues of the learned feature representations across layers. This establishes a principled framework for deriving hypothesis-dependent, representation-aware generalization bounds. These bounds offer a systematic upgrade over approaches based on model size, products of norms, and infinite-width linearizations, yielding guarantees that are orders of magnitude tighter in both theory and experiment. Analytically, we identify the structural properties and mathematical principles that explain the tractability of deep networks. Empirically, the pointwise Riemannian Dimension exhibits substantial feature compression, decreases with increased over-parameterization, and captures the implicit bias of optimizers. Taken together, our results indicate that deep networks are mathematically tractable in practical regimes and that their generalization is sharply explained by pointwise, feature-spectrum-aware complexity.

---


### 586. [Resolving Representation Ambiguity in Feedforward Novel View Synthesis Transformer via Semantic-Spatial Decoupling](https://arxiv.org/abs/2605.18599)

**<font color=#1a73e8>作者：</font>** Yihang Wu, Yihang Sun, Shaofeng Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Transformer-based models have advanced feedforward novel view synthesis (NVS). Current architectures such as GS-LRM and LVSM mix semantic information (e.g., RGB) and spatial information (e.g., Plücker rays) into a shared feature space. Since Plücker rays naturally carry lattice-like spatial structure, these designs can make the spatial bias interfere with appearance representation and degrade rendering fidelity. To this end, we propose to decouple the representation of feedforward NVS transformers into separate semantic and spatial tokens. The decoupled design keeps semantic and spatial information explicit in their branches while preserving cross-branch interaction through shared attention routing. Built on this design, we introduce optional categorized supervision and bidirectional modulation: the former provides branch-specific training signals, while the latter improves interaction between the two branches. Notably, the base decoupled design introduces virtually zero additional inference latency due to its architectural design. The proposed designs achieve consistent improvements, demonstrating effectiveness across decoder-only and encoder-decoder feedforward NVS models.

---


### 587. [Physics-Aligned Canonical Equivariant Fourier Neural Operator under Symmetry-Induced Shifts](https://arxiv.org/abs/2605.18606)

**<font color=#1a73e8>作者：</font>** Jiaxiao Xu, Changhong Mou, Yeyu Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural operators approximate PDE solution maps, but they need not respect the symmetries of the governing equation. In out-of-distribution (OOD) regimes, a standard neural operator must often learn coordinate alignment and physical evolution within a single map, which can hurt generalization. We use known continuous symmetries of evolution equations on periodic domains to separate these two roles. We propose the Physics-Aligned Canonical Equivariant Fourier Neural Operator (PACE-FNO), which estimates the input frame with a Lie-algebra coordinate estimator, maps the field to a reference frame, applies a standard Fourier Neural Operator (FNO), and restores the prediction to the target frame. We train alignment and operator prediction jointly using bounded symmetry perturbations, with an optional low-dimensional refinement step that updates the estimated frame at inference. Equivariance is enforced by the input and output transformations, while the FNO architecture remains unchanged. Across 1-D and 2-D Burgers, shallow-water, and Navier-Stokes equations on periodic domains, PACE-FNO matches the in-distribution (ID) accuracy of standard neural operators and reduces out-of-distribution (OOD) relative error by up to 12x over FNO with symmetry augmentation (FNO+Aug) under translations and Galilean shifts, with smaller gains for coupled rotation-translation shifts. Ablations show that aligning the input and restoring the output frame account for most OOD gains; inference-time refinement provides a smaller correction.

---


### 588. [Dance Across Shifts: Forward-Facilitation Continual Test-Time Adaptation through Dynamic Style Bridging](https://arxiv.org/abs/2605.18608)

**<font color=#1a73e8>作者：</font>** Zhilin Zhu, Yabin Wang, Zhiheng Ma 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Continual Test-Time Adaptation (CTTA) aims to empower perception systems to handle dynamic distribution shifts encountered after deployment. Existing methods predominantly follow a backward-alignment paradigm, which rigidly aligns incoming data with supervisory surrogates derived from the source domain. Consequently, they struggle with unreliable supervision and evolving distribution shifts. To overcome these limitations, we introduce a novel forward-facilitation paradigm through a method termed Dynamic Style Bridging. Prior to deployment, we construct a compact knowledge base of generated class exemplars. During test time, to mitigate inherent generative bias and adapt these proxies to incoming data, we propose a multi-level bridging mechanism. This mechanism dynamically injects the proxies with incoming data styles at the input, statistical, and representation levels, while preserving the original semantics of the proxies. These high-fidelity proxies are then used to provide reliable, on-demand supervisory signals, enabling stable adaptation under continual shifts. Extensive experiments across standard CTTA benchmarks demonstrate that our method achieves consistent and substantial improvements over recent state-of-the-art approaches. Code is available at \href{this https URL}.

---


### 589. [Perfect Parallelization in Mini-Batch SGD with Classical Momentum Acceleration](https://arxiv.org/abs/2605.18609)

**<font color=#1a73e8>作者：</font>** Sachin Garg, Michał Dereziński  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accelerating stochastic gradient methods with classical momentum schemes, such as Polyak's heavy ball, has proven highly successful in training large-scale machine learning models, particularly when combined with the hardware acceleration of large mini-batch computations. Yet, the effect of classical momentum on stochastic mini-batch optimization has been poorly understood theoretically, with prior works requiring strong noise assumptions and extremely large mini-batches. In this work, we develop a general theory of stochastic momentum acceleration for optimizing over quadratics in the interpolation regime, a popular abstraction for studying deep learning dynamics which also includes classical methods such as randomized Kaczmarz and coordinate descent. Our framework encompasses both heavy ball and Nesterov-style momentum, allows for arbitrary mini-batch sizes, and makes minimal assumptions on the stochastic noise. In particular, we show that acceleration from classical momentum is directly proportional to the gradient mini-batch size (up to a natural saturation point), thereby enabling perfect parallelization of mini-batch computations. Our theory also provides a simple choice for the momentum parameter, which is shown to be effective empirically.

---


### 590. [CATA: Continual Machine Unlearning via Conflict-Averse Task Arithmetic](https://arxiv.org/abs/2605.18610)

**<font color=#1a73e8>作者：</font>** Shen Lin, Junhao Dong, Rongjie Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) have shown remarkable ability in aligning visual and textual representations, enabling a wide range of multimodal applications. However, their large-scale training data inevitably raises concerns about privacy, copyright, and undesirable content, creating a strong need for machine unlearning. While existing studies mainly focus on single-shot unlearning, practical VLM deployment often involves sequential removal requests over time, giving rise to continual machine unlearning. In this work, we make the first attempt to study continual unlearning for VLMs and identify three key challenges in this setting: effectiveness in removing target knowledge, fidelity in preserving retained model utility, and persistence in preventing knowledge re-emergence under sequential updates. To address these challenges, we propose CATA, a conflict-averse task arithmetic method that represents each forget request as an unlearning task vector. By maintaining historical task vectors and performing sign-aware conflict-averse aggregation, CATA suppresses conflicting update components that may weaken previous forgetting effects. Extensive experiments under both single-shot and continual settings show that CATA outperforms baselines in terms of forgetting effectiveness, model fidelity, and forgetting persistence.

---


### 591. [Stochastic Penalty-Barrier Methods for Constrained Machine Learning](https://arxiv.org/abs/2605.18618)

**<font color=#1a73e8>作者：</font>** Adam Bosák, Andrii Kliachkin, Jana Lepšová 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Constrained machine learning enables fairness-aware training, physics-informed neural networks, and integration of symbolic domain knowledge into statistical models. Despite its practical importance, no general method exists for the non-convex, non-smooth, stochastic setting that arises naturally in deep learning. We propose the Stochastic Penalty-Barrier Method (SPBM), which extends classical penalty and barrier methods to this setting via exponential dual averaging, a~stabilized penalty schedule, and the Moreau envelope to handle non-smoothness. Experiments across multiple settings show that SPBM matches or outperforms existing constrained optimization baselines while incurring only linear runtime overhead compared to unconstrained Adam for up to 10,000 constraints.

---


### 592. [Learning to Look Benign: Targeted Evasion of Malware Detectors via API Import Injection](https://arxiv.org/abs/2605.18624)

**<font color=#1a73e8>作者：</font>** Juozas Dautartas, Olga Kurasova, Juozapas Rokas Čypas 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Machine learning-based malware detectors are widely deployed in antivirus and endpoint detection systems, yet their reliance on static features makes them vulnerable to adversarial manipulation. This paper investigates whether a malware sample can be intentionally misclassified as a specific benign software category, not merely as "not malware", by adding a small number of Win32 API imports characteristic of that selected category, without removing any existing imports or retraining the detector. We propose a framework centered on a Conditional Variational Autoencoder (CVAE) whose decoder is strictly additive. It can introduce new API calls but never remove existing ones, preserving malware functionality by design. For each malware sample, the framework automatically identifies which benign category it most closely resembles and uses that as the evasion target. A knowledge-distilled differentiable proxy enables gradient-based training against the non-differentiable ensemble detector. Experiments on a six-class dataset of binary Win32 API import vectors extracted from 3,799 Windows executables (five benign categories, one malware class) show that, against a detector achieving 87.5% malware recall, adding just 20 API imports reduces recall to 30%. At k=20, among samples that evaded detection, 99% are classified as the intended target category. The CVAE outperforms both a frequency-based baseline and random selection at every tested injection size (k = 5 to 50). Validation on real PE files submitted to VirusTotal confirms that the attack transfers to commercial static detection engines, with an average 54.5% reduction in flagging engines. These findings expose a concrete vulnerability in API-based malware classifiers and demonstrate that targeted evasion into a chosen benign category is achievable with minimal, functionality-preserving modifications.

---


### 593. [Learning Lifted Action Models from Traces with Minimal Information About Actions and States](https://arxiv.org/abs/2605.18627)

**<font color=#1a73e8>作者：</font>** Jonas Gösgens, Niklas Jansen, Hector Geffner  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> It has been recently shown that lifted STRIPS models can be learned correctly and efficiently from action traces alone; i.e., applicable action sequences from a hidden STRIPS model. The result is remarkable because the states are not assumed to be observable at all, and yet it is not practical enough as STRIPS actions include arguments that are not needed for selecting the actions. This shortcoming has been addressed by assuming that the action traces come instead from a hidden STRIPS+ model where some action arguments are implicit in the hidden action preconditions. A limitation of this approach, however, is that it assumes that the states are fully observable. In this work, we relax these restrictions and consider the problem of learning STRIPS+ action domains from traces in a more general context where the traces carry partial information about both actions and states. In particular, we formulate algorithms and completeness results for three general cases, all of which assume full observability of selected action arguments. In the first case, no observability of the state is assumed; in the second case, full observability of some state predicates is assumed, and in the third case, local observability of some state predicates is assumed instead. Given a STRIPS+ domain, these results characterize the conditions under which an equivalent domain can be learned from traces. Experimental results are reported.

---


### 594. [Aligned Training: A Parameter-Free Method to Improve Feature Quality and Stability of Sparse Autoencoders (SAE)](https://arxiv.org/abs/2605.18629)

**<font color=#1a73e8>作者：</font>** Michał Brzozowski, Neo Christopher Chung  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse autoencoders (SAEs) are one of the main methods to interpret the inner workings of deep neural networks (DNNs), decomposing activations into higher-dimensional features. However, they exhibit critical shortcomings where a large fraction of features are never activated and are unstable. Despite variants of SAEs that attempt to mitigate these issues, they require additional data, resampling, or training. We propose the \textbf{aligned training}, a parameter-free reparameterization of SAEs that simultaneously improves reconstruction quality, eliminates dead features, and significantly enhances stability across training seeds. Our approach is motivated by an overlooked observation that SAE feature quality, measured by the inner product between encoder and decoder directions (which we call the \textbf{alignment score}), follows a bimodal distribution across all modern architectures. The proposed aligned training enforces a geometric constraint between the encoder and decoder such that their inner product equals one for every feature, which removes a source of degeneracy in the SAE training without adding any hyperparameters. Across multiple models, dictionary sizes, and sparsity levels, the aligned training shows Pareto improvements on the SAEBench benchmarks. Beyond improving dead features, stability and reconstruction, our method readily integrates with techniques in mechanical interpretability such as Top/BatchTop-K architectures and p-Annealing. Overall, the aligned training substantially improves feature quality and stability of SAE without computational complexity or cost.

---


### 595. [Position: Weight Space Should Be a First-Class Generative AI Modality](https://arxiv.org/abs/2605.18632)

**<font color=#1a73e8>作者：</font>** Zhangyang Wang, Peihao Wang, Kai Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural network checkpoints have quietly become a large-scale data resource: millions of trained weight vectors now exist, each encoding task-, domain-, and architecture-specific knowledge. This position paper argues that model checkpoints should be treated as a first-class data modality, and that generative modeling in weight space should be standardized as a core machine learning primitive. Recent advances demonstrate that neural weights can be synthesized on demand, often matching fine-tuning performance while reducing adaptation cost by orders of magnitude. We contend that these results reflect an underlying structural fact: high-performing models occupy low-dimensional, highly structured regions of weight space shaped by symmetry, flatness, modularity, and shared subspaces. Building on this view, we organize existing methods into a five-stage pipeline, survey applications where the approach is already practical, and clarify current limits: adapter-scale and conditional generation are advancing rapidly, while unrestricted frontier-scale checkpoint synthesis remains open. Our goal is to shift the community's default mindset from optimizing models per task to sampling models from learned weight distributions, accelerating toward an era in which AI systems routinely improve or create other AI systems.

---


### 596. [SPIKE: An Adaptive Dual Controller Framework for Cost-Efficient Long-Horizon Game Agents](https://arxiv.org/abs/2605.18636)

**<font color=#1a73e8>作者：</font>** Wencan Jiang, Jiangning Zhang, Jianbiao Mei 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-horizon multimodal agents in open-world games must stay goal-directed across many low-level interactions under tight token and latency budgets. Existing approaches often trade off costly per-step reasoning against reactive execution that can drift, repeat failures, and recover poorly. Our key idea is to reuse strategic reasoning across locally stable segments and reinvoke it at event boundaries. We present SPIKE, an adaptive dual controller framework for cost-efficient long-horizon game control. Its Strategic Controller performs low-frequency global planning, failure analysis, and recovery, while its Reactive Controller handles fast local execution under a strict token budget. An Event Trigger monitors visual change, task progress, repeated actions, and failure signals to decide when control should stay reactive or escalate to strategic reasoning. Hierarchical Memory separates short-term experience reuse in the State-Action Memory Bank (SA-MB) from structured evidence in the State Action Knowledge Graph (SA-KG), allowing each controller to retrieve the context it needs. This design reuses strategic proposals over multiple reactive steps, supports local override when plans become stale, and reserves expensive reasoning for moments where extra deliberation is useful. On the Lite-100 split of StarDojo, SPIKE improves Lite-100 success rate (SR) by 5.0 percentage points (38.5% relative) over the strongest Lite-100 baseline and Budgeted SR by 9.3 points (75.6% relative) over the strongest budgeted baseline. It also reduces token consumption by 54.9% and latency by 40.8%. Ablations show that event triggering, reactive override, and heterogeneous memory each contribute to success and recovery, supporting selective reasoning rather than reasoning at every step.

---


### 597. [Articulation in Prime: Primitive-Based Articulated Object Understanding from a Single Casual Video](https://arxiv.org/abs/2605.18645)

**<font color=#1a73e8>作者：</font>** Arslan Artykov, Tom Ravaud, Nicolás Violante-Grezzi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Retrieving the 3D kinematics of articulated objects from monocular video is a fundamental challenge in computer vision. Existing methods rely on complex video setups or cues such as long-term point tracking or wide-baseline matching, but are frequently brittle under severe occlusions, rapid camera ego-motion, or weak local features. Learning-based methods, meanwhile, struggle to generalize beyond their training categories. We propose a category-agnostic optimization framework that treats articulated object understanding as a primitive-fitting problem. Geometric primitives serve as a proxy representation that avoids the pitfalls of unstable point tracks; a novel mechanism organizes them into coherent parts constrained by revolute and prismatic joints. Our formulation jointly optimizes part segmentation and joint parameters, recovering complex kinematics from a single casually captured video. A visibility-aware procedure handles partial observations and occlusions inherent to real-world data. We also propose the AiP-synth and AiP-real benchmarks, featuring significant camera motion and heavy occlusions, and outperform existing methods. Project page: this https URL

---


### 598. [Federated Naive Bayes with Real Mixture of Gaussians and Institutional Governance Regularization for Network Intrusion Detection](https://arxiv.org/abs/2605.18647)

**<font color=#1a73e8>作者：</font>** Herrera Logroño, Edgar Oswaldo; López Rubio, Ezequiel 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Federated learning for intrusion detection rests on a flawed premise: that every participating institution contributes equally to the shared model. In practice, a financial institution with mature security controls and low vulnerability exposure produces fundamentally different data than a government agency running with weaker controls and higher exposure. Treating their local models as equivalent discards information that organisations already collect through standard risk management audits. Four governance indicators from the CRISC framework of ISACA, specifically control maturity (CMM), proportion of implemented controls (KCI), risk indicator activation frequency (KRI), and mean vulnerability score (CVSS), are combined here into an Institutional Coherence Index (ICC). This index enters a Nelder-Mead federated weight optimizer as a regularization prior, guiding weight assignment toward institutional quality without imposing any fixed allocation. Each node trains a hybrid local classifier combining Categorical and Gaussian Naive Bayes. The server combines local distributions as a real Mixture of Gaussians, preserving each node's statistical identity rather than collapsing it into a global parameter vector. Validation on NSL-KDD (2009), CIC-IDS2017 (2017), and UNSW-NB15 (2015), under seven Dirichlet heterogeneity levels, shows that the ICC-regularized proposal outperforms size-proportional federated averaging in all three datasets: F1-macro 0.9135 vs. 0.9076 (+0.0059), 0.7556 vs. 0.6771 (+0.0785), and 0.2110 vs. 0.2060 (+0.0050). Statistical significance holds in 70 of 94 configurations (McNemar, p < 0.05). In all three cases, the optimizer assigned the highest weight to the institutionally most mature node and the lowest to the least mature, without any explicit ordering constraint.

---


### 599. [An Assessment of Human vs. Model Uncertainty in Soft-Label Learning and Calibration](https://arxiv.org/abs/2605.18648)

**<font color=#1a73e8>作者：</font>** Maja Pavlovic, Silviu Paun, Massimo Poesio  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Central to human-aligned AI is understanding the benefits of human-elicited labels over synthetic alternatives. While human soft-labels improve calibration by capturing uncertainty, prior studies conflate these benefits with the implicit correction of mislabeled data (mode shifts), obscuring true effects of soft-labels. We present a controlled audit of soft-label learning across MNIST and a synthetic variant, re-annotating subsets to extract human uncertainty. By decoupling soft-label supervision from underlying label mode shifts, we show that while human soft-labels do provide accuracy gains, their larger value lies in acting as a regularizer that improves model calibration on difficult samples and promotes stable convergence across training runs. Dataset cartography reveals models trained on human soft-labels mirror human uncertainty, whereas those trained on synthetic labels fail to align with humans. Broadly, this work provides a diagnostic testbed for human-AI uncertainty alignment.

---


### 600. [Evaluating Multi-turn Human-AI Interaction](https://arxiv.org/abs/2605.18660)

**<font color=#1a73e8>作者：</font>** Shi Ding, Sijian Tan  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used as collaborative assistants, yet dominant NLP evaluation practices remain centered on aggregate metrics such as accuracy and fluency. These approaches often overlook behaviors that are critical in human-facing settings (e.g., consistency across multiple turns and iterative refinement). In this paper, we examine limitations of current NLP evaluation practices and introduce TCR, a structured framework for evaluating human--AI interaction using educational LLM assistants as an illustrative example. TCR emphasizes dimensions such as transparency, consistency, and refinement. We further present structured evaluation prompts and illustrative interaction examples demonstrating how structured evaluation can complement aggregate metrics and LLM-as-a-judge approaches. Our work highlights the need for more human-centered evaluation practices for interactive LLM systems.

---


> [!TIP]
> 当前位于：**551-600**（第 12/13 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | **551-600** | [601-619](./part-13.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
