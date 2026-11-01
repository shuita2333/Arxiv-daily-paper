# 📦 其他研究 | 2026年11月02日

> 本类共 **432** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-432](./part-09.md)

---

### 51. [Predicting Sparse Observables in Parameterized Unsteady Flows Using Coarse-Mesh Graph Neural Networks](https://arxiv.org/abs/2610.37986)

**<font color=#1a73e8>作者：</font>** Brener Ramos, William R. Wolf, Tarcísio C. D. Oliveira 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Full-order surrogates for high-dimensional nonlinear flows are often unnecessary when applications require only selected degrees of freedom. We propose reduced-order models that bypass full-state reconstruction by deploying graph neural networks (GNNs) directly on coarse meshes. Applied to parameterized 2D/3D confined cylinder flows and an unevenly heated cavity over Reynolds/Rayleigh-number ranges, the models generalize to unseen conditions and accurately predict sparse probe locations and integrated quantities. Coarse-mesh GNNs match or outperform finer-mesh surrogates while reducing training time and memory, even for 3D chaotic dynamics. A dynamics-informed adaptive sampling strategy guided by frequency-spectrum variations reduces maximum errors by an order of magnitude versus uniform sampling at negligible cost. Coarse-mesh training also makes noise-augmented multi-step unrolling practical, improving long-horizon autoregressive predictions. The approach outperforms parametric DMD, sparse MLPs, U-Nets, and Fourier neural operators at lower cost, and enables system identification and state estimation from sparse observations. These results show that coarse-mesh representations, adaptive sampling, and noise-augmented unrolled training form an efficient framework for reduced-order modeling of parameterized unsteady flows without solver-resolution reconstruction.

---


### 52. [Deep learning for non-transvenous ICD screening: tailored neural network architectures, extended experiments, and explainability](https://arxiv.org/abs/2610.37993)

**<font color=#1a73e8>作者：</font>** Bartosz Morawski, Samuel J. Ward, Alex Touze 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper studies two non-transvenous implantable cardioverter-defibrillators (ICDs), namely the Subcutaneous ICD (S-ICD) and the Extravascular ICD (EV-ICD). Both avoid the complications of transvenous leads but are prone to oversensing, which can trigger inappropriate shocks associated with increased mortality. Oversensing risk is predicted by the ratio of T- or P-wave amplitude to R-wave amplitude (T:R, P:R), and these ratios vary over a 24-hour period. Yet S-ICD screening uses a single 10-second electrocardiogram (ECG) segment, and the EV-ICD has no formal screening protocol whatsoever. We present a 24-hour ambulatory screening framework for both devices which includes the first T:R analysis in an EV-ICD cohort and the first full evaluation of P:R prediction. We introduce AmpRatioNet, a family of 1D convolutional neural network architectures operating directly on the ECG signal, and benchmark it against the best existing approach - based on 2D phase space reconstruction images. Evaluation uses 4,605 clinician-annotated 10-second segments from 89 patients, with patient-level 10-fold cross-validation and bootstrap confidence intervals. AmpRatioNet-SE demonstrates superior performance on every metric in each setting with no device- or ratio-specific redesign. An explainability analysis against interpretable classical peak labelling algorithms shows that AmpRatioNet-SE's increase in error on oversensing-prone segments is up to 14 times smaller than theirs. Segment-level predictions are aggregated into a 24-hour timeline, extending S-ICD screening beyond 10 seconds and offering a plausible EV-ICD screening pathway pending device-level validation.

---


### 53. [Towards Generalizing Pretrained All-Atom Representations to Unified Binder Design](https://arxiv.org/abs/2610.37994)

**<font color=#1a73e8>作者：</font>** Maojiang Su, Jiale Chen, Qijie Zhu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> PairFormer-based all-atom models demonstrate strong capabilities in biomolecular binder design. However, existing methods often use all-atom representations for modality-specific binder design, such as protein and peptide design. In contrast, recent geometric latent diffusion models pursue unified binder design by representing molecular blocks from different modalities in a shared latent space. These complementary strengths motivate us to investigate how to generalize the use of pretrained all-atom representations to unified binder design. We introduce PairFuse, a parameter-efficient method that enables this generalization through representation fusion. Specifically, we use lightweight layerwise adapters to integrate pretrained all-atom representations into an independently pretrained geometric latent diffusion model. Our adapters integrate pretrained all-atom representations through two mechanisms: enriching the diffusion model's molecular block features and incorporating pairwise structural information into the geometric diffusion model's denoiser. Theoretically, we prove that the augmented denoiser preserves geometry and pairwise attention fusion provides additional attention expressivity beyond feature-only fusion. Experimentally, across antibody, peptide, and small molecule binder-design benchmarks, PairFuse achieves stronger performance than the pretrained diffusion model and existing representation-fusion baselines.

---


### 54. [QMUL_AK at AISA-ArabicFC: Schema-Constrained Function Calling with ALLaM](https://arxiv.org/abs/2610.37995)

**<font color=#1a73e8>作者：</font>** Ali Khairallah, Arkaitz Zubiaga  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We describe the QMUL_AK submission to AISA-ArabicFC 2026. The system adapts the Arabic-English ALLaM-7B-Instruct model to function calling with low-rank adaptation (LoRA). It combines an Arabic schema-aware prompt, dialect and no-call resampling, a token-weighted training objective, and deterministic validation of generated calls against the candidate tool schema. The same output supports Track A function calling and Track B reasoning-augmented calling. Training uses only the official task data. On the development set, the system achieves 0.9982 function accuracy and 0.8920 argument exact match, corresponding to overall A and B scores of 0.9345 and 0.9454. On the blind test set, the system reaches overall A and B scores of 0.9253 and 0.9380, ranking 3rd on both submission tracks and 1st of 21 teams on the Track C dialect-robustness diagnostic with a macro-averaged score of 0.9075 and the smallest dialect gap in the shared task (0.077). The results show that function selection is nearly saturated, while argument extraction remains the main source of error.

---


### 55. ["It Would Make a Geordie Feel at Home": Regional Accent Perceptions and Speech Accommodation in Voice AI](https://arxiv.org/abs/2610.38005)

**<font color=#1a73e8>作者：</font>** Dana Serditova, Kevin Tang, Jochen Steffens  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Automatic speech recognition (ASR) systems often perform less accurately for speakers of regional dialects, but less is known about how users respond to these limitations and how regional voices produced by voice assistants (VAs) are evaluated through a sociolinguistic lens. This study investigates these issues among speakers of Newcastle English (Geordies), examining both linguistic accommodation to voice technologies and perceptions of regional versus mainstream-accented VA voices. Participants interacted with a simulated VA that spoke either Newcastle English or Standard Southern British English (SSBE). They subsequently completed semi-structured interviews about their experiences with the experimental VA and voice technologies, language use, accent attitudes, and place orientation. The findings reveal a two-way process of sociolinguistic bias. The Geordie VA was associated with familiarity, warmth, personality, and local belonging, but also with concerns about professionalism and authority, whereas the SSBE voice was perceived as more neutral, clear, and credible. Participants also reported adapting their speech when voice technologies failed to recognise them, most commonly by shifting to a more mainstream accent, enunciating more clearly, and speaking more slowly. These strategies are similar to accommodation in human-human interaction and reflect users' perceptions of what technologies can recognise, also known as perceived intelligibility pressures. Overall, the findings demonstrate that voice technologies can reproduce existing accent biases both by encouraging users to suppress regional features and by activating established social stereotypes through synthetic voices. The study positions sociolinguistics as a bridge between understanding human-AI interaction and designing inclusive technologies around users' own linguistic priorities.

---


### 56. [Algorithmic Bias from the Perspectives of Healthcare Professionals](https://arxiv.org/abs/2610.38006)

**<font color=#1a73e8>作者：</font>** Jennifer Xu, Tamara Babaian  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper focuses on algorithmic bias of machine learning and artificial intelligence applications in healthcare information systems. Based on the quantitative data and qualitative comments from a survey and interviews with healthcare professionals, who have different job roles (e.g., clinical vs. administrative), this study provides findings about the relationships between algorithmic bias, perceived fairness, and the intended acceptance and adoption of ML algorithms and algorithm generated outcomes. The results suggest that the opinions of healthcare professionals toward the causes of algorithmic bias, the criteria of algorithm assessment, the perceived fairness, and bias mitigation approaches may vary depending on their job roles, perspectives, tasks, and the algorithm characteristics. More research is needed to investigate algorithmic bias to ensure fairness and equality in healthcare.

---


### 57. [Frequency-Adaptive Gaussian Grids for Efficient Image Representation](https://arxiv.org/abs/2610.38007)

