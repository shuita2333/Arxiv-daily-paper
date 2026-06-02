# 📦 其他研究 | 2026年06月03日

> 本类共 **651** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**501-550**（第 11/14 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | **501-550** | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-651](./part-14.md)

---

### 501. [AutoBG: A Board Game Design Assistant with Interactive Ideation, Iterative Rulebook Generation, and Individualized Feedback](https://arxiv.org/abs/2606.01976)

**<font color=#1a73e8>作者：</font>** Zizhen Li, Chuanhao Li, Yibin Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Designing a board game demands both thinking as a designer and experiencing as a player, while iterating through repeated prototyping and playtesting cycles, making it a cognitively intensive creative task well suited for human-AI collaboration. However, current systems lack end-to-end support to guide designers through the complete workflow from vague early ideation to iterative rulebook revision and audience testing. To this end, we present AutoBG, a board game design assistant built around critic-driven iterative refinement, comprising four specialized modules: BG-Ideator guides designers via multi-turn dialogue to produce structured design drafts; BG-Realizer generates complete rulebooks from drafts and revises them in a closed loop with BG-Critic, which diagnoses design flaws and gates each revision so that only verified improvements are accepted; and BG-Persona simulates individualized feedback from 150 real player profiles. Together, these modules enable designers to go from an initial idea to a polished, audience-tested rulebook within a single integrated workflow. The system is built on 2.2K structured rulebooks and 180K quality-filtered real player reviews, with task-specific training data derived for each module. Experiments on 207 held-out games show that AutoBG substantially outperforms state-of-the-art baselines (e.g., GPT-5.4), generating rulebooks that approach the quality of published games. Furthermore, a user study with 30 participants across diverse experience levels confirms that AutoBG effectively reduces blank-page anxiety, surfaces hidden design flaws, and provides highly rated, practical assistance throughout the creative process.

---


### 502. [A Simple Hierarchical Causality Primer](https://arxiv.org/abs/2606.01979)

**<font color=#1a73e8>作者：</font>** Tim Gebbie  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> We provide a brief primer for the idea behind formalising hierarchical causality in the context of complex systems. Here actors are not simply agents. Actors instantiate causation classes. Agents implement local dynamics in given levels or organisation in a given system. Hierarchical causality then describes how actor-level roles constrain, select, and organise agent-level behaviour across levels. The system then necessarily requires three additional structures. First, causation classes to abstract a given form of causal influence that an actor instantiates. Second, aggregation operators to move across the levels. Third, discrete event-time maps are required because the system comprises events, and the relation between local event counts and any global clock must be specified. Our formulation here is purposefully simple and discrete.

---


### 503. [Generalization Limits in Vehicle Re-Identification](https://arxiv.org/abs/2606.01981)

**<font color=#1a73e8>作者：</font>** Anis Yassine Ben Mabrouk, Antoine Tadros, Rafael Grompone von Gioi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vehicle re-identification focuses on retrieving images of the same vehicle from a gallery given a query image. Upon closer inspection of commonly used datasets, we observe that vehicles with few visual differences-e.g., the same make, model, and color-appear in both the training and test sets. As a result, methods that effectively memorize the training data tend to perform well on these test sets but struggle to generalize to other datasets. In this paper, we address this issue by proposing a novel evaluation approach that more effectively measures generalization capability to unseen vehicle types. To further study generalization performance, we also propose splitting the evaluation based on view, allowing us to differentiate the effect of viewpoint robustness from that of same-view re-identification. Our findings reveal that most state-of-the-art methods struggle with unseen vehicle types, and that their robustness to viewpoint changes and attention to detail are limited to vehicle types seen during training.

---


### 504. [MT-EditFlow: Reinforcement Learning for Multi-Turn Image Editing with Flow Matching](https://arxiv.org/abs/2606.01985)

**<font color=#1a73e8>作者：</font>** Jiahui Huang, Yasi Zhang, Tianyu Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent breakthroughs in instruction-based image editing have captured significant attention, as models are now capable of handling real-world editing demands with the practicality required by everyday users. However, editing models trained primarily for single-turn edits often break down in multi-turn editing--the natural interactive setting where a user iteratively refines an image based on the model's own previous outputs. This failure stems from the all-or-nothing requirement, where a single failed turn compromises the entire sequence, and error propagation, where exposure bias leads to compounding editing errors. To address these challenges, we introduce MT-EditFlow, a flow-matching reinforcement learning framework designed to optimize reward signals for sequential image editing. MT-EditFlow integrates a multi-turn perspective with a multi-reward formulation to provide a unified structure applicable to both GRPO and NFT-based reinforcement learning methods. We systematically analyze and optimize the reward signal by investigating effective scoring strategies for turn-level aggregation, VLM reasoning modes to trade off reward bias and variance, and advantage fusion levels to prevent reward hacking. Our findings reveal that broadcasting the aggregated advantage across the entire editing trajectory effectively bridges the gap between local planning and global multi-turn task success. Extensive experiments demonstrate that MT-EditFlow significantly improves performance across diverse base models. Notably, it boosts FLUX.1-Kontext-dev by 6.85 points in turn-3 overall performance, surpassing state-of-the-art open-source models such as Qwen-Image-Edit. By maintaining high marginal success rates and reducing exposure bias, MT-EditFlow provides a foundation for more reliable and natural human-AI collaboration in visual content creation.

---


### 505. [A Structured Benchmark for Text-Guided Anomaly Detection: When Language Stops Conditioning the Decision](https://arxiv.org/abs/2606.01992)

**<font color=#1a73e8>作者：</font>** Stefano Samele, Eugenio Lomurno, Teodora Jovanovic 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Industrial anomaly detection has historically been a unimodal task. Recent multimodal vision-language models have produced systems that admit textual input alongside the image and are presented as enabling text-guided zero- and few-shot inspection. Yet these methods are evaluated with protocols inherited from unimodal benchmarks that hold the textual condition constant and therefore cannot measure whether language conditions the decision; whether reported gains reflect text guidance or strong pretrained visual features remains open. We introduce Text-Guided Anomaly Detection (TGAD), a structured benchmark that progressively increases the functional role of language across three scenarios: a controlled prompt-sensitivity setting on MVTec AD; a component-tagged extension of MVTec AD that requires the model to restrict its assessment to an instructed part; and the new Assembled Panel Dataset (APD), a realistic industrial setting that requires both defect-type and component-location knowledge. We evaluate one representative model per paradigm: generative large vision-language, training-free discriminative, and embedding-adaptive discriminative. In all three, the textual interface conditions the decision only superficially: prompt content is absorbed unless the object noun is removed (the generative model's I-AUROC drops from 97.4 to 82.6); component-level instructions do not constrain the decision once defects outside the instructed part are admitted as normal (from 90.3 to 66.3); and when both combine on APD, image-level discrimination collapses below the MVTec level, in one case below chance (71.2, 50.5, 31.5). These results suggest that standard benchmarks overstate the text-guided capabilities of current multimodal anomaly detection systems, and that a protocol of this kind is a prerequisite for models that can be reliably controlled through language for industrial deployment.

---


### 506. [Why Do Time Series Models Need Long Context Windows?](https://arxiv.org/abs/2606.01999)

**<font color=#1a73e8>作者：</font>** Luca Butera, Giovanni De Felice, Andrea Cini 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern deep learning models for forecasting groups of time series rely on increasingly longer observation windows. However, the benefit of increasing the window size is often simply attributed to capturing long-range dependencies, and broader discussion on how global forecasting models leverage input observations has been limited. In this paper, we show that forecasting groups of time series involves two objectives: (i) generative process identification (GPI), i.e., inferring the specific process generating the input sequence, and (ii) conditional forecasting (CF), i.e., predicting future values given input observations. From this perspective, optimal predictions can be interpreted as an average over plausible data-generating processes, weighted by their likelihood given the input window. This suggests another explanation for the benefits of long context windows: they reduce the uncertainty about which specific process is generating the input time series during operation. We prove that even for processes with memory length $P$, an input window size strictly larger than $P$ is necessary to achieve the minimum attainable error. Finally, we show how decoupling GPI and CF can improve computational scalability without compromising accuracy. Experiments on synthetic and real-world data validate our insights and their relevance for designing forecasting architectures.

---


### 507. [Towards 3D-Aware Video Diffusion Models: Render-Free Human Motion Control with Mesh Tokenization](https://arxiv.org/abs/2606.02000)

