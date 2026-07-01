# 📦 其他研究 | 2026年07月02日

> 本类共 **274** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-250**（第 5/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-274](./part-06.md)

---

### 201. [Preserve the Hard, Regenerate the Rest: Uncertainty-Guided Synthetic Training Data Augmentation with Diffusion Models](https://arxiv.org/abs/2606.31603)

**<font color=#1a73e8>作者：</font>** Nikolai Röhrich, Julian Gleißner, Ahmed H. A. Ibrahim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Semantic segmentation models struggle with data sparsity and rare or visually diverse regions, e.g., dense regions or small objects in aerial or autonomous mobility data. While synthetic augmentation is an appealing solution, directly generating new labeled data risks misalignment of labels and generated pixels. Existing solutions to this problem often rely on external models, or employ coarse heuristics such as indiscriminately augmenting all foreground objects or entire backgrounds, which wastes capacity on uninformative pixels. To address this, we propose an uncertainty-guided synthetic context augmentation strategy that strictly preserves label validity and efficiently maximizes pixel informativeness per synthetic sample - no external guardrails required. Using a baseline segmenter's predictive entropy, we identify uncertain semantic regions and inpaint only the complementary visual context. When fine-tuning the segmenter on this synthetic data, we compute the loss only over the original pixels, excluding inpainted regions. This focuses learning on the unmodified, uncertain regions while presenting them in novel contexts. We demonstrate substantial mIoU gains on Cityscapes, UAVID, and BDD100K with the largest gains on rare and difficult classes such as buses, trains, or (from the aerial perspective) cars. Our results demonstrate that uncertainty-guided context augmentation is a highly effective lever to improve segmentation performance on complex datasets, with code provided at this https URL.

---


### 202. [Learning Structurally Consistent Representations for Multi-View Radar Semantic Segmentation](https://arxiv.org/abs/2606.31609)

**<font color=#1a73e8>作者：</font>** Ali Zia, Muhammad Umer Ramzan, Abdelwahed Khamis 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Radar sensors provide reliable perception under adverse weather and lighting conditions, but their sparse, noisy, and weakly semantic measurements make dense semantic segmentation challenging. Most existing radar segmentation methods rely on grid-based encodings and pairwise interactions, which struggle to capture the higher-order relational structure formed by multiple radar returns from the same physical object. We introduce a unified higher-order structural alignment framework for multi-view radar segmentation. The proposed method refines radar feature representations using learnable hypergraphs to capture higher-order dependencies among spatially related responses. To ensure consistency across heterogeneous radar projections, we further align view-specific features using Unbalanced Optimal Transport (UOT), enabling correspondence-free alignment under varying measurement densities and partial observations. An adaptive attention mechanism then fuses complementary radar views while emphasising structurally informative responses under sparsity and noise. The resulting architecture learns structurally consistent representations across Range Angle (RA), Range Doppler (RD), and Angle Doppler (AD) views and is trained using supervised segmentation together with cross-view consistency regularisation. Experiments on the CARRADA and RADIal benchmarks demonstrate consistent improvements over strong radar-specific baselines, achieving 63.8% mIoU on CARRADA and 83.4% mIoU on RADIal, improving the previous best methods by +1.7 and +2.3 mIoU, respectively. These results highlight the importance of higher-order relational modelling for robust radar perception.

---


### 203. [What Memory Do GUI Agents Really Need? From Passive Records to Active Task-Driving States](https://arxiv.org/abs/2606.31612)

**<font color=#1a73e8>作者：</font>** Chen Liu, Ling Chen, Hanzhang Zhou 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Mobile GUI agents increasingly face long-horizon tasks that require reading, updating, and reusing task-relevant data across pages and applications. Existing memory methods treat memory largely as passive storage, where past observations are accumulated and retrieved when needed. Yet retrieving a value does not reveal its current role in the workflow. The agent must still infer from accumulated records whether the value should be used now, has already been used, or must wait for a later dependency. This implicit reconstruction becomes unreliable in long trajectories with similar fields, repeated values, distractors, and outdated states, causing repeated or missed operations. We propose Active Task Driving Memory (ATMem), which shifts GUI-agent memory from passive storage to an actively maintained execution state. ATMem maintains task-relevant information as a continually updated execution state that links each value to its role and current status, enabling action selection based on the current workflow state. We therefore introduce \textbf{STR-GRPO}, an online reinforcement learning method that learns to use ATMem selectively according to its contribution to task completion. STR-GRPO contrasts memory-on and memory-off rollouts to estimate when memory use improves execution, while memory-cost-aware reward discourages costly memory usage that does not improve execution. To evaluate whether agents can complete all in-scope work while avoiding out-of-scope actions over long-horizon execution, we build a challenging mobile benchmark. From a list of near identical entries, agents must act on every entry that satisfies the instruction and reject entries that violate its constraints.

---


### 204. [Scientific Explanations in Health Sciences: Causality, Trust, and Epistemic Adequacy](https://arxiv.org/abs/2606.31616)

**<font color=#1a73e8>作者：</font>** Martina Mattioli, Marcello Pelillo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Medical Artificial Intelligence (AI) is widely expected to transform clinical practice, yet the decision-making processes of many Machine Learning (ML) models remain opaque. Explainability has been advanced as a partial remedy to clarify why AI generates predictions, particularly in high-stakes contexts. Despite ongoing efforts, debates on what constitutes an adequate medical explanation remain unsettled. Yet, explanation has long been a central topic of inquiry in the philosophy of science and medicine. The insights developed in these fields, however, have been largely overlooked in contemporary explainable AI (XAI) research, leaving its foundational assumptions insufficiently examined. To address this gap, this paper develops a critical review at the intersection of philosophy of science and XAI. It examines prevailing accounts of what counts as an explanation in the health sciences and assesses their adequacy for informing XAI in medicine, arguing that they provide necessary conditions for a philosophically grounded approach to explainability in this domain. Building on this foundational philosophical literature, the discussion identifies three central axes of analysis: the role of causality in medical reasoning, the epistemic and relational dimensions of medical trust, and the criteria of explanatory adequacy as shaped by the pragmatic needs of diverse stakeholders. By integrating philosophical analysis with current developments in medical AI, the paper outlines principles for designing XAI systems that offer explanations that are not only epistemically robust but also aligned with the epistemic and practical requirements of clinical decision-making, shaping ongoing debates in medical XAI toward underexplored conceptual foundations.

---


### 205. [Hybrid Topological Data Analysis and LSTM Networks for Enhanced Network Intrusion Detection Using CIC-IDS2017 Dataset](https://arxiv.org/abs/2606.31619)

**<font color=#1a73e8>作者：</font>** Amar Jeet, Bhaskar Ranjan Karn, Dinesh Kumar  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Network intrusion detection systems (NIDS) are crucial in cybersecurity infrastructure, needing advanced techniques to detect hostile activity in network traffic. This research introduces a hybrid approach that combines Topological Data Analysis (TDA) with Long Short-Term Memory (LSTM) networks to improve anomaly detection in network security. Our multi-layered design combines TDA's persistent homology with LSTM networks to capture topological characteristics of network traffic patterns and simulate temporal sequences. We assessed our methodology using the CIC-IDS2017 dataset, which includes over 2.8 million labelled flows, 77 network variables, and 14 attack categories that reflect modern threat landscapes such as DDoS, brute force, web attacks, penetration, and botnet activities. Integrating Betti curves and persistence diagrams with deep learning architectures enhances feature extraction performance. Our hybrid TDA+LSTM model has an AUC of 1.000 and F1-score of 1.000, with 5-fold cross-validation producing a mean AUC of 1.000 $\pm$ 0.000 and mean F1 of 0.999 $\pm$ 0.001. An ablation research demonstrates the complimentary contributions of topological (F1=0.990) and temporal characteristics (F1=1.000). Comparative research shows that the suggested strategy beats TDA+Random Forest (F1=0.994) and Isolation Forest (F1=0.835) baselines in several attack categories.

---


### 206. [PrISM-IQA: Image Quality Assessment Made Practical for Smartphone Photography](https://arxiv.org/abs/2606.31626)

**<font color=#1a73e8>作者：</font>** Shuyan Zhai, Jiaqi He, Weixia Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing smartphone image quality assessment (IQA) methods commonly reduce perceptual quality to a single score. However, this scalar formulation is poorly aligned with practical image signal processor (ISP) tuning, where engineers must identify specific quality issues, estimate their severities, and determine whether they are acceptable or require intervention. In this work, we introduce a Practical ISP-aware Structured Model for IQA (PrISM-IQA), which reformulates smartphone IQA as a multi-issue ordinal diagnosis problem. Rather than regressing a single quality score, PrISM-IQA predicts an \textit{ordered} severity level -- absent, minor, severe, or critical -- for each ISP-relevant issue, covering both global image-level artifacts and local content-dependent defects. To produce logically consistent predictions, PrISM-IQA combines cumulative ordinal encoding with structured inference that captures within-issue monotonicity as well as cross-issue subsumption and exclusion relations. We evaluate PrISM-IQA on a reconstructed SPAQ benchmark annotated with $53$ ISP-relevant quality issues and on a small-scale expert-annotated real-world dataset. Experimental results demonstrate the effectiveness of PrISM-IQA for practical issue-level diagnosis, reveal transferable perceptual quality representations through linear probing, and further show how its predictions can support actionable and meaningful ISP tuning.