**<font color=#1a73e8>作者：</font>** Anatolii Evdokimov, Stavros Diolatzis, Bingxuan Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Neural representation has emerged as a powerful tool to mitigate the demand for increasingly higher-resolution images. However, a fundamental trade-off remains between structured (e.g., feature grids, which offer spatial consistency) and unstructured (e.g., 2D Gaussians, which adaptively capture local variances) representations. This choice significantly affects how well an algorithm represents an image. Here, we present Gaussian-Grid, a hybrid neural representation that adaptively integrates structured and unstructured primitives. By dynamically partitioning computation between 2D Gaussian distributions and their attached multi-resolution feature grids based on the local frequency content, Gaussian-Grid automatically optimizes its architecture to match the underlying complexity of the target signal. We evaluate our approach using high-resolution natural images and demonstrate its applications as GPU-native dataset storage, showing $1.24$-$2.14\times$ decoding speed improvement and PCIe data traffic reduction of $23\times$-$176\times$ over JPEG + ZIP data archiving. The results show that Gaussian-Grid maintains small memory footprints while achieving high reconstruction fidelity across a variety of datasets.

---


### 58. [Making Smart Homes Fit for Autistic Children: Family Work and Monitored Independence](https://arxiv.org/abs/2610.38008)

**<font color=#1a73e8>作者：</font>** Tingting Xiang, Weihan Jiang, Hrishitva Patel 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> General-purpose smart-home technologies are increasingly present in family life, yet how they support or disrupt autistic children and families with autistic children remains underexamined. We conducted a multi-source qualitative study drawing on five caregiver interviews, Xiaohongshu (also known internationally as RedNote) posts explicitly situated in autism contexts, and contextual posts from Xiaohongshu and Weibo. We find that families create support for autistic children by adapting environmental outputs, prompts, and interaction channels, while sensory intensity, communicative rules, and opaque operating states can turn the same technologies into barriers. Support also depends on continuing family work, including translation, configuration, modification, maintenance, and boundary-setting. Remote monitoring enables conditional independence while generating tensions among safety, privacy, and control. We contribute three concepts, including relational fit, family work as support infrastructure, and monitored independence, for understanding accessible domestic technology. We derive design implications for adjustable interaction, legible and recoverable failure, lower-burden configuration, and negotiable monitoring.

---


### 59. [Beyond Aggregate WER: In-domain Adaptation, Learner Speech, Code-Switching, and Speaker Attribution in Online Spanish Learning Classrooms](https://arxiv.org/abs/2610.38016)

**<font color=#1a73e8>作者：</font>** Olga Kellert, Samhitha Harish, Johnatan E Bonilla 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic speech recognition (ASR) increasingly supplies transcripts for educational NLP, but aggregate word error rate (WER) can conceal errors concentrated in learner speech, multilingual turns, and speaker attribution. We compare platform-integrated, open-weight, adapted, and commercial ASR configurations on held-out sessions of online L2 Spanish interaction between L1 English learners and their instructors and tutors. Because English is the learner's shared first language, the interactions contain Spanish-only, English-only, and code-switched turns. Evaluation combines overall WER and character error rate (CER), WER disaggregated by speaker role and language context, and diarization error rate (DER). We also adapt Whisper large-v3 and MOSS-Transcribe-Diarize with LoRA using human-corrected in-domain classroom data. MOSS adaptation produced consistent improvements across speaker roles and language contexts, whereas Whisper showed smaller gains. Domain match proved more important than data volume: Larger out-of-domain bilingual and learner corpora did not outperform the smaller classroom corpus, where learner speech and code-switching are embedded in instructor--learner interaction. The open-weight MOSS adapter was competitive with commercial Muse Voice Transcribe on WER and CER and achieved lower system-provided DER on the recordings eligible for each system. Learner, English-only, and code-switched speech remained more difficult than instructor and Spanish-only speech. The findings demonstrate the value of condition-aware evaluation and interactionally matched data for bilingual educational ASR.

---


### 60. [Detecting Brain Cancer Progression Through Signatures of Wearable Accelerometry Data](https://arxiv.org/abs/2610.38021)

**<font color=#1a73e8>作者：</font>** Rishit Das, Barbora Barancikova, Matt Williams  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Glioblastoma and other high-grade gliomas (HGG) have a poor prognosis and are associated with progressive functional decline. The standard of care to assess progressive disease is contrast-enhanced MRI, which is expensive, claustrophobic, and performed only once every 2-3 months. Wearable accelerometers offer a non-invasive alternative for continuously monitoring patient function between clinic visits. However, accelerometry data streams are typically noisy and highly patient-specific, making conventional time series methods and summary statistics poorly suited to detecting clinically meaningful change. This work aims to classify stable versus progressive disease states by applying rough path signatures for feature extraction from wrist-worn accelerometer data. We convert accelerometer recordings from HGG patients enrolled in the BrainWear study into walking-path segments and use signature kernel maximum mean discrepancy (SigMMD) to quantify change in patients' walking behaviour. We overcome the challenge of inter-patient heterogeneity by adjusting for the natural variation in a patient's walking during stable tumour periods. This patient-specific normalisation substantially improves separation, yielding a candidate biomarker of tumour progression. Our results provide proof-of-concept evidence that signature-based analysis of wearable accelerometry can distinguish stable from progressive disease states, motivating larger longitudinal studies of continuous wearable monitoring as a digital biomarker in neuro-oncology.

---


### 61. [Making Sense of Audience Change: Causal Attribution and Boundary Management on Xiaohongshu](https://arxiv.org/abs/2610.38026)

**<font color=#1a73e8>作者：</font>** Zhiyi Zhou, Kyrie Zhou  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Recommendation-driven platforms can reshape not only what users see, but also who becomes visible and how community boundaries are negotiated. We examine Xiaohongshu discussions surrounding a perceived World Cup-related audience influx to understand how users attributed community change and how those explanations related to boundary-management strategies. We analyzed 262 comments from eight high-engagement threads using researcher-led thematic analysis, structured coding, and permutation-based association analysis. Users described personalization as both social separation and a boundary that could fail, interpreted platform growth through audience acquisition and commercialization, and contested whether gender should define community membership. Among 70 comments with explicit attributions and strategies, attribution and strategy were strongly associated (Cramer's V = .583): algorithmic attributions concentrated in technical boundary management, while social-actor attributions more often aligned with social enforcement or normative socialization. These findings connect causal sensemaking with boundary management and show how audience restructuring can create governance consequences on recommendation-driven platforms.

---


### 62. [Learning from Relative Action Credit for Escaping Local Minima](https://arxiv.org/abs/2610.38034)

**<font color=#1a73e8>作者：</font>** Giovanni Minelli, Giulio Turrisi, Lorenzo Amatucci 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning holds the promise of robots that learn manipulation skills from interaction alone, without pretrained priors or demonstration data. In practice, on-policy methods such as PPO routinely stall on long-horizon, contact-rich tasks: dense reward shaping carries the policy through stages, yet stitching them together and discovering sparsely rewarded events rarely succeeds. We trace this failure to the missing action discrimination in state-value credit assignment: a state-value critic judges progress only by episode outcomes, so when the policy converges to a partial solution all outcomes coincide, and improvement stops because no action can prove better than another. We therefore extend PPO with an action conditioned value critic which, can compare the executed action with alternatives sampled at the same state and aid the learning signal. Combined with Generalized Advantage Estimation and a bound on exploration noise, we show how the extended algorithm escapes the plateau and completes precise peg insertion within a training budget where PPO with identical exploration fails.

---


### 63. [Integral Probability Boundaries](https://arxiv.org/abs/2610.38036)

**<font color=#1a73e8>作者：</font>** Bogdan Kulynych, Shahab Asoodeh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bounds based on Integral Probability Metrics (IPMs) are ubiquitous in machine learning and statistics, appearing, e.g., in generalization, alignment, fairness, and privacy. IPMs reduce the discrepancy between two distributions to a single worst-case gap between expectations. This compression is costly: for rare events, safety failures, or under-represented groups, IPM-based bounds are loose or vacuous. We introduce a non-linear generalization of IPMs, which we term Integral Probability Boundaries (IPBs). Unlike IPMs, IPBs provide bounds that are tight at the extremes. We derive their basic properties and present algorithms for estimating them in practically relevant settings. We demonstrate the usage of IPBs in both theoretical and practical applications for alignment, judge-free performance estimation, and fairness, where they enable us to obtain sharp bounds on performance and fairness gaps, e.g., 15 p.p. more precise estimates on fairness gaps for rare groups in a realistic generative modeling task, compared to the state of the art.

---


### 64. [Measuring Deep Learning Performance - An Empirical Study of Performance Distributions Across Architectures and Tasks](https://arxiv.org/abs/2610.38037)

