# 📦 其他研究 | 2026年05月15日

> 本类共 **328** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**251-300**（第 6/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-328](./part-07.md)

---

### 251. [Limits of Personalizing Differential Privacy Budgets](https://arxiv.org/abs/2605.13503)

**<font color=#1a73e8>作者：</font>** Edwige Cyffers, Juba Ziani  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> A key technical difficulty in differential privacy is selecting a privacy budget that satisfies privacy requirements while maximizing utility. A natural and well-studied workaround is to use personalized privacy budgets, which may differ across agents. In this paper, we show that personalized budgets come with major limitations and that for mean estimation, the dominant factor is not full personalization, but rather choosing the right effective privacy budget. This can be achieved through a simple thresholding operator that we describe. Compared with this thresholding baseline, the gains obtained by fully personalized mechanisms are limited. In particular, we precisely quantify the constant-factor improvement in settings with mixed private and public datasets and in private datasets with two levels of privacy requirements. We also establish upper bounds and identify regimes of maximal gain for arbitrary privacy requirements.

---


### 252. [ArcVQ-VAE: A Spherical Vector Quantization Framework with ArcCosine Additive Margin](https://arxiv.org/abs/2605.13517)

**<font color=#1a73e8>作者：</font>** Jaeyung Kim, YoungJoon Yoo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vector Quantized Variational Autoencoder (VQ-VAE) has become a fundamental framework for learning discrete representations in image modeling. However, VQ-VAE models must tokenize entire images using a finite set of codebook vectors, and this capacity limitation restricts their ability to capture rich and diverse representations. In this paper, we propose ArcCosine Additive Margin VQ-VAE (ArcVQ-VAE), a novel vector quantization framework that introduces a spherical angular-margin prior (SAMP) for the codebook of a conventional VQ-VAE. The proposed SAMP consists of Ball-Bounded Norm Regularization, which constrains all codebook vectors within a time-dependent Euclidean ball, and ArcCosine Additive Margin Loss, which encourages greater angular separability among latent vectors. This formulation promotes more discriminative and uniformly dispersed latent representations within the constrained space, thereby improving effective latent-space coverage and leading to improved codebook utilization. Experimental results on standard image reconstruction and generation tasks show that ArcVQ-VAE achieves competitive performance against baseline models in terms of reconstruction accuracy, representation diversity, and sample quality. The code is available at: this https URL

---


### 253. [Beyond VMAF: Towards Application-Specific Metrics for Teleoperation Video](https://arxiv.org/abs/2605.13525)

**<font color=#1a73e8>作者：</font>** Ines Trautmannsheimer, Richard Grauberger, Frank Diermeyer  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Automated driving has made remarkable progress, yet situations still arise where human intervention is necessary. Teleoperation provides a scalable solution to address such cases, enabling remote operators to support vehicles without being physically present. In this context, video transmission forms the operator's primary source of situational awareness, making video quality a decisive factor for both safety and task performance. In an online study, participants rated compressed video sequences from the Zenseact Dataset and provided subjective quality ratings. These ratings were then used to retrain the Video Multi-Method Assessment Fusion (VMAF) model, yielding an adapted variant tailored to teleoperation. The retrained model demonstrated improved alignment with human ratings compared to the original 4K VMAF. In particular, RMSE decreased from 10.36 to 8.83, and MAD from 8.71 to 6.38, corresponding to improvements of 15% and 27%, respectively. These results highlight that incorporating domain-specific data can enhance the predictive power of established quality metrics in safety-critical applications. At the same time, Outlier cases emerged in which videos received high objective scores despite noticeable degradations in regions critical for the driving task.

---


### 254. [AI-Generated Slides: Are They Good? Can Students Tell?](https://arxiv.org/abs/2605.13532)

**<font color=#1a73e8>作者：</font>** Juho Leinonen, Lisa Zhang, Arto Hellas  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As generative AI (GenAI) tools become easily accessible, there is promise in using such tools to support instructors. To that end, this paper examines using GenAI to help generate slides from instructor authored course notes, emphasizing instructor and student perceptions. We examine an end-to-end education tool (NotebookLM), two general-purpose LLMs (Claude, M365 Copilot), and two coding assistants (Cursor, Claude Code). We first analyze whether GenAI generated slides are ``good'' via narrative assessment by educators. We choose the best slides to use (with some modification) in a real course setting, and compare the student perception of human vs. AI generated slides. We find that coding assistant tools produce slides that were most accurate, complete, and pedagogically sound. Additionally, students rate GenAI slides to be of similar quality as instructor-created slides, and cannot reliably identify which slides are AI-generated. Additionally, we find a negative correlation between a high quality rating and a high ``AI-generated'' rating, suggesting students associate poor quality with the source of the slides being AI. These findings highlight promising opportunities for integrating GenAI into instructional design workflows and call for further research on how educators can best harness such tools responsibly and effectively.

---


### 255. [Scaling Retrieval-Augmented Reasoning with Parallel Search and Explicit Merging](https://arxiv.org/abs/2605.13534)

**<font color=#1a73e8>作者：</font>** Jiabei Liu, Wenyu Mao, Junfei Tan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deep search agents have proven effective in enhancing LLMs by retrieving external knowledge during multi-step reasoning. However, existing methods often generate a single query for retrieval at each reasoning step, limiting information coverage and introducing high noise. This may result in low signal-to-noise ratios (SNR) during search, degrading reasoning accuracy and leading to unnecessary reasoning steps. In this paper, we introduce MultiSearch, an RL-based framework that addresses these limitations through multi-query retrieval and explicit merging of retrieved information. At each reasoning step, MultiSearch generates queries from multiple perspectives and retrieves external information in parallel, expanding the scope of relevant information and mitigating the reliance on any single retrieval result. Then, the agent consolidates and refines retrieved information at the merging process, improving the SNR and ensuring more accurate reasoning. Additionally, we propose a reinforcement learning framework with a multi-process reward design to optimize agents for both multi-query retrieval and information consolidation. Extensive experiments on seven benchmarks demonstrate that MultiSearch outperforms baseline methods, enhancing the SNR of retrieval and improving reasoning performance in question-answering tasks.

---


### 256. [HLS-Seek: QoR-Aware Code Generation for High-Level Synthesis via Proxy Comparative Reward Reinforcement Learning](https://arxiv.org/abs/2605.13536)

**<font color=#1a73e8>作者：</font>** Qingyun Zou, Feng Yu, Hongshi Tan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> High-Level Synthesis (HLS) compiles algorithmic C/C++ descriptions into hardware, with Quality of Results (QoR) -- latency and resource utilization -- critically governed by pragma configurations and code structure. Existing LLM-based HLS approaches train for functional correctness but ignore QoR entirely. We observe that reinforcement learning (RL) for HLS does not require absolute synthesis results -- only relative comparisons between candidates. Based on this insight, we propose \textbf{HLS-Seek}, a QoR-aware NL-to-HLS framework that replaces expensive synthesis-in-the-loop RL with a comparative proxy reward model achieving 99.53\% Pareto-dominance accuracy. To prevent reward hacking, we introduce \textit{uncertainty-aware Monte Carlo (MC) dropout switching} that selectively invokes real Vitis HLS synthesis for low-confidence candidates and online updates the proxy, creating a self-improving reward system. HLS-Seek achieves 81.5\% syntax correctness pass@1 and 81.4\% Func@5 on HLS-eval with only 7B parameters, surpassing GPT-5.1 and other frontier models while achieving 8.5$\times$ faster training than real-reward RL. On QoR evaluation, HLS-Seek achieves the lowest latency on 16/30 kernels and Pareto-dominates HLS-specific baselines on 9 kernels.

---


### 257. [CA-GCL: Cross-Anatomy Global-Local Contrastive Learning for Robust 3D Medical Image Understanding](https://arxiv.org/abs/2605.13544)