---


### 207. [LiteMatch: Lightweight Zero-Shot Stereo Matching via Cost Volume Stabilization](https://arxiv.org/abs/2606.31636)

**<font color=#1a73e8>作者：</font>** Md Raqib Khan, Santosh Kumar Vipparthi, Subrahmanyam Murala  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite rapid progress in learning-based stereo matching, high accuracy is often achieved at the cost of heavy backbones and computationally intensive 3D cost volume processing, resulting in substantial memory and runtime overhead. More critically, these methods frequently struggle to generalize across domains, limiting their practical deployment. We present \textit{LiteMatch}, a lightweight stereo matching framework that achieves strong zero-shot generalization through cost volume stabilization-without expensive 3D convolutions. LiteMatch employs two complementary encoders: a Cross-View Correspondence Encoder (CVCE) to capture global cross-view interactions, and a High-Frequency Encoder (HFE) that enhances fine structural details via FFT-based frequency cues. To stabilize the cost volume, we introduce the \textit{Cost Volume Consistency Loss (CVC-Loss)}, a voxel-wise binary cross-entropy objective applied to softmax-normalized cost distributions. By encouraging sharp and unimodal disparity probabilities, CVC-Loss promotes stable cost distributions and enables rapid convergence. A lightweight refinement module further produces sharp full-resolution disparities with low-iteration updates, avoiding heavy recurrent refinement. With a flexible design ranging from 3.36M to 9.58M parameters, LiteMatch achieves exceptional zero-shot generalization, delivering competitive EPE and D1 performance across Scene Flow, KITTI, Middlebury, ETH3D, and DrivingStereo. Our results establish that lightweight architectures can indeed generalize across domains without sacrificing accuracy. \href{this https URL}{\textcolor{blue}{Code}}

---


### 208. [Tone-Conditioned Curriculum Learning for Low-Resource Bantu Speech Recognition](https://arxiv.org/abs/2606.31642)

**<font color=#1a73e8>作者：</font>** Kesego Mokgosi, Vukosi Marivate, Sitwala Mundia 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Southern Bantu languages are spoken by over 80 million people, yet current foundation ASR models still produce zero-shot WER above 100%, which limits practical use in education and public services. We addressed this gap with a tone conditioned curriculum framework for 6 Southern Bantu languages that combined hybrid difficulty scoring, gated adapters driven by tonal statistics and staged curriculum training. We trained on a community corpus and tested transfer to NCHLT to measure robustness beyond matched evaluation. Results revealed clear interactions between architecture and language, with W2V-BERT outperforming Whisper on Nguni languages by 3 to 4 WER points whilst Whisper performed better on Sotho-Tswana languages. W2V-BERT with tone conditioning reached 28.41% average WER across datasets and 23.79% on Xitsonga transfer. No single model suited all 6 languages, so deployment should pair model selection per language with validation across corpora.

---


### 209. [Technical Report of RoboSpatial Challenge at CVPR 2026: Selective Reasoning Activation and Reference-Frame Disambiguation for Embodied Spatial Reasoning](https://arxiv.org/abs/2606.31645)

**<font color=#1a73e8>作者：</font>** Yuxiang Xie, Qi Lv, Jianming Xing 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models achieve strong general perception but often struggle with the spatial reasoning required for embodied tasks. We present RoboSpatialBrain, our submission to the RoboSpatial Challenge at the Embodied Reasoning in Action Workshop, CVPR 2026, built on RoboBrain2.5-8B-NV. RoboSpatialBrain combines two training-free, inference-time mechanisms: a forced <think> prefix activation strategy paired with a task-specific post-prompt that elicits deliberate reasoning on context and compatibility tasks, and an explicit reference-frame redirection pipeline that resolves camera-centric and object-centric ambiguity for context tasks. We additionally explore fine-tuning RoboBrain2.5 on compatibility data and present a detailed analysis of its interaction with prompting. RoboSpatialBrain achieved first place in the RoboSpatial Challenge, with an overall success rate of 80.9\% on RoboSpatial-Home. Code is available at this https URL.

---


### 210. [FARS: A Fully Automated Research System Deployed at Scale](https://arxiv.org/abs/2606.31651)

**<font color=#1a73e8>作者：</font>** Qiong Tang, Xiangkun Hu, Xiangyang Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent automated research systems show that language-model agents can generate hypotheses, run experiments, and write complete manuscripts, but most evidence still comes from selected examples, human-framed topics, or a few pre-defined research tasks. We present FARS (Fully Automated Research System), a fully automated AI-for-AI research system designed to operate across research topics at scale. FARS autonomously generates and advances projects through ideation, planning, experimentation, and writing, using stage-specific agents coordinated through a shared workspace that records proposals, code, logs, results, and manuscripts. In its first public deployment, FARS produced 166 complete research papers spanning 67 fine-grained AI/ML topics while preserving intermediate artifacts as an auditable corpus rather than a curated set of successes. We evaluate this corpus with 282 structured reviews from volunteer reviewers covering 140 papers, including overall ratings, sub-scores, integrity checks, and LLM-use disclosure. The reviews indicate that FARS can produce review-worthy and occasionally strong AI/ML research artifacts in a large-scale public deployment, while also exposing recurring failure modes in narrow experimental scope, methodological limitations, and integrity issues.

---


### 211. [Improving Certified Robustness via Adversarial Distillation](https://arxiv.org/abs/2606.31653)

**<font color=#1a73e8>作者：</font>** Matteo Melis, Jesus Martinez Del Rincon, Vishal Sharma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Certified training aims to produce models whose predictions can be formally verified against adversarial perturbations, typically by optimising upper bounds on the worst-case loss over an allowed perturbation set. For neural networks, certified training methods based purely on tight relaxation bounds produce networks that are amenable to certification, but sacrifice standard accuracy. Conversely, adversarial training often yields stronger empirical robustness and standard accuracy, but the resulting models are generally difficult to certify with neural network verifiers. Recently, the literature has shown that better standard-certified accuracy trade-offs can be achieved by combining adversarial training objectives with loose over-approximations based on Interval Bound Propagation (IBP), effectively interpolating between lower and upper bounds of the worst-case loss. Building on this, we introduce AD-CERT, a certified training objective that combines adversarial distillation with an IBP upper bound. We show that distilling adversarial information over the logit space from an empirically robust teacher provides an effective lower bound surrogate for certified training, with AD-CERT achieving state-of-the-art certified performance on several robustness benchmarks. Furthermore, in a unified setup, distilling adversarial information at the logit-level is shown to improve certified accuracy over a robust feature-space distillation objective by up to 5.40 percentage points.

---


### 212. [Sparsity-Inducing Divergence Losses for Biometric Verification](https://arxiv.org/abs/2606.31664)

**<font color=#1a73e8>作者：</font>** Dimitrios Koutsianos, Ladislav Mošner, Yannis Panagakis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Performance in face and speaker verification is largely driven by margin-penalty softmax losses such as CosFace and ArcFace. Recently introduced $\alpha$-divergence loss functions offer a compelling alternative, particularly due to their ability to induce sparse solutions (when $\alpha>1$). However, standard geometric margins are designed for the softmax function and do not naturally extend to this generalized probabilistic framework. In this paper we propose Q-Margin, a novel $\alpha$-divergence loss that introduces a principled probabilistic margin. Unlike conventional methods that apply geometric penalties to the logits (unnormalized log-likelihoods), Q-Margin encodes the margin penalty directly into the reference measure (prior probabilities). This formulation naturally encourages discriminative embeddings while preserving the beneficial sparsity properties of the $\alpha$-divergence. We demonstrate that Q-Margin achieves competitive or superior performance on the challenging IJB-B and IJB-C face verification benchmarks and similarly strong results in speaker verification on VoxCeleb. Crucially, against ArcFace and CosFace baselines trained under an identical recipe, Q-Margin consistently improves at low False Acceptance Rates (FARs), a capability critical for practical high-security applications. Finally, the extreme sparsity of the Q-Margin posteriors enables exact and memory-efficient training, offering a scalable solution for datasets with millions of identities.

---


### 213. [ForecastAgentSearch: Towards a Multi-Expert Agent Search System for Geopolitical Event Forecasting](https://arxiv.org/abs/2606.31665)