**<font color=#1a73e8>作者：</font>** Kevin L Coakley, Odd Erik Gundersen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Context: Non-determinism in deep learning algorithm design and implementation leads to performance variation, meaning model performance is not a single value, but rather a distribution. These model performance distributions are underexplored despite their impact on robustness. Objective: We investigate the robustness of deep learning performance to sources of non-determinism, specifically focusing on how performance distributions differ across various architectures and tasks. Method: We conducted 186 experiments on image classification and time series forecasting architectures. Each experiment was run 100 times with different random seeds to generate performance distributions, resulting in 18,600 runs. Robustness was quantified using metrics for spread, symmetry, and tail risk. Results: Performance distributions are frequently non-Gaussian, particularly in time series forecasting. Model size does not systematically affect robustness -- larger image classification models show fewer outliers but not lower spread, while smaller time series models show lower spread but more extreme underperformers. Training duration does not scale linearly; early stopping effectively balances performance and robustness. Mean performance does not predict robustness - time series forecasting shows moderate correlation while image classification shows none. Time series models produce nearly three times more underperforming outliers than image classification models, indicating substantially higher tail risk. Conclusions: Tail risk poses serious concerns for Trustworthy AI in high-stakes applications. Models performing well on average may exhibit long tails and extreme outliers revealed only through distributional analysis. Mean performance alone should not guide model selection; assessment of spread, symmetry, and tail risk is essential for reliable model assessment where consistent performance is critical.

---


### 65. [Classifying Urban Locations by Cyclist Facility Usage and Directional Alignment: A Validated Camera-Based Framework from Multi-Site Observations](https://arxiv.org/abs/2610.38045)

**<font color=#1a73e8>作者：</font>** Ao He, Mohit Gupta, Deborah Salon 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Objectives: Agencies invest in bicycle facilities but lack tools to assess whether cyclists use them as designed. We examine whether usage patterns follow facility configurations and whether higher bike lane usage is associated with less wrong-way riding.
Methods: Motion-triggered cameras covered 19 deployments at 17 locations in Tempe, Arizona, in 2023. Manual review identified 1,963 cycling events; excluding 20 crossings left 1,943 labeled events for analysis. An automated pipeline on the same captures counted 92.9 percent of the full manual total (per-deployment r = 0.99), and every automated wrong-way call was visually verified. Deployments were classified using thresholds on facility usage shares.
Findings: Deployments were bike-lane dominant (9), sidewalk dominant (6), or mixed (4). Cyclists in bike lanes rode against the flow in 4.6 percent of events; on sidewalks, riders opposed the near-side traffic flow in 49.6 percent. Across deployments, bike lane share and wrong-way rate were negatively correlated (Spearman rho = -0.87, p < 0.001, n = 16). An independent volunteer count in the same city showed a similar sidewalk-direction pattern (rho = 0.79).
Novelty: The study combines multi-site still-camera observations with a fully hand-verified benchmark to characterize facility use and travel direction.
Practical Applications: The workflow offers planners a low-cost screen for locations with high sidewalk cycling and travel against the near-side traffic flow, supporting more detailed site investigation.

---


### 66. [Cooperative EV Charging Assignment Using Multi-Agent Reinforcement Learning: A Comparison of QMIX and Independent Q-Learning Under Urban Traffic Uncertainty](https://arxiv.org/abs/2610.38053)

**<font color=#1a73e8>作者：</font>** Nour-Eddine Moumni, Rachid Alaoui, Driss Kiouach  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> The allocation of electric vehicles to public charging stations is increasingly constrained by the fact that several heterogeneous facilities often serve the same stream of requests while observing only partial local information. An accept/reject decision that is defensible for one station may nevertheless reduce the efficiency of the charging district as a whole. We formulate this operational problem as a Decentralized Partially Observable Markov Decision Process (Dec-POMDP) and examine whether Centralized Training with Decentralized Execution (CTDE), instantiated through QMIX, improves assignment performance relative to a cooperative Independent Q-Learning baseline (IQL). The evaluation uses a six-station urban network simulated with SUMO, five independent random seeds, 200 training episodes, and four traffic flux scenarios ranging from 100 to 250 vehicles/hour. Under this protocol, QMIX reaches a mean reward per evaluated decision of +0.776, versus +0.578 for IQL (delta = +0.198, seed-paired Cohens dz = 2.98, exact two-sided Wilcoxon p = 0.0625, the minimum attainable value at this sample size), and raises the acceptance rate from 72.4% to 94.0% (delta = +21.6 pp, dz = 5.24, Wilcoxon p = 0.0625). A five-variant ablation suggests this gain is primarily attributable to the CTDE architecture when holding cooperative reward terms fixed, though not formally isolated with a single seed. By contrast, cooperative reward shaping and experience sharing show no clear descriptive benefit and may slightly reduce performance. These findings support the view that, for multi-station charging assignment, coordination should be embedded in the learning architecture rather than added only through heuristic cooperation terms.

---


### 67. [Vision Tomography: Towards Portable 3D Bidirectional Face-Skull Inference from Visual Data](https://arxiv.org/abs/2610.38065)

**<font color=#1a73e8>作者：</font>** Zidu Wang, Meng Xu, Miao Xu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Traditional computed tomography (CT) can capture paired 3D face and skull geometry, but it remains costly, fixed in location, and exposes patients to radiation. For applications such as remote diagnostics, digital healthcare, forensic identification, missing-person investigation, and archaeological analysis, there is an urgent need for a portable, safe, and accessible solution to capture 3D skull geometry. In this work, we introduce Vision Tomography (VT), a concept and framework capable of reconstructing paired 3D face-skull geometry from various visual modalities, and also enabling joint manipulation of 3D facial and skull geometry. To achieve this, we first construct a dataset of over 200 samples, where each case includes a CT-based skull, a CT-based face, and a high-fidelity textured face scan. Secondly, we propose a novel dense ray matching registration method that ensures topological consistency across face, skull, and their tissue correspondences. Building on this registration, we introduce the 3D Bidirectional Face-Skull Morphable Model (BFSM) as the foundation of Vision Tomography, which enables shape inference between the face and skull through a shared coefficient space, while also modeling tissue thickness variation to support one-to-many facial reconstructions from the same skull, reflecting individual facial changes such as age or body fat. Finally, we demonstrate the effectiveness of Vision Tomography across various forensic and medical applications, including paired 3D face-skull reconstruction from images or sketches and predicting surgical outcomes with joint face-skull editing. Extensive experiments confirm the robustness and accuracy of our method. Vision Tomography is available at this https URL

---


### 68. [Progressive-Observation Physical-Layer Fingerprinting for Efficient Open-Set Ethernet Authentication](https://arxiv.org/abs/2610.38074)

**<font color=#1a73e8>作者：</font>** Chenming Zhang, Jiaxiang Geng, Aiqun Hu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Physical-layer fingerprinting (PLF) has emerged as a promising authentication approach for Internet of Things devices. However, most PLF systems acquire and process a fixed-length waveform for every authentication query, burdening resource-constrained edge nodes. To address this issue, we propose a progressive-observation PLF method that adapts the waveform length to each query. Specifically, a lightweight convolutional neural network (CNN) first rejects clearly unknown devices from a short observation. Spectral matching then accepts clearly registered devices from a slightly longer observation. Only ambiguous queries proceed to the same matching on the full-length waveform, reducing both data acquisition and computation. Because fingerprints drift across days, we also design an adaptive calibration algorithm to avoid retraining the CNN. The algorithm realigns the features and decision thresholds using a few current-day references from registered devices. We evaluate the method with 100BASE-TX Ethernet devices of two controller types on held-out days. Compared with fixed-length processing, it keeps the false rejection and false acceptance rates equal or lower for both controller types on both days. It also reduces the waveform data per query by 75.1% and the CPU processing time on a Raspberry Pi 5 by 73.7% on average. With the same monitoring bandwidth, an edge node can therefore serve about four times as many authentication queries.

---


### 69. [Infrastructure and its Discontents: Contestations of Power in Canada's AI Governance Scaffold](https://arxiv.org/abs/2610.38077)

**<font color=#1a73e8>作者：</font>** Christelle Tessono, Nusrat Jahan Mim, Shion Guha  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This paper develops a critical theoretical framework for understanding national Artificial Intelligence (AI) strategies through the lens of "Governance as Infrastructure." Integrating insights from Infrastructure Studies, Science and Technology Studies (STS), this paper employs Black Feminist Technoscience (BFTS) to reveal how AI governance infrastructures are assembled, maintained, and contested, and whose forms of knowledge, labour, and experience are rendered visible or invisible in these processes. We analyze the Canadian AI governance landscape through in-depth interviews with bureaucrats, civil society advocacy groups, academic researchers, and industry actors. Our inductive thematic analysis reveals how AI governance infrastructure enacts specific configurations of power, particularly through the politics of expertise; how actors navigate profound ambiguities related to AI's opacity, often involving strategic ignorance; and how mechanisms for justice and accountability struggle to address AI-related harms. We contend that a BFTS perspective highlights the limitations of current governance approaches and points toward alternative infrastructural designs prioritizing care, maintenance, participatory democracy, and adaptive temporalities to foster more equitable and accountable technology governance.

---


### 70. [CADENCE: Distributional Next-Transaction Forecasting for Business Cash-Flow Underwriting](https://arxiv.org/abs/2610.38084)