**<font color=#1a73e8>作者：</font>** Hanwen Zhang, Yao Liu, Die Dai 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fine-grained Vision-Language Pre-training (FVLP) demonstrates significant potential in 3D medical image understanding by aligning anatomy-level visual representations with corresponding textual descriptions. However, existing FVLP paradigms often suffer from severe representation collapse in the textual embedding space, where text embeddings of distinct anatomical structures become highly clustered and indistinguishable. This distributional degeneracy renders the model hypersensitive to prompt variations, hindering reliable clinical deployment. To address these challenges, we propose a novel Cross-Anatomy Global-Local Contrastive Learning framework (CA-GCL). CA-GCL introduces a global contrastive objective that enforces separation between anatomical categories in the latent space, effectively counteracting the aggregation tendency induced by local alignment. Furthermore, we incorporate a clinical-aware text augmentation strategy based on permutation invariance and partial completeness to enhance robustness against descriptive incompleteness. Extensive evaluations on the CT-RATE and Rad-ChestCT datasets demonstrate that CA-GCL consistently outperforms existing VLP paradigms in zero-shot abnormality detection, achieving superior performance while exhibiting strong cross-dataset generalization. Crucially, CA-GCL reduces performance variance across diverse prompt templates, transforming the collapsed textual similarity distribution into a bell-shaped distribution. These results validate CA-GCL as an effective framework for robust 3D medical image understanding.

---


### 258. [Mixed neural posterior estimation for simulators with discrete and continuous parameters](https://arxiv.org/abs/2605.13551)

**<font color=#1a73e8>作者：</font>** Jan Boelts, Cornelius Schröder, Jonas Beck 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural Posterior Estimation (NPE) enables rapid parameter inference for complex simulators with intractable likelihoods. NPE trains an inference network to estimate a probability density over parameters given data, typically assumed to be \emph{continuous}. However, many scientific models involve parameter spaces that are \emph{mixed}, that is, they contain both discrete and continuous dimensions. We address this limitation by extending NPE to mixed parameter spaces through an inference network that jointly handles discrete and continuous parameters. The inference network factorizes the joint posterior into discrete and continuous components, combining an autoregressive classifier for the discrete parameters with a generative model for the continuous parameters, trained jointly under a single simulation-based objective. In addition, we propose a diagnostic tool to assess the calibration of the mixed posterior approximation. Across tractable toy examples and real-world scientific simulators, our joint inference approach yields accurate and calibrated posteriors. The inference framework is available in the \texttt{sbi} Python package.

---


### 259. [Self-Supervised On-Policy Reinforcement Learning via Contrastive Proximal Policy Optimisation](https://arxiv.org/abs/2605.13554)

**<font color=#1a73e8>作者：</font>** Asim Osman, Sasha Abramowitz, Mark Bergh 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Contrastive reinforcement learning (CRL) learns goal-conditioned Q-values through a contrastive objective over state-action and goal representations, removing the need for hand-crafted reward functions. Despite impressive success in achieving viable self-supervised learning in RL, all existing CRL algorithms rely on off-policy optimisation and are mostly constrained to continuous action spaces, with little research invested in discrete environments. This leaves CRL disconnected from widely used and effective, modern on-policy training pipelines adopted across both single-agent and multi-agent RL in continuous and discrete environments. To establish a first connection, we introduce Contrastive Proximal Policy Optimisation (CPPO). CPPO is an on-policy contrastive RL algorithm that derives policy advantages directly from contrastive Q-values and optimises them via the standard PPO objective, without requiring a reward function or a replay buffer. We evaluate CPPO across continuous and discrete, single-agent and cooperative multi-agent tasks. Whilst the existence of an on-policy approach is inherently useful, we observe that \textbf{CPPO not only significantly outperforms the previous CRL baselines in 14 out of 18 tasks, but also matches or exceeds PPO's performance, which uses hand-crafted dense rewards, in 12 out of the 18 tasks tested.}

---


### 260. [Uncertainty-Aware Prediction of Lung Tumor Growth from Sparse Longitudinal CT Data via Bayesian Physics-Informed Neural Networks](https://arxiv.org/abs/2605.13560)

**<font color=#1a73e8>作者：</font>** Lingfei Kong, Haoran Ma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This work studies lung tumor growth prediction from sparse and irregular longitudinal computed tomography (CT) observations with measurement variability. A Bayesian physics-informed neural network is developed by combining Gompertz growth dynamics with low-dimensional Bayesian inference in the log-volume domain. The framework employs a two-stage inference strategy combining maximum a posteriori (MAP) estimation and Hamiltonian Monte Carlo (HMC) sampling to estimate posterior predictive distributions and uncertainty intervals. The method was evaluated on longitudinal data from the National Lung Screening Trial (30 patients). Results show that the model captures heterogeneous tumor growth patterns while maintaining reasonable prediction accuracy under limited observations. Compared with deterministic modeling approaches, the proposed approach additionally provides calibrated uncertainty estimates. The inferred posterior parameter correlations were consistent with expected biological growth behavior. The proposed framework achieved a cohort-level log-space RMSE of approximately 0.20 together with well-calibrated 95% credible interval coverage across 30 patients. These findings suggest that Bayesian physics-informed modeling may be useful for uncertainty-aware tumor growth assessment when only limited longitudinal follow-up scans are available.

---


### 261. [Spatiotemporal downscaling and nowcasting of urban land surface temperatures with deep neural networks](https://arxiv.org/abs/2605.13566)

**<font color=#1a73e8>作者：</font>** Solomiia Kurchaba, Angela Meyer  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Land Surface Temperature (LST) is a key variable for various applications, such as urban climate and ecology studies. Yet, existing satellite-derived LST products provide either high spatial or high temporal resolution, resulting in a fundamental trade-off between the two. To address this trade-off, we combine observations from a geostationary and a polar orbiting satellite and provide LST fields at high spatial and high temporal resolution (1 km at 15-min intervals). We demonstrate their application for intraday forecasting of LSTs. To estimate LST fields at high spatiotemporal resolution, a U-Net model is trained to map LST fields from SEVIRI/MSG (3 km and 15 min resolution) to LST fields from Terra/Aqua MODIS (1 km, 4 overpasses per day) that are collocated in space and time. The presented model has been trained on LSTs across large European cities with a population exceeding 1 million inhabitants, and achieves an RMSE = $1.92$°C and near-zero bias MBE = $0.01$°C on the hold-out test set. As a second step, we present an LST nowcasting model based on ConvLSTM architecture, trained across downscaled LST fields with forecast lead times of 15 to 75 minutes. The nowcasting model outperforms a persistence and a Climatological Rolling Median benchmarks, with RMSEs of $0.57$ to $1.15$°C for the considered lead times and biases ranging from $-0.1$ to $0.14$°C. An additional validation conducted against independent MODIS overpasses confirms robust performance. Our LST forecast model at high spatiotemporal resolution is directly applicable to operational satellite-based LST monitoring.

---


### 262. [Dynamical Predictive Modelling of Cardiovascular Disease Progression Post-Myocardial Infarction via ECG-Trained Artificial Intelligence Model](https://arxiv.org/abs/2605.13568)

**<font color=#1a73e8>作者：</font>** Riccardo Cavarra, Lupo Lovatelli, Shaheim Ogbomo-Harmitt 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Myocardial infarction (MI) is a leading cause of death, and its adverse outcomes are urgent to predict. Yet ECG-based prognostic models underperform because deep learning requires large, labelled datasets, which are scarce in medicine. Foundation models can learn from unlabelled ECGs via selfsupervision, but medically relevant training strategies remain underexplored. We propose a pretrained artificial intelligence model that combines patient-specific temporal information using contrastive learning with supervised multitask heads, then fine-tunes on post-MI outcome prediction. The proposed model outperformed a model trained from scratch (0.794 vs 0.608 AUC) showing that clinically structured ECG modelling improves classification in limited data regimes.

---


### 263. [Learning Local Constraints for Reinforcement-Learned Content Generators](https://arxiv.org/abs/2605.13570)

**<font color=#1a73e8>作者：</font>** Debosmita Bhaumik, Julian Togelius, Georgios N. Yannakakis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Constraint-based game content generators that learn local constraints from existing content, such as Wave Function Collapse (WFC), can generate visually satisfying game levels but face challenges in guaranteeing global properties, such as playability. On the other hand, reinforcement-learning trained generators can guarantee global properties -- because such properties can easily be included in reward functions -- but the results can be visually dissatisfying. In this paper, we explore ways to combine these methods. Specifically, we constrain the action space of a PCGRL generator with constraints learned by WFC, effectively allowing the PCGRL generator to achieve global properties while forced to adhere to local constraints. To better analyze how this hybrid content generation method operates, we vary the number and type of inputs, and we test whether to randomly collapse the starting state and exclude rare patterns. While the method is sensitive to hyperparameter tuning, the best of our trained generators produce visually satisfying and playable puzzle-platform game levels -- such as Lode Runner levels -- with desired global properties.

---