**<font color=#1a73e8>作者：</font>** Miaomiao Cai, He Chang, Yunshan Ma 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Geopolitical event forecasting is a challenging task, as it requires understanding complex regional contexts, dynamic event signals, and uncertain future outcomes. Recent advances in large language model agents provide new opportunities for building forecasting systems that can reason with diverse sources and expert perspectives. In this paper, we present \textit{ForecastAgentSearch}, a preliminary framework that formulates geopolitical event forecasting as a multi-expert agent search problem. Given a forecasting query, the system first analyzes the task context, then searches and ranks relevant expert agents based on their regional knowledge, domain expertise, reliability, and complementarity. The selected agents provide specialized analyses, which are further coordinated to generate a final forecast with explanations and uncertainty awareness. We discuss the key design challenges of agent profiling, expert retrieval, ranking, and multi-agent coordination, and outline possible evaluation protocols for future development. This work aims to provide an initial step toward searchable and reliable agent-based forecasting systems.

---


### 214. [REDI: Corpus Aware Patch Ranking for DINOv3 Token Reduction](https://arxiv.org/abs/2606.31676)

**<font color=#1a73e8>作者：</font>** Chanjong Im, Sebastian Diem, Thomas Mandl  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Most token reduction methods for Vision Transformers seek favorable tradeoffs between accuracy and efficiency by pruning, merging, or pooling patch tokens. REDI (Relevance for DINOv3 Token Reduction) studies this question through a controlled supervised reference: how should a fixed token budget be allocated across patches for image classification? REDI quantizes final block DINOv3 patch representations into a visual vocabulary and derives class conditioned corpus scores using supervised TF-IDF over visual words. For each validation image, the ground truth class selects a row of the TF-IDF table, and four transformed views produce a TF-IDF map aligned to a reference center crop. A separate dense pass on the same crop provides an attention map. After independent min max normalization, their elementwise product defines the REDI score. A fixed keep, merge, and compress operator then uses score rank to assign patch roles and score magnitude to weight merging and compression.
With precomputed REDI scores, a frozen DINOv3 ViT-B/16 backbone, and the same linear classifier used for dense evaluation, the operator reduces the sequence length from 201 to 107 tokens, a 46.8% sequence reduction. The REDI variant based on incoming attention mass achieves 84.706% Top-1 accuracy on ImageNet-1K, compared with 83.514% for the dense baseline, 82.634% for incoming attention mass alone, and 81.796% for supervised TF-IDF alone. The same corpus term also improves reduced classification for three alternative attention formulations relative to their attention only counterparts. Together, these controlled comparisons indicate that class specific corpus statistics and image specific attention provide complementary signals for patch ranking in this setting.

---


### 215. [Exploring Side-Channel Protections in Hardware Implementations of PQC ML-KEM Verification](https://arxiv.org/abs/2606.31681)

**<font color=#1a73e8>作者：</font>** Davis Ranney, Yashaswini I Makaram, A. Adam Ding 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As ML-KEM is adopted as a post-quantum cryptographic standard, resilience against physical side-channel attacks has become essential. Among the constituent steps, the decapsulation Fujisaki-Okamoto (FO) verification is particularly vulnerable to side-channel power and electromagnetic (EM) analysis. In this work, we focus on common FPGA-based implementations and examine their side-channel vulnerabilities, and compare them with those of microcontroller implementations. Three verification implementations, unprotected, hash-based (first-order), and higher-order masked, are evaluated for side-channel security on both a microcontroller and an FPGA. While FPGAs offer higher speed and parallelism, they often exhibit stronger side-channel leakage, especially in high bandwidth configurations. The higher-order masked designs still leak information about the underlying data due to hardware-level effects and data-dependent processing. Our experiments show that their parallelized processing on FPGAs introduces sufficient first-order leakage for full secret-key recovery. These results underscore the persistent challenge of securing PQC algorithms in performance-constrained and parallelized hardware environments.

---


### 216. [Histogram-constrained Image Generation](https://arxiv.org/abs/2606.31683)

**<font color=#1a73e8>作者：</font>** Haoming Liu, Yuanhe Guo, Yijia Cao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models have emerged as a dominant paradigm in generative modeling, enabling high-fidelity sampling from complex data distributions. Despite impressive capabilities, controlling diffusion models to produce outputs aligned with user intent remains an open challenge, especially when balancing global coherence with local precision. Existing control mechanisms vary in the granularity of their conditioning signals. For example, textual prompts guide generation globally through high-level semantics, while ControlNet-like approaches secure precise local structure via dense conditions. In this work, we introduce Histogram-constrained Image Generation (HIG), a novel control mechanism that falls into the middle ground of control granularity. Our framework enforces user-specified distributional constraints (e.g., color histograms or latent token distributions) during the generation process with exact precision. We model such control as an optimal transport (OT) problem and apply explicit guidance transformations during sampling, thereby driving the diffusion trajectory to align with the desired histogram. We demonstrate the versatility of HIG across diverse applications, including constrained generation via color/latent histograms and high-capacity information embedding through histogram-level encoding. Our findings underscore the promise of distributional control, a flexible and interpretable control scheme that is fully compatible with existing control mechanisms, diversifying the hybrid strategies for controllable image generation. Our project page is available at: this https URL.

---


### 217. [When to Truncate a Feature Ranking: A Residual-Overlap Stopping Rule for Subset Selection](https://arxiv.org/abs/2606.31686)

**<font color=#1a73e8>作者：</font>** Jesus S. Aguilar-Ruiz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Feature rankings are widely used in supervised feature selection because they are simple, scalable and easy to interpret. Variables are first ranked by a relevance score, and a subset is then obtained by retaining the top-ranked variables. Although the first stage has been extensively studied, the second is often governed by an arbitrary cardinality, an empirical threshold or cross-validation, without a direct interpretation. This raises a basic question: given a feature ranking, when is there enough accumulated class-separation evidence to stop selecting features?
This paper develops a distributional framework for transforming supervised feature rankings into class-independent subsets through an explicit risk-calibrated stopping rule. For each variable and each pair of classes, marginal separation is measured by the Bhattacharyya coefficient between the corresponding class-conditional distributions. The proposed method selects a single global subset shared by all classes by retaining the shortest prefix of a ranking whose residual product overlap falls below a prescribed threshold for every relevant class contrast. We derive binary and multiclass Bayes-risk bounds for the labelled product marginal problem, and obtain prior-dependent and prior-free calibrations of the residual-overlap threshold from a target all-pairs risk level.
An empirical comparison on high-dimensional genomic datasets illustrates that the rule can reduce tens of thousands of variables to a few dozen while maintaining predictive performance statistically comparable to the all-features baseline. As the stopping rule only requires one-dimensional marginal overlap estimates and scans a precomputed ranking, it is well suited to very high-dimensional settings where exhaustive subset search is infeasible and interpretable truncation of feature rankings is essential.

---


### 218. [Semantic Occupancy Prediction with Dual Range-Voxel Representation](https://arxiv.org/abs/2606.31688)

**<font color=#1a73e8>作者：</font>** Sitao Chen, Zhuangwei Zhuang, Hui Luo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> LiDAR-based 3D semantic occupancy prediction, which aims to provide accurate and comprehensive scene representation, is crucial for autonomous driving systems. As point clouds suffer from sparsity and incompleteness, leading to insufficient semantic learning and difficult occupancy perception, existing methods often stack multi-sweep point clouds to obtain dense spatial information. However, such a naive strategy also results in efficiency (e.g., additional computational burden) and robustness (e.g., pose transformation noise) concerns, which hinder their practical applications. In this work, we propose a Dual Range-Voxel Representation (DRVR) that leverages the range-view context and voxel-view geometry of single-sweep point clouds for 3D semantic occupancy prediction, eliminating the concerns associated with the multi-sweeps. Specifically, we use the range-view encoder to extract the compact context of the scene. To fully exploit the spatial information, we design a geometry-aware voxel-view encoder that extracts multi-scale voxel-view features separately and combines them for better geometric occupancy prediction. Moreover, we propose a range-voxel fusion module to cooperate range- and voxel-view features via voxel-to-range and range-to-voxel fusions. Extensive experiments on nuScenes-Occupancy, SemanticKITTI and SemanticPOSS show the superiority of our method. Especially on nuScenes-Occupancy, our single-sweep DRVR achieves 5.4% improvement in mIoU and 2.1x acceleration compared to the multi-sweep method.

---


### 219. [Overview of the TalentCLEF 2026: Skill and Job Title Intelligence for Human Capital Management](https://arxiv.org/abs/2606.31692)