**<font color=#1a73e8>作者：</font>** Alexander Wu, Jingchao Huang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recurring cash flows are the backbone of cash-flow underwriting: they separate durable revenue from one-off deposits, expose standing obligations, and ultimately determine ability to pay. For small businesses, recurrence is both indispensable and hard to estimate, because much of their income arrives as ambiguous transfers, most payment streams are short, and schedules follow calendar conventions that frequency-domain methods treat as noise. We present CADENCE, Calendar-Aware Distributional Event Network for Cash-Flow Estimation, a compact causal Transformer that treats each transaction as a token and predicts the amount and a full, nonparametric timing distribution of every cash flow's next payment. Inheriting transaction semantics from an external labeler and a frozen text encoder keeps CADENCE compact yet general across the long tail of small-business counterparties, while predicting a calibrated distribution rather than an opaque embedding makes its outputs interpretable enough to feed existing underwriting models and power credit decisions. Ablations confirm the role of each design choice, with counterparty semantics driving recall on short histories, calendar inputs driving timing accuracy, and no-event supervision driving precision. Against the production FFT baseline, CADENCE improves one-day timing accuracy by 93.3% and next-event F1 by 6.7%, while producing calibrated distributions that serve directly as a confidence gate for downstream decisions. In an end-to-end credit evaluation on production applications, replacing FFT recurrence features with CADENCE features raises KS by 4.8%, raises the approval rate at a fixed loss rate by 18.2%, and lowers the loss rate at a fixed approval rate by 13.1%.

---


### 71. [From Next Day Wildfire to Next Days Wildfire: A New Multi-Continent Dataset of Active-Fire Spread for Sequence-to-Sequence Forecasting](https://arxiv.org/abs/2610.38086)

**<font color=#1a73e8>作者：</font>** Jose Guillen, Renzo Zanca, Valentin Barriere  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Benchmarks such as WildfireSpreadTS (WSTS) have enabled data-driven forecasting of wildfire spread from multimodal satellite time series, but they suffer from limitations: size restricts them to large fires that burn for weeks, and they are from similar environments. We introduce AFSeq, a multimodal dataset of 1,194 recent fire events (2023 to 2026) from 8 different countries across three regions, dominated by the short, small fires that existing benchmarks underrepresent. Our dataset is the largest and most diverse to date for time-series-based wildfire spread prediction. We also introduce UTAE-AR, an extension of a classical U-Net with Temporal Auto Encoder, enhanced with recurrent modules before the decoder. This allows the model to not only predict the next day but the whole sequence in an autoregressive way. Moreover, our model can feed its own predicted fire mask back one day at a time, producing the day-by-day forecasts that single-step models cannot. Our results show that UTAE-AR surpasses state-of-the-art on both WSTS, WSTS+ and AFSeq for next-day accuracy while having 21.5% of their parameters, and being able to predict confidently at a longer horizon.

---


### 72. [AI-Driven Digital Twin Framework for Warehouse Logistics Automation Optimization](https://arxiv.org/abs/2610.38101)

**<font color=#1a73e8>作者：</font>** Md Mahinur Alam, Kanita Jerin Tanha, Md Tanjin Alam 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In recent years, warehouse logistics optimization has increasingly focused on intelligent, data-driven systems to enhance operational efficiency. Conventional static product placement strategies are being progressively replaced by dynamic slotting approaches that can adapt to real-time variations in warehouse conditions. In this work, we present a novel framework that employs a reinforcement learning agent integrated within a FlexSim-based Digital Twin environment for real-time product placement optimization. The proposed agent continuously learns from streaming operational data, enabling it to reduce picking time while improving overall system throughput. The simulation environment models a four-zone warehouse layout with forklift-based material handling and leverages the Asset Administration Shell framework to ensure seamless interaction between the learning agent, physical asset, and the digital twin. Experimental evaluation demonstrates substantial performance gains, with the proposed approach achieving a 29.66\% reduction in average picking time, a 35.42\% increase in throughput, and an 18.54\% decrease in travel distance.

---


### 73. [SPARSEBLEED: Bypassing Attribute-Inference Defenses via Sparsity Optimizations](https://arxiv.org/abs/2610.38110)

**<font color=#1a73e8>作者：</font>** Darsh Asher, Farshad Dizani, Joshua Kalyanapu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Deep neural networks (DNNs) are widely deployed in safety- and privacy-critical domains such as healthcare and finance, where models are trained on confidential data. This paper presents the first hardware-level attribute-stealing attack that bypasses state-of-the-art privacy defenses, revealing that accelerator optimizations intended for performance can directly undermine data confidentiality. SparseBleed requires no access to gradients, logits, model weights, ground-truth labels, power traces, DVFS manipulation, shared caches, or other channels. Instead, we show that sparsity-driven execution paths encode stable timing signatures that act as a surrogate for model confidence, enabling high-fidelity attribute inference from a single query. SparseBleed generalizes across heterogeneous backends and hardware engines, including Intel AVX2/AVX-512/AMX, NVIDIA Ampere Tensor Cores with 2:4 sparsity, and nine well-known sparse and dense libraries such as Intel oneDNN, oneMKL SparseBLAS, and NVIDIA cuSPARSE. We evaluate SparseBleed to infer sensitive input attributes and true output labels. On Texas-100X, SparseBleed infers sensitive input attributes such as Sex with 66.39% accuracy and recovers the true output label, Surgical Procedure, with 99.8% accuracy. Finally, we evaluate mitigations. Constant-time execution by disabling sparsity optimizations is expensive (e.g., up to $2\times$ higher latency on NVIDIA Sparse Tensor Cores and $\approx 25\%$ higher power in AMX microbenchmarks). By contrast, a padding defense that equalizes responses to the worst-case time masks timing leakage with only 7.24% average performance overhead across nine libraries on Texas-100X/Adult and near-zero extra energy.

---


### 74. [Too Hard, Too Easy, Just Right: Performance-Driven Challenge Adaptation in Virtual Reality Firefighter Training](https://arxiv.org/abs/2610.38117)

**<font color=#1a73e8>作者：</font>** Xuan Wang, Jianan Jiang, Rongqian Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Effective firefighter training requires practice under dynamic and stressful emergency conditions, yet real-world live-fire exercises are costly, risky, and difficult to scale. Virtual Reality (VR) offers a safe and controllable alternative, but many existing VR firefighter training systems rely on fixed scenarios or provide limited difficulty adaptation, making it difficult to maintain an appropriate level of challenge for skill development as trainees' performance changes over time. To address this limitation, we present ProACT, a performance-driven adaptive training system that regulates scenario difficulty through closed-loop interactions between trainee performance and simulated fire dynamics. Specifically, ProACT combines a global module that continuously adjusts scene-level fire spread dynamics in real time based on trainee performance with a local module that periodically updates object-level flammability across the environment. Our evaluation shows that ProACT improves both objective training performance and subjective user experience compared with existing adaptive and non-adaptive baselines. We further discuss how adaptive immersive environments can extend beyond firefighting to broader training domains.

---


### 75. [What Does LOL Measure? Hidden Label Shifts in Low-Light Enhancement Benchmarks](https://arxiv.org/abs/2610.38121)

**<font color=#1a73e8>作者：</font>** Adityan Thirumani Srinivasan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> LOL-v1 and LOLv2-Real are the standard benchmarks for supervised low-light image enhancement, and several leading methods ship hand-set test-time adjustments with their evaluation scripts. We audit both benchmarks with 18 public checkpoints of eight methods under one metric implementation that reproduces every published number to within 0.09 dB, and find that their test labels differ from their training labels. (i) The 15 LOL-v1 test labels are rendered differently: the same captures appear in LOLv2 with labels of identical luminance but 1.48x lower saturation, and LOL-v1's own training labels match the LOLv2 rendering; we confirm this on the official release. (ii) The LOLv2-Real test set is the contiguous block of images 690-789, whose labels are 14% darker than the training labels (Cliff's delta = -0.45, p < 1e-12) with no comparable shift in the input statistics we examined; methods trained without any labels score up to 5.5 dB higher on test than on train. (iii) All 15 LOL-v1 test inputs reappear in LOLv2-Real, 12 in its training set. The released test-time settings are consistent with compensating for these shifts. Separating what can be calibrated on training data from what only test-set tuning finds, the test-only residual has median 0.00 dB on LOLv2-Syn, which has no shift, but 0.37 dB on LOL-v1 and 0.92 dB on LOLv2-Real (up to 3.9 dB). Under the shift, test-set checkpoint selection inflates a from-scratch model by 0.9-2.0 dB, and removing the released settings changes which method ranks first. We give concrete reporting recommendations.

---


### 76. [A Separation Principle for Adversarial Attacks and Defense of Graph Neural Networks](https://arxiv.org/abs/2610.38127)