### 264. [Beyond Anthropomorphism: Exploring the Roles of Perceived Non-humanity and Structural Similarity in Deep Self-Disclosure Toward Generative AI](https://arxiv.org/abs/2605.13574)

**<font color=#1a73e8>作者：</font>** Satoru Shibuya  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This study investigates deep self-disclosure toward generative AI by examining perceived non-humanity and structural similarity as psychological factors beyond anthropomorphism. Perceived non-humanity may reduce evaluation apprehension, whereas structural similarity refers to the perceived logical alignment between a user's thinking and AI responses. Using cross-sectional survey data from 2,400 participants collected in 2025, this study analyzed associations with both the occurrence and depth of self-disclosure. Logistic regression indicated that the group high in both perceptions (Segment D) showed a significantly higher likelihood of disclosure than the baseline group (Segment A; OR = 11.35). ANOVA further showed significant between-group differences in disclosure depth. The findings suggest that trust-related behavior in deep self-disclosure may involve factors other than anthropomorphic perception. Because the study is exploratory and based on self-reported survey data, the results should be interpreted as associative rather than causal, and future longitudinal or experimental research is needed.

---


### 265. [HIR-ALIGN: Enhancing Hyperspectral Image Restoration via Diffusion-Based Data Generation](https://arxiv.org/abs/2605.13581)

**<font color=#1a73e8>作者：</font>** Li Pang, Heng Zhao, Yijia Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hyperspectral image (HSI) restoration is crucial for reliable analysis, as real HSIs suffer from degradations like noise, blur, and resolution loss. However, existing models trained on source data often fail on target domains lacking clean references, a common occurrence in practice. To address this issue, we present HIR-ALIGN, a plug-and-play target-adaptive augmentation framework that enhances hyperspectral image restoration by augmenting limited training images with synthetic data that closely matches the target distribution using no extra data. It consists of three stages: (i) proxy generation, where off-the-shelf restoration models restore degraded target observations to produce semantics-preserving proxy HSIs that approximate target-domain clean images; (ii) distribution-adaptive synthesis, where a blur-robust unCLIP diffusion model generates target-aligned RGBs from proxy RGBs, with prompt conditioning and embedding-space noise initialization. Then, a warp-based spectral transfer module synthesizes HSIs by aligning each generated RGB with the proxy RGB, estimating soft patch-wise transport weights, and applying these weights and learnable local interpolation kernels to the proxy HSI; and (iii) aligned supervised finetuning, where restoration networks pretrained on the source distribution are finetuned using both the proxy HSIs and synthesized target-aligned HSIs, and are then deployed on degraded target images. We further provide theoretical analysis showing that augmentation-based finetuning can achieve lower target-domain restoration risk by jointly improving target distribution coverage and controlling spectral bias. Extensive experiments on simulated and real datasets across denoising and super-resolution tasks demonstrate that HIR-ALIGN consistently improves source-only supervised baselines, outperforming both source-only counterparts and representative unsupervised methods.

---


### 266. [Phy-CoSF: Physics-Guided Continuous Spectral Fields Reconstruction and Super-Resolution for Snapshot Compressive Imaging](https://arxiv.org/abs/2605.13583)

**<font color=#1a73e8>作者：</font>** Wudi Chen, Zhiyuan Zha, Xin Yuan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances have demonstrated that coded aperture snapshot spectral imaging (CASSI) systems show great potential for capturing 3D hyperspectral images (HSIs) from a single 2D measurement. Despite the inherent spectral continuity of scenes captured by CASSI, most existing reconstruction methods are restricted to fixed, discrete spectral outputs, thereby precluding continuous spectral reconstruction or spectral super-resolution. To address this challenge, we propose Phy-CoSF, which synergizes deep unfolding networks with implicit neural representations, establishing a new paradigm for continuous spectral reconstruction and super-resolution in CASSI. Specifically, we propose a two-phase architecture that bridges discrete-wavelength training with continuous spectral rendering, enabling the synthesis of high-fidelity HSIs at arbitrary target wavelengths. At the core of our framework lies the continuous spectral fields (CoSF) module, embedded within each unfolding stage as a dynamic prior, which comprises a triple-branch cross-domain feature mixer for comprehensive spatial-frequency-channel feature fusion, alongside a spectral synthesis head that generates spectral intensities by querying continuous wavelength coordinates. Extensive experimental results demonstrate that Phy-CoSF not only achieves continuous modeling at arbitrary spectral resolutions but also outperforms many state-of-the-art methods in both reconstruction fidelity and spectral detail preservation. Our code and more results are available at: this https URL.

---


### 267. [HetScene: Heterogeneity-Aware Diffusion for Dense Indoor Scene Generation](https://arxiv.org/abs/2605.13586)

**<font color=#1a73e8>作者：</font>** Zini Chen, Junming Huang, Rong Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating controllable and physically plausible indoor scenes is a pivotal prerequisite for constructing high-fidelity simulation environments for embodied AI. However, existing deeplearning-based methods usually treat all objects as homogeneous instances within a unified generation process. While effective for sparse and simplistic layouts, they struggle to model realistic layouts with dense object arrangements and complex spatial dependencies, leadingto limited scalability and degraded physical plausibility. To deal with these challenges, we revisit indoor layout generation from the perspective of structural heterogeneity and decompose the objects into primary objects and secondary objects according to their distinct roles in shaping a scene. Based on this decomposition, we propose HetScene, a heterogeneous two-stage generation framework that decouples indoor layout synthesis into Structural Layout Generation (SLG) and Contextual Layout Generation (CLG). SLG first generates globally coherent structural layouts with only primary objects conditioned on text descriptions, top-down binary room masks, and spatial relation graphs, establishing a stable global macro-skeleton of large core furniture.

---


### 268. [Real2Sim: A Physics-driven and Editable Gaussian Splatting Framework for Autonomous Driving Scenes](https://arxiv.org/abs/2605.13591)

**<font color=#1a73e8>作者：</font>** Kaicong Huang, Talha Azfar, Weisong Shi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable autonomous driving relies on large-scale, well-labeled data and robust models. However, manual data collection is resource-intensive, and traditional simulation suffers from a persistent reality gap. While recent generative frameworks and radiance-field methods improve visual fidelity, they still struggle with temporal and spatial consistency and cannot ensure physics-aware behavior, limiting their applicability to driving scenario generation. To address these challenges, we propose Real2Sim, an unified framework that combines 4D Gaussian Splatting (4DGS) with a differentiable Material Point Method (MPM) solver. Real2Sim explicitly reconstructs dynamic driving scenes as temporally continuous Gaussian primitives, supports instance-level editing, and simulates realistic object-object and object-environment interactions. This framework enables physics-aware, high-fidelity synthesis of diverse, editable scenarios, including challenging corner cases such as collisions and post-impact trajectories. Experiments on the Waymo Open Dataset validate Real2Sim's capabilities in rendering, reconstruction, editing, and physics simulation, demonstrating its potential as a scalable tool for data generation in downstream tasks such as perception, tracking, trajectory prediction, and end-to-end policy learning.

---


### 269. [Creativity Bias: How Machine Evaluation Struggles with Creativity in Literary Translations](https://arxiv.org/abs/2605.13596)

**<font color=#1a73e8>作者：</font>** Kyo Gerrits, Rik van Noord, Ana Guerberof Arenas  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This article investigates the performance of automatic evaluation metrics (AEMs) and LLM-as-a-judge evaluation on literary translation across multiple languages, genres, and translation modalities. The aim is to assess how well these tools align with professionals when evaluating translation, creativity (creative shifts & errors), and see if they can substitute laborious manual annotations. A dataset of literary translations across three modalities (human translation, machine translation, and post-editing), three genres and three language pairs was created and annotated in detail for creativity by experienced professional literary translators. The results show that both AEMs and LLM-as-a-judge evaluations correlate poorly with professional evaluations on creativity, with LLM-as-a-judge showing a systematic bias in favour of machine-translated texts and penalising creative and culturally appropriate solutions. Moreover, performance is consistently worse for more literary genres such as poetry. This highlights fundamental limitations of current automatic evaluation tools for literary translation and the need to create new tools that do not frequently consider out of routine translations as errors.

---


### 270. [Rethinking Generalization in Graph Neural Networks: A Structural Complexity Perspective](https://arxiv.org/abs/2605.13597)