**<font color=#1a73e8>作者：</font>** Jingyun Liang, Min Wei, Shikai Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models have shown remarkable success in video generation. However, whether such models are truly aware of the 3D structure underlying visual observations, rather than simply reproducing plausible 2D projections, remains an open question. In this work, we investigate this question through human motion control, a task that requires precise modelling of 3D human geometry, motion, camera viewpoint, and scene context. Unlike prior methods that rely on rendered 2D motion guidance videos, we propose a render-free framework that conditions video generation directly on compressed 3D human mesh tokens. This representation preserves full 3D geometric information while enabling a unified token-based generation pipeline that processes video tokens jointly with motion tokens in a DiT-based architecture. This design requires the model to reason jointly about appearance, 3D structure, and camera viewpoint during video generation. Experimental results demonstrate strong performance on human motion control benchmarks, while reducing artifacts induced by view-dependent 2D guidance and trajectory-pose mismatches during editing. These findings suggest that video diffusion models, when equipped with mesh tokenization, can better capture complex 3D human structures and their interactions with the surrounding environment.

---


### 508. [Distortion-Aware Fusion of Statistical and Vision-Language Features for Blind Image Quality Assessment](https://arxiv.org/abs/2606.02002)

**<font color=#1a73e8>作者：</font>** Bishr Omer Abdelrahman Adam, Xu Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Blind image quality assessment (BIQA) aims to predict perceived image quality without access to a reference image. Classical natural scene statistics (NSS) descriptors and modern vision-language model (VLM) embeddings address this problem from fundamentally different perspectives, yet whether combining them yields complementary benefits and how to weight their contributions per input image remains unexplored. We propose a distortion-aware fusion framework that integrates a 138-dimensional NSS descriptor with two complementary VLM embeddings, SigLIP and CLIP-H, through a multiplicative gating mechanism that learns per-input stream weights conditioned on image content. Unlike static concatenation fusion, the proposed gating network suppresses or amplifies each stream's contribution based on the input, producing weights that correlate positively (Spearman rank correlation rho=0.33) with the per-distortion NSS contribution measured by independent ablation on KADID-10k. The framework requires no end-to-end fine-tuning of the VLM backbones and is trained with a hybrid loss combining mean squared error, Pearson linear correlation, and pairwise ranking objectives. We evaluate on three standard benchmarks: KonIQ-10k (SROCC=0.9142, PLCC=0.9279), KADID-10k (SROCC=0.9715, PLCC=0.9733, surpassing recent state-of-the-art methods), and LIVE Challenge in-the-Wild (SROCC=0.8527, PLCC=0.8802 with cross-dataset pretraining and fine-tuning). A per-distortion analysis on KADID-10k reveals that NSS features contribute most on noise and color-shift distortions where pixel statistics are directly affected, and least on perceptual distortions such as color saturation changes. The learned gate values validate these findings, confirming that the model autonomously discovers distortion-stream affinity patterns consistent with the manual per-distortion study.

---


### 509. [Machine Learning for Coding Retail Product Names to Consumer-Price Categories: A Rule-plus-Bag-of-Words Pipeline with Reliability-Weighted Human-in-the-Loop Labeling](https://arxiv.org/abs/2606.02004)

**<font color=#1a73e8>作者：</font>** Vladimir Beskorovainyi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Consumer-price measurement increasingly draws on alternative data sources -- scanner, web-scraped, and transaction/receipt data. A recurring obstacle is that product descriptions in such sources are short, noisy, and abbreviated, with no standard product code, so each item must first be mapped to a consumption classification (e.g., the UN COICOP scheme) before prices can be compared. This paper studies that mapping as a general, reproducible method. The pipeline is: (i) text normalization and tokenization of noisy item names; (ii) a prefix-tree (trie) rule-based pre-classifier driven by per-category key-phrases and stop-phrases; and (iii) a per-category binary confirmation model deciding whether an item belongs to a tentatively assigned category. For labels at scale we use a human-in-the-loop protocol in which annotators give a binary valid/reject judgment, aggregated by a dynamically updated reliability weight; the model joins the same rule, enabling continual fine-tuning. Our empirical finding is deflationary: in a controlled, leakage-free study (one category, real positives vs. hard negatives, five seeds), bag-of-words models essentially saturate the task (F1 about 0.99) -- a linear classifier matches a multilayer perceptron, explicit word-order (n-gram) features add nothing, and about 67 labeled examples already suffice. A Monte-Carlo study of the labeling protocol shows the reliability-weighted vote barely beats plain majority (its additive weights saturate) while Dawid-Skene recovers labels markedly better. We also discuss price-level quality control and design lessons for statistical offices considering transaction data. All figures are illustrative; no confidential data, code, or documentation is reproduced.

---


### 510. [Automated Essay Scoring and Language Certification: Assessing Generalizability, Agreement and Validity for French](https://arxiv.org/abs/2606.02009)

**<font color=#1a73e8>作者：</font>** Rodrigo Wilkens, Rémi Cardon, Vincent Folny 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In Automated Essay Scoring (AES), benchmarking practices have fostered minimalist evaluation practices, in contrast with the broader-view recommendations of evaluation frameworks, such as the argument-based validation framework (ABV), which argued in favor of a multidimensional assessment of systems, especially in the context of high-stakes language tests. In this paper, we introduce an enhanced and more practical version of the ABV framework, incorporating fairness analysis, correlations with linguistic features, prediction error evaluation, and model agreement compared with human raters. Applying this framework to French AES, we compare 8 model architectures on a corpus of 27k exam essays (2 raters each) and a generalization corpus of 961 essays (at least nine raters each). Our analyses illustrate the benefits of applying the ABV framework to better understand the capabilities and pitfalls of AES models, while also advancing the state-of-the-art for French AES.

---


### 511. [Evaluating Real-World Generalizability of Algorithm Selection Models](https://arxiv.org/abs/2606.02016)

**<font color=#1a73e8>作者：</font>** Gjorgjina Cenikj, Jakub Kudela, Eva Tuba 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Algorithm Selection (AS) aims to automatically identify the most suitable optimization algorithm for a given problem instance by leveraging measurable problem characteristics and historical performance data. In this study, we investigate the generalization ability of AS models across both synthetic and real-world optimization landscapes. We consider two widely used academic benchmark suites (BBOB and CEC) and two real-world problem sets (robotics trajectory optimization tasks and unmanned aerial vehicle path-planning problems). Through a systematic cross-benchmark evaluation, we analyze how AS models transfer between domains, identify where generalization succeeds or breaks down, and highlight the challenges that arise when applying AS in realistic, domain-specific contexts. Our findings provide insights into the robustness of current AS approaches and inform the development of more reliable, broadly applicable AS systems for real-world optimization.

---


### 512. [Unveiling the Entropy Dynamics of Chain-of-Thought Reasoning](https://arxiv.org/abs/2606.02020)

**<font color=#1a73e8>作者：</font>** Ting Xu, Xu He, Yupu Lu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper investigates the entropy dynamics of Chain-of-Thought (CoT) and uncovers a consistent two-phase structure: an Uncertainty Region of exploration transitioning sharply to a Confidence Region of convergence. We demonstrate that the Confidence Region possesses two critical properties: 1) High Reliability -- answers in the confidence region become highly accurate and stable, and 2) High Redundancy -- models generate unnecessary tokens long after reaching the correct answer. These properties unlock more efficient and reliable inference strategies: 1) Early Exit leverages reliability and redundancy to terminate computation safely when returns diminish, and 2)Test-Time Scaling uses the Confidence Region signal to prioritize converged trajectories. To operationalize these insights, we formulate Confidence Region detection as a sequential change-point detection problem, being the first to apply classical change-point methods to monitor CoT reasoning. Using the Cumulative Sum (CUSUM) algorithm, a statistically optimal change-point detector, we develop a training-free framework for real-time inference control. Experiments show our approach establishes a superior Pareto-frontier for early exit. CUSUM achieves 63.06% accuracy with 11.1% token reduction, outperforming DEER and Dynasor by 3.28% and 4.36% in accuracy respectively. For test-time scaling, CUSUM-weighted voting consistently outperforms self-consistency.

---


### 513. [PerBite: A Curated Diagnostic Workflow for Bite-Aware Food Volume Estimation](https://arxiv.org/abs/2606.02021)

**<font color=#1a73e8>作者：</font>** Ahmad AlMughrabi, Farid Al-Areqi, David Fernández Gómez 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Can a visually plausible food mesh be trusted to estimate the volume of consumed food? \method investigates this question using selected paired before- and after-consumption states from the MetaFood CVPR 2026 Continuous 3D Reconstruction While Eating Challenge. The submitted workflow follows a curated reconstruction protocol: SAM~3 segments the food and plate regions; Hunyuan3D/SAM~3D generates a dimensionless food mesh; the plate diameter provides the metric scale; the plate geometry is removed in Blender; and the remaining mesh is hole-filled, made watertight, and integrated to estimate volume. MoGe-2 is used only as an auxiliary cue for initial dish-diameter estimation when direct plate measurement is uncertain; it is not the primary scale source for the reported challenge result. \method ranks first, with an average Chamfer distance of 8.31 across 34 meshes using rigid ICP without scale correction. On 17 before- and after-pairs, it achieves 33.87\% state-level volume MAPE and zero monotonicity violations, while consumed-volume MAPE remains 53.74\%. The results show that surface reconstruction, metric scale, controlled mesh cleanup, watertight volume integration, and physical depletion consistency should be evaluated separately for dietary assessment. Source code and evaluation scripts will be available at \href{this https URL}{this http URL}.