**<font color=#1a73e8>作者：</font>** Farid Mafi, Saber Jafarpour, Mohammad Pirani  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adversarial attacks on graph neural networks (GNNs) have been studied as a model-centric optimization problem driven by gradients, learned policies, or meta-learning, with the graph treated as a passive substrate. This view overlooks a defining feature of GNNs: their predictions are produced by structured message passing along the graph, so their adversarial vulnerabilities are encoded as much in the geometry of the graph as in the learned weights. We develop a structure-driven framework for feature attacks in which the attack is derived from the spectral properties of the normalized adjacency operator. Its central result is a separation principle: under a natural relaxation of the attack objective, the optimal feature perturbation is rank one and factorizes into a graph-dependent component (degree-proportional spatial allocation, depending only on the graph) and a weight-dependent component (top singular vector of the composed weights, depending only on the weights). Node degree thus emerges as the fundamental graph quantity governing adversarial vulnerability to feature perturbations. The resulting attack, which we call SepAttack, requires no gradient computation, carries analytical guarantees, achieves competitive or superior performance against established baselines such as Nettack and IG-Attack with up to ${\sim}70\times$ speedup in the targeted setting, and transfers near-perfectly across architectures on continuous-feature graphs because its graph-dependent component is architecture-invariant by construction. We further derive a separation-principle adversarial training procedure (SepAT) directly from the closed-form worst-case attack and report robustness gains on binary-feature benchmarks.

---


### 77. [LogicTree: Object-Oriented Writing for Structured Human-AI Academic Authoring](https://arxiv.org/abs/2610.38136)

**<font color=#1a73e8>作者：</font>** Jiajun Zhu, Xinyu Cheng, Wenshuo Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Academic writing is non-linear, iterative, and structure-driven, requiring authors to develop fragmented ideas into arguments with local coherence and global consistency. However, current AI-assisted tools primarily exchange linear prompts and free-form text, forcing authors to reconstruct generated logic and repeatedly verify its alignment with their structural intentions. We propose object-oriented writing (OOW), an OOD-inspired representation and interaction paradigm in which persistent writing objects serve as shared, manipulable referents for authors and AI. We instantiate OOW in LogicTree, an Overleaf-integrated prototype that combines a hierarchical object representation with a structure-grounded writing assistance module for author-initiated generation and issue-grounded revision and a structural logical review module for inspecting local coherence and global consistency. A within-subjects study (N=12) provides initial evidence that, in controlled academic writing tasks, LogicTree helps users structure ideas, reduces workload, and improves measured logical quality compared with a conversational baseline.

---


### 78. [Zero Trust-Enabled Adaptive Incident Response using Hierarchical Reinforcement Learning](https://arxiv.org/abs/2610.38146)

**<font color=#1a73e8>作者：</font>** Jisoo Lee, Bhagath Singh Bondili, Harshith Doppalapudi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern enterprises increasingly operate through complex information systems (IS) enabled by cloud computing, remote and hybrid work practices, and digitally integrated supply chains. These structural shifts have expanded organizational attack surfaces and weakened traditional perimeter-based trust assumptions, giving rise to new and persistent forms of cyber threats. In response, adversaries have shifted toward identity-centric, trust-based intrusion techniques that exploit legitimate access within organizational systems. This evolution has created a pronounced speed asymmetry, whereby attackers can adapt and act at machine speed while defenders remain constrained by reactive or rule-based incident response (IR) processes. Drawing on design science research, we propose ZT-AIR, an adaptive IR artifact that uses zero trust architecture as its design theory and hierarchical reinforcement learning as its kernel theory. ZT-AIR learns context-aware trust decisions, separates strategic prioritization from tactical execution, encodes zero-trust controls as actions, and jointly optimizes security effectiveness and operational continuity. Experimental results across diverse adversarial strategies, network scales, and defense environments show that ZT-AIR achieves a strong balance between security and continuity through frequent, minimally disruptive interventions. Practitioner validation further confirms the design's practical viability. This study contributes to IS research by extending computational design science from threat identification to response execution, theorizing zero trust architecture for adaptive IR, and deriving reusable design principles for adaptive decision support artifacts.

---


### 79. [Estimating Implicit Expected Log Density Ratios](https://arxiv.org/abs/2610.38151)

**<font color=#1a73e8>作者：</font>** Avi Amalanshu, Chandler Squires, Yizhou Lu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When exact probabilities cannot be computed, \emph{density ratio estimation (DRE)} is a key subroutine in the wide range of applications where density ratios appear, from experimental design to generative modelling and reinforcement learning. In this paper, we introduce the concept of an \emph{expected log density ratio (ELDR)}: log density ratios that are integrated under some third, possibly distinct measure. We show many problems with implicit densities where DRE is naïvely used are actually ELDR estimation tasks, and prove fundamental limitations on finite-sample ELDR estimation. Based on these results, we argue that the typical DRE-based approaches are unsuitable for ELDR estimation, and provide some foundational motivation towards bespoke ELDR estimators. To demonstrate, we propose a simple modification to some DRE methods that allows samples convergent to the integral distribution to appear in training data. We show through benchmarks that this can improve ELDR estimation error.

---


### 80. [BridgeRouter: Gain-Aware Instance Routing over Cross-Modal Bridge Portfolios](https://arxiv.org/abs/2610.38152)

**<font color=#1a73e8>作者：</font>** Ruoxi Piao, Alicia Lu, Yunzhen Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Lightweight representation bridges make pretrained, task-adapted EEG foundation models executable on other biosignal modalities without retraining their backbones. However, selecting a single bridge pathway globally assigns every instance to the same transfer route and ignores complementary errors across routes. We therefore formulate multi-bridge transfer as an instance-level algorithm-selection problem and introduce BridgeRouter, a gain-aware router over a portfolio of frozen cross-modal pathways. A validation-selected Single Best Solver (SBS) serves as a protected default route. During training, task labels are used to compute the reduction in negative log-likelihood provided by each alternative route relative to the SBS, and a lightweight MLP predicts these route-specific gains from a target-modality representation extracted by a frozen encoder. At inference, BridgeRouter observes only the target modality, requires neither EEG, task labels, nor predictions from all candidate routes, and executes exactly one bridge pathway: the route with the largest predicted gain when that gain exceeds a validation-calibrated threshold, and the SBS otherwise. We evaluate seven EEG foundation-model bridge pathways for EMG-based freezing-of-gait detection on FOG and ECG-based sleep classification on ISRUC. Across five seeds, BridgeRouter achieves $81.38\pm1.11\%$ balanced accuracy on FOG, improving over the BIOT SBS by $11.49$ percentage points, and $62.92\pm2.17\%$ on ISRUC, improving over the CBraMod SBS by $3.83$ points. Per-instance bridge oracles reach $99.96\%$ and $78.61\%$, respectively, revealing substantial remaining portfolio headroom. These results show that anchor-relative gain prediction can convert complementary cross-modal bridge behavior into deployable instance-level routing improvements while retaining single-route inference.

---


### 81. [StepControl: Long-Horizon Human Motion Generation from Foot-Contact Schedules](https://arxiv.org/abs/2610.38153)

**<font color=#1a73e8>作者：</font>** Hojun Jang, Jinseok Bae, Donggeun Lim 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Controllable human motion generation has largely focused on specifying what action should occur or where the body should move. We study a complementary question: can full-body motion be controlled by specifying only when each foot contacts the ground? We introduce StepControl, an autoregressive diffusion model conditioned on a future binary left/right foot-contact schedule, without requiring target root and body poses, or semantic prompts. StepControl represents contact as explicit temporal events and injects them through dedicated cross-attention with classifier-free guidance. We further introduce a stochastic mixture noise schedule and warmup strategy for stable long-horizon autoregressive generation. Experiments show that StepControl follows prescribed contact timing more accurately than adapting existing spatially guided motion generators to contact constraints. It maintains effective contact control over long continuous rollouts and responds to edited schedules such as cadence changes, stop-and-go pauses, limping gaits, and bilateral jumping. Our results show that minimal foot-contact schedules provide an effective and intuitive temporal interface for controllable motion generation.

---


### 82. [MASS: Multi-mask Selective Self-Distillation for Leakage-Resilient Reasoning](https://arxiv.org/abs/2610.38154)

**<font color=#1a73e8>作者：</font>** Xiuqi Liu, Oveys Delafrooz Noroozi, Upamanyu Madhow  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy self-distillation enables the same model to act as student and teacher, with dense token-level supervision obtained by the teacher being given access to privileged information. However, conditioning the teacher on a single reference can concentrate its predictions on one reasoning trajectory and limit transfer to the student. We propose Multi-Mask Selective Self-Distillation (MASS), which approximates the unavailable marginal over diverse reference realizations using multiple independently masked views of one verified solution. MASS aggregates these complementary teacher predictions, selectively transfers reliable token-level corrections, and adaptively focuses masking on influential reference spans. Across mathematical reasoning benchmarks and model families, MASS consistently outperforms strong self-distillation baselines.

---


### 83. [Floor It, Then Fill It: Simulating Creator Ecosystems for Fair Video-Content Recommendation Systems at Billion User Scale](https://arxiv.org/abs/2610.38155)