**<font color=#1a73e8>作者：</font>** Peiyao Wang, Liang Bai, Xian Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph neural networks (GNNs) have emerged as a fundamental tool for learning from graph-structured data, achieving strong performance across a wide range of applications. However, understanding their generalization capabilities remains challenging due to the complex structural dependencies inherent in such data. Existing generalization analyses largely follow the classical machine learning paradigm, focusing primarily on model complexity while overlooking the fundamental role of graph structure. Therefore, in this work, we systematically investigate this role by asking: does the graph structure actually influence generalization, and if so, by how much? To answer the first question and validate our intuition, we theoretically prove that incorporating more edges into the prediction process transforms the input representations to be overly accommodating to the output model, thereby inducing overfitting. To address the second question, we formulate a structural complexity measure based on the number of effective edges and derive a Rademacher complexity-based generalization bound. In doing so, we demonstrate that GNN generalization depends explicitly on structural complexity, alongside traditional parameter-dependent factors. Motivated by these theoretical findings, we propose a structural entropy regularization method. This approach controls structural complexity by regulating effective edges to balance underfitting and overfitting, ultimately improving the generalization performance of GNNs.

---


### 271. [Sparse Code Uplifting for Efficient 3D Language Gaussian Splatting](https://arxiv.org/abs/2605.13600)

**<font color=#1a73e8>作者：</font>** Lovre Antonio Budimir, Yushi Guan, Steve Ryhner 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Language Gaussian Splatting (3DLGS) augments 3D Gaussian Splatting with language-aligned visual features for open-vocabulary 3D scene understanding. A core challenge is efficiently associating high-dimensional vision-language embeddings with millions of 3D Gaussians while preserving efficient feature rendering for text-based querying. Existing methods either store dense features directly on Gaussians, causing high storage costs and slow rendering, or learn compact representations through expensive per-scene optimization with repeated feature rasterization. No existing method simultaneously achieves fast 3D semantic reconstruction, efficient storage, and fast rendering. We propose SCOUP (Sparse COde UPlifting), which addresses all three by decoupling language representation learning from 3D Gaussian optimization. Rather than working directly in 3D, we learn sparse codebook-based representations entirely using features associated with 2D image regions, associating each region with a sparse set of codebook coefficients. We then uplift these coefficients to 3D Gaussians with our weighted sparse aggregation using Gaussian-to-pixel associations, where each Gaussian accumulates coefficients over codebook atoms across views. Top-$K$ filtering then extracts the most dominant multi-view coefficients per Gaussian, enabling efficient storage and fast rendering. Our method achieves up to $400\times$ training speedup while being $3\times$ more memory efficient during training compared to the state-of-the-art in rendering speed. Across multiple benchmarks, SCOUP matches or outperforms existing methods in open-vocabulary querying accuracy.

---


### 272. [Unweighted ranking for value-based decision making with uncertainty](https://arxiv.org/abs/2605.13601)

**<font color=#1a73e8>作者：</font>** Aarón López García, Natalia Criado, Jose Such  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As intelligent systems are increasingly implemented in our society to make autonomous decisions, their commitment to human values raises serious concerns. Their alignment with human values remains a critical challenge because it can jeopardise the integrity and security of citizens. For this reason, an innovative human-centred and values-driven approach to decision making is required. In this work, we introduce the Fuzzy-Unweighted Value-Based Decision Making (FUW-VBDM) framework, where agents incorporate both quantitative and qualitative criteria to generate human-centred decisions. We also address the normative bias introduced by stakeholders with arbitrary weights by removing prior weights and introducing a fuzzy domain of decision variables defined for a score function. This concept allows us to generalise any VBDM problem as the search for feasible solutions when optimising the score in the weight domain. To provide a solution to FUW-VBDM, we present Rankzzy, a customizable unweighted ranking method that integrates fuzzy-based reasoning to quantify uncertainty. We mathematically prove the consistency of the Rankzzy for any admissible configuration selected by stakeholders. We show the applicability of our method through an illustrative case study, which we also use as a running example. The evaluation conducted indicates a reduced computational cost in large-scale value-based decision-making problems and a strong rank performance regarding existing approaches when employing the aggregation via Pythagorean means.

---


### 273. [Rethinking Graph Convolution for 2D-to-3D Hand Pose Lifting](https://arxiv.org/abs/2605.13604)

**<font color=#1a73e8>作者：</font>** Chanyoung Kim, Donghyun Kim, Dong-Hyun Sim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Graph convolutional networks (GCNs) are widely used for 3D hand pose estimation, where the hand skeleton is encoded as a fixed adjacency graph. We revisit whether this is the most effective way to incorporate hand topology in 2D-to-3D lifting. In this paper, we perform controlled, parameter-matched ablations on the FPHA benchmark and show that standard multi-head self-attention consistently outperforms GCN baselines. Even when the GCN is strengthened with multi-hop adjacency and matched parameter count, self-attention reduces MPJPE from 12.36 mm to 10.09 mm. A skeleton-constrained graph attention network recovers most of this gap, indicating that input-dependent aggregation is a major source of improvement, while fully connected attention yields additional gains. We further show that hand topology is most effective when introduced as a soft structural prior through graph-distance positional encoding, rather than as a hard adjacency constraint. These results suggest that, for hand pose lifting, adaptive spatial attention is a more effective inductive bias than fixed graph convolution.

---


### 274. [Deep Learning as Neural Low-Degree Filtering: A Spectral Theory of Hierarchical Feature Learning](https://arxiv.org/abs/2605.13612)

**<font color=#1a73e8>作者：</font>** Yatin Dandi, Matteo Vilucchio, Luca Arnaboldi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding how deep neural networks learn useful internal representations from data remains a central open problem in the theory of deep learning. We introduce Neural Low-Degree Filtering (Neural LoFi), a stylized limit of gradient-based training in which hierarchical feature learning becomes an explicit iterative spectral procedure. In this limit, the dynamics at each layer decouple: given the current representation, the next layer selects directions with maximal accessible low-degree correlation to the label. This yields a tractable surrogate mechanism for deep learning, together with a natural kernel-space interpretation. Neural LoFi provides a mathematically explicit framework for studying multi-layer feature learning beyond the lazy regime. It predicts how representations are selected layer by layer, explains how emergence of concepts arises with given sample complexity,and gives a concrete mechanism by which depth progressively constructs new features from old ones through low-degree compositionality. We complement the theory with mechanistic experiments on fully connected and convolutional architectures, showing that Neural LoFi improves over lazy random-feature baselines, recovers meaningful structured filters, and predicts representations aligned with early gradient-descent feature discovery with real datasets.

---


### 275. [WD-FQDet: Multispectral Detection Transformer via Wavelet Decomposition and Frequency-aware Query Learning](https://arxiv.org/abs/2605.13621)

**<font color=#1a73e8>作者：</font>** Chunjin Yang, Xiwei Zhang, Yiming Xiao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Infrared-visible object detection improves detection performance by combining complementary features from multispectral images. Existing backbone-specific and backbone-shared approaches still suffer from the problems of severe bias of modality-shared features and the insufficiency of modality-specific features. To address these issues, we propose a novel detection framework WD-FQDet that explicitly decouples modality-shared and modality-specific information from infrared and visible modalities in the new view of low- and high-frequency domains, allowing fusion strategies tailored to their frequency characteristics. Specifically, a low-frequency homogeneity alignment module is proposed to align modality-shared features across modalities via a cross-modal attention mechanism, and a high-frequency specificity retention module is proposed to preserve modality-specific features through the multi-scale gradient consistency loss. To reinforce the feature representation in the frequency domain, we propose a hybrid feature enhancement module that incorporates spatial cues. Furthermore, considering that the contributions of homogeneous and modality-specific features to object detection vary across scenarios, we propose a frequency-aware query selection module to dynamically regulate their contributions. Experimental results on the FLIR, LLVIP, and M3FD datasets demonstrate that WD-FQDet achieves state-of-the-art performance across multiple evaluation metrics.

---


### 276. [How to Interpret Agent Behavior](https://arxiv.org/abs/2605.13625)