---


### 514. [Ranking vs. Assignment: The Metric Mismatch in Multi-View Object Association](https://arxiv.org/abs/2606.02022)

**<font color=#1a73e8>作者：</font>** Matvei Shelukhan, Timur Mamedov, Aleksandr Chukhrov 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-view object association is an important computer vision problem that underlies many multi-camera perception tasks. While this task is naturally formulated as a constrained one-to-one matching problem, recent works heavily rely on pairwise ranking metrics like AP and FPR-95 for model evaluation. We highlight a fundamental mismatch between these metrics and the actual assignment objective. Theoretically, we show that AP and FPR-95 can be imperfect even when the assignment is already correct, and that Sinkhorn-based normalization can make them perfect. Conversely, optimal pairwise ranking can still lead to incorrect assignments. We validate this mismatch in practice by using our Sinkhorn-based normalization as a controlled post-processing stress test. We show that optimizing just a few post-processing parameters significantly boosts AP and FPR-95 without corresponding improvements in assignment-level metrics such as ACC and IPAA.

---


### 515. [RL-ACRGNet: Reinforcement Learning-Based Chest Radiology Report Generation Network](https://arxiv.org/abs/2606.02035)

**<font color=#1a73e8>作者：</font>** Yogesh Kumar Meena, Saurabh Agarwal, K.V. Arya  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Medical imaging interpretation is a foundational pillar of modern clinical diagnostics, yet the manual generation of radiology reports remains a time-consuming process prone to interpretation inconsistencies. Within the field of medical AI, automating these descriptions through deep learning promises to streamline clinical workflows and standardise diagnostic output. However, accurate disease detection and precise report generation remain significant challenges due to limitations in capturing fine-grained visual features and ensuring clinical coherence. To address these issues, we propose RL-ACRGNet, an improved encoder-decoder model that integrates a pre-trained DenseNet encoder with a multilevel LSTM decoder within an off-policy reinforcement learning framework. Using a dual-network approach to refine visual-semantic embeddings through a metric-based reward mechanism, we demonstrate that RL-ACRGNet consistently outperforms state-of-the-art baselines on the IU-Xray dataset, achieving quantitative improvements in BLEU-4 (0.47%), METEOR (0.17%) and ROUGE-L (0.518). Furthermore, comprehensive evaluations on the large-scale MIMIC-CXR data set confirm the robust generalisation of the model and its ability to generate high-quality, clinically relevant reports

---


### 516. [Respectful Things: Adding Social Intelligence to 'Smart' Devices](https://arxiv.org/abs/2606.02037)

**<font color=#1a73e8>作者：</font>** Max Van Kleek, William Seymour, Reuben Binns 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> In this paper, we propose that the idea of devices respecting their end-users may serve as a strong design goal for highly personal and intimate smart devices. We ask what respect is, how it shapes interaction, and how good-faith simulation of respect might inform user-friendly smart device design. Respect is a natural and integral part of natural human relationships that is seen to shape work and personal relations. In a basic sense, this is the core purpose of smart things: we expect them to be ready and willing to help us. In this vein, we distil the characteristics of more complex respectful behaviours into 4 main types relevant to smart devices, drawing from philosophical analyses of the conceptual dimensions of respect: directive respect, obstacle respect, recognition respect, and care respect. We discuss the implications of each of these kinds of respect for the future of smart personal devices.

---


### 517. [Normality-Preserving Continual Industrial Anomaly Detection via Orthogonal LoRA Banks](https://arxiv.org/abs/2606.02042)

**<font color=#1a73e8>作者：</font>** Weibai Fang, Haijun Che, Feiyang Ren 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Continual industrial anomaly detection with diffusion models suffers from historical normality prior drift and catastrophic forgetting. Existing continual diffusion methods preserve previous knowledge through replay or constrained optimization, but they lack an explicit mechanism for isolating and protecting category-specific normality priors during sequential adaptation. Although low-rank adaptation provides modular residual updates, standard LoRA neither freezes historical normality subspaces nor prevents new adapters from interfering with previous ones. To address this issue, we propose a normality-preserving continual anomaly detection framework based on two modules: History Frozen Orthogonal LoRA Bank (HF-OLB) and Hierarchical Novelty Adaptive Bank Growth module (HNABG). HF-OLB freezes both the pre-trained U-Net backbone and the learned LoRA banks, and constrains new task-specific normality residuals to the orthogonal complement of historical LoRA subspaces. HNABG further allocates layer-dependent residual capacity and expands the bank only when the residual normality novelty exceeds the expressive capacity of existing banks. Extensive experiments on MVTec and VisA demonstrate the effectiveness of the proposed method. On the challenging VisA 2x6 setting, our method achieves 83.6/91.8 image and pixel level A-AUROC with 3.8/3.9 FM, improving pixel level A-AUROC over the state of the art by 3.2 points while reducing pixel level FM by 1.3. These results show that our method effectively preserves historical normality priors in long horizon continual category sequences.

---


### 518. [Realistic noise synthesis reduces bias and improves tissue microstructure estimation with supervised machine learning](https://arxiv.org/abs/2606.02044)

**<font color=#1a73e8>作者：</font>** Bradley G. Karat, Maëliss Jallais, Ali R. Khan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion MRI enables non-invasive probing of tissue microstructure, but accurate parameter estimation is challenged by noise-related effects. In supervised machine learning frameworks trained on simulated data, discrepancies between the noise characteristics of simulated and acquired signals introduce a form of covariate shift, whereby the input signal distribution differs between training and inference. We investigated the impact of this mismatch on microstructure parameter estimation and propose a realistic noise synthesis (RNS) framework to mitigate it. RNS incorporates both the Rician expectation and the effective post-processing noise variance into simulated training signals. The Rician expectation was modelled using a noise standard deviation estimated with MPPCA, while the effective standard deviation was derived from spherical harmonic residuals of preprocessed data. The method was evaluated using the cylinder-zeppelin and the SANDI models on simulated datasets across multiple SNR levels and on in vivo diffusion data with repeated acquisitions. Sensitivity to noise misestimation was also assessed. Ignoring magnitude-induced noise effects during training produced systematic, SNR-dependent parameter bias, particularly at low SNR. Incorporating the Rician expectation substantially reduced bias to the level of noise-aware nonlinear least-squares fitting. Modelling the effective standard deviation further improved precision. Performance was largely independent of regression architecture but sensitive to accurate noise estimation. These findings demonstrate that realistic noise modelling in simulated training data mitigates signal-domain covariate shift and is essential for unbiased supervised microstructure estimation, particularly in low-SNR regimes associated with high b-values or high spatial resolution.

---


### 519. [Attention mechanisms and transfer learning for robust peach leaf damage classification under domain shift](https://arxiv.org/abs/2606.02045)

**<font color=#1a73e8>作者：</font>** Adrián Cánovas-Rodriguez, Miguel A. González-Illán, Maria Fernanda García-Cruz 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence provides a practical framework for crop damage assessment from imagery data, supporting early decision-making in agricultural management. In peach orchards, climate change increases abiotic stress and biotic pressures, including pests and diseases, which often produce visually similar foliar symptoms. This overlap makes manual diagnosis difficult, especially across multiple fields with varying environmental conditions, highlighting the need for automated models with strong generalization ability.
We propose an image-based classification approach for peach leaf damage detection. A benchmark dataset was created through manual annotation of publicly available images, consisting of 1,366 peach leaves across six damage categories. Several deep learning architectures were evaluated. EfficientNet models achieved the best results, with EfficientNetB0 reaching 92.9 percent accuracy, EfficientNetB3 achieving 91.5 percent, and EfficientNetB5 showing the strongest performance on minority classes. DenseNet121 reached 92.6 percent accuracy. The integration of the Convolutional Block Attention Module (CBAM) improved performance in several backbones, particularly EfficientNetB5 and InceptionV3, while showing limited or negative impact in others. The CBAM-enhanced EfficientNetB5 achieved the best overall accuracy of 93.3 percent.
To evaluate robustness under realistic conditions, a local dataset of 180 images across four classes was collected, and transfer learning strategies were applied to address domain shift. Three fine-tuning strategies were tested. EfficientNetB3 combined with CBAM achieved the best performance in the local domain, reaching a 93 percent macro F1-score after transfer. Overall, attention-based models showed improved robustness for minority classes and better generalization across different field conditions.