**<font color=#1a73e8>作者：</font>** Sohini Roychowdhury, Long Sha, Sunand Agarwal 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Engagement-optimized content recommendation systems exhibit a well-documented rich-get-richer dynamic that structurally disadvantages emerging creators on large-scale platforms. Evaluating debiasing interventions at scale demands faithful simulation of creator-viewer ecosystems, yet the fidelity, diversity, and validity of such simulators remain underexplored. We present a grounded user-simulation framework that models a heterogeneous population of ${\sim}42$K creators and their coupled viewer interactions over 12~weeks, and use it to evaluate equitable view-allocation policies formulated as a budgeted multi-armed bandit (MAB). The simulator captures three behavioral dimensions: (i)~\textbf{creator diversity}, modeled via a clustering approach grounded in real platform creator-level distributions; (ii)~\textbf{behavioral fidelity}, captured through coupled creator-content state machines that represent growth trajectories, engagement accumulation, and graduation dynamics; and (iii)~\textbf{population-level validity}, measured by calibration against observed platform metrics. We evaluate simulative-configurations that vary content-viewership target definitions, reward functions, and a small-creator reserve lever to maximize creator-content recommendation equity. A floor-protected per content-view-target with a view-parity-gap reward guarantees 90\% of view targets being met by creators every week, grows small-creator organic reach ${\sim}{+}33\%$ per week, and achieves high distribution stability (set of creators with funded-views Jaccard $= 0.819$). We analyze the Sim2Real gap and propose validation protocols, contributing evidence for when simulation-derived fairness conclusions can be trusted.

---


### 84. [Neighbourhood shortcuts in building damage assessment from very-high-resolution satellite imagery: diagnosis and a building-evidence plug-in](https://arxiv.org/abs/2610.38162)

**<font color=#1a73e8>作者：</font>** JianChong Guo, YuTing Wan, Kefan Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Building damage assessment (BDA) from very-high-resolution imagery supports disaster response, and deep models now achieve high overall accuracy on public benchmarks. Because damage is spatially clustered, most buildings share the damage level of their neighbours, so overall scores are dominated by such buildings, whereas damaged buildings among intact ones are rare and easily overlooked. A high overall score therefore cannot tell whether a model judges the building itself or relies on its neighbourhood as a shortcut, and this study tests which of the two current models do. We stratify buildings by their agreement with their neighbours, move buildings into new neighbourhoods with their pixels unchanged, and diagnose nine models covering the main paradigms of BDA. All models miss a third to half of the isolated damaged buildings, and in non-flood events they call 73--87% of intact buildings damaged once these are moved into a damaged neighbourhood. We propose a building-evidence plug-in that adds two experts to an existing model without retraining it. One expert sees only the building, and the other sees its surroundings but is trained with seamlessly swapped neighbourhoods so that it learns not to trust them. With each of the nine models, the plug-in maintains or improves overall accuracy, reduces errors on buildings that disagree with their neighbours by 8--18%, and cuts by 40--69% the intact buildings that a damaged neighbourhood turns into damaged ones. It also raises the detection of synthetic isolated damage from 1--6% to 13--39% and carries over to optical--SAR data and to an unseen earthquake. High overall scores thus conceal a systematic reliance on the neighbourhood, which building-level evidence reduces at low cost.

---


### 85. [Replaying the Same Gradients at a Different $\varepsilon$: A Registered Test of the Fixed-Trajectory Account of Adam's $\varepsilon$ for One Rare Row](https://arxiv.org/abs/2610.38169)

**<font color=#1a73e8>作者：</font>** Lngel Kyo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adam divides every update by the square root of a running average of squared gradients plus a small constant, epsilon. For an output-embedding row whose token is rare, which we call the probe row, raising epsilon can be read as shrinking that row's steps by arithmetic alone. We test that reading directly. While a training run proceeds, we also divide the probe row's update by a different epsilon, using the run's own moment estimates; this replay is exact arithmetic on the gradients the run actually saw, so it holds the run's trajectory fixed. A rule for when the replay counts as wrong was written down before the runs.
We train a small causal transformer in a standard configuration. When epsilon rises by four orders of magnitude, the replay counts as wrong on each of the three seeds registered for the test: the probe row keeps 8.9--11.4 times more of its displacement than predicted with the main, sampled-negative head, and 5.0--7.7 times more with a full-softmax head scored as a second instrument. At three orders of magnitude, tested with the main head only, it does not, by narrow margins; a further two seeds, registered after this result had been committed and scored on their own, follow the same pattern. In separate real runs, raising epsilon on the probe row alone is enough to reproduce the row's change and raising it on every other parameter alone also moves the row part of the way --- readings about the runs that do not rescue the replay; scaling the row's learning rate instead, with the denominator untouched, is mispredicted by the replay in the same direction.
This is one embedding row of one model family on one corpus; we make no claim about rates, about rows in general (other rows were read only as a panel on one trajectory) or about how the effect changes with model size.

---


### 86. [B2P-Corr: Batch-to-Population Gradient Estimators for Non-Decomposable Correlation Losses](https://arxiv.org/abs/2610.38171)

**<font color=#1a73e8>作者：</font>** Jingquan Yan, Yuwei Miao, Peiran Yu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Correlation metrics such as the Pearson Correlation Coefficient (PCC) and Concordance Correlation Coefficient (CCC) are standard regression metrics and learning objectives, but their non-decomposable nature poses a challenge for stochastic optimization. Since these metrics depend on dataset-level moments (mean, variance, covariance), naive mini-batch training with local statistics yields biased, high-variance gradients whose expectation does not align with the population gradient. To bridge this ``batch-to-population'' (B2P) gap, we propose \textbf{B2P-Corr}, a novel framework that transforms correlation objectives into decomposable pseudo-losses driven by lightweight global ``moment sketches''. We introduce two efficient variants: \textbf{B2P-EMA}, which utilizes exponential moving averages and stop-gradient operators to ensure asymptotic gradient tracking with $O(B)$ cost ($B$ is batch size); and \textbf{B2P-U}, which uses sampled cross-batch U-statistic estimators and a reservoir-based stabilization with an $O(B)$ implementation. Theoretically, we quantify the $O(B^{-1})$ bias of naive mini-batch optimization, prove a moving-target tracking result for B2P-EMA under a fast-sketch / slow-parameter regime, and provide an idealized control-variate analysis for B2P-U. Experiments on two synthetic and three real-world datasets demonstrate B2P-Corr achieves stable optimization and higher correlation than naive mini-batch optimization with negligible overhead.

---


### 87. [Data Amount Heterogeneity Improves Performance in Federated Learning for Neuroimaging](https://arxiv.org/abs/2610.38172)

**<font color=#1a73e8>作者：</font>** Paul Kurian, Tamoghna Chattopadhyay, Abhijith Shaji 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated Learning (FL) allows for secure analysis of distributed data without data sharing. We and others have successfully applied FL to neuroimaging tasks, such as Alzheimer's disease classification from structural magnetic resonance imaging (MRI). FL trains a deep learning model locally at each site, encrypts the local model parameters and sends them to a federation controller that aggregates the local models under homomorphic encryption, the resulting community model is sent back to the sites for further training, and the process repeats for a number of rounds. FL often achieves learning performance (e.g., accuracy) close to centralized training, but no data leaves the sites and model parameters are protected through encryption and other measures.
In this paper, we show that federations composed of sites with heterogeneous amounts of data (1 large site plus small sites) perform better than homogeneous (same data per site) federations, particularly in low data regimes, while reaching performance close to centralized training. Having a big site often results in faster convergence and higher final accuracy. Heterogeneous federations better exploit sites with small amounts of data, a common situation in large consortia such as ENIGMA.

---


### 88. [A Gradient based Adversarial Augmentation Framework for Mitigating Unlearnable Datasets](https://arxiv.org/abs/2610.38173)

**<font color=#1a73e8>作者：</font>** Long Dang, Satpal Sura, Kaiqi Xiong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Unlearnable data methods (ULD) protect public data from unauthorized model training by adding imperceptible perturbations that create a learning shortcut. A deep neural network can exploit the shortcut learning path to minimize training loss without learning generalizable features. Intuitively, finding adversarial versions of perturbed images that can substantially increase the model's loss can force the model to learn generalizable features. Existing data augmentation based attacks rely on heuristic search strategies/random sampling over a curated augmentation set to identify adversarial augmentation operations, an approach that often does not scale when the number of candidate operations is large. To address the challenge of a large search space, we propose {\techname}, a gradient based adversarial augmentation framework that learns an augmentation policy via stochastic gradient ascent. {\techname} leverages a differentiable data augmentation pipeline to efficiently search a set of up to 18 augmentation techniques, from which a grid search selects a protection-specific subset. The augmentation subset is trained to maximize a surrogate model's classification loss. We introduce a perceptual-plus-pixel regularization to learn operation parameters that preserve image semantics. Under a controlled ablation, {\techname} consistently outperforms an equivalent random sampling baseline (80.0\% vs. 77.29\% clean test accuracy on EMIN-protected CIFAR-10 for ResNet-18 and 83.28\% vs. 66.45\% on NTGA-protected CIFAR-10 for MobileNet-V2), demonstrating that gradient guidance drives the clean test accuracy recoverability rather than the expanded search space. {\techname} offers an effective and scalable adversarial augmentation framework for stress-testing ULD methods, a critical tool for developing robust ULD methods.