**<font color=#1a73e8>作者：</font>** Luis Gasco, Hermenegildo Fabregat, Laura García-Sardiña 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper presents an overview of the second edition of the TalentCLEF challenge, organized as a Lab at the Conference and Labs of the Evaluation Forum (CLEF) 2026. TalentCLEF is an initiative aimed at advancing Natural Language Processing research in Human Capital Management. The second edition of the challenge consisted of two tasks: Task A, contextualized job-person matching, focuses on identifying and ranking the most suitable candidates represented by their resumes for a given job vacancy in English and Spanish. Task B, job-skill matching with skill type classification, addresses retrieving the most relevant skills for a given job title in English and distinguishing between core and contextual skills. TalentCLEF attracted 113 registered teams and received more than 400 submissions in the two tasks, reflecting the growing interest of the research community in shared evaluation benchmarks for Human Capital Management. This paper describes the motivation and organization of the challenge, summarizes the datasets and evaluation settings, and reports the main results obtained by the participating teams.

---


### 220. [Intrinsically Stable Spiking Neural Networks: Overcoming the Performance Barrier in the Absence of Batch Normalization](https://arxiv.org/abs/2606.31695)

**<font color=#1a73e8>作者：</font>** Ruichen Ma, Xiaoyang Zhang, Jian Bai 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The performance of deep spiking neural networks (SNNs) often relies on batch normalization (BN). However, the advanced dynamic BN variants used in state-of-the-art models introduce runtime multiplications, which weaken the hardware-efficiency motivation of SNNs. To address this tension, we identify catastrophic firing-rate decay as a primary cause of severe performance degradation in normalization-free SNNs. Guided by this insight, this work proposes the Intrinsically Stable SNN (IS-SNN) architecture, which removes activation-normalization layers by enforcing signal homeostasis through topology-aware weight standardization and modified residual connections. By folding the standardization operations into static weights offline, IS-SNN removes the runtime statistics tracking and multiplications introduced by activation normalization, restoring an accumulation-oriented inference datapath. Comprehensive experiments show that IS-SNN achieves performance competitive with or superior to computationally expensive dynamic BN techniques across VGG, ResNet, and Transformer-based models. Notably, it achieves a competitive accuracy of 68.05\% on ImageNet and overcomes the severe depth limitations of prior BN-free attempts. Together with a 96.4\% reduction in FPGA lookup table resource consumption for neuron implementations, these results support IS-SNN as a practical framework for building accurate and hardware-friendly deep neuromorphic systems.

---


### 221. [Look But Don't Touch with Sparse Autoencoders for Unlearning in Diffusion Models](https://arxiv.org/abs/2606.31699)

**<font color=#1a73e8>作者：</font>** Enrico Cassano, Riccardo Renzulli, Rayyan Ahmed 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sparse autoencoders (SAEs) have recently been proposed as interpretable tools for concept-level manipulation, under the assumption that isolated features can serve as controllable intervention points. In this work, we systematically evaluate this assumption in the context of object erasure and steering in diffusion models. We show that while SAEs reliably detect and localize semantic concepts within diffusion model activations, direct intervention in their latent space frequently induces out-of-distribution activations, resulting in severe visual artifacts. To disentangle detection from intervention, we use SAE activations purely as semantic detectors to identify image regions containing the target object, and replace those patch embeddings with the ones that do not contain it. This detection-based replacement preserves the diffusion model's activation statistics and produces significantly cleaner erasure results than latent steering. Our findings reveal a fundamental gap between concept detection and concept intervention in diffusion models: monosemantic or sparse features are not inherently suitable as control knobs for steering. These results position SAEs as powerful interpretability tools for analyzing generative models, but highlight important limitations when used for direct manipulation, such as unlearning.

---


### 222. [Diffusing Blame: Task-Dependent Credit Assignment in Biologically Plausible Dual-Stream Networks](https://arxiv.org/abs/2606.31700)

**<font color=#1a73e8>作者：</font>** Yutaro Yamada, Luca Grillotti, Rujikorn Charakorn 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Biological neural circuits obey Dale's principle: each neuron's synapses are uniformly excitatory or inhibitory. Artificial networks that respect this constraint must coordinate separate excitatory and inhibitory populations, fundamentally changing how credit is assigned during learning. Several biologically plausible learning rules avoid backpropagation's weight transport requirement, but it has been difficult to achieve strong performance under Dale's principle beyond MNIST. Error Diffusion (ED) was originally proposed in a dual-stream excitatory/inhibitory architecture, where learning is driven by routing global error signals to all layers without transporting transposed forward weights or relying on random feedback matrices. Whether such a rule can scale under Dale's principle across both supervised classification and reinforcement learning remains unknown. Here, we introduce modulo error routing to extend Error Diffusion beyond binary classification, and show that a dual-stream excitatory/inhibitory architecture trained with this method achieves 96.7% on MNIST and establishes a 61.7% baseline on CIFAR-10, demonstrating that representation learning is possible even when strictly enforcing Dale's principle. For the classification setting, we introduce three domain-specific innovations: layer-specific sigmoid widths, batch-centered class error signals, and asymmetric initialization, and ablation analysis reveals that their relative importance reverses between MNIST and CIFAR-10, exposing task-dependent credit-assignment bottlenecks invisible to single-benchmark evaluation. In reinforcement learning, we integrate ED with Proximal Policy Optimization (PPO) and evaluate it on continuous-control tasks in Google Brax and on Craftax, an open-ended exploration task. We show that ED-PPO achieves competitive performance relative to Direct Feedback Alignment, a backpropagation-free baseline.

---


### 223. [Phantom: A Unified Face-Swap Deepfake Protection Framework with Latent and Spatial Constraints](https://arxiv.org/abs/2606.31703)

**<font color=#1a73e8>作者：</font>** Jungkon Kim, Cheolseung Jung, Jong-Min Choi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Face-swapping deepfakes pose an escalating threat to personal privacy by enabling unauthorized identity manipulation. While adversarial approaches have demonstrated success against black-box face recognition (FR) models, their applicability to face-swapping scenarios remains underexplored. In particular, reliance on fixed or random targets yields ambiguous latent guidance, and the lack of explicit spatial constraints causes perturbations to spill into identity-irrelevant regions. These issues are further exacerbated by identity-style disentanglement, which suppresses adversarial signals during deepfake generation. In this paper, we present Phantom, a unified face-swap deepfake protection framework that jointly constrains perturbations in latent and spatial domains. Phantom adaptively synthesizes identity-shifted yet attribute-preserving targets to guide identity-aware latent optimization, and applies masked perturbations confined to semantically relevant facial regions. Extensive experiments on state-of-the-art face-swapping deepfakes demonstrate that Phantom improves protection success rates in dodging scenarios by 27.8%, 25.6%, and 16.6% on UniFace, INSwapper, and SimSwap, respectively, while also enhancing visual quality. Furthermore, Phantom generalizes to impersonation scenario, yielding up to 10.2% higher protection while improving perceptual fidelity. These results underscore the effectiveness of jointly leveraging latent and spatial constraints for robust and coherent facial privacy protection.

---


### 224. [WIDER-FAIR: An Annotated Version of the WIDER-FACE Dataset for Fairness Evaluation](https://arxiv.org/abs/2606.31704)

**<font color=#1a73e8>作者：</font>** Maxime Moussi, Benoît Ronval, Siegfried Nijssen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The deployment of face detection models in real-world applications raises important fairness concerns, as these systems may showcase performance disparities across demographic groups. A key obstacle to studying and mitigating such biases is the lack of face detection datasets with sensitive feature annotations. To address this gap, we introduce WIDER-FAIR, a new dataset built on the widely used WIDER-FACE benchmark, manually annotated with the perceived ethnicity and sex of each face. The dataset contains 16,256 images annotated across four ethnic groups: Asian, Black, Indian, and White, and two sex categories. We assess the quality and coherence of the annotations using face embeddings, a K-Nearest Neighbors classifier, and a t-SNE visualization, all of which support the consistency of the labeling process. As a demonstration of the dataset's potential, we train a YOLOv5 model and perform ablation studies on each sensitive feature. Among other findings, our experiments show that detection performance is notably lower for faces of Black individuals, and that excluding this group from training increases fairness disparity more than excluding any other ethnic group. These observations illustrate the value of demographically annotated datasets for understanding and evaluating bias in face detection models.

---


### 225. [Arena-T2I Hard: Benchmarking and Improving Faithfulness with Dependency-Aware Checklist](https://arxiv.org/abs/2606.31711)