---


### 520. [Topological texture analysis of microscopy images of dynamic casein gelation and its relation to rheological properties](https://arxiv.org/abs/2606.02048)

**<font color=#1a73e8>作者：</font>** Zahra Tabatabaei, Diana Soto Aguilar, Jose C. Bonilla 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We propose a novel computational toolbox that integrates Topological Data Analysis (TDA), Differential Box Counting (DBC), Multifractal Partition (MFP), and Local Binary Patterns (LBP), applied to time-lapse super-resolution STED microscopy images of sodium caseinate gelation induced by glucono-delta-lactone (GDL) at 30 °C and 40 °C and two GDL concentrations (1.8% and 3.5% w/v).
TDA tracked topological loops, closed ring-like structures reflecting protein network interconnectivity, via max-Betti-1 curves, which revealed a lag phase of dispersed aggregates, a sharp decay coinciding with network percolation and the rheologically observed sol-gel transition, and a post-gelation increase corresponding to network rearrangements. These topological transitions were corroborated by DBC and MFP as these methods were able to resolve changes in structural complexity and spatial heterogeneity. The toolbox was validated on simulated fractal images prior to experimental application. Together, these descriptors provided sensitivity to subtle microstructural transitions that bulk rheology captured as averaged bulk mechanical responses. This integrated approach provides a robust quantitative tool for characterizing complex microstructure in food and material science with evolving microstructural dynamics. Code is available at this https URL

---


### 521. [Explainable Data-driven Deep Reinforcement Learning Methods for Optimal Energy Management in Buildings](https://arxiv.org/abs/2606.02049)

**<font color=#1a73e8>作者：</font>** Hallah Shahid Butt, Qiong Huang, Gökhan Demirel 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The increasing integration of renewable energy sources into power systems, particularly in buildings equipped with photovoltaic (PV) panels and energy storage systems, introduces significant complexity in energy systems. Volatile power generation, varying electricity tariffs, and increased entities, e.g., PV systems, and heat pumps, have increased the complexity and made the system harder to operate. This leads to the demand for additional control and optimization routes including data-based controls, such as reinforcement learning. While deep reinforcement learning (DRL) has emerged as a promising solution to optimize building operations in dynamic and ever more complex environments, its black-box nature impedes user trust and practical adoption. This paper presents a framework for explainable deep reinforcement learning (XRL) applied to energy management in residential buildings. We demonstrate its usage on both synthetic data but also on real-world data from the Living Lab Energy Campus (LLEC) at KIT. We train and compare both on-policy and off-policy DRL agents on an expanded state space that incorporates real-time measurements (demand, PV generation, battery power, state of charge), external signals (dynamic electricity price, local weather data), calendrical and holiday indicators, and forecasts for demand and price. Our experimental results indicate that on-policy algorithms, particularly Advantage Actor Critic (A2C) and Proximal Policy Optimization (PPO), outperform off-policy methods in terms of cumulative rewards and policy stability. To explain these models, we employ post-hoc interpretation techniques to elaborate the learned control policies. Our findings demonstrate that the XRL framework not only reduces electricity costs through optimal battery management, but also provides transparent, actionable insights into the agent's decision-making process.

---


### 522. [eMoT: evolving Memory-of-Thought via Symbolic Anchoring and Memory Corrosion](https://arxiv.org/abs/2606.02054)

**<font color=#1a73e8>作者：</font>** Xiang Li, Jiwei Wei, Ke Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While Large Language Models (LLMs) achieve impressive performance on multi-step reasoning tasks, their reliability is persistently hindered by critical limitations such as unconstrained hallucinations and poor numerical computation. Fundamentally, these issues arise because standard models treat reasoning as a transient, one-off generation process rather than retaining and refining successful procedural logic. To address these challenges, we propose eMoT (evolving Memory-of-Thought), a unified framework that stabilizes multi-step reasoning by treating reasoning trajectories as dynamic, evolving memories rather than static templates. The framework primarily consists of three interconnected modules: (i) a memory corrosion mechanism that reinforces high-utility reasoning structures while gradually decaying less frequent ones; (ii) a symbolic anchoring engine that utilizes Python for deterministic computation, much like a human uses a calculator; and (iii) a consistency-driven refinement process that aligns neural inference with symbolic outcomes, reducing the accumulation of logical discrepancies. Across multiple reasoning benchmarks, eMoT improves accuracy and solution consistency over standard Chain-of-Thought and structured reasoning this http URL the traditional task Game of 24, eMoT achieves 100% accuracy, surpassing the baseline by up to 17.6%. Evaluations on mathematical task GSM8K, ASDiv, SVAMP, and MGSM further show consistent gains in multi-step mathematical reasoning. In our evaluation, we achieve superior performance despite utilizing a lightweight backbone model with constrained baseline capabilities. Compared to alternative methods that rely on massively scaled models, our results demonstrate that the performance gains are fundamentally driven by the eMoT framework's reasoning control rather than sheer model size.

---


### 523. [TIDES: Time-Derivative Event Simulation via Deformable Reconstruction](https://arxiv.org/abs/2606.02058)

**<font color=#1a73e8>作者：</font>** Christopher Thirgood, Dipon Kumar Ghosh, Simon Hadfield  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Event cameras emit asynchronous events in response to environmental appearance changes. The scarcity of real-world event datasets makes simulation essential. However, most simulators infer event timestamps from frame sequences, forcing many threshold crossings to share a small set of discrete times; a failure mode we term timestamp batching that worsens under fast motion and occlusion.
We present TIDES, a continuous-time event simulator built on dynamic Gaussian splatting. Because TIDES operates on an explicit 3D scene representation with learnt geometry and motion, it can derive per-pixel intensity dynamics directly from the scene, rather than by differencing rendered frames. This enables accurate threshold-crossing prediction, including multiple crossings per rendering step, without temporal upsampling or frame interpolation. The same 3D scene model reveals where objects partially occlude one another; TIDES uses this to guide adaptive time stepping, concentrating computation only in regions where occlusion dynamics make simple models of brightness change unreliable.
Finally, we model finite sensor bandwidth using a tile-level arbiter whose throughput, jitter, and event drops reproduce realistic sensor artifacts. Across paired RGB-event benchmarks, TIDES attains state-of-the-art event-stream fidelity. We also show that events simulated by TIDES transfer more effectively to real downstream tasks than competitors'.

---


### 524. [Where Do Deep-Research Agents Go Wrong? Span-Level Error Localization in Agent Trajectories](https://arxiv.org/abs/2606.02060)

**<font color=#1a73e8>作者：</font>** Jiaming Wang, Ziteng Feng, Jiangtao Wu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deep-research agents solve tasks through long trajectories of search, tool use, evidence inspection, and answer synthesis. Evaluation based on final answers shows whether an agent succeeds, but not which parts of the trajectory make the answer unreliable. We study span-level error localization for deep-research agents. We collect 2,790 real trajectories from two agent frameworks, three backbone models, and three benchmarks, convert raw logs into semantic spans, and annotate harmful error spans through LLM-assisted expert review. From these annotations, we build TELBench, a 1,000-instance benchmark for identifying error spans among normal exploration, failed searches, tentative hypotheses, and harmless noise. We further propose DRIFT, a claim-centric auditing framework that tracks agent claims, checks their support in trajectory evidence, and marks spans where unsupported or conflicting claims affect the answer path. Experiments across model families and auditing frameworks show that DRIFT improves span-level error localization and first-error accuracy by up to 30 percentage points. Our work provides a process-level view of reliability in deep-research agents.

---


### 525. [Ablating Archetypes: The Stability of Archetypal SAEs is an Artifact of Initialization and Metric Design](https://arxiv.org/abs/2606.02061)

**<font color=#1a73e8>作者：</font>** Michał Brzozowski, Neo Christopher Chung  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dictionary learning with sparse autoencoders (SAEs) produces overcomplete bases from neural network activations that are often interpretable and reduces polysemanticity. However, features from SAEs vary substantially across random seeds -- a problem known as instability. Archetypal SAEs (Fel et al., 2025) were proposed as a general dictionary-learning intervention for more reliable concept extraction, and report more stable dictionaries at the end of training. We demonstrate that the stability claimed by archetypal SAEs is a result of setting identical initialization across multiple runs. Through our analyses, we attempt to clarify two distinct notions in mechanistic interpretability that may be ambiguously used: stability is agreement between two independently trained models, whereas stabilization is the convergence of independently initialized runs toward a common solution. This distinction is critical for mechanistic interpretability of natural language processing (NLP), where feature stability is increasingly used as evidence that SAE features are reusable units of analysis. Experiments from archetypal SAEs share a deterministic k-means decoder initialization, setting inter-run dictionary distance to zero before training begins. When this initialization is removed, the archetypal constraint provides no stabilization advantage in our setting. We further identify a preprocessing-dependent cosine geometry issue that complicates interpretation of endpoint stability metrics. Overall, our study supports the value of studying SAEs within the larger dictionary-learning tradition while showing that stability claims require trajectory diagnostics and initialization ablations.