**<font color=#1a73e8>作者：</font>** Jie Gao, Kaiser Sun, Jen-tse Huang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous agents such as Claude Code and Codex now operate for hours or even days. Understanding their runtime behavior has become critical for downstream tasks such as diagnosing inefficiencies, fixing bugs, and ensuring better oversight. A primary way to gain this understanding is analyzing the reasoning trajectories and execution traces these agents generate. Yet such data remains in unstructured natural-language form, making it difficult for humans to interpret at scale. We introduce ACT*ONOMY (a combination of Action and Taxonomy), a taxonomy for describing and analyzing agent behavior at runtime. ACT*ONOMY has two components: (1) the taxonomy itself, developed through Grounded Theory and structured as a three-level hierarchy of 10 actions, 46 subactions, and 120 leaf categories; and (2) an open repository that hosts the living taxonomy, provides an automated analysis pipeline that applies it to agent trajectories analysis, and defines an extension protocol for customization and growth. Our experiments show that ACTONOMY can compare behavioral profiles across agents and characterize a single agent's behavior across diverse trajectories, surfacing patterns indicative of failure modes. By providing a shared vocabulary, ACT*ONOMY helps researchers, agent designers, and end users interpret agent behavior more consistently, enabling better oversight and control.

---


### 277. [Achieving $ε^{-2}$ Sample Complexity for Single-Loop Actor-Critic under Minimal Assumptions](https://arxiv.org/abs/2605.13639)

**<font color=#1a73e8>作者：</font>** Ishaq Hamza, Zaiwei Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper, we establish last-iterate convergence rates for off-policy actor--critic methods in reinforcement learning. In particular, under a single-loop, single-timescale implementation and a broad class of policy updates, including approximate policy iteration and natural policy gradient methods, we prove the first $\tilde{\mathcal{O}}(\epsilon^{-2})$ sample complexity guarantee for finding an $\epsilon$-optimal policy under minimal assumptions, namely, the existence of a policy that induces an irreducible Markov chain. This stands in stark contrast to the existing literature, where an $\tilde{\mathcal{O}}(\epsilon^{-2})$ sample complexity is achieved only through nested-loop updates and/or under strong, algorithm-dependent assumptions on the policies, such as uniform mixing and uniform exploration. Technically, to address the challenges posed by the coupled update equations arising from the single-loop implementation, as well as the potentially unbounded iterates induced by off-policy learning, our analysis is based on a coupled Lyapunov drift framework. Specifically, we establish a geometric convergence rate for the actor and an $\tilde{\mathcal{O}}(1/T)$ convergence rate for the critic, and combine the two Lyapunov drift inequalities through a cross-domination property. We believe this analytical framework is of independent interest and may be applicable to other coupled iterative algorithms with unbounded

---


### 278. [Multi-Objective and Mixed-Reward Reinforcement Learning via Reward-Decorrelated Policy Optimization](https://arxiv.org/abs/2605.13641)

**<font color=#1a73e8>作者：</font>** Yang Bai, Kaiyuan Liu, Ziyuan Zhuang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Complex reinforcement learning environments frequently employ multi-task and mixed-reward formulations. In these settings, heterogeneous reward distributions and correlated reward dimensions often destabilize the construction of scalar advantages. To address these challenges, we propose Reward-Decorrelated Policy Optimization (RDPO), a reward-processing method designed to explicitly target both failure modes. RDPO first utilizes Magnitude-Aware Quantile normalization to stabilize prompt-level advantage allocation across binary, fractional, and continuous rewards. It then applies Mahalanobis whitening within each active reward subspace to mitigate correlation redundancy prior to aggregation. When applied during the post-training of LongCat-Flash, RDPO enhances instruction following, writing quality, and robustness to hard prompts while remaining broadly competitive on reasoning and coding evaluations.

---


### 279. [Prefix Teach, Suffix Fade: Local Teachability Collapse in Strong-to-Weak On-Policy Distillation](https://arxiv.org/abs/2605.13643)

**<font color=#1a73e8>作者：</font>** Kaiyuan Liu, Ziyuan Zhuang, Yang Bai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) trains a student model on its own rollouts using dense feedback from a stronger teacher. Prior literature suggests that, provided teacher feedback is available, supervising the full sequence of response tokens should monotonically improve performance. However, we demonstrate that this assumption sometimes fails to hold in strong-to-weak OPD settings. While later segments of a generated trajectory may still exhibit a non-zero teacher-student advantage, they frequently lack the local contrast that makes dense feedback effective for prioritizing student learning. We term this failure mode local teachability collapse. The resulting principle is straightforward: supervision should concentrate on trajectory regions where the teacher's feedback remains discriminative, rather than uniformly covering the entire response. We operationalize this principle through a trajectory-specific release rule. This rule measures the teacher's margin over the student's top-$K$ candidate set, aggregates this margin across NLTK-tokenized sentence segments, and truncates dense OPD supervision upon detecting a BIC-style downward change point. Experimental results across strong-to-weak distillation tasks using the Qwen3 model family indicate that this release rule consistently outperforms standard full-trajectory OPD across five in-domain benchmarks at various student scales. Furthermore, compared to baseline distillation methods, our approach better preserves model capabilities on out-of-domain task. These results suggest that effective strong-to-weak OPD requires evaluating not only the availability of teacher guidance but also its local utility, ensuring that the generated feedback remains teachable.

---


### 280. [HADAR-Based Thermal Infrared Hyperspectral Image Restoration](https://arxiv.org/abs/2605.13664)

**<font color=#1a73e8>作者：</font>** Cheng Dai, Jiale Lin, Bingxuan Song 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Thermal-infrared (TIR) hyperspectral imagery (HSI) provides critical scene information for various applications. However, its practical utility is severely limited by unique sensor degradations beyond the capabilities of existing restoration methods, which are ignorant of underlying thermal physics. Here, we propose HAIR (HADAR-based Image Restoration) as a physics-driven framework for ground-based TIR-HSI restoration. HAIR utilizes the HADAR rendering equation (HRE) and combines it with the atmospheric downwelling radiative transfer equation (RTE) to model TIR-HSI using temperature, emissivity, and texture (TeX) physical triplets. This physical model leads to a TeX decompose-synthesize strategy that guarantees physical consistency and spatio-spectral noise resilience, in stark contrast to existing approaches. Moreover, our framework uses a forward-modeled atmospheric downwelling reference, along with spectral smoothness of emissivity and blackbody radiation, to enable spectral calibration and generation that would otherwise be elusive. Our extensive experiments on the outdoor DARPA Invisible Headlights dataset and in-lab FTIR measurements show that HAIR consistently outperforms state-of-the-art methods across denoising, inpainting, spectral calibration, and spectral super-resolution, establishing a benchmark in objective accuracy and visual quality.

---


### 281. [Pattern-Enhanced RT-DETR for Multi-Class Battery Detection](https://arxiv.org/abs/2605.13670)

**<font color=#1a73e8>作者：</font>** Xu Zhong, Enyuan Hu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate and efficient battery detection is increasingly important for applications in electronic waste recycling, industrial quality control, and automated sorting systems. In this paper, we present both a comprehensive benchmark and a novel method for multi-class battery detection. We systematically compare three CNN-based detectors (YOLOv8n, YOLOv8s, YOLO11n) and two transformer-based detectors (RT-DETR-L, RT-DETR-X) on a publicly available dataset of approximately 8,591 annotated images under identical experimental conditions, and further propose PaQ-RT-DETR, which introduces pattern-based dynamic query generation into RT-DETR to alleviate query activation imbalance with negligible computational overhead. Among baselines, YOLO11n achieves the best CNN-based accuracy (mAP@50: 0.779) at only 2.6M parameters, while YOLOv8n delivers the fastest inference at ~1,667 FPS. PaQ-RT-DETR-X achieves the highest overall mAP@50 of 0.782, surpassing RT-DETR-X by +2.8% with consistent per-class gains across all six battery categories including the data-scarce Bike Battery class. Our findings provide practical guidance for selecting object detection models in battery-related industrial applications.

---


### 282. [SpurAudio: A Benchmark for Studying Shortcut Learning in Few-Shot Audio Classification](https://arxiv.org/abs/2605.13672)

**<font color=#1a73e8>作者：</font>** Giries Abu Ayoub, Morad Tukan, Loay Mualem  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-shot classification (FSC) is widely used for learning from limited labeled data, yet most evaluations implicitly assume that target concepts are independent of contextual cues. In real-world settings, however, examples often appear within rich contexts, allowing models to exploit spurious correlations between foreground content and background signals. While such effects have been studied in few-shot image classification, their role in few-shot audio classification remains largely unexplored, and existing audio benchmarks offer limited control over contextual structure. We introduce SpurAudio, a benchmark that leverages the natural separability of foreground events and background environments in audio to enable controlled, multi-level evaluation of contextual shifts across support and query sets. Using this benchmark, we show that many state-of-the-art few-shot methods suffer severe performance degradation when background correlations are disrupted, despite achieving similar accuracy under standard evaluation protocols. Crucially, this vulnerability persists even in large pretrained audio foundation models, ruling out limited backbone capacity as an explanation. Moreover, methods that appear comparable under conventional benchmarks can exhibit markedly different sensitivity to spurious correlations, revealing systematic algorithmic strengths and vulnerabilities tied to how feature representations interact with classifier heads at inference time. These findings provide new insight into the behavior of few-shot methods in audio and highlight the need for benchmarks that explicitly probe context dependence when evaluating FSC models.