**<font color=#1a73e8>作者：</font>** Yuanhao Ban, Tong Xie, Sohyun An 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Faithfulness -- how precisely a generated image aligns with its prompt -- is increasingly central to the real-world utility of text-to-image (T2I) models. Existing faithfulness benchmarks, however, rely on simple atomic instructions, on which top-tier systems already achieve near-perfect scores. As T2I models enter creative workflows, users issue multi-faceted requests combining intricate spatial relationships, stylistic constraints, and complex text rendering. In this setting, a single binary VLM-judge score no longer captures which specific constraints the model fails to satisfy. We introduce Arena-T2I Hard, a 310-prompt stress benchmark drawn from real arena T2I logs, with approximately 30 decomposed yes/no constraints per prompt spanning six categories, including text rendering. The strongest closed-source system we evaluate reaches 0.855 with a 33~pp performance gap across 11 systems, demonstrating substantial discriminative power. Moreover, high public-arena rankings fail to predict faithfulness, confirming that holistic Bradley-Terry (BT) preference scores prioritize aesthetics over fine-grained prompt adherence. We propose a dependency-aware checklist reward that decomposes each prompt into a DAG of yes/no questions and zeroes descendants of failed parents, turning faithfulness into a per-constraint training signal. Combined with a BT aesthetic reward via group-decoupled normalization (GDPO), which standardizes each reward within its rollout group so neither collapses, the recipe attains a strictly better faithfulness-aesthetics trade-off on SD3.5-Medium and FLUX.1-dev under MMRB2 pairwise comparisons than every single-reward, naive weighted-sum, or 4-reward BT-ensemble baseline.

---


### 226. [Nonlinearity-Aware LoRA: Structured Gate Adaptation under Low-Rank Constraints](https://arxiv.org/abs/2606.31717)

**<font color=#1a73e8>作者：</font>** Shuai Yuan, Sudong Cai, Bingzhi Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-rank adaptation (LoRA) is commonly viewed as an update-space approximation to full fine-tuning, yet this view is incomplete for self-gated Transformer feed-forward networks. In gated FFNs, a low-rank residual can change not only projected features but also the nonlinear selection weights that determine which channels contribute to the output. We formalize this effect as selection misalignment and connect it to the local effective homogeneity of self-gated activations. This motivates a nonlinearity-aware principle for parameter-efficient fine-tuning: low-rank updates should allocate capacity to gate channels whose nonlinear states remain responsive and should shape the temporal evolution of selection. We propose NA-LoRA, a training-only method with two lightweight mechanisms: a derivative-based temporal-importance mask for gate-related LoRA updates and an activation-specific step-scaling rule when a meaningful coarse effective-homogeneity partition is available. NA-LoRA adds no auxiliary loss and incurs no inference-time overhead. Experiments on language-model fine-tuning and vision-language transfer benchmarks show that NA-LoRA consistently improves over vanilla LoRA and is competitive with or better than strong PEFT variants.

---


### 227. [Adapting Foundation ASR Models to Dysarthric Speech: A Case Study](https://arxiv.org/abs/2606.31722)

**<font color=#1a73e8>作者：</font>** Christian Huber, Laura Kernahan, Alexander Waibel  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic speech recognition (ASR) systems often perform poorly in dysarthric speech, limiting their usefulness to affected speakers in everyday communication. This paper presents a personalized ASR system for a dysarthric speaker, built by adapting a foundation ASR model to speaker-specific data. Using the TEQST tool, we collected 92 hours of read speech and later added 8.8 hours of user corrections gathered through a deployed mobile application. Starting from Whisper, fine-tuning reduced word error rate to 15.8% with only 1.4 hours of adaptation data, reached 10.7% with 22.5 hours, and achieved the best result of 9.7% when using all available data including the corrections. Using LoRA adaptation and/or Qwen3-ASR as foundation model performed worse in this setting. The results show that personalized fine-tuning can make foundation ASR models substantially more effective for dysarthric speech and suitable for practical deployment.

---


### 228. [Rhythm-Structured Predictive Learning for Remote Photoplethysmography](https://arxiv.org/abs/2606.31736)

**<font color=#1a73e8>作者：</font>** Ba-Thinh Nguyen, Huu-Dung Nguyen, Thi-Duyen Ngo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remote photoplethysmography (rPPG) estimates physiological signals from facial videos by analyzing subtle pulse induced skin color variations. Despite recent progress, existing self-supervised rPPG methods mainly reconstruct masked pixels or low-level visual representations, which can bias the model toward facial appearance rather than latent physiological dy namics. Moreover, most recent Mamba-based approaches scan facial video tokens only in chronological order, limiting their ability to exploit the cyclic structure of pulse signals. To ad dress these limitations, we propose RhythmJEPA, a rhythm structured joint-embedding predictive learning framework for rPPG. Instead of reconstructing RGB frames, RhythmJEPA predicts latent teacher representations from masked facial videos, thereby encouraging physiology-aware representation learning in the embedding space. To explicitly model pulse-related tem poral structure, we introduce a Cyclic Rhythm-State Plan ner (CRSP), which estimates frame-wise latent physiological states and decodes the most plausible cyclic state path via dynamic programming with a constrained transition grammar. Guided by the decoded states, we further design a Dual Order Mamba Encoder (DOM), which combines conventional chronological scanning with state-ordered scanning to capture both local temporal continuity and long-range rhythm-consistent dependencies. Finally, a lightweight Spatial Pulse Mixer (SPM) extracts compact pulse-sensitive facial tokens with a favorable balance between complexity and performance. Experiments on PURE, UBFC-rPPG, and MMPD show competitive performance over representative rPPG methods. The codes are available at this https URL.

---


### 229. [STEB: Style Text Embedding Benchmark](https://arxiv.org/abs/2606.31741)

**<font color=#1a73e8>作者：</font>** Rafael Rivera Soto, Anna Wegmann, Cristina Aggazzotti  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While semantic embeddings are rigorously evaluated on the Massive Text Embedding Benchmark, the evaluation of style embeddings remains fragmented, with each work relying on their own set of tasks and datasets. To bridge this gap, we introduce the Style Text Embedding Benchmark, a comprehensive open-source benchmark intended to standardize the evaluation of style embeddings. STEB encompasses 96 datasets across 7 languages, spanning applications such as authorship verification, authorship retrieval, AI-text detection, probing of linguistic features, and others. We find that semantic embeddings consistently fail in stylistic tasks, and that there is no style embedding that is universally superior across all tasks evaluated. We open-source the STEB code base at: this https URL.

---


### 230. [FedXDS: Leveraging Model Attribution Methods to counteract Data Heterogeneity in Federated Learning](https://arxiv.org/abs/2606.31742)

**<font color=#1a73e8>作者：</font>** Maximilian Andreas Hoefler, Karsten Mueller, Wojciech Samek  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Explainable AI (XAI) methods have demonstrated significant success in recent years at identifying relevant features in input data that drive deep learning model decisions, enhancing interpretability for users. However, the potential of XAI beyond providing model transparency has remained largely unexplored in adjacent machine learning domains. In this paper, we show for the first time how XAI can be utilized in the context of federated learning. Specifically, while federated learning enables collaborative model training without raw data sharing, it suffers from performance degradation when client data distributions exhibit statistical heterogeneity. We introduce FedXDS (Federated Learning via XAI-guided Data Sharing), the first approach to utilize feature attribution techniques to identify precisely which data elements should be selectively shared between clients to mitigate heterogeneity. By employing propagation-based attribution, our method identifies task-relevant features through a single backward pass, enabling selective data sharing that aligns client contributions. To protect sensitive information, we incorporate metric privacy techniques that provide formal privacy guarantees while preserving utility. Experimental results demonstrate that our approach consistently achieves higher accuracy and faster convergence compared to existing methods across varying client numbers and heterogeneity settings. We provide theoretical privacy guarantees and empirically demonstrate robustness against both membership inference and feature inversion attacks. Code is available at this https URL.

---


### 231. [JL1-CC&QA: Extending the JL1-CD Benchmark with Change Captioning and Question Answering](https://arxiv.org/abs/2606.31745)

**<font color=#1a73e8>作者：</font>** Ziyuan Liu, Ruifei Zhu, Ouqiao Ma 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remote sensing change detection (CD) traditionally focuses on pixel-level binary segmentation, which identifies where changes occur but neither what nor why. To bridge this semantic gap, we introduce JL1-CC&QA, a multi-task benchmark that extends the JL1-CD dataset with two complementary annotation layers: change captioning (CC) and change question answering (QA). Built upon 5,000 bi-temporal image pairs acquired by the Jilin-1 satellite at 0.5-0.75m ground sample distance, the benchmark comprises: (i) JL1-CC, providing 17,021 quality-verified captions that describe diverse land-cover transformations; and (ii) JL1-QA, offering 20,060 question-answer pairs across eight question types, enabling fine-grained, interactive interrogation of surface changes. All annotations are produced via a three-stage pipeline consisting of multi-modal large language model (LLM) generation, vision-grounded LLM judging, and human expert verification. We hope that JL1-CC&QA, as a benchmark unifying binary change masks, change captions, and change-oriented QA over the same image set, will serve as a valuable resource for the community to advance multi-task change understanding in remote sensing. The dataset is available at this https URL.

---


### 232. [Estimating Velocity of Spheres from Rolling-Shutter Image(s)](https://arxiv.org/abs/2606.31760)