---


### 526. [Fast and Lightweight Novel View Synthesis with Differentiable Multiplane Image](https://arxiv.org/abs/2606.02068)

**<font color=#1a73e8>作者：</font>** Kaidi Zhang, Guanxu Zhu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recently, novel view synthesis has witnessed remarkable progress, with mainstream methods such as Neural Radiance Fields (NeRF) and 3D Gaussian Splatting (3DGS) delivering impressive results. However, these approaches often struggle to balance rendering speed and model size, and their optimization-based training can be highly time-consuming. Furthermore, they typically rely on dense observations, often failing to produce satisfactory results under sparse-view conditions. Although feed-forward reconstruction significantly reduces the optimization time of 3DGS, its pixel-aligned formulation generates millions of Gaussians from a single image, severely limiting its practical deployment on mobile devices. To address these limitations, we revisit the Multiplane Image(MPI) representation, which represents scenes using a compact set of planar layers for efficient novel view synthesis. Leveraging recent advances in visual foundation models, we utilize predicted point maps for reliable geometric initialization, followed by differentiable optimization. To address the issues of holes and artifacts in sparsely initialized MPI, we introduce one-step diffusion, which participates in both the differentiable optimization of MPI and the postprocessing of rendering results. Compared with a representative GS-based method, our approach is 30.7% faster and uses only 14.8% of its model size, while achieving competitive synthesis quality on front-view scenarios

---


### 527. [Planar Symmetric Pattern Generation](https://arxiv.org/abs/2606.02073)

**<font color=#1a73e8>作者：</font>** Ning Lin, Luxi Chen, Huaguan Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generating objects with specific symmetries is essential in various real-world scenarios. However, adapting existing 2D continuous representations to enforce planar group symmetry remains a challenge, as the transformation of non-reflective group elements may disrupt continuity. To overcome this limitation, we propose a symmetrization framework for arbitrary planar groups. Our method transforms any 2D continuous representation into a symmetric one while preserving continuity. We provide the mathematical formulation of this representation, demonstrate its approximation capability for symmetric functions, and detail the construction methodology. We validate our approach through three visual design tasks (pattern design, paper-cutting design and stylized topology design) and one material design task. Experiments confirm that our representation enables effective symmetry control and demonstrate its broader applicability.

---


### 528. [Beyond $\ell_2$-norm and $\ell_\infty$-norm: A Curvature-Inspired $\ell_p$-Norm Scheme for Deep Neural Networks](https://arxiv.org/abs/2606.02078)

**<font color=#1a73e8>作者：</font>** Jianhao Xu, Zhuang Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The existing optimizers for deep neural networks (DNNs) typically rely on either the $\ell_2$ norm or the $\ell_\infty$ norm, resulting in optimizers that do not adapt well to substantial changes in curvature across parameter dimensions. Generally, the training process of DNNs often exhibits strong curvature anisotropy in the early period, whereas in the later period, the training process of DNNs tends to move toward flatter regions with weaker anisotropy. Particularly, optimizers based on the \(\ell_2\)-norm are usually dominated by high-curvature directions, restricting updates of optimizers along with lower curvature direction and thus leading to a slower convergence rate. While optimizers based on the \(\ell_\infty\)-norm are prone to oscillations in flatter regions, due to the coordinate-wise updates of the same magnitude. To address these two extreme cases generated by $\ell_2$ and $\ell_\infty$ norms, we propose a novel $\ell_p$-norm scheme with a dynamical value of $p$ and incorporate it into stochastic gradient descent (SGD) and SGD with momentum (SGDM), leading to two novel optimizers with better generalization performance: ${\ell_p}$-SGD (LPSGD) and ${\ell_p}$-SGDM (LPSGDM). Particularly, the resulting optimizers suppress the dominance of high-curvature directions in the early period by utilizing a large $p$ ($p>2$), followed by a gradual decrease of $p$ toward 2 to enable more stable and refined updates, where the latter process is motivated by the cosine annealing strategy. We establish theoretical guarantees of the resulting algorithms and analyze that both LPSGD and LPSGDM achieve an \(O(T^{-1/2})\) convergence rate for the nonconvex setting. Extensive experiments are conducted on benchmark datasets, including CIFAR-10, CIFAR-100, and ImageNet-1K, with multiple DNNs such as VGG-11, ResNet-18, and ResNet-50.

---


### 529. [FACT: A Simple and Efficient Framework for Active Finetuning](https://arxiv.org/abs/2606.02079)

**<font color=#1a73e8>作者：</font>** Wenshuai Xu, You Song, Yuzhuo Cui 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The main goal of active finetuning is to improve a pretrained model's performance on a specific task or domain by finetuning it with carefully selected informative or challenging data. Previous research has predominantly focused on the active aspect (i.e., data selection) while uniformly employing full finetuning for model adaptation, which inevitably distorts pretrained features due to distribution shift. This issue becomes particularly pronounced when the model size is large relative to the finetuning data quantity, leading to heightened overfitting risks. To address this critical gap, we formally outline the FiAF task that emphasizes systematic exploration of finetuning methodologies in active learning. We propose FACT, a three-phase hierarchical finetuning framework featuring both efficiency and simplicity, specifically designed for active finetuning scenarios. Our comprehensive experiments span: (1) Three major dataset categories encompassing classic (CIFAR10, CIFAR100, ImageNet-1k), imbalanced (CIFAR10-LT, CIFAR100-LT), and fine-grained (StanfordCars, FGVCAircraft) image classification datasets, each evaluated under 3-5 distinct sampling ratios; (2) Diverse pretrained architectures including Convolutional Neural Network (ConvNeXt), Vision Transformer (ViT), and Vision LSTM (ViL) networks; (3) A systematic investigation of frozen feature augmentation (FroFA) strategies. (4) A comprehensive and rigorous analysis of efficiency and generalizability. The results demonstrate significant improvements with strong generalization and robustness. Notably, under low sampling ratios, our framework achieves remarkable performance gains of over 20% on the ViT model for CIFAR10, CIFAR100, and ImageNet-1k benchmarks. This systematic approach establishes new state-of-the-art performance while maintaining parameter efficiency, proving particularly effective when labeled data is scarce.

---


### 530. [Overview of the ClinicalSkillQA 2026 Shared Task on Continuous Perception and Procedural Reasoning in Clinical Skill Assessment](https://arxiv.org/abs/2606.02082)

**<font color=#1a73e8>作者：</font>** Xiyang Huang, Renxiong Wei, Yihuai Xu 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This paper presents an overview of the ClinicalSkillQA 2026 shared task, which was organized with the BioNLP Workshop at ACL 2026. The goal of this shared task is to evaluate continuous perception and procedural reasoning in clinical skill assessment by requiring systems to reconstruct the correct temporal order of shuffled clinical key frames and generate rationales grounded in clinical workflow knowledge. The benchmark contains 200 test-only instances sampled from clinical skill videos, covering three emergency-care procedures. Each instance is annotated with the ground-truth temporal order and an expert-verified rationale. A total of seven teams participated in the task, collectively making 90 submissions, with four teams providing system description papers. Systems are evaluated using Task Accuracy, Pairwise Accuracy, and BERTScore, which measure exact sequence reconstruction, local temporal consistency, and rationale quality, respectively. In this paper, we describe the task setup, dataset construction, and evaluation criteria. We further summarize the methodologies adopted by participating teams and present a comprehensive analysis of the submitted systems. The official results suggest that current models still struggle with continuous perception and procedural reasoning, especially when they must integrate visual evidence, temporal structure, and clinical workflow knowledge.

---


### 531. [FocusDiT: Masking Queries in Diffusion Transformers for Fine-grained Image Generation](https://arxiv.org/abs/2606.02090)

**<font color=#1a73e8>作者：</font>** Xueji Fang, Liyuan Ma, Jianhao Zeng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion transformer (DiT) has been widely adopted in the generative diffusion field, advancing the denoising of query tokens through attention and Feed-Forward (\text{FFN}) layers. FFN actually acts as the key-value vocabulary for decoding visual contents where the value embeds the visual semantical knowledge. We present that focusing on critical query tokens corresponding to more complex details and encouraging the model to improve these tokens is essential for fine-grained visual generation. To this end, we propose FocusDiT, which applies a Masking scheme to focus on critical query tokens that are exclusively fed into FFN. The masked queries can retrieve visual tokens from the FFN vocabularies, and use them to decode their visual details. Extensive text-to-image experiments validate the effectiveness of token masking in enhancing generative performance.