---


### 283. [Graph Neural Networks with Triangle-Based Messages for the Multicut Problem](https://arxiv.org/abs/2605.13673)

**<font color=#1a73e8>作者：</font>** Jannik Irmai, Lucas Fabian Naumann, Bjoern Andres  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The multicut problem is an NP-hard combinatorial optimization problem with diverse applications in fields such as bioinformatics, data mining and computer vision. Graph neural networks have been defined for the multicut problem but can be adapted further to its specific objective function and constraints. In this article, we introduce such an adapted graph neural network architecture in which features are assigned only to edges, and the computation of messages is based on triangles in the underlying graph. Experiments with synthetic and real-world instances with up to 200 nodes show that our method outperforms state-of-the-art heuristic solvers in terms of solution quality while maintaining feasible runtimes. For some instances, our method finds optimal solutions in seconds whereas exact solvers need hours to find and certify optimal solutions.

---


### 284. [Weakly Supervised Segmentation as Semantic-Based Regularization](https://arxiv.org/abs/2605.13674)

**<font color=#1a73e8>作者：</font>** Stefano Colamonaco, Andrei-Bogdan Florea, Jaron Maene  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Weakly supervised semantic segmentation (WSSS) trains dense pixel-level segmentation models from partial or coarse annotations such as bounding boxes, scribbles, or image-level tags. While recent work leverages foundation models such as the Segment Anything Model (SAM) to generate pseudo-labels, these approaches typically depend on heuristic prompt choices and offer limited ways to incorporate prior knowledge or heterogeneous labels. We address this gap by taking a neurosymbolic perspective: integrating differentiable fuzzy logic with deep segmentation models. Weak annotations and domain-specific priors are unified as continuous logical constraints that fine-tune SAM under weak supervision. The refined foundation model then produces improved pseudo-labels, from which we train a second-stage prompt-free segmentation model. Experiments on Pascal VOC 2012 and the REFUGE2 optic disc/cup segmentation dataset show that our logic-guided fine-tuning yields higher-quality pseudo-labels, leading to state-of-the-art segmentation accuracy that often exceeds densely supervised baselines.

---


### 285. [Characterizing Universal Object Representations Across Vision Models](https://arxiv.org/abs/2605.13675)

**<font color=#1a73e8>作者：</font>** Florian P. Mahner, Johannes Roth, Ka Chun Lam 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep neural networks trained with different architectures, objectives, and datasets have been reported to converge on similar visual representations. However, what remains unknown is which visual properties models actually converge on and which factors may underlie this convergence. To address this, we decompose the object similarity structure of 162 diverse vision models into a small set of non-negative dimensions. To determine universal versus model-specific dimensions, we then estimate how often each dimension reappears across models. In contrast to model-specific dimensions, universal dimensions are more interpretable and more strongly driven by conceptual image properties, indicating the relevance of interpretability and semantic content as implicit factors driving universality across models. Differences in architecture, objective function, training data, model size, and model performance do not explain the emergence of universal dimensions. However, models with more universal dimensions also better predict macaque IT activity and human similarity judgments, suggesting that universality reflects representations relevant to biological vision. These findings have important implications for understanding the emergent representations underlying deep neural network models and their alignment with biological vision.

---


### 286. [EBCC: Enclave-Backed Confidential Containers via OCI-Compatible Runtime Integration](https://arxiv.org/abs/2605.13676)

**<font color=#1a73e8>作者：</font>** Di Lu, Qingwen Zhang, Yujia Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Container runtimes provide a stable operational interface for deploying, monitoring, and controlling modern workloads, while trusted execution environments (TEEs) provide hardware-enforced isolation for sensitive computation. Existing confidential-container systems often rely on VM-backed deployment stacks or TEE-specific execution substrates, which can separate confidential execution from the conventional OCI runtime lifecycle. This paper presents EBCC (Enclave-Backed Confidential Containers), an OCI-compatible runtime architecture for managing composite confidential-computing workloads. EBCC treats the REE-side anchor and TEE-side confidential stages as a single containerized confidential-computing composite, preserves standard OCI lifecycle operations, and keeps TEE-specific execution behind a backend adapter. It also maintains persistent per-instance state and per-stage artifacts for request handling, response generation, logging, and evidence binding.
We implement EBCC on a Keystone backend and evaluate its correctness, performance, footprint, and concurrent execution behavior. The results show that EBCC introduces additional latency over native Keystone execution, mainly due to lifecycle mediation, request validation, EID allocation, backend dispatch, and artifact persistence, while keeping the added footprint concentrated on host-side management state. Cross-TEE case studies on SGX, TDX, and OP-TEE show that the same lifecycle and stage abstraction can be mapped to enclave-style, VM-style, and embedded-style TEEs. These results indicate that EBCC can make TEE-backed execution manageable through an OCI-style lifecycle without materially enlarging the protected-side TCB.

---


### 287. [Three-Stage Learning Unlocks Strong Performance in Simple Models for Long-Term Time Series Forecasting](https://arxiv.org/abs/2605.13678)

**<font color=#1a73e8>作者：</font>** Zhenan Yu, Guangxin Jiang, Jin Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent studies on long-term time series forecasting have shown that simple linear models and MLP-based predictors can achieve strong performance without increasingly complex architectures. However, many competitive baselines still rely on structural priors such as frequency-domain modeling, explicit decomposition, multi-scale mixing, or sophisticated cross-variable interaction modules, while paying less attention to how simple temporal mappings should be trained and organized. In this paper, we propose STAIR, short for Stagewise Temporal Adaptation via Individualization and Residual Learning, a training paradigm for long-term time series forecasting that aims to unlock the capacity of simple temporal mapping models without introducing complex architectural modules. STAIR decomposes forecasting ability into three progressive stages: it first learns common temporal dynamics across variables through a shared temporal mapping, then adapts the shared model to each variable via channel-wise fine-tuning to capture variable-specific patterns, and finally complements the backbone with cross-variable information through residual learning. We further introduce Shared-to-Individual Fine-tuning and alpha-RevIN to mitigate the limitations of strict channel independence and the overly strong normalization prior induced by standard RevIN. This design gradually increases modeling flexibility while keeping the core temporal predictor as a shallow MLP in the main experiments, with linear variants analyzed separately. Experiments on nine long-term forecasting benchmarks show that STAIR matches or outperforms recent strong baselines while preserving a simple temporal backbone, providing a concise and effective modeling perspective for long-term time series forecasting.

---


### 288. [Scale-Sensitive Shattering: Learnability and Evaluability at Optimal Scale](https://arxiv.org/abs/2605.13684)

**<font color=#1a73e8>作者：</font>** Shashaank Aiyer, Yishay Mansour, Shay Moran 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the optimal scale at which real-valued function classes exhibit uniform convergence and learnability. Our main result establishes a scale-sensitive generalization of the fundamental theorem of PAC learning: for every bounded real-valued class and every $\gamma>0$, uniform convergence at scale $\gamma$, agnostic learnability at scale $\gamma/2$, and finiteness of the fat-shattering dimension at every scale $\gamma'>\gamma$ are equivalent. This resolves a question by Anthony and Bartlett (Cambridge Univ. Press 1999) on the precise scales governing learnability, refuting a conjecture attributed there to Phil Long that a multiplicative 2-factor gap is unavoidable, and improves the upper bounds of Bartlett and Long (JCSS 1998), which incur such a loss.
The key technical ingredient is a direct bound on empirical $\ell_\infty$ covering numbers, avoiding the standard detour through packing numbers. As a consequence, we obtain sharp asymptotic metric-entropy bounds in terms of the fat-shattering scale $\gamma$: an $O(\log^2 n)$ bound holds already at scale $\gamma/2$, while an $O(\log n)$ bound holds at scale $2\gamma$. We further show that the $O(\log^2 n)$ bound is sometimes tight. These results resolve open questions by Alon et al. (JACM 1997) and Rudelson and Vershynin (Ann. of Math. 2006).
As an application, we establish a sharp dichotomy for bounded integral probability metrics: every such IPM is either estimable or cannot be weakly evaluated within any multiplicative factor $c<3$, while $3$-weak evaluability always holds, resolving an open question from Aiyer et al. (ICML 2026). We also highlight several open questions on quantitative sample complexity and evaluability.