**<font color=#1a73e8>作者：</font>** Wenjie Xue, Jun Yang, Jingmin Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Rolling-shutter cameras introduce characteristic distortions when imaging fast moving objects, and these effects are typically treated as artifacts to be corrected. In this work, we instead leverage rolling-shutter distortions as a valuable source of temporal information to estimate the 3D translational and angular velocities of rapidly moving spherical objects from a single rolling-shutter frame. We design a robust and easily detectable spherical pattern and propose a correspondence-free formulation that recovers motion by enforcing geometric consistency in a back-projection framework. By exploiting the geometry of the sphere, translational and rotational motions are decoupled and estimated through a two-stage optimization process, enabling reliable velocity recovery even for textureless objects. Extensive experiments on both synthetic and real datasets demonstrate accurate and robust estimation of motion parameters under challenging high-speed conditions.

---


### 233. [Policy Optimization Achieves Data-Dependent Regret Bounds in MDPs with Unknown Transitions](https://arxiv.org/abs/2606.31769)

**<font color=#1a73e8>作者：</font>** Mingyi Li, Taira Tsuchiya, Kenji Yamanishi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study policy optimization for online episodic tabular Markov decision processes with unknown transition kernels, aiming for best-of-both-worlds guarantees together with data-dependent regret bounds. Recent work (Dann et al., 2023; Li et al., 2026) has shown that policy optimization can adapt to both adversarial and stochastic losses with first-order, second-order, and path-length bounds, but only under known transitions, leaving open whether such data-dependent guarantees are achievable by policy optimization when the transition kernel is unknown. We resolve this by developing a new algorithm based on optimistic follow-the-regularized-leader that attains these guarantees under unknown transitions. The key ingredient is a new design of optimistic $Q$-function estimators together with a data-dependent transition bonus that controls estimator bias through the loss-prediction error. Our analysis further identifies an unavoidable transition-dependent complexity term that captures the intrinsic cost of estimating the transition kernel. As a result, we obtain first-order, second-order, and path-length bounds with the transition-dependent complexity term while simultaneously achieving gap-dependent $\mathrm{polylog}(T)$ regret in the stochastic regime.

---


### 234. [Mesh BDF: Barycentric Dominance Field for 3D Native Mesh Generation](https://arxiv.org/abs/2606.31777)

**<font color=#1a73e8>作者：</font>** Gaochao Song, Haohan Weng, Luo Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive (AR) modeling has recently achieved remarkable progress in native 3D mesh generation, largely due to its natural ability to handle variable-length, discrete data structures. However, the inherent constraints of the AR paradigm severely restrict the generated meshes, leading to limited face counts, bounded vertex resolutions, and difficulties in supporting textures. To overcome these bottlenecks, we propose the Barycentric Dominance Field (BDF), a continuous representation defined on triangular mesh surfaces that elegantly encodes vertex topological connectivity. BDF bridges the fundamental gap between discrete mesh topology and continuous diffusion-based generative modeling by transforming connectivity into a continuous surface signal. As an intrinsic mesh property, BDF shares strong similarities with texture maps, enabling its seamless integration into existing 3D diffusion pipelines without requiring architectural modifications. Extensive experiments demonstrate that BDF empowers diffusion models to generate native meshes with significantly higher quality, greater scalability, and stronger robustness compared to state-of-the-art autoregressive methods.

---


### 235. [Bridging the Gap Between Latent and Explicit Reasoning with Looped Transformers](https://arxiv.org/abs/2606.31779)

**<font color=#1a73e8>作者：</font>** Ying Fan, Anej Svete, Kangwook Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language models typically reason via explicit chain-of-thought (CoT), generating intermediate steps token-by-token. Latent CoT offers an alternative: it performs multi-step reasoning in the model's hidden states, replacing decoded tokens with continuous representations for greater efficiency. However, existing latent CoT methods underperform explicit CoT beyond 1B parameters, and the gap widens with scale. Looped, or recurrent-depth, Transformers, which reuse their weights to increase computation depth without adding parameters, are a natural fit for latent reasoning. We therefore ask whether looped Transformers can bridge this gap. We answer affirmatively with a simple recipe: a looped padded Transformer that processes K latent blocks in parallel for R iterations, with a cross-entropy loss on each latent position's gold CoT-step token, similar to explicit CoT supervision. We instantiate it as LOTUS (Looped Transformers with parallel supervision on latents). LOTUS is, to our knowledge, the first latent-CoT method to bridge the gap to explicit CoT at the 3B scale, while cutting thought-phase latency by 2.5x-6.9x from compact math expressions to natural language. Projecting LOTUS's post-loop latents through the base LM head recovers the gold reasoning steps and even surfaces alternative valid intermediate steps, evidence that its latent space is interpretable and CoT-aligned. Ablations confirm that both the looped backbone and the parallel supervision on gold CoT tokens are essential.

---


### 236. [SpikeLogBERT: Energy-Efficient Log Parsing Using Spiking Transformer Networks](https://arxiv.org/abs/2606.31781)

**<font color=#1a73e8>作者：</font>** Thuan Bui, Duong Do, Tung Vu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Log parsing is a fundamental step in automated log analysis, transforming raw system logs into structured event templates for downstream tasks such as anomaly detection and system monitoring. Existing log parsing methods range from rule-based and clustering-based approaches to neural models that learn semantic representations from log messages. However, neural approaches typically rely on dense matrix multiplications, which can result in high computational cost and energy consumption. This paper presents SpikeLogBERT, a spiking neural network framework for energy-efficient log parsing. The proposed model integrates a spiking transformer architecture with knowledge distillation from a BERT teacher model, enabling spike-driven computation while preserving semantic representation capability. By leveraging sparse spike activations and event-driven processing, the number of active operations during inference can be significantly reduced. As an initial benchmark study, experiments on the HDFS dataset demonstrate that SpikeLogBERT outperforms ANN-based neural log parsing models with a parsing accuracy of 0.99997, while reducing estimated theoretical energy consumption by up to 62.6% under standard 45nm CMOS assumptions.

---


### 237. [Self-Supervised Temporal Regularization for Landmark-Based Cardiac Segmentation with Automatic AHA Regional Mapping](https://arxiv.org/abs/2606.31785)

**<font color=#1a73e8>作者：</font>** David Montalvo-García, Nicolás Gaggion, María J. Ledesma-Carbayo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Graph-based cardiac segmentation with implicit anatomical correspondences provides topological guarantees and population-level analysis capabilities, but models trained on independent frames of image sequences exhibit temporal discontinuities that affect reliable clinical measurements, particularly in cardiac ultrasound. In this work, we introduce self-supervised temporal regularization as a post-training refinement stage that exploits the temporal coherence in image sequences to enforce consistent cardiac segmentation and motion estimation over time, without requiring per-frame annotations. By penalizing velocity and acceleration discontinuities across consecutive frames, our method achieves temporally consistent segmentations while maintaining the learned anatomical correspondences. We further leverage these correspondences to automatically map landmarks to the AHA 17-segment clinical standard, enabling standardized regional assessment and detection of pathological myocardial motion patterns. Validation on CAMUS dataset demonstrates the clinical utility of combining temporal consistency with automatic regional mapping. The code is publicly available at this https URL

---


### 238. [Robocalls: A Worldwide or US-only Problem? Analyzing Spam and Fraud in International Phone Calls](https://arxiv.org/abs/2606.31790)

**<font color=#1a73e8>作者：</font>** Kemal Altwlkany, Andro Merćep, Tomislav Đuričić 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Unsolicited automated phone calls (robocalls) are a serious threat: in the US alone, these calls resulted in reported losses of 1.1$ billion during 2025. Phishing and spoofing consistently rank among the most reported crimes within the FBI's Internet Crime Complaint Center, with phone call scams having the highest reported median loss. Combating robocalls is difficult due to many legal and practical constraints: robocalls often encompass multiple legal jurisdictions of different countries/states, the large volume of robocalls, their multilingual nature, the lack of publicly available data, privacy concerns with obtaining data, etc. We present a study of international robocalls, aggregating robocall reports from countries across all inhabited continents and contribute by providing new findings on international robocalls from 65 different countries. We also present the first publicly available multimodal and international robocall dataset: 8.7 million call detail records, 839 robocall transcripts from 28 identified robocall campaign clusters, and 677 robocall recordings. We describe our methodology for collecting robocall data over a 9-month period and provide a detailed analysis comparing robocalls in the US with those in other countries. Our analysis covers several aspects, including uncovering calling patterns, identifying co-targeting attacks, discovering common robocall campaigns, extracting callback numbers, analyzing linguistic differences among robocalls in the same language but different regions, and other insights. Our results indicate that although robocalls are an international problem, the severity of the threat is significantly higher in the US than in other countries. We provide steps for future research and suggest remedies to reduce the effectiveness of robocalls based on our analysis.