---


### 532. [The Role of Ambiguity in Error Prediction via Uncertainty Quantification](https://arxiv.org/abs/2606.02093)

**<font color=#1a73e8>作者：</font>** Ieva Raminta Staliūnaitė, James Bishop, Andreas Vlachos  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The task of Error Prediction, namely predicting whether a model output is correct, is commonly tackled with Uncertainty Quantification (UQ). However, while uncertainty metrics capture when models lack knowledge or capacity to make a prediction, they also reflect aleatoric uncertainty, which is inherent in the model input and context. This paper presents a method for improving error prediction for Large Language Models (LLMs), by disentangling input ambiguity from UQ signal. We conduct experiments on the task of Question Answering (QA) with six UQ metrics and show that UQ metrics are more predictive of errors on unambiguous instances than on questions with multiple plausible answers. We use Gated Experts and Selective Prediction to incorporate gold and predicted ambiguity labels into the error prediction pipeline. We find that ambiguity information improves error prediction scores across model families, training and evaluation paradigms, datasets (including allegedly unambiguous ones), and sources of aleatoric uncertainty, yielding improvements of over 10 points of PRR for individual UQ metrics on standard datasets.

---


### 533. [WebSpline: Structure-Informed Splines for Real-Time 3D Gaussians from Monocular Videos](https://arxiv.org/abs/2606.02096)

**<font color=#1a73e8>作者：</font>** Jongmin Park, Jeonghwan Yun, Minh-Quan Viet Bui 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dynamic scene reconstruction from monocular videos remains highly challenging, as existing methods often struggle to balance global structural coherence and local fine-grained details under limited multi-view cues. To address this challenge, we propose WebSpline, a novel dynamic 3D Gaussian framework that enables structurally coherent and high-fidelity reconstruction from monocular videos with fast rendering. The core of WebSpline is the Structure-Informed Spline (SIS) representation, which models each dynamic Gaussian trajectory using a learnable cubic Hermite spline whose motion is structurally organized with an auxiliary Structural Proxy Graph (SPG). The proposed framework is optimized in two stages: (i) in the first stage, the SPG is initialized from 2D point tracks and refined with temporal rigidity regularization to establish structural coherence for moving objects across the sequence; and (ii) in the second stage, the SIS representation is initialized from the refined SPG and optimized under both spatial and structural neighborhood constraints. At inference, Gaussian motion is obtained solely by evaluating the learned SIS, enabling fast rendering. Extensive experiments on the challenging monocular dynamic scene benchmarks, iPhone and NVIDIA, demonstrate that our WebSpline achieves state-of-the-art rendering quality while rendering over 10 times faster than WorldTree, the second-best method on the iPhone dataset.

---


### 534. [How Hard Can It Be? Hardness-Aware Multi-Objective Unlearning](https://arxiv.org/abs/2606.02119)

**<font color=#1a73e8>作者：</font>** Jiangwei Chen, Xinyuan Niu, Rachael Hwee Ling Sim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine unlearning aims to remove the influence of specific forget training data due to privacy, copyright or bias concerns while maintaining the model performance on the remaining retain data. Existing unlearning algorithms, such as optimizing a weighted combination of losses, have tried to achieve these objectives of improving forget quality and maintaining retain utility. However, they do not guarantee that these objectives can be improved by a specified extent for all forget and retain data. In this work, we address this limitation with a novel and theoretically-grounded approach from a constrained optimization perspective. Firstly, we identify that the hardness of reconciling both objectives can be quantified by the similarity between the forget data and the retain data. Next, we derive an unlearning algorithm (HAMU) with the overall goal of guaranteeing a specified improvement in forget quality while minimizing the retain utility cost/degradation by updating the model weights based on our hardness measure. Our hardness measure also informs users when retain utility degradation is unavoidable, i.e., both objectives cannot be improved simultaneously, and stopping should be considered. Our algorithm is applicable to non-convex models and is easily parallelizable, making it readily deployable in real-world scenarios. We empirically demonstrate HAMU's superior performance over baselines on both image and text datasets using large models. Our code is available at this https URL.

---


### 535. [Understanding-Enhanced Model Collaboration for Long-Tailed Egocentric Mistake Detection](https://arxiv.org/abs/2606.02120)

**<font color=#1a73e8>作者：</font>** Boyu Han, Qianqian Xu, Shilong Bao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this report, we address the problem of determining whether a user performs an action incorrectly from egocentric video data. To this end, we propose an Understanding-Enhanced Model Collaboration Method (UE-MCM) that combines efficient coarse-grained video understanding with accurate fine-grained action reasoning. Specifically, UE-MCM contains a small model branch and a large model branch. The large model branch focuses on whether the fine-grained action itself is executed incorrectly, while the small model branch jointly takes the coarse-grained video and fine-grained segment as input to identify actions that may be locally correct but inconsistent with the overall workflow. The small model branch is built on a CLIP4CLIP video encoder initialized from a CLIP model enhanced by Diffusion Contrastive Reconstruction, and the large model branch uses the Qwen3-VL Embedding model to extract high-capacity representations from fine-grained action segments. The small-branch prediction and the large-branch prediction are then adaptively fused by a lightweight collaboration gate. To handle the long-tailed distribution of mistake instances, we optimize the classifiers with complementary objectives, including reweighted cross-entropy, AUC-oriented learning, and label-aware adjustment. The resulting system balances speed and accuracy, making it effective for detecting subtle, rare, and ambiguous mistakes in egocentric instructional videos.

---


### 536. [PeAR: A Static Binary Rewriting Framework for Binary-Only Fuzzing](https://arxiv.org/abs/2606.02126)

**<font color=#1a73e8>作者：</font>** Alvin Charles, Adrian Herrera, Peter Oslington 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Binary-only fuzzing is a key technique for finding bugs in close-source software. Without access to source code, the fuzzer must rely on static or dynamic binary instrumentation for coverage guidance. In practice, most fuzzers favor dynamic binary instrumentation (DBI), accepting runtime overhead to avoid the perceived accuracy and soundness challenges associated with static binary instrumentation (SBI). We show that these concerns are unwarranted, and that accurate, scalable~SBI is achievable using off-the-shelf frameworks. Building on these frameworks, we develop PeAR, an extensible binary-only fuzzing framework. We demonstrate PeAR's versatility by implementing several modern fuzzer features -- including, deferred initialization, persistent mode, and shared-memory fuzzing.
We evaluate PeAR over 4.25 CPU-yrs of fuzzing on the FUZZBENCH benchmark and find that PeAR: (i) successfully instruments 88% of FUZZBENCH targets, comparable to the best SBI-based fuzzers; (ii) achieves a median throughput improvement of 4x when using persistent mode and shared memory fuzzing; and (iii) attains coverage comparable to compiler-based instrumentation.
Our results show that SBI is a practical and effective technique for binary-only fuzzing, and that modern binary rewriting frameworks can apply complex instrumentation with high granularity and negligible performance compromise.

---


### 537. [Equilibrated Diffusion: Frequency-aware Textual Embedding for Equilibrated Image Customization](https://arxiv.org/abs/2606.02129)

**<font color=#1a73e8>作者：</font>** Liyuan Ma, Xueji Fang, Guo-Jun Qi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image customization learns target subjects from reference concept images and generates conditioned images per text prompts, mainly modifying styles or backgrounds. Prevailing methods adopt fine-tuning to pack diverse concept attributes into a unified latent embedding, yet entangled attributes hinder elimination of irrelevant disturbances from style and background. To address this issue, we propose Equilibrated Diffusion, a frequency-driven approach that disentangles tangled concept features for balanced customization and consistent text-visual matching. Unlike conventional methods learning full concepts with shared embeddings and unified tuning, our work utilizes the inherent link between image frequency components and semantics: low frequencies represent subject content and high frequencies correspond to styles. We decompose concepts in frequency space and optimize each embedding independently. This separate optimization enables the denoiser to capture style detached from subject identity and generalize better to unseen stylistic prompts. Merging multi-frequency embeddings preserves the model's original spatial customization ability. We further deploy mask-guided diffusion to restrict irrelevant background changes and boost text alignment. Residual Reference Attention (RRA) is inserted into spatial attention to retain subject structure and identity consistency. Experiments prove Equilibrated Diffusion exceeds mainstream baselines on subject fidelity and text adherence, verifying our method's superiority.

---


### 538. [Variational Learning for Insertion-based Generation](https://arxiv.org/abs/2606.02133)