---


### 289. [Cross Modality Image Translation In Medical Imaging Using Generative Frameworks](https://arxiv.org/abs/2605.13686)

**<font color=#1a73e8>作者：</font>** Giulia Romoli, Alessia Capoccia, Filippo Ruffini 等 23 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical image-to-image (I2I) translation enables virtual scanning, i.e. the synthesis of a target imaging modality from a source one without additional acquisitions. Despite growing interest, most proposed methods operate on 2D slices, are evaluated on isolated tasks with different experimental set-ups and lack clinical validation. The primary contribution of this work is a reproducible, standardized comparative evaluation of 3D I2I translation methods in oncological imaging, designed to standardize preprocessing, splitting, inference, and multi-level evaluation across heterogeneous clinical tasks. Within this framework, we compare seven generative models, three Generative Adversarial Networks (GANs: Pix2Pix, CycleGAN, SRGAN) and four latent generative models (Latent Diffusion Model, Latent Diffusion Model+ControlNet, Brownian Bridge, Flow Matching), across eleven datasets spanning three anatomical regions (head/neck, lung, pelvis) and four translation directions (cone-beam CT to CT, MRI to CT, CT to PET, MRI T2-weighted to T2-FLAIR), for a total of 77 experiments under uniform training, inference, and evaluation conditions. The results show that GANs outperform latent generative models across all tasks, with SRGAN achieving statistically significant superiority. Our lesion-level analysis reveals that all models struggle with small lesions and that, in CT to PET synthesis, models reproduce lesion shape more reliably than absolute uptake-related intensity. We also performed a Visual Turing test administered to 17 physicians, including 15 radiologists, which shows near-chance classification accuracy (56.7%), confirming that synthetic volumes are largely indistinguishable from real acquisitions, while exposing a dissociation between quantitative metrics and clinical preference.

---


### 290. [MedCore: Boundary-Preserving Medical Core Pruning for MedSAM](https://arxiv.org/abs/2605.13688)

**<font color=#1a73e8>作者：</font>** Cenwei Zhang, Suncheng Xiang, Lei You  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical segmentation foundation models such as SAM and MedSAM provide strong prompt-driven segmentation, but their image encoders are still too large for many clinical settings. Compression is also risky in medicine because a model can keep high Dice while losing boundary fidelity. We propose MedCore, a structured pruning framework for MedSAM. The main idea is to preserve two kinds of structures: structures that became important during SAM-to-MedSAM adaptation, and structures that have high boundary leverage. We identify the first type by a dual-intervention score that compares zeroing a group with resetting it to its original SAM weight. We identify the second type by boundary-aware Fisher estimation. We also introduce a boundary leverage principle, which shows that compression-induced boundary displacement is controlled by logit perturbation on the boundary divided by the logit spatial gradient. This principle explains why boundary metrics can degrade even when Dice remains high. On polyp segmentation benchmarks, MedCore reduces parameters by 60.0% and FLOPs by 58.4% while achieving Dice 0.9549, Boundary F1 0.6388, and HD95 5.14 after recovery fine-tuning. It also reaches 86.6% parameter reduction and 90.4G FLOPs with strong boundary quality. Our analysis further shows that MedSAM lies in a head-fragile boundary regime: head-pruning steps have 2.887 times larger 95th-percentile boundary leverage than MLP-pruning steps, and this logit-level effect is consistent with BF1 and HD95 degradation. Our code is available at this https URL.

---


### 291. [The WidthWall: A Strict Expressivity Hierarchy for Hypergraph Neural Networks](https://arxiv.org/abs/2605.13690)

**<font color=#1a73e8>作者：</font>** Fengqing Jiang, Yuetai Li, Yichen Feng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hypergraphs provide a natural framework to model higher-order interactions in scientific, social, and biological systems. Hypergraph neural networks (HGNNs) aim to learn from such data, yet it remains unclear which higher-order structures these models can represent. We show that hypergraph expressivity is governed by which small patterns an architecture can detect and count. We formalize this via homomorphism densities, which measure how often a structural motif appears in a hypergraph. Combining classical homomorphism-count completeness with invariant approximation, we show that homomorphism densities generate all continuous hypergraph invariants and organize them into a strict hierarchy indexed by hypertree width. This yields a Width Wall: a fundamental architectural limit beyond which no hidden dimension, training procedure or fixed-depth HGNN can represent invariants requiring wider patterns. Our framework provides a unified characterization of 15 HGNN architectures, precisely identifies information lost by clique expansion, and motivates density-aware models that extend expressivity beyond bounded-width message passing. We experimentally validate this finding on an APPLICATION NODE CLASSIFICATION SUITE of real-world hypergraphs, where the Width Wall predicts when graph-reduction baselines fail and when density features help.

---


### 292. [Polyhedral Instability Governs Regret in Online Learning](https://arxiv.org/abs/2605.13692)

**<font color=#1a73e8>作者：</font>** Yuetai Li, Fengqing Jiang, Yichen Feng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many online decision problems over combinatorial actions are addressed via convex relaxations, leading to online convex optimization with piecewise linear objectives and induced polyhedral structure. We show that regret in such problems is governed by \emph{polyhedral instability}: the number of changes of the active region. Under full information feedback and fixed partition assumptions, if $\mathrm{RS}_T$ denotes the number of region switches and $V_{\max}$ the maximum number of vertices per region, we prove $\Regret_T= \Theta(\sqrt{(1+\mathrm{RS}_T)\,T\,\log V_{\max}})$ interpolating between experts-like and dimension-dependent OCO rates. For online submodular--concave games under Lovász convexification, this reduces to the permutation-switch count $\mathrm{SC}_T$, yielding the matching rate $\Regret_T= \Theta(\sqrt{(1+\mathrm{SC}_T)\,T\,\log n})$. Experiments on synthetic and real combinatorial problems (shortest path, influence maximization) validate the predicted scaling and indicate that low-instability regimes can arise in practice without explicit enumeration of actions.

---


### 293. [MQTT Across a Raspberry Pi 5 IoT Network Utilizing Quantum-resistant Signature Algorithms](https://arxiv.org/abs/2605.13698)

**<font color=#1a73e8>作者：</font>** Ray Feingold, Chansu Yu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The rapid expansion of the Internet of Things (IoT) has introduced millions of resource-constrained devices into critical infrastructures, consumer environments, and industrial systems. These devices rely on lightweight communication protocols such as MQTT to support low-power, intermittent, and bandwidth-limited operation. However, common TLS algorithms used to secure MQTT communications are vulnerable to quantum attacks made feasible by Shor's algorithm. As a result, IoT infrastructures must evaluate and adopt post-quantum cryptographic (PQC) methods capable of providing long-term resilience. This report investigates the implementation of PQC algorithms within an MQTT-based IoT networks using three Raspberry Pis. Specifically, it integrates the FALCON digital signature scheme, one of NIST's selected post-quantum signature algorithms, to maintain message authenticity and integrity across resource-constrained MQTT clients and brokers. By measuring system performance, the research characterizes the practical trade-offs of deploying lattice-based PQC on lightweight hardware.

---


### 294. [Adaptive mine planning under geological uncertainty: A POMDP framework for sequential decision-making](https://arxiv.org/abs/2605.13702)

**<font color=#1a73e8>作者：</font>** Hamza Khalifi, Jef Caers, Yassine Taha 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Strategic mine production scheduling under geological uncertainty is conventionally formulated as a stochastic optimization problem in which a fixed extraction sequence and routing decisions are computed ex ante. This plan-driven paradigm treats uncertainty as passive: decisions are hedged across geological scenarios, but planning does not anticipate how future observations will inform future decisions. We propose a different perspective by formulating mine scheduling as a Partially Observable Markov Decision Process (POMDP), in which extraction and routing decisions are made sequentially with planning explicitly integrating the expectation of future belief updates. To achieve computational tractability, we introduce a hybrid SA-POMDP architecture that combines simulated annealing-based (SA) value approximation with ensemble-based belief updating via ensemble smoother with multiple data assimilation (ES-MDA). At each decision epoch, candidate actions are evaluated through their expected long-term value under the current belief, and the belief is updated as mining observations are assimilated. This yields an adaptive policy rather than a fixed plan. We evaluate the framework on a copper-gold open-pit mining complex with multiple processing destinations. Under a statistically consistent prior, the SA-POMDP reduces the expectation-reality gap from 22.3% to 4.6%, improving realized NPV by USD8.4M relative to one-shot stochastic optimization. Under systematic prior misspecification of 10%, the adaptive framework outperforms static planning by up to USD44.6M (36.9%), demonstrating structural robustness beyond scenario hedging. These results show that sequential belief updating transforms geological uncertainty from a passive constraint into an active component of value creation.