---


### 89. [Scaling Lean Theorem Proving for Real-World Code Verification](https://arxiv.org/abs/2610.38174)

**<font color=#1a73e8>作者：</font>** Debargha Ganguly, Divya Raghunathan, Dejan Jovanović 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present EasyProver, a Lean proving system built from recursive agents with isolated contexts, asynchronous search, parallel tactic probing, and an elastic elaboration service. Using an off-the-shelf frontier model with no additional training, it proves 669/672 PutnamBench problems and all six IMO 2026 formalizations and resolves 597/600 NTP4VC verification conditions and all 189 VERINA tasks by proof or refutation. Because these benchmarks are close to saturation, we also introduce Aegis, which converts competitive programming problems into much harder verification tasks over real implementations. The pipeline writes safe Rust solutions, translates them into Lean with Aeneas, generates specifications, and labels each frozen statement with a kernel-checked proof or refutation. It produces 2,045 differentially validated Rust-Lean program pairs and 11,533 candidate specifications. Unlike hand-written benchmarks, these tasks carry implementation-level obligations from fixed-width arithmetic, explicit failure, generated loops, casts, and functionalized mutation. On a stratified sample of 2,000 statements, EasyProver proves 1,054 (52.7%) within a 30-minute budget per statement. The same tasks can also be used to benchmark other provers and as rewards for reinforcement learning.

---


### 90. [Prototype-Guided Dynamic Domain Modulation and a Large-Scale Multi-SKU Benchmark for Shampoo Bottle Surface Defect Detection](https://arxiv.org/abs/2610.38194)

**<font color=#1a73e8>作者：</font>** Yuehang Li, Xiao Wang, Qiang Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Industrial shampoo-bottle surface defect detection must operate across many stock keeping units (SKUs), where differences in bottle geometry, material, label layout, reflectance, and imaging conditions can substantially alter the appearance of the same defect. Existing industrial defect datasets rarely provide both instance-level defect annotations and product-variant identities, making it difficult to study SKU-aware detection under realistic manufacturing conditions. We introduce Bottle-SKU, a large-scale multi-SKU benchmark for shampoo bottle surface defect detection. Bottle-SKU contains 13,119 images, 20,419 instance-level bounding boxes, seven defect categories, and 48 bottle SKUs, enabling evaluation of both shared defect recognition and SKU-specific appearance variation. To address the challenge of SKU-specific appearance variation, we propose Prototype-Guided Dynamic Domain Modulation (ProDMM). ProDMM constructs a visual prototype for each SKU from training images and predicts a soft SKU distribution for each input. The resulting prototype-conditioned representation dynamically generates low-rank Query/Value modulation for the visual backbone and residual conditioning for defect-text-to-visual attention, while preserving the pretrained Grounding DINO detection pathway. The model is trained jointly with detection, SKU-domain classification, and modulation-regularization objectives. Experiments on Bottle-SKU and the public GC10-DET-SKU metallic surface defect dataset demonstrate the effectiveness of prototype-guided domain conditioning for industrial surface defect detection.

---


### 91. [Convex-SKM-Net: Low-Latency Block Halfspace Corrections for Neural Convex Constraint Satisfaction](https://arxiv.org/abs/2610.38197)

**<font color=#1a73e8>作者：</font>** Haoyu Zhu, Xiaochen Zhang, Qingchun Hou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fast inference and strict constraint satisfaction are essential for learning-based decision-making. Existing methods often rely on constraint-specific projections or feasible-set parameterizations, while iterative repair can be costly. We introduce Convex-SKM-Net, a convex constraint-satisfaction layer that forms linearization halfspaces from residual and (sub)gradient oracles without constraint-specific inequality projectors. It applies fixed-depth dual projected-gradient descent (dual PGD) to minimum-displacement block problems using GPU-friendly matrix operations. We jointly learn the predictor and a positive-definite mobility, adapting the correction geometry to improve objective quality. We prove convergence of the outer iterates at fixed dual depth and linear convergence in distance under Slater's condition and bounded subgradients. All our test outputs on three second-order-cone model-predictive control (SOC-MPC) horizons and six power-system convex relaxations satisfy a $10^{-3}$ feasibility tolerance. Comparisons with the latest constraint-satisfaction methods show inference speedups of up to $144.3\times$ on SOC-MPC and $7.7\times$ on a convex quadratically constrained quadratic programming (QCQP) benchmark with joint training. On QCQP, the mean objective gap is $0.012\%$, with full test feasibility at $10^{-4}$. Learning mobility reduces the five-seed affine-task mean gap by $22.4\%$ and improves gaps in matched power-system comparisons.

---


### 92. [Averaged Annealed Markov Chains Achieve the Algorithmic Threshold for Tensor PCA, Part II: Langevin Dynamics](https://arxiv.org/abs/2610.38206)

**<font color=#1a73e8>作者：</font>** Aniket Das, Tselil Schramm  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We consider the tensor principal components analysis (tensor PCA) problem on the sphere, in which we are asked to recover an unknown vector in $\mathcal{S}_N=\{x\in\mathbb{R}^N:\lVert x\rVert^2=N\}$ from a noisy observation of its $k$-th tensor power, for a fixed $k\ge3$. Tensor PCA exhibits a well-studied information-computation gap: global algorithms such as spectral methods and sum-of-squares work above an algorithmic threshold, below which we know matching lower bounds (against these and some other restricted models of computation). In contrast, local algorithms such as Markov chains were only known to succeed from a random initialization at a polynomially larger signal-to-noise ratio, and were believed to be inferior to global algorithms for tensor PCA. Continuing the program initiated in Part I [arXiv:2610.16705], we show that spherical Langevin dynamics, when supplemented with annealing and ergodic averaging, achieves polynomial-time strong recovery above the algorithmic threshold from a uniformly random initialization. Together with Part I, our results demonstrate that local Markov chains can succeed all the way down to the algorithmic threshold from an uninformative cold start.

---


### 93. [Progressive Coupling Method for Diffusion Posterior Sampling in Ptychography](https://arxiv.org/abs/2610.38207)

**<font color=#1a73e8>作者：</font>** Yihan Qiu, Mingtao Huang, Tianyuan Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Ptychography is a computational imaging method that reconstructs a sample from overlapping diffraction measurements. This technique relies on these overlapping measurements to provide the redundancy information needed for robust reconstruction, but dense scanning increases acquisition time and data volume. Reducing scan overlaps can improve measurement efficiency but weakens the physical constraints available for reconstruction. Diffusion models provide strong learned prior information, offering a promising approach to compensate for the loss of measurement redundancy. However, effectively utilizing this prior information under weak measurement constraints remains a challenge. We propose a progressive coupling posterior sampling (PCPS) method, which allows for a broader exploration of the solution space under high uncertainty while maintaining stronger diffusion-guided consistency as the reconstruction becomes more refined. Experiments on real X-ray ptychographic data at various scan overlaps demonstrate that PCPS consistently improves reconstruction accuracy compared to traditional iterative methods and existing diffusion posterior samplers, especially at low overlaps. These results show that diffusion priors can reduce the measurement redundancy required for accurate ptychography reconstruction.

---


### 94. [RainCheck: Harnessing Historical Weather Data with Machine Learning for Rainfall Forecasting in Bangladesh](https://arxiv.org/abs/2610.38211)

**<font color=#1a73e8>作者：</font>** Shahran Rahman Alve, Muhammad Zawad Mahmud, Samiha Islam 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine-learning rainfall forecasts are often evaluated by shuffling station records into random training and test sets. For rainfall, this lets a model see what happened at neighbouring stations on the very day it is asked to forecast, and it hides the fact that a seasonal lookup table already explains most of the variance. We quantify both effects on 618,650 station-days from 35 Bangladesh Meteorological Department stations (1948-2014). We compare random, temporal (train <=1999, test 2005-2014) and spatio-temporal (unseen stations and unseen years) evaluation, calendar-only versus antecedent-rainfall features, and six learners against climatology, persistence and SARIMA. Three findings stand out. First, a station-month climatology alone classifies high-rainfall months with 88.4% accuracy (AUC 0.950), and no learner improved on it by more than 0.8 points under temporal evaluation. Second, a calendar-only random forest reached a next-day wet-day AUC of 0.889 under a random split, higher than any model with real predictors under temporal evaluation, yet fell to 0.835, below climatology (0.859), on future years. Third, models with lagged rainfall add genuine but modest skill for next-day forecasts: a Brier skill score of 0.074 (95% CI 0.064-0.088) over climatology, rising to 0.091 when station and year inputs are removed and to 0.131 when other stations' same-day observations are added. A GRU sequence model matches but does not exceed gradient boosting, and skill disappears beyond a two-day lead. For monthly totals, no learner beat climatology significantly. We release a leakage-aware protocol and code so that future station-based studies report skill against climatology on held-out years.