**<font color=#1a73e8>作者：</font>** Yangtian Zhang, Zhe Wang, Arthur Gretton 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Non-monotonic sequence generation methods, such as masked diffusion models, provide a flexible alternative to left-to-right autoregressive modeling by allowing tokens to be generated in non-fixed and prescribed orders. Despite their practical advantages, most existing non-monotonic models are order-agnostic and rely on a fixed-length grid, limiting their ability to support variable-length generation and adaptive insertion order. In this work, we introduce a probabilistic framework for learning insertion order in variable-length insertion models. We formalize a bijective correspondence between insertion trajectories and permutations, which enables an exact reparameterization of the data likelihood as a sum over permutations. Building on this result, we propose the Insertion Process (IP), a stochastic generative model that jointly learns where to insert, what to insert, and when to terminate, trained via permutation-based variational inference. Unlike prior fixed-canvas approaches, IP natively supports variable-length generation and learns data-driven preferences over insertion orders. Experiments on goal-conditioned planning and molecular string generation demonstrate that learning insertion order improves both modeling quality and generalization in domains without a canonical left-to-right structure.

---


### 539. [Rethinking Evaluation Paradigms in IBP-based Certified Training](https://arxiv.org/abs/2606.02134)

**<font color=#1a73e8>作者：</font>** Konstantin Kaulen, Hadar Shavit, Holger H. Hoos  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep neural networks achieve strong performance on many supervised learning tasks but remain vulnerable to adversarial perturbations. Neural network verification provides mathematically rigorous robustness guarantees, yet at substantial computational cost. To mitigate this, certified training techniques optimise for verifiable robustness during training, typically inducing a trade-off between natural and certified accuracy controlled by method-specific hyperparameters. Because these metrics are inherently conflicting, the common practice of reporting a single configuration is problematic: it can mislead conclusions about overall performance and prevents unbiased assessments of the state of the art. We address this by evaluating certified training methods via Pareto front comparisons over the natural--certified accuracy trade-off. To enable fair, method-agnostic comparisons, we perform efficient automated multi-objective hyperparameter optimisation to identify a set of Pareto-optimal configurations for each method. This approach often uncovers substantial undertuning in previously reported configurations, yielding superior performance and establishing a new state of the art. Leveraging these fronts, we present the first comprehensive multi-objective comparison of certified training approaches, showing that prior advancements are less pronounced than assumed and revealing previously unreported performance complementarities.

---


### 540. [Edge-aware Decoding for Neural Asymmetric Routing](https://arxiv.org/abs/2606.02136)

**<font color=#1a73e8>作者：</font>** Li Liang, Jinbiao Chen, Zizhen Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural asymmetric routing models increasingly encode directionality through matrix representations and asymmetry-aware attention. The final routing action, however, is not a node in isolation but a directed transition chosen under the current partial route. This creates a representation--decision mismatch: pairwise cost information may be encoded upstream while the final candidate logit is still largely parameterized as context--node compatibility. We propose a decoder-design principle for neural asymmetric routing: the final score should explicitly expose transition-level quantities suggested by the problem's cost-to-go structure. We instantiate this principle with an edge-aware decoder that adds candidate-specific terms for the current directed edge, return-to-start closure, and static lightweight lookahead, while keeping the representation backbone fixed. On a controlled SVD/Sinkhorn asymmetric backbone, the decoder improves over the RADAR reference when trained on ATSP-100 and evaluated zero-shot on ATSP-100/200/500/1000, reducing the ATSP-1000 gap from $4.13\%$ to $2.73\%$. On ACVRP, the same score-level modification shows the same qualitative trend under a richer routing state. ATSP ablations and directed-transition diagnostics sharpen the mechanism: the strongest evidence concerns sensitivity to the current directed edge, while closure and static lookahead act as heuristic continuation cues. The results support a mechanism study: a key decoder-side signal in neural asymmetric routing is decision-time exposure of transition-level edge information.

---


### 541. [VLBM: Variational Latent Basis Modeling for OOD Robust Multivariate Time Series Forecasting](https://arxiv.org/abs/2606.02138)

**<font color=#1a73e8>作者：</font>** Xudong Zhang, Jierui Lei, Jiacheng Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Out of distribution (OOD) events in multivariate time series forecasting are rare but often dominate real world risk, making average case forecasting insufficient for reliable deployment. Under standard average risk training on mixed ID/OOD distributions, optimization signals from rare OOD events can be overwhelmed by frequent in distribution (ID) patterns, so strong benchmark accuracy may not translate into reliability under high impact shifts. To address this issue, we propose VLBM (Variational Latent Basis Model), a theory guided latent forecasting framework that separates stable dynamics from OOD induced deviations. VLBM learns a shared latent basis that defines a low rank subspace for stable ID dynamics, explicitly decomposes inputs into basis subspace components and orthogonal residual components, and aligns a future aware posterior with a future blind prior so that test time latent inference depends only on historical input. Across 12 benchmark tasks spanning transportation, weather, power systems, and other real world domains, including newly constructed real world OOD traffic datasets, VLBM achieves state of the art OOD robustness and ID accuracy, with average MAE and MSE gains of 15.08\% and 7.74\% over the strongest baseline. On a synthetic simulation dataset, VLBM also consistently achieves the best performance and better tracks OOD pulse recovery. These results support latent structured forecasting as a principled route to robust prediction under mixed ID and OOD conditions. The code is available at this https URL.

---


### 542. [TimeBlocks: Foundational and Continual Time-Series Blockbase -- Extended Version](https://arxiv.org/abs/2606.02142)

**<font color=#1a73e8>作者：</font>** David Campos, Bin Yang, Tung Kieu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The ongoing digitization has led to a proliferation of time-series data streams that monitor a variety of processes, from which valuable insights may be obtained. Further, the emergence of successful foundational language models begs the question of whether it is possible to achieve time-series models with the foundational properties of handling multiple tasks, while being sufficiently lightweight to allow real-time data stream processing. Existing foundational time-series models are often large and only effective in offline settings without stringent time and computational constraints, and where repeated model calibration is not needed. However, when applied to data streams, these models are ineffective due to their size and lack of support for continual calibration, which compromise their ability to deliver accurate real-time responses, their durability, and their deployability in hardware-limited settings. We propose TimeBlocks to enable versatile time-series processing by facilitating the efficient building of lightweight models suitable for multiple tasks under variable conditions. In particular, the method maintains a pool of interchangeable and modular model blocks that can be used to construct new time-series models. When presented with specific time-series data, a routing strategy iteratively selects the most suitable blocks to construct a lightweight and accurate model for the data. We equip TimeBlocks with a method called StreamCore to build a representative small subset of the data stream, which preserves a guaranteed approximation of the stream over time, enabling continual model calibration. An experimental study on multiple data sets and covering multiple tasks shows that TimeBlocks enables to build models capable of outperforming existing baselines.

---


### 543. [Hybrid Neural Ordinary Differential Equations for Data-Efficient Polymerization Modeling with Incomplete Kinetics](https://arxiv.org/abs/2606.02145)

**<font color=#1a73e8>作者：</font>** Marah Almanasreh, Alexander Mitsos, Eike Cramer  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate prediction of polymerization dynamics is essential for process design, control, and optimization. Yet, purely mechanistic models require labor-intensive parameterization of partially characterized kinetics, while purely data-driven models demand large, diverse datasets that are costly to obtain, particularly in early-design stages. We propose a hybrid Neural Ordinary Differential Equation (NODE) framework for data-efficient modeling of free-radical polymerization. Using batch polymerization of methyl methacrylate (MMA) as a case study, the mechanistic mass balances are retained explicitly, and only the partially-characterized effective radical concentration governing monomer consumption is learned from data through a neural network surrogate, while established reactions such as initiator decomposition, propagation, and termination remain physically modeled. The hybrid NODE is evaluated against a discrete-time feedforward neural network and a purely data-driven NODE under sparse data conditions, with models trained on as few as ten measurements under both regular and irregular sampling. The hybrid NODE consistently achieves lower prediction errors and more physically consistent extrapolations than both purely data-driven baselines. In a generalization scenario with noisy data and unseen operating conditions, the hybrid NODE achieves an RMSE of 0.013, compared to 0.31 for the data-driven NODE and 0.68 for the discrete-time model, demonstrating that learning only a closure term rather than the full dynamics is sufficient for reliable prediction under limited data availability.

---


### 544. [Multilingual Idioms in Sentences and Conversations Across High-, Medium-, and Low-Resource Languages](https://arxiv.org/abs/2606.02147)