---


### 239. [MuSViT: A Foundation Vision Model for Sheet Music Representation](https://arxiv.org/abs/2606.31811)

**<font color=#1a73e8>作者：</font>** Carlos Penarrubia, Antonio Rios-Vila, Eliseo Fuentes-Martinez 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Foundation models have transformed vision and language processing by providing rich, reusable representations that transfer across diverse tasks. Sheet music, as a visual encoding of musical language, lacks such a strong domain-specific backbone. We introduce MuSViT (Music Score Vision Transformer): the first foundation vision model for sheet music representation -- a ViT encoder pre-trained via Masked Autoencoders on 9.7 million pages from the IMSLP. To handle the complexity of real-world scores, we adopt a two-stage curriculum: a synthetic warm-up on typeset scores followed by large-scale training on the full IMSLP corpus. We evaluate MuSViT on four downstream tasks -- full-page and staff-level music score recognition, music symbol detection, and score difficulty classification -- under two scenarios: linear probing (frozen encoder) and fine-tuning. Under linear probing, MuSViT consistently outperforms modern vision encoders, revealing that general-purpose representations, regardless of scale, fall systematically short on the structured symbolic properties of musical notation. Under fine-tuning, MuSViT generally improves upon task-specific state-of-the-art methods. An additional embedding-transcription consistency analysis reveals that MuSViT encodes symbolic musical structure directly in its representation space -- unlike other encoders, whose embeddings do not correlate with music notation content. These results establish MuSViT as a foundation backbone for sheet music understanding.

---


### 240. [Generative Lane Topology Reasoning via Autoregressive Model with Geometry Prior](https://arxiv.org/abs/2606.31814)

**<font color=#1a73e8>作者：</font>** Jiahui Fu, Zehao Huang, Han Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Lane topology reasoning aims to construct a lane graph from onboard sensor observations. Existing methods follow a detection and association paradigm that treats each lane instance independently, leading to geometric inconsistency at connected endpoints and incomplete graphs due to visual occlusions. To address these issues, we propose TopoGPT, a generative framework that learns the geometry prior from typical lane graph structures through autoregressive sequence modeling. Specifically, we construct a large-scale map dataset comprising 3.3M scenes. For each lane graph, a lane tokenizer serializes it into discrete tokens, while a scene context encoder converts it into a rasterized image and extracts global features as scene tokens. We pre-train an autoregressive lane sequence transformer via scene-conditioned next-token prediction, endowing the model with the geometry prior over lane graph structures. Building upon this prior, a perception adapter aligns BEV features from multi-view images with the pre-trained scene condition, transferring the learned geometry prior to sensor-based lane graph prediction. On the OpenLane-V2 benchmark, TopoGPT outperforms existing methods by an average of +6.4 on lane-level and +11.6 on point-level metrics, and produces geometrically consistent and structurally complete lane graphs.

---


### 241. [Creating Intelligence: A Computational Foundation for AGI](https://arxiv.org/abs/2606.31819)

**<font color=#1a73e8>作者：</font>** Peter Overmann  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This work introduces a new computational theory of mind grounded in set theory and hyperdimensional computing. Whereas traditional neural networks rely on continuous weights and matrix multiplication, this framework works with sparse binary data. It represents information as discrete sets, directly modeling biological neural population codes. I demonstrate that associative memory emerges naturally from network topologies featuring a combinatorially expanded hidden layer. Learning is driven by topological plasticity rather than scalar weight adjustments. This architecture unifies auto-associative and hetero-associative learning under a single core algorithm: information retrieval via subset pattern matching and exact nearest-neighbor search. Operating with constant-time complexity, these mechanisms bridge perceptual data (sparse distributed representations) and symbols (sparse holographic representations) without continuous bottlenecks. Mapping this framework to neuroanatomy, I propose that both the cerebellum and the neocortex implement variants of this algorithm, making subset pattern matching the fundamental engine of cognition. Because it relies on discrete logic rather than matrix arithmetic, this algorithm translates directly into in-memory hardware. This opens a new route toward synthetic intelligence with human-level energy efficiency.

---


### 242. [Adaptive Cluster-First Route-Second Decomposition for Industrial-Scale Vehicle Routing](https://arxiv.org/abs/2606.31820)

**<font color=#1a73e8>作者：</font>** Oguzhan Karaahmetoglu, Hyong Kim  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large-scale capacitated vehicle routing problems (CVRPs) are commonly addressed using cluster-first route-second (CFRS) approaches that split a routing instance into smaller, computationally tractable subproblems. Existing splitting methods typically rely on fixed partitioning rules, predefined optimization objectives, or learned policies, which may perform inconsistently across instances exhibiting different spatial, demand, and operational characteristics. In this work, we propose an adaptive CFRS system that formulates a decomposition procedure as an iterative decision-making process. Motivated by the recent success of large language models (LLMs) in reasoning and tool selection, the system employs an LLM as a high-level decision maker that analyzes the evolving decomposition state and selectively applies further clustering, balancing, and refinement operators. The proposed algorithm jointly partitions customers and vehicles, enabling capacity-aware clustering while adapting partitioning decisions to the characteristics of each problem. We evaluate the approach on synthetic and benchmark-derived CVRP instances containing up to 500,000 customers. Experimental results demonstrate competitive performance on benchmark-scale instances while exhibiting improved scalability and robust routing quality on substantially larger problems. These results highlight the potential of adaptive, LLM-guided decision support as a practical approach for industrial-scale vehicle routing and large-scale logistics planning.

---


### 243. [Absorption-Feature-Guided Distance-Decoupled Estimation and Band Selection for LWIR Hyperspectral Passive Ranging](https://arxiv.org/abs/2606.31824)

**<font color=#1a73e8>作者：</font>** Shuo Liu, Chen Fan, Zhihe Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-wave infrared (LWIR) hyperspectral observations contain distance-dependent atmospheric absorption signatures, providing a physical basis for long-range passive ranging. However, in natural scenes, these signatures are nonlinearly coupled with target temperature, material emissivity, and path radiance, making distance inversion from observed radiance ill posed. Existing methods typically rely on full-band measurements and pixel-wise joint optimization, which is computationally expensive and does not explicitly exploit sharp atmospheric absorption structures. This paper proposes an Absorption-Guided Distance-Decoupled Estimation and Refinement (ADER) framework for LWIR hyperspectral passive ranging. ADER represents emissivity with B-spline control points under a smoothness prior, suppressing overfitting to atmospheric absorption structures and enabling distance-decoupled estimation. It further uses ozone-absorption cues to classify pixels into emission-dominant and reflection-dominant groups. For emission-dominant pixels, ADER compensates path radiance and transmittance and estimates distance by one-dimensional absorption-residual minimization. For reflection-dominant pixels, ADER refines the initial estimate using downwelling-radiance compensation based on the complete radiative model. To reduce spectral redundancy, ADER also introduces a greedy band selection strategy based on multi-scene effective Fisher information for the distance parameter. Experiments on real scenes show that ADER recovers LiDAR-consistent spatial distance structures under both full-band and 20-band settings, improves ranging accuracy in the evaluated regions, and achieves approximately two orders of magnitude speedup over a public full-band hyperspectral ranging method.

---


### 244. [PriorEye: Geospatial Visual Priors for End-to-End Autonomous Driving](https://arxiv.org/abs/2606.31830)

**<font color=#1a73e8>作者：</font>** Kyuhwan Yeon, Benjamin Ramtoula, Daniele De Martini  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Most end-to-end autonomous driving methods rely solely on instantaneous sensor observations, limiting them to reactive behavior without the anticipatory foresight human drivers employ through prior experience. We introduce geospatial visual priors, street-level visual context anchored to the intended driving route, providing visual-spatial foresight independent of real-time sensors. We propose a memory augmentation module featuring a dual-memory architecture and an adaptive memory gate, which can be easily integrated into existing end-to-end approaches. This design pairs a contextual memory for retrieved priors with a persistent fallback memory, and dynamically regulates the influence of memories based on current state compatibility. Evaluated on the NAVSIM-v2 benchmark, our approach consistently improves performance across diverse end-to-end baselines. Furthermore, because these priors are independent of onboard sensors, our method inherently improves robustness against sensor corruption, while the dual-memory design ensures safe fallback when the retrieved priors themselves become unreliable. Our project page is available at this https URL.

---


### 245. [Real-Time Source-Free Object Detection](https://arxiv.org/abs/2606.31834)