---


### 95. [Silhouette-Based Gaitomics for Frailty Assessment in Older Adults](https://arxiv.org/abs/2610.38223)

**<font color=#1a73e8>作者：</font>** Laura McDaniel, Ryan Roemmich, Crystal Szczesny 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Walking offers a window into physical function that may support interpretable video-based frailty assessment. We developed silhouette-based "gaitomics" to connect frailty predictions with measurable patterns of body configuration and movement. In 66 older adults assessed using the Fried Frailty Phenotype, standardized silhouettes and gait energy images yielded 90 descriptors of shape, temporal variation, motion, and texture. Minimum redundancy maximum relevance selection using the mutual information difference criterion prioritized informative features while limiting redundancy. Each classifier was evaluated using nested stratified cross-validation with five outer and three inner folds at the participant level, with feature ranking and feature-count selection confined to training partitions. Shapley additive explanations examined contributions to held-out predictions. Bilateral silhouette difference led the aggregate feature-selection rankings for three-class classification and both comparisons involving frail participants. Attribution profiles differed across tasks, with texture and consecutive-frame silhouette differences prominent in three-class classification. Among classifier-specific evaluations, CatBoost achieved the highest mean three-class micro-AUC of 0.647 \pm 0.085. Leading pairwise mean micro-AUCs were 0.833 \pm 0.249 for frail versus nonfrail, 0.765 \pm 0.168 for frail versus prefrail, and 0.554 \pm 0.129 for prefrail versus nonfrail classification. These findings connect model predictions to explicit gait characteristics while revealing task-dependent feature priorities and limited separation of prefrail and nonfrail participants. The framework provides an interpretable basis for further investigation, with larger independent studies needed to establish reliability and clinical relevance.

---


### 96. [FACTS-MAS: A Multi-Agent Architecture for Adaptive Forecasting from Heterogeneous Evidence](https://arxiv.org/abs/2610.38225)

**<font color=#1a73e8>作者：</font>** Madumita Karthikeyan, Umang Rajnikant Bid, Rong Pan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Real-world forecasting often requires integrating heterogeneous evidence whose predictive value varies across horizons, operating regimes, and domains. We introduce FACTS-MAS, a domain-agnostic multi-agent forecasting framework that decomposes evidence into specialized channels for temporal dynamics, exogenous context, seasonality, structural information, and discrete events. Each agent generates an independently testable forecast through a common interface, while leakage-safe historical validation measures its predictive skill relative to a naive reference. These skill estimates are used to weight and combine agent forecasts, so that uninformative evidence is either removed or downweighted rather than forced to participate. A calibration procedure selects domain-specific constant means based on historical validation folds. We evaluate FACTS-MAS on weekly for-sale housing inventory from Zillow and weekly unemployment insurance claims from FRED, for 15 U.S. metropolitan areas at 4-, 8-, and 13-week forecasting horizons. Our method outperforms both a naive last-value forecast method and the TimesFM foundation model. However, a factor-adjusted exponential smoothing model performs as well as the fused forecast. The evidence therefore supports FACTS-MAS as a systematic protocol for testing, calibrating, and recomposing evidence channels before assembling them into the strongest single model for a specific application domain. Code, data, and results are available at this https URL.

---


### 97. [Variational Consequence-Driven Offline Reinforcement Learning](https://arxiv.org/abs/2610.38238)

**<font color=#1a73e8>作者：</font>** Wen Jiang, Ke Jiang, Xiaoyang Tan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Offline reinforcement learning (RL) typically mitigates distribution shift by imposing divergence constraints on the action distributions of the learned and behavior policies. However, this paradigm cannot ensure the underlying dynamic consistency structure: even minor action deviations can lead to drastically different transitions, inadvertently driving the agent away from the offline dataset. To address this, we explore policy constraints through their induced state-consequence distributions rather than relying on pure action-distribution matching. Nevertheless, directly enforcing such consequence-aware constraints is computationally intractable without access to the true underlying dynamics model. To bypass this issue, we propose Structural Behavior Regularization (StBR), which replaces the intractable objective with a closed-form latent divergence. Structuring this latent space to reflect transition dynamics renders the latent divergence a theoretically bounded surrogate for the true consequence-distribution divergence. By regularizing the learned policy with this latent divergence, StBR adaptively tightens the behavior constraint in dynamics-sensitive regions, effectively preventing deviations outside the offline dataset. Empirically, we demonstrate that StBR achieves superior performance across diverse offline RL benchmarks.

---


### 98. [MEV: A Multi-Event Video Dataset for Long-Take Generation](https://arxiv.org/abs/2610.38241)

**<font color=#1a73e8>作者：</font>** Peiyuan Zhu, Shaoan Xie, Yifan Shen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current datasets for text-to-video generation are largely limited to short clips depicting a single event or coarse-grained captions. As a result, they provide limited supervision for modeling long-take temporal dependencies, often leading to temporally inconsistent generations when describing multiple events. In this paper, we introduce MEV, a multi-event video dataset designed for long-take video generation. MEV provides high-quality real-world videos where subjects can perform a sequence of distinct, non-overlapping events, featuring precise temporal boundaries and fine-grained procedural annotations. This event-centric discretization reduces confounding factors and enables models to support temporally localized conditioning and build long-take videos from atomic event units. Furthermore, we introduce a comprehensive annotation pipeline that segments videos into temporally grounded events, and generates structured captions at both the global level and the event level. In addition, under an event-centric evaluation protocol, we conduct multi-event generation experiments by fine-tuning on MEV with temporally grounded event conditioning, leading to improved long-take event transitions and more coherent content. We believe this work provides a publicly available resource for multi-event fine-tuning and event-centric evaluation, together with practical insights into learning from temporally structured video-text data.

---


### 99. [Nearly Minimax Optimal Regret for Adversarial Linear Bandits with Strong Corruptions](https://arxiv.org/abs/2610.38243)

**<font color=#1a73e8>作者：</font>** Qiwei Di, Quanquan Gu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study adversarial linear bandits with strong corruption, in which an adaptive adversary chooses the reward vectors and a strong adversary corrupts each observed reward after seeing the learner's action, subject to a known total corruption budget $C$. Strong corruption breaks the importance-weighted reward estimates used by adversarial bandit algorithms: by corrupting only the rounds in which a rarely sampled action is drawn, the adversary amplifies each unit of corruption by the inverse of its sampling probability. The best known bound for this problem, $\tilde O(\sqrt{d^3T} + dC)$ by Liu et al. (2024), is a factor $\sqrt{d}$ above the corruption-free rate in its leading term, and whether $\tilde O(d\sqrt{T} + dC)$ regret is achievable was left open. We propose CRW-FTRL, which runs follow-the-regularized-leader with a radius-weighted entropy regularizer and estimates rewards with a normalized kernel estimator whose sensitivity to corruption is governed by per-action radii instead of inverse sampling probabilities. The radii are nondecreasing and are chosen jointly with the sampling distribution through a monotone log-determinant barrier problem, so that a negative linear term in the regularizer cancels both the corruption bias and the estimation error of every comparator. For $K$ actions in $\mathbb{R}^d$, CRW-FTRL achieves $\tilde O(\sqrt{dT\log K} + dC)$ regret with high probability against an adaptive adversary, which matches the best known corruption-free rate and the $\Omega(dC)$ lower bound up to logarithmic factors. Applied to a discretization of a general compact action set, it yields $\tilde O(d\sqrt{T} + dC)$ regret, which settles the statistical rate of corrupted adversarial linear bandits under strong corruption.

---


### 100. [Verification-Guided Retrosynthesis: Reaction Feedback and Evidence Timing](https://arxiv.org/abs/2610.38245)

**<font color=#1a73e8>作者：</font>** Hongxuan Shi, Hankz Hankui Zhuo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Retrosynthesis planning seeks synthesis routes from purchasable starting materials to a target molecule. Search over predicted reactions can connect a target to available materials, yet an infeasible reaction can invalidate the resulting route. Evaluating route quality only after search has finished cannot correct errors made during search. We introduce Verification-Guided Reflow (VGR), incorporating reaction verification as a decision action in AND/OR search. Verification results are represented as binary verdicts; queries are scheduled from the search structure, and acquired verdicts exclude reactions or adjust search priorities. We define verified solvability as the fraction of targets for which a complete route accepted stepwise by the verifier is found. On Retro190, feeding verification results into search increases verified solvability from 51.1% to 62.6% relative to route evaluation without feedback. Further controlled experiments show that earlier verification and immediate prioritization of accepted reactions each improve route discovery, yet combining them performs worse than either change alone. We therefore propose early pruning and delayed guidance: rejected reactions are pruned immediately, while accepted reactions gain search priority when processed as part of a complete candidate route. In a separate comparison with the verification scheduling rule fixed, this strategy increases verified solvability from 61.1% with immediate guidance to 71.1%, using fewer proposal calls and unique verifier queries.

---


> [!TIP]
> 当前位于：**51-100**（第 2/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-432](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