**<font color=#1a73e8>作者：</font>** Saeed Almheiri, Bilal Elbouardi, Salsabila Zahirah Pranida 等 19 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Idiomatic expressions pose a major challenge for multilingual NLP because their meanings shift between figurative and literal usage, often requiring context for accurate interpretation. Prior work has focused on high-resource languages typically evaluates isolated idiom-meaning questions, overlooking realistic discourse. We introduce MIDI, a multilingual idiom dataset spanning 3 high-, 3 medium-, and 12 low-resource languages, curated by native speakers. Unlike previous datasets, MIDI provides idioms embedded in both sentence-level and conversational contexts, capturing both literal and figurative readings. Benchmarking state-of-the-art models shows that idiom comprehension degrades in low-resource languages and that, in all resource tiers, literal interpretations are substantially harder than figurative ones. Conversational context improves performance but does not eliminate these disparities. Through controlled tests and interventions on hidden representations, we further separate memorization from reasoning, exposing core limitations of current models.

---


### 545. [S3TS: Stochastic Scenario-Structured Tree Search for Advanced Planning Under Uncertainty](https://arxiv.org/abs/2606.02151)

**<font color=#1a73e8>作者：</font>** Fabio Pavirani, Bert Claessens, Pierre Pinson 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Effective scheduling in the energy sector is essential to ensure the reliable operation of electrical grids and their connected assets by, for instance, optimizing the dispatch of generation units and storage systems. An effective planning strategy must (a) accommodate advanced and potentially non-linear system models -- exploiting the increasing data availability of modern grids, and (b) explicitly handle uncertainties arising, for instance, from the integration of renewable energy sources. While existing approaches can address either non-linearity (e.g., Monte Carlo Tree Search) or uncertainty (e.g., stochastic mathematical optimization), there is a lack of planning techniques capable of addressing both challenges simultaneously. To bridge this gap, we propose a Stochastic Scenario-Structured Tree Search (S3TS) algorithm that explicitly represents uncertainty through scenario trees while enabling the integration of advanced non-linear models. We evaluate S3TS on a simulated demand response signal publication problem, largely mimicking the imbalance settlement mechanism in Belgium. The results demonstrate near-optimal performance in linear, analytically tractable settings, with costs within 14% of the mathematically optimal solution conditioned to the scenario trees. In highly non-linear scenarios, S3TS significantly outperforms baseline methods, achieving cost reductions of up to 51% and 5.4% compared to a myopic algorithm and deterministic MCTS, respectively.

---


### 546. [Ultra Diffusion Poser: Diffusion-Based Human Motion Tracking From Sparse Inertial Sensors and Ranging-Based Between-Sensor Distances](https://arxiv.org/abs/2606.02153)

**<font color=#1a73e8>作者：</font>** Dominik Hollidt, Tommaso Bendinelli, Christian Holz  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Methods using inertial measurement units (IMUs) provide a wearable alternative to camera-based motion capture. To mitigate drift from inertial signals, recent sparse inertial pose estimators integrate inter-sensor distances measured by ultra-wideband (UWB) ranging. So far, UWB distances have only been used as an additional input feature, ignoring the physical constraints they impose on sensor positions. However, these distances can also be used to reconstruct the underlying 3D sensor layout, which in turn provides more informative input for pose reconstruction. We propose Ultra Diffusion Poser, a diffusion model that explicitly models these geometric constraints. It includes a Spatial Layout Module that analytically reconstructs the 3D sensor positions from UWB measurements. These sensor positions are used alongside IMU signals and UWB distances as a conditioning signal during diffusion. Still, network predictions can violate inter-sensor distance measurements. To address this, we introduce UWB-Diffusion Guidance, which encourages alignment between predicted poses and measured distances during diffusion sampling. Together, these contributions enable our model to achieve state-of-the-art performance, reducing joint position error by up to 22% over prior work.

---


### 547. [On the Salience of Low-Probability Tokens for AI-Generated Text Detection: A Multiscale Uncertainty Perspective](https://arxiv.org/abs/2606.02158)

**<font color=#1a73e8>作者：</font>** Yikai Guo, Bin Wang, Xilai Fan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> AI-generated text increasingly blends with human writing, raising practical risks such as misinformation, academic misuse, and corpora contamination. While statistical detectors are appealing for efficiency and generalization, they suffer from two key limitations. (i) Boilerplate dominance, boilerplate tokens shared across human and LLM writing can overwhelm discriminative signals. (ii) Brittle point estimates, relying on a single probability score yields unstable decisions under adversarial manipulations. To address these issues, we propose Uncertainty, a multiscale uncertainty estimator that focuses on informative low-probability tokens, which more clearly expose distributional discrepancies. Locally, it alleviates boilerplate dominance by averaging the log-probabilities of low-probability tokens; globally, it reduces brittleness by capturing the distributional shape of this low-probability region via Rényi entropy. We further extend the detector to Uncertainty++ via conditional independent sampling, yielding a more stable uncertainty estimation. Experiments across seven datasets and sixteen LLMs demonstrate high effectiveness, generalization, and robustness. Our code is available at this https URL.

---


### 548. [An Abstract Worlds Semantic Framework for Belief Change Operators](https://arxiv.org/abs/2606.02163)

**<font color=#1a73e8>作者：</font>** Daniel Grimaldi, M. Vanina Martinez, Ricardo O. Rodriguez  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This article proposes a set-theoretic framework for belief change, called Abstract Worlds Semantics, in which no logical syntax is assumed. Inspired by Grove's (1988) results, our approach treats worlds as primitive elements, over which world contraction and world revision operators are defined. This semantic framework enables a unified analysis of belief change models. Within this framework, we unify classical and non-prioritized belief change constructions by defining versatile operators. When classical propositional logic is considered, our framework provides a homogeneous account of AGM, KM, and Multiple Change models. In summary, AWS systematizes belief change frameworks and operators, simplifying and generalizing belief change theory over belief sets.

---


### 549. [EEG-FuseFormer: A Transformer-Driven Feature Fusion Framework for Seizure Onset Prediction](https://arxiv.org/abs/2606.02166)

**<font color=#1a73e8>作者：</font>** Vigneshwar Hariharan, Chithra Reghuvaran, Arlene John 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Epilepsy is one of the most common neurological disorders globally, characterized by recurring seizures and significantly impacting the quality of life. Despite advancements in diagnostic techniques, the mitigation of risks faced by epilepsy patients remains challenging due to the unpredictability of seizure events. An accurate forecast of seizure onset helps to reduce risks in epilepsy patients. In this paper, we propose EEG-FuseFormer, a transformer-based feature fusion framework for seizure-onset prediction that combines intermediate features extracted from Convolutional Neural Networks-Long Short-Term Memory (CNN-LSTM) and ResNet-18 networks. The CNN-LSTM architecture captures both spatial and temporal features directly from the raw signal, whereas the ResNet-18 extracts features from the Short-Time Fourier Transform (STFT) representation of the EEG signals. Fusion is carried out using a transformer encoder, and the final prediction is generated using fully connected dense layers. The CHB-MIT dataset was used to validate the proposed model. The results show that the proposed model achieves a mean recall of 98.85% and outperforms most of the state-of-the-art methods. This study evaluates the ability of the proposed feature fusion model to generalize in cross-patient testing scenarios. Fine-tuning pre-trained models on limited target patient data (target adaptation) within the cross-patient validation framework results in higher recall, precision, and F1-score metrics in comparison to the conventional cross-patient validation approach. Finally, the runtime-based computational complexity of the model is assessed across diverse hardware platforms to highlight the performance-complexity trade-off.

---


### 550. [From Capability Models to Automated Planning: An AAS-Native Approach for Automatic PDDL Generation](https://arxiv.org/abs/2606.02167)

**<font color=#1a73e8>作者：</font>** Hamied Nabizada, Thomas Wirt, Luis Miguel Vieira da Silva 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Engineers designing production systems need to verify that a given layout supports all required production sequences. Automated planning techniques can answer such questions, but formulating the required planning problems in the Planning Domain Definition Language (PDDL) demands specialized expertise that production engineers typically lack. Asset Administration Shells (AAS) have emerged as the standardized Digital Twin for industrial assets in Industry 4.0. We show that AAS capability models, structured using four established Industry 4.0 standards (VDI 3682 for process descriptions, IEC 61360-1 for semantic property qualification, IDTA 02011 for type hierarchies, and IDTA 02016 for instance descriptions), contain sufficient information to generate complete PDDL problems automatically. Unlike prior work that introduced PDDL-specific submodels, our approach derives all planning elements from domain-level descriptions of resource functions, so-called capabilities, allowing engineers to model capabilities without any exposure to PDDL syntax or planning concepts. Our extraction algorithm transforms distributed Multi-AAS architectures into complete PDDL planning problems. We validate the approach on AAS models of a laboratory production system, comparing four layout variants using optimal planning to demonstrate how engineers can systematically explore design trade-offs by modifying the AAS model and regenerating the planning domain

---


> [!TIP]
> 当前位于：**501-550**（第 11/14 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | **501-550** | [551-600](./part-12.md) | [601-650](./part-13.md) | [651-651](./part-14.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