**<font color=#1a73e8>作者：</font>** Sairam VCR, Varun Gopal, Poornima Jain 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-world detectors for autonomous driving, surveillance, and robotics must handle domain-shifts under strict latency and memory constraints, yet existing source-free object detection (SFOD) methods rely on heavyweight architectures that prioritize accuracy alone. We show this trade-off is unnecessary: building on YOLOv10, an NMS-free dual-head detector, we achieve state-of-the-art adaptation accuracy while being faster and more compact. We observe that directly applying vanilla mean-teacher self-training to dual-head detectors leads to suboptimal adaptation performance due to two key factors. First, simple pseudo-label generation strategies, such as using a single head or directly combining high-confidence predictions from both heads, yield suboptimal supervision under domain-shift. We propose DHF (Dual-Head Pseudo-Label Fusion) which selectively admits one-to-one (O2O) and one-to-many (O2M) head predictions, preserving precision and recovering missed objects. Second, we observe domain-shift collapses multi-scale feature discriminability. We propose the use of our MARD (Multi-scale Adaptive Representation Diversification) loss which mitigates this by enforcing detection-aware variance and covariance constraints on multi-scale feature maps. Both modules are training-time only, leaving inference unchanged. Across domain-shift benchmarks, our method, RT-SFOD yields 1.4 to 3.5\% mAP gains, 1.3$\times$ higher throughput, with $\sim$2$\times$ fewer parameters than prior state-of-the-art SFOD methods, thus advancing the Pareto frontier of the speed-accuracy-model size trade-off. We report main results with YOLOv10, and demonstrate generalizability with additional YOLO- and DETR-based dual-head detectors. Code is available here: this https URL

---


### 246. [Towards Voxel Spacing Consistency for Medical Image Segmentation](https://arxiv.org/abs/2606.31839)

**<font color=#1a73e8>作者：</font>** Xin You, Runze Yang, Minghui Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Volumetric medical image segmentation is essential for both preoperative diagnosis and intraoperative guidance. While recent years have witnessed rapid progress in segmentation architectures, comparatively little attention is paid to the physical voxel spacing of anatomical data. Indeed, volumetric image resampling is a ubiquitous preprocessing step before segmentation, yet its interaction with downstream segmentation has not been systematically exploited. In this work, we study the correlation between image resampling and segmentation, and propose Consispace, a semantic-aware resampling framework that achieves consistent voxel spacing in the axial direction while preserving anatomical and semantic consistency. Consispace introduces an ODE-based anatomical constraint to model inter-slice dynamics with a continuous interpolator, enabling faithful reconstruction under complex anatomical transitions beyond discrete interpolation. To further couple resampling with segmentation objectives, we leverage dense features from a pretrained vision model to build intra-slice semantic correlation maps and inject class-wise semantic consistency via feature reweighting during resampling. Both intra-slice and inter-slice constraints are integrated into an implicit neural network, supporting arbitrary-scale resampling. Extensive experiments on multiple datasets demonstrate that Consispace achieves superior reconstruction quality and perceptual fidelity, produces smoother inter-slice anatomy, and improves downstream segmentation performance when used as a preprocessing step.

---


### 247. [Explicit Fuzzy Logic in the Feed-Forward Layer: Self-Forgetting Quantifiers Discover Legible Grammatical-Licensing Detectors](https://arxiv.org/abs/2606.31845)

**<font color=#1a73e8>作者：</font>** Mark Oskin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A transformer's feed-forward (FFN) sublayer materializes the distinctions attention gathers, yet gives no account of what it computes. In a parameter-neutral replacement, each hidden unit is an explicit fuzzy set operation on sigmoid-bounded [0,1] memberships: intersection A*B and set-difference A*(1-B), the latter a bounded positive negation ("A but not B") that gated/bilinear units lack -- a negation-capable FFN (NC-FFN). On N-bit parity they are the most parameter-efficient reasoning basis at shallow depth; at scale (125M, OpenWebText) NC-FFN ties the GELU baseline's perplexity, every unit carrying explicit logical form. Two limits share one cause: two-operand logic localizes to layer 0 and erodes under training, and the one robust grammatical deficit concentrates in licensing and quantifiers, beyond within-token operators. We resolve both with a small block of sequence quantifiers: a soft existential and a soft proportion, each with a per-unit learned forgetting rate from a sticky init. This recovers the deficit at epoch one (halving the wider epoch-two gap), modestly leads on LAMBADA, and makes the FFN legible: the structure now holds and migrates into depth; the decay un-learns its stickiness (median half-life ~1.5 tokens; zero latch units); and at the semantic layers the units read, without dictionary learning, as grammatical licensing detectors: each fires on a licensor (a comparative, a passive participle, a negative-polarity item) and carries its memory forward to predict the licensed word (than, by, nor). This legibility is localized and free only up to a partition (a fully Boolean FFN diverges in training), but the result is a parameter-neutral, language-model-quality transformer with a readable, interpretable-by-construction grammatical mechanism -- an account not just of what a feed-forward layer represents but how it licenses.

---


### 248. [Low-dimensional topology of deep neural networks](https://arxiv.org/abs/2606.31856)

**<font color=#1a73e8>作者：</font>** Junyu Ren, Lek-Heng Lim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study layered models, including feedforward networks, ResNets, and transformers, by limiting each layer to a width of $d = 3$, i.e., $\mathbb{R}^3$ as representation space. This allows us to track how a neural network changes low-dimensional topological invariants through its layers. Just about any topological structure may be simplified or even trivialized by simply increasing dimension; e.g., any knot is equivalent to an unknot in $\mathbb{R}^4$. By restricting to $\mathbb{R}^3$, we not only isolate the effects of activation and depth from that of width, we work in a space that lends itself to easy visualization. We focus on linking number here, deferring other invariants like link groups, Milnor's $\bar{\mu}$-invariants, knot types, ambient cobordisms, to a sequel. We provide full proofs and empirical experiments to justify the following insights: When measured by their power to effect changes in linking numbers, the layer-skipping feature in ResNets is as powerful as the attention mechanism in transformers; both ResNets and transformers are strictly more powerful than feedforward neural networks with monotonic activations, which are in turn more powerful than invertible and flow-based models; but replacing monotonic activation with a nonmonotonic one elevates a feedforward network into the same expressivity class as ResNets and transformers. These results suggest that low-dimensional topology can be a useful tool to guide designs of AI architectures. We also generalize our results from $d = 3$ to arbitrary $d > 3$.

---


### 249. [Review Residuals: Update-Conditioned Residual Gating for Transformers](https://arxiv.org/abs/2606.31859)

**<font color=#1a73e8>作者：</font>** Kyle Kramer  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Residual connections add every sublayer's proposed update with a fixed coefficient of one; the network never evaluates whether an update is reliable before committing it. Drawing on the human-factors principle of independent verification, we introduce Review Residuals, which scale each update by a learned, input-dependent gate conditioned on both the current state and the proposed update: h_l = h_{l-1} + r_l * u_l with r_l = sigmoid(W[RMSNorm(h_{l-1}), RMSNorm(u_l)]). Conditioning the gate on the update is the property that distinguishes it from prior gated and scaled residuals. We report two findings. First, a depth-stability result: a convex (Highway-style) form of the gate reintroduces vanishing gradients and fails to train beyond ~20 layers, whereas the additive, identity-preserving form trains stably at all depths we tested. Second, an emergence-with-scale result: trained from scratch across five sizes (60M-1B parameters, multi-seed), Review Residuals show no advantage at small scale but at 590M significantly outperform both a parameter-matched Highway gate and a parameter-matched standard residual (p<0.05), with a larger advantage at 1B. The benefit grows with model size rather than shrinking.

---


### 250. [SENSE-VAD: Sentient and Semantic Video Anomaly Detection for Autonomous Driving](https://arxiv.org/abs/2606.31875)

**<font color=#1a73e8>作者：</font>** Nghia T. Nguyen, Lokman Bekit, Yasin Yilmaz  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autonomous vehicles (AVs) must navigate not only motion-based hazards but also socially complex situations whose danger is constituted by inter-agent relationships rather than movement statistics alone. A child running away from a guardian, a person being carried by another, or a pursuer chasing a pedestrian across a sidewalk are all anomalous in social context, yet none produces an obvious motion signal that current anomaly detectors are equipped to flag. We introduce SENSE-VAD, the first synthetic video anomaly detection benchmark for autonomous driving explicitly designed around socially complex anomalies. Using the CARLA simulator and Unreal Engine (UE), we generate distinct anomaly scenarios across multiple categories: individual behaviors, group behaviors, person--object interactions, cyclist interactions, vehicle & agent, each annotated with per-frame binary labels. A key design principle is the separation of social anomaly from motion-based or appearance-based anomaly: many scenarios involve motion of objects that appears unremarkable in isolation but is anomalous in relational context. We additionally provide real-world normal and anomalous videos as a sim-to-real transfer probe. We evaluate state-of-the-art video anomaly detection baselines and demonstrate that socially complex anomalies constitute a distinct and currently unsolved challenge. Our dataset, annotations, and generation code are publicly available.

---


> [!TIP]
> 当前位于：**201-250**（第 5/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-274](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