---


### 295. [DisAgg: Distributed Aggregators for Efficient Secure Aggregation in Federated Learning](https://arxiv.org/abs/2605.13708)

**<font color=#1a73e8>作者：</font>** Haaris Mehmood, Giorgos Tatsis, Dimitrios Alexopoulos 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Federated learning enables collaborative model training across distributed clients, yet vanilla FL exposes client updates to the central server. Secure-aggregation schemes protect privacy against an honest-but-curious server, but existing approaches often suffer from many communication rounds, heavy public-key operations, or difficulty handling client dropouts. Recent methods like One-Shot Private Aggregation (OPA) cut rounds to a single server interaction per FL iteration, yet they impose substantial cryptographic and computational overhead on both server and clients. We propose a new protocol called DisAgg that leverages a small committee of clients called Aggregators to perform the aggregation itself: each client secret-shares its update vector to Aggregators, which locally compute partial sums and return only aggregated shares for server-side reconstruction. This design eliminates local masking and expensive homomorphic encryption, reducing endpoint computation while preserving privacy against a curious server and a limited fraction of colluding clients. By leveraging optimal trade-offs between communication and computation costs, DisAgg processes 100k-dimensional update vectors from 100k 5G clients with a 4.6x speedup compared to OPA, the previous best protocol.

---


### 296. [Learning to Optimize Radiotherapy Plans via Fluence Maps Diffusion Model Generation and LSTM-based Optimization](https://arxiv.org/abs/2605.13713)

**<font color=#1a73e8>作者：</font>** Isabella Poles, Simon Arberet, Riqiang Gao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Volumetric Modulated Arc Therapy (VMAT) is a cornerstone of modern radiation therapy, enabling highly conformal tumor irradiation and healthy-tissue sparing. Yet, its planning solves inverse and nested optimization for multi-leaf collimators, monitor units and dose parameters, while enforcing their consistency to ensure mechanical deliverability. Nevertheless, this process often requires repeated re-optimization when treatment configurations change, resulting in substantial planning time per patient. To address these problems, we present a diffusion-driven Learning-to-Optimize (L2O) method for end-to-end VMAT planning. A distribution-matching distilled diffusion model learns a clinically feasible manifold of fluence maps, enabling their one-shot generation. On top of this, an LSTM-based L2O module learns gradient update dynamics to swiftly refine fluence maps toward prescribed dose objectives during inference. Experimental results on clinical and public prostate cancer cohorts demonstrate improved planning efficiency, flexibility, and machine deliverability over currently available end-to-end VMAT planners.

---


### 297. [Tight Sample Complexity Bounds for Entropic Best Policy Identification](https://arxiv.org/abs/2605.13717)

**<font color=#1a73e8>作者：</font>** Amer Essakine, Claire Vernade  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study best-policy identification for finite-horizon risk-sensitive reinforcement learning under the entropic risk measure. Recent work established a constant gap in the exponential horizon dependence between lower and upper bounds on the number of samples required to identify an approximately optimal policy. Precisely, known lower bounds scale in $\Omega(e^{|\beta| H})$ where $H$ is the horizon of the MDP, while the state-of-the-art upper bound achieves at best $O(e^{2|\beta| H})$ (arXiv:2506.00286v2) using a generative model. We show that this extra exponential factor can be traced to overly loose concentration control for exponential utilities. To close this open gap, we revisit the analysis of this problem through a forward-model based algorithm building on KL-based exploration bonuses that we adapt to the entropic criterion. The improvement we get is due to two main novel technical innovations. We leverage the smoothness properties of the exponential utility to derive sharper concentration bounds, and we propose a new stopping rule that exploits further this tightness to obtain a sample complexity that matches the lower bound.

---


### 298. [Humanwashing -- It Should Leave You Feeling Dirty](https://arxiv.org/abs/2605.13723)

**<font color=#1a73e8>作者：</font>** Ben Wilson, Matimba Swana, Peter Winter 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The phrase 'human in the loop' is increasingly used to imply a sense of safety in relation to AI decision systems. It shouldn't. There are contexts where it can be applied appropriately, but these are not in the deployed decision systems we see dominating today. Human oversight of AI decision processes is one of the most popular proposals for addressing concerns, especially about bias, discrimination, misinformation, manipulation, accountability, and transparency. But there is insufficient examination of what human oversight actually means. The question raised in this paper is whether using the metaphor of a loop does anything to assist understanding of what is required and what is achieved in a particular decision context. Indiscriminate use of the loop metaphor obscures both processes and outcomes. It enables 'humanwashing', an activity analogous to 'greenwashing', where writers and commentators use language primarily aimed at putting systems in the best possible light.

---


### 299. [AnyFlow: Any-Step Video Diffusion Model with On-Policy Flow Map Distillation](https://arxiv.org/abs/2605.13724)

**<font color=#1a73e8>作者：</font>** Yuchao Gu, Guian Fang, Yuxin Jiang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-step video generation has been significantly advanced by consistency distillation. However, the performance of consistency-distilled models often degrades as more sampling steps are allocated at test time, limiting their effectiveness for any-step video diffusion. This limitation arises because consistency distillation replaces the original probability-flow ODE trajectory with a consistency-sampling trajectory, weakening the desirable test-time scaling behavior of ODE sampling. To address this limitation, we introduce AnyFlow, the first any-step video diffusion distillation framework based on flow maps. Instead of distilling a model for only a few fixed sampling steps, AnyFlow optimizes the full ODE sampling trajectory. To this end, we shift the distillation target from endpoint consistency mapping $(z_{t}\rightarrow z_{0})$ to flow-map transition learning $(z_{t}\rightarrow z_{r})$ over arbitrary time intervals. We further propose Flow Map Backward Simulation, which decomposes a full Euler rollout into shortcut flow-map transitions, enabling efficient on-policy distillation that reduces test-time errors (i.e., discretization error in few-step sampling and exposure bias in causal generation). Extensive experiments across both bidirectional and causal architectures, at scales ranging from 1.3B to 14B parameters, demonstrate that AnyFlow achieves performance matches or surpasses consistency-based counterparts in the few-step regime, while scaling with sampling step budgets.

---


### 300. [ScioMind: Cognitively Grounded Multi-Agent Social Simulation with Anchoring-Based Belief Dynamics and Dynamic Profiles](https://arxiv.org/abs/2605.13725)

**<font color=#1a73e8>作者：</font>** Yitian Yang, Yiqun Duan, Linghan Huang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM)-based multi-agent simulation offers a powerful testbed for studying social opinion dynamics. Yet current approaches often adopt two contrasting methods: either relying on fixed update rules with limited cognitive grounding or delegating belief change largely to unconstrained LLM interaction. We introduce ScioMind, a cognitively grounded simulation framework that bridges these paradigms by combining structured opinion dynamics with LLM-based agent reasoning. ScioMind integrates three key components: 1) a memory-anchored belief update rule that modulates susceptibility to influence via personality-conditioned anchoring strength; 2) a hierarchical memory architecture that supports persistent, experience-driven belief formation; and 3) dynamic agent profiles derived from a corpus-grounded retrieval pipeline, enabling heterogeneous personalities, rationales, and evolving internal states. We evaluate ScioMind on multiple case studies in a real-world policy debate scenario. Across metrics including polarisation, diversity, extremization, and trajectory stability, the proposed components consistently yield improvements in behavioural realism. In particular, dynamic profiles increase opinion diversity, memory and reflection reduce unstable oscillation, and anchoring induces persistent belief trajectories that better align with patterns reported in political psychology. These results suggest that our cognitively grounded design provides a novel solution to LLM-based social simulation that improves both stable and behavioural realism

---


> [!TIP]
> 当前位于：**251-300**（第 6/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | **251-300** | [301-328](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
