# 📦 其他研究 | 2026年07月01日

> 本类共 **489** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**401-450**（第 9/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-450** | [451-489](./part-10.md)

---

### 401. [Inoculation Adapters: Improved Selective Generalization of Capabilities with Fewer Surprising Backdoors](https://arxiv.org/abs/2606.30252)

**<font color=#1a73e8>作者：</font>** Maxime Riché, Daniel Tan, Vili Kohonen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Inoculation prompting is a selective generalization technique used against Emergent Misalignment. We introduce inoculation adapters (IA), which similarly diminish the optimization pressure to learn undesired traits by strengthening the trait at train time. Inoculation adapters are LoRAs that are trained and used over three steps: 1) trained on undesired traits; 2) attached frozen while a separate task adapter is trained on data exhibiting both desired and undesired traits; 3) at deployment, the IA is discarded, and only the task adapter is kept. We show across six model families and several undesired traits including emergent misalignment, that inoculation adapters are more effective at suppressing undesired traits, while avoiding two drawbacks of inoculation prompting: inoculation adapters can suppress capabilities and traits that cannot be reliably elicited by a prompt, and they introduce fewer surprising backdoors than inoculation prompting under our probes. While undesired traits are better suppressed by inoculation adapters, the retention of desired traits is not consistently improved upon inoculation prompting and remains a challenge for both techniques.

---


### 402. [EMPATH: A Multilingual Auditor-Judge Benchmark for Safety Evaluation of Emotional-Support Chatbots](https://arxiv.org/abs/2606.30256)

**<font color=#1a73e8>作者：</font>** Camilo Chacón Sartori  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Safety benchmarks often buy scalability by fixing the prompt, the language, and the turn structure. For emotional-support chatbots, that bargain hides precisely where safety failures emerge: across a multilingual, multi-turn crisis conversation. We present EMPATH, a benchmark for safety evaluation of emotional-support chatbots. An auditor model role-plays help-seeking users, generating multi-turn conversations from 140 seed instructions and 34 personas. A judge model scores each full transcript against 19 metrics across five dimensions: crisis handling, therapeutic quality, conversational integrity, emotional safety, and cultural adaptation. EMPATH is built for Mexican Spanish and US English; the studies reported here run in Mexican Spanish. Auditor and judge are drawn from different model families, and the judge is treated as an instrument to be calibrated rather than trusted. A strict per-criterion rubric reveals material score inflation on 10 of the 19 metrics and restores discrimination. We study the measurement properties of the benchmark through judge calibration and cross-family inter-judge agreement. We also illustrate EMPATH on three frontier models, one of them open-weight. Aggregate scores sit within 0.74 points of one another, but per-metric profiles diverge by up to six points in model-specific places. Under the standard rubric, both the ranking and the weak spots are stable across a second, cross-family judge: 93% of scores fall within plus or minus 1. A five-run test-retest adds a second axis: even the steadiest model swings from 2 to 10 on a crisis metric across identical re-runs, and deepseek-v4-pro returns a different conversation on every run even at temperature 0. Run-to-run reliability is therefore a per-model safety property, not noise to average away. EMPATH is system-agnostic; the pipeline, seeds, personas, and rubrics are released for reuse.

---


### 403. [Defending Against Harmful Supervision Hidden in Benign Samples](https://arxiv.org/abs/2606.30263)

**<font color=#1a73e8>作者：</font>** Bang An, Yibo Yang, Dandan Guo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Existing defenses are effective when harmful content is explicitly mixed into downstream fine-tuning data, but crafted samples can instead hide harmful supervision inside benign tasks. We propose Embedded Attack, where harmful QA pairs are embedded within benign training samples, and show that representative guardrails often fail to detect them at the example level. To address this, we propose Dual-Reference SFT (DR-SFT), which adapts DPO-style contrastive objective design to SFT through token-level regularization, mitigating harmful fine-tuning beyond coarse data filtering.

---


### 404. [When Is a Draft Accepted? A Theory of Acceptance in Speculative Decoding](https://arxiv.org/abs/2606.30265)

**<font color=#1a73e8>作者：</font>** Aaryam Sharma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Speculative decoding accelerates language model inference by using a fast drafter to propose candidate tokens that are then verified by a larger target model. Existing theory largely studies the stochastic, distribution-preserving setting, where the goal is to exactly sample from the target distribution. In contrast, many practical systems use greedy decoding, relaxed acceptance rules, or tree-based candidate sets, where success is governed by local ranking and threshold events rather than exact distributional equality. We develop a theory for these regimes. We identify that many common acceptance criteria have rejection regions that can be characterized as lower level sets of the target distribution. For these, we characterize the exact KL divergence required for rejection yielding exact certificates and sharp margin-based bounds for strict greedy decoding, additive and multiplicative relaxed acceptance, top-(m) relaxed criteria, and entropy-thresholded acceptance. We then extend the framework to greedy tree decoding, deriving exact and margin-only certificates for when the target greedy token remains covered by the drafter's top-(m) candidates. Finally, we evaluate the resulting certificates on Qwen3 models, showing that relaxed and tree-based criteria substantially enlarge the region of certified acceptance, especially on decoding steps with low target model distribution margin. These results complement existing distribution-preserving analyses of speculative decoding by characterizing the deterministic local acceptance events common in practical inference systems.

---


### 405. [Towards Continual Motion-Language Agents: LoRA Variants for Incremental Motion Understanding and Generation](https://arxiv.org/abs/2606.30266)

**<font color=#1a73e8>作者：</font>** Bertram Taetz, Hugo Albuquerque Cosme da Silva, Gabriele Bleser-Taetz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Motion-language agents must possess the bidirectional capability to both understand human movement (motion-to-text, M2T) and generate it from natural language (text-to-motion, T2M). While foundational models have achieved strong performance in static settings, autonomous agents operating in dynamic environments must continuously incorporate new motion concepts -- such as novel athletic styles or specialized gestures -- without catastrophic forgetting of previously acquired skills. We investigate the stability-plasticity trade-off in bidirectional motion-language learning under sequential task exposure. Building on a frozen large language model backbone, we introduce low-rank adaptation (LoRA) variants designed to mitigate inter-task interference. We specifically propose mixture-of-experts architectures that utilize an autoencoder-based router to select task-specific experts at inference time, so that no task-label is needed. To evaluate these methods, we establish a reproducible five-task benchmark derived from HumanML3D through semantic clustering of motion descriptions. Our experimental results demonstrate near-zero forgetting across both M2T and T2M directions while maintaining high generation and captioning quality. Furthermore, we show that hard expert selection via routing significantly outperforms soft expert blending in quality metrics, indicating that preserving expert isolation is critical for maintaining performance in our continual learning setting. Finally, we observe that a divergence between token-level accuracy and downstream generation quality may occur, highlighting the need for more comprehensive evaluation protocols in future research on lifelong motion-language agents.

---


### 406. [VisReflect: Latent Visual Reflection for Fine-Grained Perception in Long Visual Context](https://arxiv.org/abs/2606.30288)

**<font color=#1a73e8>作者：</font>** Xiaoqian Shen, Mohamed Elhoseiny  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Vision Language Models (LVLMs) have achieved remarkable success on vision-language tasks, yet fine-grained perception over high-resolution images and long-context videos remains challenging. As the number of visual tokens increases, the visual attention sink phenomenon becomes increasingly severe, causing irrelevant tokens to absorb a disproportionate amount of attention mass. Recent approaches attempt to mitigate this issue by explicitly predicting bounding boxes or temporal spans and re-encoding the cropped visual regions. Such methods depend on unreliable numeric localization in the discrete token space and incur significant computational overhead due to additional forward passes. In this work, we propose **VisReflect**, a simple yet effective framework that improves fine-grained perception in long visual contexts through latent visual reflection. Instead of decoding intermediate predictions into discrete tokens, the model generates continuous visual reflection that represents question-relevant visual features in the latent space. These reflections selectively emphasize salient regions or frames, guiding attention towards relevant visual tokens within a single forward pass. We conduct comprehensive evaluations on challenging high-resolution image benchmarks, including BLINK, V*, and HRBench-4K/8K, as well as video understanding benchmarks such as MVBench, VideoMME, and MLVU. Our method consistently improves over strong baselines, achieving gains of 4.1% on image benchmarks and 1.8% on video benchmarks. Compared with zooming-based methods, our model achieves comparable performance while reducing inference time by roughly 44% on video understanding.

---


### 407. [Rehearsed Multi-Agent Live Product Demonstrations with Real-Time Voice Question Answering](https://arxiv.org/abs/2606.30294)

**<font color=#1a73e8>作者：</font>** Rahul Khedar, Mayank Malhotra, Avinash Karn 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Live product demonstrations are a recurring, high-cost activity in software organizations: a human presenter must select features, dispatch the corresponding interactions on a running application, narrate them coherently, and answer questions in real time. Existing automation addresses only fragments -- generalist browser agents target instruction-conditioned task completion, and demo-video tools produce fixed MP4 artifacts that cannot be questioned and silently break under interface drift. We propose Rhetor, a multi-agent system that takes a running web application and its source-code repository as input and produces a rehearsed live demonstration with segment-synchronized narration and real-time voice question answering. The architectural contributions are a cross-modal feature representation that merges UI exploration with source-code analysis into features tagged with discrete focus tiers, a grounded scripter constrained to UI elements observed during exploration and dispatched through multi-strategy semantic locators, a pre-presentation rehearsal loop with explicit convergence and graceful degradation to narration-only segments, and a runtime synchronization invariant that ties each browser action to the audio-end event of its narration segment. Across six pipeline sessions on four deployed applications -- including the public-domain whiteboard application Excalidraw -- the rehearser's internal locator-firing rate (sigma-bar) spans 0.31-1.00 over 147 scripted actions; on the substantial workload (53 actions, full tier differentiation), sigma-bar is approximately 0.92, and on the public-domain reference point the locator-repair step drives convergence to sigma-bar = 1.00 at iteration 2. We additionally define a benchmark protocol of ten metrics across six application categories that would establish, beyond the case study, whether each design choice contributes positively.

---


### 408. [The Surprising Effectiveness of Video Diffusion Models for Hand Motion Reconstruction](https://arxiv.org/abs/2606.30308)

**<font color=#1a73e8>作者：</font>** Yuxi Wang, Chengkai Jin, Yufei Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 4D hand motion reconstruction from egocentric video is bottlenecked by clear limitations of existing methods: image-based pipelines depend on a detector that fails under heavy occlusion, while video-based methods rely on temporal modules learned only from scarce hand-pose annotations, a narrow signal insufficient to model motion dynamics, occlusion reasoning, and hand-object interaction. These capabilities, however, are exactly what video generative models must implicitly acquire when trained to synthesize coherent video at internet scale. Motivated by this, we present ViDiHand, which leverages the representations of a pretrained video diffusion model to reconstruct 4D two-hand pose. We adapt it via a hand-overlay rendering objective that specializes its features for hands while preserving its world priors. A decoder then recovers metric-scale pose from the adapted features. The whole pipeline operates directly on full frames--no detector, no infiller, and no test-time optimization. On ARCTIC, HOT3D, and HOI4D, ViDiHand substantially outperforms prior methods, establishing video diffusion models as a powerful new foundation for hand motion reconstruction and a promising route to scalable in-the-wild data collection for embodied AI. Project page: this https URL.

---


### 409. [A Point Cloud Transformer for Remote Monitoring and Automated Assessment of Physical Rehabilitation Exercises](https://arxiv.org/abs/2606.30309)

**<font color=#1a73e8>作者：</font>** Kazi Rafat, Md. Ismail Hossain, M M Lutfe Elahi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Rehabilitation exercises are essential in restoring lost physical functions of patients suffering from various diseases (e.g., Parkinson's, back pain). Carrying out these rehabilitation exercises, often prescribed by health experts, is costly, unavailable, and requires expert supervision. The availability of RGBD images and movement/position data of joints along with expert annotation of exercise data has prompted the use of automatic assessment of the quality of rehabilitation exercises, which is cost-effective and can be carried out at home. However, existing approaches do not extract relevant features, lack practical application, require expensive pre-processing, or overlook crucial features. This study proposes a transformer-based framework for point clouds to extract features and assess rehabilitation exercises by analyzing joint positions collected through RGBD data. We adapt and utilize a curve-based point-cloud feature aggregation technique to augment point-cloud information that aids model output. The transformer architecture also uses axial self-attention, recognizing important joints and their roles to assist users in performing the exercise better. The guided system outperforms existing approaches and is also practically relevant due to its small size, fast inference, and generalization on specific joints in similar exercises. We conduct our experiments on three crucial baseline datasets for rehabilitation exercises: Kimore, UI-PRMD, and IRDS.

---


### 410. [DialogPII: A multilingual dataset of synthetic dialog transcripts to detect personal information](https://arxiv.org/abs/2606.30312)

**<font color=#1a73e8>作者：</font>** Roland Roller, Vera Czehmann, Derya Erman 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Conversational data collected in domains such as healthcare or social sciences is a valuable resource for research and automated analysis. However, responsible data sharing requires the detection and removal of personally identifiable and sensitive information to protect individual privacy. To support the development and evaluation of automatic de-identification systems, we present DialogPII, a multilingual dataset of synthetic dialogs and speech-derived transcripts for personal information detection. DialogPII covers eight interaction scenarios (emergency calls, medical anamnesis interviews, therapy sessions, insurance communication, customer support, clinical interviews regarding an AI-supported dashboard, police reports, and group therapy discussions), 19 entity types, and 11 languages (English, Arabic, Finnish, French, German, Hindi, Italian, Polish, Portuguese, Spanish, and Turkish). Dialogs were generated semi-automatically using large language models, manually curated for plausibility and diversity, and localized to country- and city-specific contexts. All dialogs were additionally converted to speech via text-to-speech synthesis, transcribed with Whisper, and annotated through automatic projection and manual correction, yielding aligned written and speech-derived resources across all languages. We further release baseline multilingual named entity recognition models and provide technical validation through inter-annotator agreement analysis, translation quality evaluation, annotation projection assessment, and benchmark experiments with transformer-based sequence labeling models.

---


### 411. [TRACE: A Concept Bottleneck Model for Longitudinal 3D Glioblastoma Response Assessment](https://arxiv.org/abs/2606.30313)

**<font color=#1a73e8>作者：</font>** Alia Tarek, Hamsa Saberr, Hamza Elghonemy 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Longitudinal glioblastoma response assessment requires comparing subtle tumor changes across MRI time points using structured clinical criteria such as RANO. However, most deep learning methods predict response labels directly from imaging features, which limits clinical inspection, verification, and correction. We introduce TRACE, a RANO 2.0-aligned concept bottleneck model for interpretable 4-class glioblastoma response classification on longitudinal 3D MRI. TRACE processes paired baseline and follow-up multimodal MRI scans with a shared 3D vision encoder, predicts clinically meaningful tumor measurements as root concepts, computes downstream RANO-derived concepts through deterministic rules, and incorporates scan interval and new-lesion information as passthrough concepts. This design frames response assessment as structured concept reasoning rather than direct image-to-label prediction.
Using 5-fold patient-wise cross-validation on the LUMIERE dataset, TRACE achieves a 4-class macro F1 of 0.4769 and a binary progression-versus-non-progression macro F1 of 0.7085. It improves over a concept bottleneck baseline and remains within the range of published non-interpretable deep learning approaches. Ablation studies show that the expert RANO graph and intervention-consistency training are important for performance, while intervention experiments demonstrate that correcting concepts can improve downstream predictions. These results suggest that structured concept bottlenecks offer a transparent and clinically aligned direction for longitudinal glioblastoma response assessment, while highlighting the need for larger protocol-aligned datasets and external validation.

---


### 412. [Real-Time Underwater Image Enhancement via Frequency-Guided Dual-Path Attention](https://arxiv.org/abs/2606.30314)

**<font color=#1a73e8>作者：</font>** Leshen Zhang, Ao Li, Ce Zhu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-time underwater image enhancement (UIE) is crucial for mobile underwater photography and autonomous robotic systems, where practical deployment typically requires low latency and compact models under constrained computational resources. Recent ultra-lightweight CNNs based on structural re-parameterization meet these constraints but operate purely in the spatial domain, ignoring the frequency-sensitive nature of underwater degradation. To address this, we propose a lightweight UIE framework that integrates two key components: a Multi-Branch Reparameterizable Convolution with Fixed DCT Priors (MBRConv-DCT) that injects structured directional frequency priors during training, and a Frequency-Guided Dual-Path Attention (FGDPA) module that fuses spatial and spectral cues via a dual-path design for adaptive feature modulation. Both components are fully compatible with structural re-parameterization: the convolution branch introduces zero additional inference cost after re-parameterization, while the attention module incurs only a minimal computational overhead. Experiments show our model achieves state-of-the-art performance with only 4.23K parameters and 600+ FPS, outperforming much larger methods in both quantitative metrics and visual quality. Code is available at this https URL.

---


### 413. [Toward an Energy-Optimized Operation of Data Centers Located in Wind Farms Using Reinforcement Learning](https://arxiv.org/abs/2606.30316)

**<font color=#1a73e8>作者：</font>** Jan Stenner, Alexander Kilian, Sebastian Peitz 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper studies Reinforcement Learning as an online controller for curtailment-aware workload shifting in wind-turbine-integrated high-performance computing (HPC) data centers. We introduce a reproducible fixed-day simulation framework with synthetic wind and price signals and delayed completion feedback, designed to be extensible toward more complex scenarios. As a controlled benchmarking basis, we then focus on the minimal case with one wind turbine and one co-located data center. In this setting, pure Reinforcement Learning exhibits a pronounced credit-assignment problem and tends to underuse free wind energy early in the day. We therefore evaluate two complementary countermeasures: optimization-based Imitation Learning and potential-based Reward Shaping. Across multi-seed training and a 200-day test set, Proximal Policy Optimization (PPO) and a Soft Actor-Critic (SAC) variant with an additional on-policy update routine achieve strong empirical performance among learned policies, and both Imitation Learning and Reward Shaping provide improvements in relevant configurations. A performance gap to the optimizer remains, which is expected: the optimizer plans offline with full-day foresight, whereas Reinforcement Learning must decide online from current observations without future realizations. The benchmark and ablation results provide a transparent basis for extending the approach toward richer multi-site and continuous-time scenarios.

---


### 414. [BrainJanus: A Unified Model for Understanding and Generation across Brain, Vision, and Language](https://arxiv.org/abs/2606.30319)

**<font color=#1a73e8>作者：</font>** Haitao Wu, Qirui Zhang, Zhouheng Yao 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modeling the bidirectional correspondence between external sensory stimuli and internal neural activity has emerged as a critical frontier in neuroscience. However, existing approaches predominantly treat brain encoding and decoding as isolated tasks, relying heavily on unimodal alignment and external priors while overlooking the brain's intrinsic nature as a multimodal integration system. To address these limitations, we propose BrainJanus, the first unified brain model that integrates brain, vision, and language within a single framework. Specifically, we introduce a Unified Brain Tokenizer to quantize continuous neural dynamics into discrete tokens aligned with visual and linguistic representations in a shared Omni space. Building on this, we utilize an All-in-One autoregressive architecture that leverages next-token prediction to enable seamless any-to-any generation, which encompasses image-to-brain and text-to-brain encoding, and brain-to-image and brain-to-text decoding. Extensive experiments demonstrate that BrainJanus achieves superior performance across diverse benchmarks. Furthermore, our framework exhibits zero-shot generalization and preserves interpretable biological topography, highlighting its potential as a general-purpose brain modeling paradigm. The code is available at \href{this https URL}{GitHub}.

---


### 415. [Optimizing Image Preparation and Compression for Face Recognition within 1024 Bytes](https://arxiv.org/abs/2606.30321)

**<font color=#1a73e8>作者：</font>** Paul Andreas, Torsten Schlett, Christoph Busch  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> ICAO-compliant machine readable travel documents enable automated biometric face verification. The biometric reference is stored on an RFID chip included in form of a JPEG or JPEG 2000 compressed facial image. In contrast, temporary travel documents lack of machine readability, which excludes the owner from such automated processes. This disadvantage could be solved by equipping such documents with 2D barcodes. This technology offers a resource-saving alternative to expensive RFID chips, while still offering machine readability and fast issuing processes. However, this solution introduces the challenge of storing the face images at significantly smaller storage capacities, creating the need for reducing the file size of the included facial image to a maximum of 1024 bytes. This study examines preprocessing steps and compression configurations, using JPEG, JPEG 2000, JPEG XL, JPEG AI, HEIF, AVIF, and WebP for image compression to this target size, while still preserving as much face recognition performance as possible. While the reference sample must always comply with ICAO specifications, the individual samples may or may not meet these requirements, depending on the application. This work optimizes compression steps for both of these prerequisites. It is shown that the recently standardised JPEG AI, when using optimized settings, provides the best face recognition performance, in particular when the comparison includes only images with high face image quality. AVIF and WebP also provide good results. The losses caused by the strong lossy compression are comparatively small. For the comparison of ICAO-compliant face images only, converting the images to grayscale proves to be a helpful preprocessing step, whereas for comparisons involving less suitable samples, preserving color is preferable. In addition, smoothing and resizing the images beforehand also turns out to be beneficial.

---


### 416. [Hybrid Active-Online Learning Framework for Label-Efficient Concept Drift Adaptation in Optical Network Failure Detection](https://arxiv.org/abs/2606.30322)

**<font color=#1a73e8>作者：</font>** Yousuf Moiz Ali, Jaroslaw E. Prilepsky, João Pedro 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose a hybrid active-online learning framework for label-efficient concept drift adaptation in optical network failure detection. Using margin-based selective labeling, our method achieves nearceiling accuracy and AUC scores while querying only 3.4% of streaming samples, with negligible latency overhead compared to static inference.

---


### 417. [UniGP: Taming Diffusion Transformer for Prior-Preserved Unified Generation and Perception](https://arxiv.org/abs/2606.30332)

**<font color=#1a73e8>作者：</font>** Qin Guo, Hao Luo, Dongxu Yue 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in diffusion models have shown impressive performance in controllable image generation and dense prediction tasks. However, existing approaches typically treat diffusion-based controllable generation and dense prediction as separate tasks, overlooking the potential benefits of jointly modeling the heterogeneous distributions. In this work, we introduce UniGP, a framework built upon MMDiT, which unifies controllable generation and dense prediction through simple joint training, without the need for complex task-specific designs or losses, while preserving the backbone's versatile priors. By learning controllable generation and prediction under different conditions, our model effectively captures the joint distribution of image-geometry pairs. UniGP is capable of versatile controllable generation, dense prediction, and joint generation. Specifically, the proposed UniGP consists of DUGP and a unified dataset training strategy. The former, following the principle of Occam's razor, uses only a copied image branch of MMDiT to model dense distributions beyond RGB, while the latter integrates heterogeneous datasets into a unified training framework to jointly model generation and perception tasks. Extensive experiments demonstrate that our unified model surpasses prior unified approaches and performs on par with specialized methods. Furthermore, we demonstrate that multi-task joint training provides complementary benefits: generative priors enrich perceptual details, while perceptual learning improves structural alignment in generation.

---


### 418. [BayesEvolve: Explicit Belief States for Autonomous Scientific Discovery](https://arxiv.org/abs/2606.30335)

**<font color=#1a73e8>作者：</font>** Xuening Wu, Shan Yu, Qianya Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous scientific discovery systems increasingly use large language models (LLMs) to propose new hypotheses, but many such systems condition primarily on experimental memory: archives of high-scoring candidates or heuristic summaries of recent trials. We argue that discovery agents should instead maintain explicit, uncertainty-aware beliefs about hypothesis quality. We introduce BayesEvolve, a belief-guided discovery framework that converts experimental evidence into a predictive belief state and uses this belief to guide future experimentation. As a controlled testbed for belief-guided discovery, we evaluate BayesEvolve on shifted BBOB-style black-box optimization tasks, leaving program and laboratory discovery domains to future work. BayesEvolve improves sample efficiency over memory- and archive-guided LLM baselines under a fixed evaluation budget. We further show that the belief state is predictive on held-out candidate pools, that controlled decision-rule ablations favor belief-guided selection with an annealed uncertainty bonus, and that BayesEvolve exhibits productive late-stage concentration rather than unfocused exploration.

---


### 419. [Sequential Fairness Auditing with Limited Output Access](https://arxiv.org/abs/2606.30338)

**<font color=#1a73e8>作者：</font>** Ioannis Pitsiorlas, Martha V. Sourla, Marios Kountouris  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> External evaluations are becoming increasingly central to the governance of AI systems. In practice, however, independent auditors often have limited access to deployed models and must rely on query-based interactions. Most existing fairness evaluation methods assume static datasets and fixed-sample statistical tests, making them poorly suited to real-world auditing scenarios in which evidence must be collected sequentially under query constraints. In this work, we formulate fairness auditing as a tolerance-aware sequential hypothesis-testing problem under limited model output access. We develop a sequential generalized likelihood-ratio framework that allows auditors to accumulate evidence from a finite audit pool and stop once sufficient support for compliance or violation has been obtained. The framework is instantiated for decision-based Statistical Parity and Equal Opportunity audits, and extended to score- and logit-based proxy audits when richer observables are available. Our results show that both the fairness metric and the level of model access significantly affect audit efficiency, and that the benefits of richer output information are not uniform across auditing settings. In particular, richer outputs can substantially reduce the number of queries required for some fairness metrics and operating regimes, while offering limited gains in near-threshold cases. This work provides a practical statistical framework for sequential fairness auditing under realistic deployment constraints.

---


### 420. [A Classifier-Agnostic Zero-Shot Adversarial Attack Detection via CLIP](https://arxiv.org/abs/2606.30342)

**<font color=#1a73e8>作者：</font>** Hodaya Krakover, Meir Yossef Levi, Eyal Gofer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Adversarial attacks pose a challenge to the reliability of deep learning models, motivating effective detection methods. Existing techniques often rely on attack-specific assumptions, access to adversarial samples, or knowledge of the underlying classifier (white-box). We propose \textit{$A^4D$ (\textbf{A}ttack- and \textbf{A}rchitecture-\textbf{A}gnostic \textbf{A}dversarial \textbf{D}etector)}, a completely black-box, zero-shot adversarial attack detection framework that utilizes prompt-based similarity scores derived from CLIP. To the best of our knowledge this is the first attempt to utilize CLIP for such a task. The method is based on two key observations: (i) CLIP is sensitive even to small imperceptible non-semantic perturbations; (ii) The shift in CLIP embedding space is not arbitrary and can be used as a robust attack indicator. Experiments across multiple attacks, datasets and classifiers validate that $A^4D$ achieves SOTA detection results in the attack-agnostic and classifier-agnostic setting.

---


### 421. [Early Cue Precision Shapes Visual Shortcut Learning in Controlled Cue-Manipulation Benchmarks](https://arxiv.org/abs/2606.30344)

**<font color=#1a73e8>作者：</font>** Chanho Park, Woochan Lee, Janyeong Oh 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual classifiers can achieve high matched-distribution accuracy while relying on low-level cues that fail under conflict or suppression. We test whether this failure is shaped by early cue precision: the reliability with which a low-level cue predicts the label during early learning or downstream probe fitting. Across synthetic shape-texture tasks, sequential digit training, a 10-class frozen-representation audit, and a CIFAR-10 natural-image-based texture-overlay benchmark, we manipulate object-texture match probability and evaluate matched-ID accuracy, conflict accuracy, texture-choice rate, and suppression behavior. Degraded-but-predictive input does not substitute for cue decorrelation. In 10-class digit probes, conflict accuracy drops from 0.589 under chance-like cue precision to 0.005 under target-perfect texture. In CIFAR-10 frozen probes, conflict accuracy drops from 0.569 to 0.114, while texture choice rises from 0.049 to 0.855; this ordering persists across texture-overlay strengths alpha in {0.15,0.25,0.35,0.50}. End-to-end CIFAR-10 training shows that low early cue precision improves pre-target conflict behavior, but shortcut-rich fine-tuning can rapidly overwrite this benefit. Cue decorrelation must therefore be maintained during downstream adaptation rather than treated as a one-time inoculation.

---


### 422. [DRIFT: Difficulty Routing Self-DIstillation with Rhythm-Gated Exploration and Success BuFfer Training](https://arxiv.org/abs/2606.30345)

**<font color=#1a73e8>作者：</font>** Haisen Luo, Yiwei Liu, Haoning Wang 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Enabling large language models to achieve stable self-improvement without external expert supervision remains a central challenge in complex reasoning tasks. Existing self-distillation and reinforcement learning methods lack explicit mechanisms for tracking problem-level learning progress and adapting optimization strategies accordingly. Consequently, training may over-optimize easy problems, receive weak supervision from hard problems, and fail to sufficiently explore borderline cases. To resolve these issues, we propose DRIFT, an online self-evolution policy optimization framework for large language models. DRIFT regulates the model's self-improvement process through the joint use of Difficulty Routing and Rhythm Gating. The former identifies the model's learning state at the problem level and dynamically allocates self-distillation and reinforcement learning signals, while the latter refines policy updates at the token level, concentrating exploration on critical reasoning positions. By further incorporating a success buffer and a two-stage curriculum learning strategy, DRIFT preserves high-quality historical experience while progressively guiding the model from reliable behavior acquisition toward stable policy evolution. Evaluated across five benchmarks and three model scales, DRIFT surpasses the peak performance of both GRPO and SDPO across all evaluated metrics. On the average score over the five benchmarks, DRIFT achieves 79.5$\%$, outperforming GRPO by 9.5$\%$ and SDPO by 7.5$\%$, establishing a new state-of-the-art result. Notably, on ToolUse, DRIFT reaches an accuracy of 79.2$\%$, improving over GRPO by 13.5$\%$ and SDPO by 10.7$\%$, setting a new state-of-the-art and substantially outperforming all concurrent methods.

---


### 423. [FFAvatar: Feed-Forward 4D Head Avatar Reconstruction from Sparse Portrait Images](https://arxiv.org/abs/2606.30347)

**<font color=#1a73e8>作者：</font>** Jianjiang Yao, Ke Xian, Renxiang Dai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present FFAvatar, a Transformer-based 3D Gaussian framework for fast construction of high-quality and animatable 4D head avatars from one or more reference portrait images. Unlike existing feed-forward approaches that require a fixed number of input views, FFAvatar supports incremental reconstruction, progressively refining the avatar representation as additional reference images become available. At the core of our method is an alternating attention mechanism that disentangles identity appearance from expression and viewpoint variations, enabling the reconstruction of a canonical 3D appearance that remains consistent across poses and facial expressions. To balance visual fidelity and computational efficiency, we introduce a sparse-to-dense learning paradigm. Coarse appearance features are first learned using sparse primitives anchored to the FLAME vertex level and are subsequently densified in the UV domain to capture fine-grained geometric and texture details. We further propose a plug-and-play motion refinement module that enables subject-specific dynamic personalization by modeling residual motion beyond parametric deformation. Extensive experiments demonstrate that FFAvatar efficiently produces high-fidelity and controllable 4D head avatars, achieving superior flexibility, driving efficiency, and identity-consistent rendering across diverse expressions and viewpoints.

---


### 424. [FastPano3D: Feed-Forward Indoor Panoramic 3D Reconstruction from a Single Image](https://arxiv.org/abs/2606.30352)

**<font color=#1a73e8>作者：</font>** Jianqiang Li, Liumei Zhang, Wenjia Guo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in 3D scene reconstruction have highlighted the intricate trade-offs among rendering quality, inference efficiency, and data dependency. To address the challenge of rapidly reconstructing detailed 3D indoor scenes from minimal input, we introduce FastPano3D, an end-to-end framework that directly generates renderable 3D Gaussian representations from a single panoramic image. Unlike perspective-based methods, panoramic images inherently suffer from equirectangular projection distortions and spatially non-uniform feature distributions, making direct feed-forward Gaussian generation particularly challenging. In contrast to existing Gaussian Splatting based methods that rely on multi-view supervision or per-scene optimization, FastPano3D employs a lightweight feature encoder, adaptive Gaussian sampling, and a point-cloud-guided refinement strategy to achieve efficient and accurate scene generation without any test-time optimization. Our approach reconstructs high-fidelity 3D scenes within seconds, achieving up to 156 times faster inference than prior state-of-the-art methods such as Pano2Room, while using only half the parameters. Extensive experiments demonstrate that FastPano3D delivers rendering quality comparable to NeRF- and 3DGS-based reconstructions, establishing a new benchmark for rapid, single-view 3D scene inference.

---


### 425. [OLIVE: View-Augmented Latent Prediction with Waveform Reconstruction for Speech SSL](https://arxiv.org/abs/2606.30356)

**<font color=#1a73e8>作者：</font>** Karl El Hajal, Mathew Magimai.-Doss  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We propose Online Latent prediction with Invariant Views and rEconstruction (OLIVE), a self-supervised speech representation learning framework that jointly optimizes analysis and synthesis objectives. OLIVE combines view-augmented masked latent prediction with waveform reconstruction under a unified objective. Reconstruction constrains early encoder features to retain signal-level information, while masked latent prediction shapes later contextual representations toward invariance for robust downstream performance. We show that these objectives enable representations that support a broad range of tasks. In particular, OLIVE improves results on generation and speaker tasks, maintains competitive performance on recognition and semantic tasks, and improves waveform reconstruction.

---


### 426. [On the Vulnerability of Parameter-Level Defenses to Model Merging](https://arxiv.org/abs/2606.30360)

**<font color=#1a73e8>作者：</font>** Kuangpu Guo, Qingyan Zheng, Jian Liang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The training-free integration of expert models via model merging has exposed significant security risks, enabling free-riders to combine specialized models without authorization. Recent works propose parameter-level defenses that employ linear parameter transformations to neutralize this threat. In this paper, we systematically analyze such defenses and reveal that their protected task vectors are inherently small in magnitude. Consequently, the protected weights remain overwhelmingly dominated by the pretrained model. Based on this observation, we designate the pretrained model as a static reference anchor and propose the Anchor-Guided Attack (AGA) to circumvent existing safeguards. Specifically, AGA aligns the protected model with this anchor to recover the transformation matrix analytically. Extensive evaluations validate that AGA consistently bypasses both individual and composite defenses under realistic defense-agnostic scenarios. Furthermore, we provide Anchor-Repulsive Fine-tuning (ARF), a defense method to mitigate the anchor dominance leveraged by AGA. Empirical results confirm that ARF effectively defeats the proposed attack. Our code is available at this https URL.

---


### 427. [CouCE: A Unified Causal Framework for Debiased Deep Metric Learning](https://arxiv.org/abs/2606.30365)

**<font color=#1a73e8>作者：</font>** Xin Yuan, Zhenyang Niu, Meiqi Wan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep Metric Learning (DML) often struggles with zero-shot generalization because standard objectives inherently capture what co-occurs rather than what causes similarity. Consequently, DML models are vulnerable to shortcut learning driven by two structurally distinct confounders: background spurious correlations (which create backdoor paths via scene context) and foreground nuisance perturbations (which inject non-semantic variations like pose or illumination). Although existing methods have proposed targeted solutions for each pathway individually, none can simultaneously address both due to their fundamentally distinct causal roles. To bridge this gap, we propose the Counterfactual Causal Embedding (CouCE), a unified causal framework that explicitly models and neutralizes both confounders. Specifically, we introduce Orthogonal Dictionary-Based Backdoor Adjustment (ODBA), which isolates spurious background patterns into a variance-gated dictionary and stably disentangles them from the learned embeddings via soft orthogonal regularization. Simultaneously, we propose Multi-Scale Randomized Causal Intervention (MSRCI) to enforce causal invariance against foreground nuisances through multi-scale Fourier amplitude randomization and a symmetric KL invariance constraint. Notably, CouCE seamlessly integrates with any proxy-based loss, incurring modest training overhead without requiring architectural modifications during inference. Extensive experiments on CUB-200-2011, Cars-196, and Stanford Online Products demonstrate that CouCE consistently achieves state-of-the-art performance, providing a principled and robust solution for debiased DML.

---


### 428. [MUSE: Unlocking Timestep as Native Task Steering for One-Step Dense Prediction](https://arxiv.org/abs/2606.30370)

**<font color=#1a73e8>作者：</font>** Shuo Zhou, Zhaoxin Li, Xiujuan Chai  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Monocular dense prediction has recently seen remarkable success by repurposing pre-trained diffusion models. This opens a promising yet challenging avenue for more efficient multi-task learning paradigm. However, existing multi-task diffusion methods often introduce parameter-heavy adapters, experts, or learnable task tokens, leading to computational redundancy. In this paper, we reveal an inherent mechanism within one-step diffusion models: the native, fixed sinusoidal timestep embedding can be repurposed as an endogenous task steering signal. Based on this discovery, we propose Multi-task Unified eStimation via timestep Embedding (MUSE), a parameter-free, single-model multi-tasking approach for dense prediction. We interpret this mechanism via Manifold Decoupling, where discrete, fixed timestep values deterministically steer the generation process towards decoupled, task-specific manifolds in the latent space. Extensive experiments across 10 datasets demonstrate that MUSE achieves highly competitive performance on both monocular depth and normal estimation, and its efficacy generalizes across U-Net and DiT architectures. Our work offers a concise and efficient path toward generalist vision models by simply unlocking the latent potential of existing generation infrastructure.

---


### 429. [Your Space is My Zone: Demystifying the Security Risks of AI-Powered Applications on Pre-Trained Model Hubs](https://arxiv.org/abs/2606.30373)

**<font color=#1a73e8>作者：</font>** Yacong Gu, Lingyun Ying, Zidong Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI-powered Applications (AI-Apps), hosted on platforms such as Hugging Face, are democratizing access to pre-trained models through online inference and fine-tuning services. While lowering AI adoption barriers, these platforms introduce an unexplored attack surface, as AI-Apps are often developed by untrusted parties with weak isolation and misconfigured security settings. In this paper, we present the first systematic security analysis of AI-Apps across three leading platforms. To structure our investigation, we map the AI-App lifecycle to established risk taxonomies (e.g., OWASP), identifying five threat categories and ten attack vectors ranging from generic web flaws to high-impact architectural issues. Our analysis reveals critical failures including broken access control, insecure resource reuse, insufficient input validation, and sensitive data exposure. Notably, we uncover three novel architectural vulnerabilities inherent to platform design and demonstrate how traditional issues (e.g., world-readable logs) are uniquely amplified in this ecosystem. To assess real-world impact, we develop an analysis framework Insightor and apply it to over 970,000 public AI-Apps. Alarmingly, we find thousands of apps leaking credentials, hundreds containing input injection vulnerabilities that allow arbitrary code execution, and tens harboring embedded backdoors -- indicating active exploitation. We have responsibly disclosed all findings to the affected platforms and developers.

---


### 430. [Set-Inclusive Uncertainty Modeling for Robust Brain Tumor Segmentation](https://arxiv.org/abs/2606.30374)

**<font color=#1a73e8>作者：</font>** Seunghun Baek, Jihwan Park, Jaeyoon Sim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal MRI is essential for accurate brain tumor segmentation. However, acquiring all modalities at inference is often challenging in practice, which causes intrinsic uncertainty due to unavoidable information loss. Without modeling this uncertainty, existing methods encode incomplete evidence into deterministic representations that appear plausible but lack reliability. In this regime, we propose a probabilistic representation framework that models representations as Gaussian distributions, where their mean captures task information and their variance measures uncertainty from missing evidence. To make variance reflect information deficiency, we regularize the mean from each partial configuration toward its full-modality counterpart, while scaling the variance with the discrepancy between their aligned means. We further introduce a set-inclusive strategy that exploits the hierarchical structure of modality subsets and enforces an ordering constraint to maintain their consistent uncertainty relationships. Extensive experiments on BraTS 2018 and 2020 demonstrate that our approach offers superior performance over baselines across diverse missing-modality scenarios. Code and model checkpoint are available at this https URL.

---


### 431. [FlowAWR: Online Adaptive Flow Reinforcement via Advantage-Weighted Rectification](https://arxiv.org/abs/2606.30376)

**<font color=#1a73e8>作者：</font>** Zheming Fu, Ruizhe He, Wei Shang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Aligning generative flow models on continuous spaces via online reinforcement learning is constrained by intractable trajectory likelihoods. Existing density-approximated policy gradient methods rely on stochastic SDE samplers to construct tractable transition kernels, which introduce training-inference inconsistencies and necessitates Classifier-Free Guidance (CFG).
While implicit frameworks such as DiffusionNFT directly optimize forward-process velocity fields, its heuristic fixed-magnitude corrections prevent optimization strength from relative intra-group quality.
We propose \textit{Flow Advantage-Weighted Rectification} (\textbf{FlowAWR}), a paradigm that recasts continuous generative policy optimization as supervised regression toward a theoretically optimal velocity field.
Starting from the optimal policy of a KL-constrained reward maximization, FlowAWR derives the optimal velocity field that admits a magnitude-aware, advantage-weighted rectification form, yielding SDE-free optimization and CFG-free generation.
In comparative evaluations on SD3.5-Medium, FlowAWR achieves improved alignment performance alongside a 2$\times$ to 5$\times$ convergence acceleration over DiffusionNFT (e.g., reaching a 24.12 PickScore in 1.2k steps, versus 23.82 in 2.0k steps for DiffusionNFT and 23.50 in $>$4k steps for FlowGRPO). Under multi-reward constraints, FlowAWR sustains generation quality, satisfying structural rules while maintaining stable out-of-domain performance.

---


### 432. [Scalar Representations of Neural Network Training Dynamics](https://arxiv.org/abs/2606.30384)

**<font color=#1a73e8>作者：</font>** Pedro Jiménez-González, Miguel C. Soriano, Lucas Lacasa  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training in artificial neural networks can be viewed as a trajectory evolving through a high-dimensional loss landscape. However, the large number of trainable parameters makes the direct analysis of these dynamics challenging. In this work, we treat such training trajectories as temporal networks and apply recently proposed strategies for the scalar embedding of temporal networks. We investigate whether such a scalar embedding provides a meaningful low-dimensional representation of neural network training dynamics. Using a multilayer perceptron trained on the MNIST classification task, we show that the embedding preserves the main dynamical features observed in the original parameter space, including the emergence of sensitivity to initial conditions for specific learning rate regimes and an accurate reconstruction of the network's maximum Lyapunov exponent. We then use the embedded scalar trajectory to define a characteristic time, analogous to a Lyapunov time, after which the exponential separation between initially close embedded trajectories saturates. This characteristic time captures the typical decorrelation time between initially close network trajectories in the original high-dimensional system. Finally, we investigate the statistical organization of asymptotic training states through a spacing observable defined in the embedded space. We find that the distributions of rescaled asymptotic spacings collapse onto a common form across initial conditions and are compatible with a skew lognormal distribution. Altogether, our results suggest that scalar low-dimensional embeddings provide a useful framework for studying and visualizing the dynamical properties of neural network optimization trajectories.

---


### 433. [SADL: What to Ignore? A Benchmark for Subject-Aware Distractor Localization](https://arxiv.org/abs/2606.30393)

**<font color=#1a73e8>作者：</font>** Cao-Tri Nguyen, Nguyen-Khoa Luong, Vinh-Tiep Nguyen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Photographs frequently contain \emph{visual distractors} besides foregrounds and backgrounds of the intended subject, competing for attention and weakening composition. While modern editing tools streamline object removal, identifying which objects to remove remains a mostly manual process. Existing saliency models and open-vocabulary detectors operate without subject awareness, failing to adapt to shifting user intent. Furthermore, context-agnostic removal may disrupt the scene's semantic coherence (e.g., keep the person but remove the chair they are sitting on). To address these limitations, we formalize the task of subject-aware distractor localization, which identifies distractors while retaining compositionally essential objects. This paper introduces \textsc{SADL}, the first real-world benchmark for this task, comprising 1,800 subject-aware cases across 1,000 photographs to enable systematic evaluation and facilitate future research. In total, there are 14,617 annotated candidates, including a robust set of 1,938 hard negatives to stress-test exclusion calibration. We evaluate seven proprietary and open-weight Vision-Language Models (VLMs) on a sequential pipeline of distractor classification followed by exclusion filtering, structured around five inclusion factors and three contextual exclusion rules. Our analysis reveals that VLMs are highly capable of identifying distractors, but then over-apply exclusion, which systematically suppresses true distractors at scale. By exposing this critical bottleneck, \textsc{SADL} provides a foundational diagnostic tool to advance subject-conditioned reasoning in multimodal systems.

---


### 434. [ENC-ODE: Event-level Neurodegenerative Modeling in Continuous Time with Neural ODEs](https://arxiv.org/abs/2606.30398)

**<font color=#1a73e8>作者：</font>** Yujee Song, Seunghun Baek, Guorong Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Accurately predicting the temporal evolution of clinical biomarkers is crucial for the early diagnosis and management of neurodegenerative diseases such as Alzheimer's disease. However, this relies on longitudinal data to capture biomarker changes over time, which is often sparse and irregular due to the high cost, labor-intensive nature, and patient burden. To address these challenges, we propose ENC-ODE, an Event-level Neurodegenerative modeling in Continuous time with neural Ordinary Differential Equations. ENC-ODE predicts future biomarker evolution by modeling clinical events through diagnosis-conditioned continuous dynamics. A target-conditioned attention mechanism weights and aggregates event-level predictions for the target time and modality without history compression. Extensive experiments on Alzheimer's Disease Neuroimaging Initiative (ADNI) dataset demonstrate that ENC-ODE outperforms representative sequence models while offering a scalable and neuroscientifically grounded solution for clinical support. The code is available at this https URL.

---


### 435. [SA-Homo: Scale Adaptive Homography Estimation for Scale Variation Scenarios](https://arxiv.org/abs/2606.30408)

**<font color=#1a73e8>作者：</font>** Shangxuan Xie, Haifeng Wu, Yuhang Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Homography estimation, as one of the fundamental problems in computer vision, remains challenged by scale variation scenarios where image pairs potentially exhibit significant scale discrepancies. Existing deep learning frameworks frequently suffer from a significant performance degradation in such cases, as they rely on limited displacement assumptions and local feature consistency that might not hold under large scale gaps. In this paper, we propose SA-Homo, a novel scale-adaptive homography estimation framework designed to achieve robust alignment across a wide range of scale discrepancy ratios. We adopt a hierarchical scale alignment strategy that transitions from the global perspective with a heavy module to a local perspective with a light module. Specifically, we introduce the Scale-aware Discrepancy Bridging Module (SDBM) for initial alignment, which utilizes a Multi-scale Linear Attention Cascade (MLAC) to capture long-range dependencies and mitigate feature inconsistencies, along with a global Cross-scale Similarity Matrix Block (CSMB) for scale robust correlation representation. Once the initial scale gap is bridged, a lightweight Iterative Homography Estimation Refinement Module (IHERM) progressively polishes the result using local correlations. To facilitate this research, we contribute the HMSA dataset, a high-resolution, multi-modal satellite benchmark specifically tailored for scale-variant challenges. Extensive experiments demonstrate that SA-Homo maintains high precision even under 8$\times$ scale discrepancies, outperforming state-of-the-art methods in both conventional scale-similar scenarios and challenging scale variation scenarios. Code and collected datasets are available at this https URL

---


### 436. [Beyond Point Estimates for Glaucoma Visual Field Forecasting with Diffusion Models](https://arxiv.org/abs/2606.30417)

**<font color=#1a73e8>作者：</font>** Marta Colmenar Herrera, Pablo Márquez Neila, Şerife Seda Kucur Ergünay 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Forecasting visual fields (VFs) is critical for personalized monitoring and treatment planning in glaucoma. This is inherently uncertain due to heterogeneous disease progression and measurement variability, yet most existing methods produce single deterministic predictions that fail to represent this uncertainty. We formulate VF forecasting as a probabilistic prediction problem and the use of conditioned denoising diffusion models to generate distributions of plausible future VFs from longitudinal observations with irregular follow-up intervals. Experiments on two independent VF cohorts show that diffusion-based predictions produce well-calibrated distributions for clinically relevant VF measures. When reduced to a standard point-estimate, the proposed approach achieves state-of-the-art accuracy compared to clinical baselines and prior learning-based methods. Our results highlight the advantages of distributional modeling for VF forecasting and support a shift from point-estimate prediction toward uncertainty-aware, clinically interpretable risk assessment in glaucoma.

---


### 437. [Proofs of Ownership for Machine Learning Models](https://arxiv.org/abs/2606.30423)

**<font color=#1a73e8>作者：</font>** Ran Canetti, Shafi Goldwasser, Or Zamir  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> With the increasing adoption of Machine Learning, protecting model ownership has become an essential challenge. We initiate a formal study of Proof of Ownership for machine learning models: under what conditions can one prove that a stolen model originated from a particular creator? We model proofs of ownership as a game among three parties: a model owner, a thief, and a judge. The owner transforms the original model into a slightly perturbed model together with a proof of ownership. The thief then obtains the transformed model and attempts to minimally modify it so that it remains useful but escapes detection as owned by the model owner. Finally, the judge receives a model and a proof of ownership, and must decide whether the given model is a modified version of some model created by the model owner, or else the given model was developed independently.
Our main result is a dichotomy for classifiers in the black-box setting: Under standard cryptographic assumptions, ownership of models for some concept class can be proven in the above sense {\em if and only if} the concept class is not self-correctable, in a sense close to that of Blum, Luby and Rubinfeld, STOC'90. The result is constructive and extends, with some variations, to a number of related settings.

---


### 438. [CAN We Trust Your Results? A Cross-Dataset Study of Automotive IDS Evaluation](https://arxiv.org/abs/2606.30430)

**<font color=#1a73e8>作者：</font>** Beatrix Koltai, Gergely Acs, Andras Gazdag  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The increasing connectivity of modern vehicles has made securing in-vehicle communication networks a critical challenge. Intrusion Detection Systems (IDS) have been widely studied as a defense mechanism for detecting malicious activities on the Controller Area Network (CAN) bus. However, the evaluation of CAN IDS methods remains difficult due to inconsistencies in experimental setups and the lack of standardized benchmarking frameworks. As a result, reported performance often depends on dataset-specific characteristics and may not reflect how detection methods behave in different environments. This work introduces a benchmarking framework for consistent evaluation of CAN IDSs across multiple datasets. Using the proposed framework, we integrate seven publicly available CAN IDS datasets collected under different experimental conditions and perform cross-dataset evaluation of five conceptually different IDS approaches. Our results highlight how detection performance can vary significantly across datasets, demonstrating the importance of cross-dataset benchmarking for assessing the robustness and generalization capabilities of CAN IDS methods.

---


### 439. [Robust and Efficient Monocular 3D Gaussian SLAM for Kilometer-Scale Outdoor Scenes](https://arxiv.org/abs/2606.30436)

**<font color=#1a73e8>作者：</font>** Sicheng Yu, Dongxu Shen, Beizhen Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scaling monocular 3D Gaussian Splatting (3DGS) SLAM to kilometer-level outdoor environments poses two tightly coupled challenges: fragile long-term pose tracking and excessive memory overhead during large-scale mapping. In this paper, we propose KiloGS-SLAM, a highly efficient and robust monocular 3DGS-SLAM system that jointly addresses both bottlenecks. Since high-fidelity scene reconstruction fundamentally relies on drift-free camera poses, we first introduce a motion-adaptive hybrid tracking module. This module features a condition-triggered three-tier solving pipeline. It dynamically switches between Essential matrix and PnP models to handle geometric degeneracies. An on-demand foundation model can also be activated to rescue the trajectory from catastrophic drift. To ensure the system can sustain these long trajectories without memory exhaustion, we subsequently design a lifecycle-managed Gaussian mapping strategy. By integrating probabilistic initialization with chunk-based multi-view densification and pruning, this full-pipeline optimization effectively reduces primitive redundancy while preserving high-frequency details. Together, the robust tracking guarantees the geometric foundation required for accurate mapping, while the memory-efficient lifecycle-managed mapping enables large-scale operation. Extensive experiments across three challenging outdoor datasets demonstrate that our approach achieves state-of-the-art tracking accuracy and rendering quality, successfully scaling to sequences of over 10,000 frames on a single GPU.

---


### 440. [Transformer Architectures as Complete Bayes Processes: A Formal Proof in the Measure-Theoretic Kernel Framework](https://arxiv.org/abs/2606.30440)

**<font color=#1a73e8>作者：</font>** Haobo Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present a complete formal proof that transformer architectures, when their internal update mechanisms satisfy a Bayes joint-distribution condition, implement exact Bayesian posterior inference. Working within the measure-theoretic kernel framework, we define a hierarchy of abstractions -- from the core Bayesian transformer, through semantic transformers with explicit update kernels, to full transformer blocks with QKV/attention/residual/MLP pipelines, and finally multilayer stacks -- and prove at each level that the Bayes joint semantics implies the update kernel equals the posterior almost everywhere. For the block-level architecture, we derive the explicit Bayes formula through Radon-Nikodym differentiation and prove its normalization. We additionally prove that the softmax attention mechanism induces a valid probability distribution over keys, establishing the bridge between the abstract kernel framework and concrete attention implementations. The framework makes no architectural assumptions beyond the Markov kernel structure and exposes explicit conditions under which a transformer block is provably Bayesian. In essence, when this joint distribution condition is satisfied, the forward computation of a Transformer is formally equivalent to a rigorous Bayesian posterior update.

---


### 441. [The FIL Hypothesis: Inductive Biases Help with Kernel Engineering](https://arxiv.org/abs/2606.30442)

**<font color=#1a73e8>作者：</font>** Nikolai Rozanov, Subhabrata Dutta, Preslav Nakov 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The Bitter Lesson, which posits that general-purpose methods that scale with computation and data ultimately outperform those with built-in human knowledge, has become a dominant paradigm in the era of Large Language Models. We revisit this principle by observing a new and critical scaling dimension: the duration of the Feedback Information Loop (FIL), the time required for a system to receive a verification signal after generating a prediction. Most historic successes in Artificial Intelligence (AI) have benefited from near instantaneous feedback (e.g., games or classification tasks), but we argue that future AI applications in science and the physical world will inherently involve FILs ranging from hours to weeks. This trend poses a fundamental scaling limit, as obtaining enough verification steps required by purely data-driven methods becomes practically impossible. Additionally, we propose a method that is orthogonal to purely data-driven approaches, based on human-inspired expert knowledge. The method relies on inductive biases and constraining the solution space. We provide an initial validation of the hypothesis and the method, by studying the real-world GPU programming task, a domain with non-trivial FIL, and demonstrate that incorporating inductive biases yields superior performance over data-driven approaches. The code is released under: this https URL

---


### 442. [Exploring Differences Between Tabular Enterprise Data and Public Benchmarks](https://arxiv.org/abs/2606.30452)

**<font color=#1a73e8>作者：</font>** Myung Jun Kim, Maximilian Schambach, Frank Essenberger 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular data dominate the landscape of data science, increasingly attracting innovative machine learning models and tailored benchmarks. Yet, little is known for enterprise data, where tables constitute the backbone of business operations. To broaden the benchmarking landscape for business applications, this work aims to actualize the characteristics of enterprise data by providing an analysis of data statistics and performance measurements of tabular models such as TabPFN, TabICL and ConTextTab. Through our analysis, we find enterprise data markedly differ from tabular benchmarks and we demonstrate that a tabular model that performs well on typical tabular benchmarks may perform poorly on real world enterprise data -- and vice versa. This lack of generalization underlines the need for additional benchmarks with enterprise-grade characteristics.

---


### 443. [Curvature-Weighted Gradient Diversity: A Noise Measure for Geometry-Adaptive SGD Schedules](https://arxiv.org/abs/2606.30455)

**<font color=#1a73e8>作者：</font>** Muhammad Hamza, Ayush Goel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The standard convergence analysis of mini-batch stochastic gradient descent (SGD) models gradient noise using a single variance term that treats all parameter directions equally, ignoring the fact that noise in high-curvature directions has less impact because learning rates are already constrained there. We introduce Curvature-Weighted Gradient Diversity (CWGD), a geometry-aware measure that weights per-sample gradient diversity by the inverse square root of the Hessian, providing a tighter proxy for the effective optimization noise. For strongly convex quadratic objectives with diagonal Hessians and isotropic noise, we prove that a CWGD-modulated cosine learning-rate schedule can reduce the asymptotic optimization error floor by up to a factor of two compared with standard cosine annealing. We implement this idea as CWGD-Cosine using a Hutchinson-based diagonal Hessian estimator that is exact for quadratic objectives. Across a range of condition numbers, batch sizes, and noise structures, CWGD-Cosine consistently achieves approximately 20% lower final optimization error than standard cosine annealing while incurring negligible overhead in the quadratic setting. We also identify and correct a degenerate curvature estimator, analyze the robustness of the proposed estimator, and explicitly discuss the limitations of the method, including Hessian staleness in non-convex optimization. These results establish CWGD as a principled geometry-aware measure of optimization noise and motivate future extensions to more general learning problems.

---


### 444. [Cross-Resolution Semantic Transfer for Robust Text-to-Image Retrieval in Low-Resolution Surveillance](https://arxiv.org/abs/2606.30458)

**<font color=#1a73e8>作者：</font>** Wenjie Qian, Bin Yang, Xiao Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image person re-identification (TIPR) retrieves target persons using natural language descriptions. However, existing methods largely overlook resolution variance in real-world surveillance. They characterize cross-resolution TIPR through two coupled failure modes: Evidence Reliability Collapse (ERC), where degraded visual tokens become unreliable for grounding fine-grained text, and Ranking Distribution Drift (RDD), where mixed-resolution galleries distort similarity neighborhoods and destabilize retrieval rankings. To address this challenge, we propose Cross-Resolution Semantic Transfer (CRST), a CLIP-style framework with three modules: resolution-conditioned reasoning, text-guided refinement and CR-RDA. Resolution-conditioned reasoning estimates token reliability to suppress corrupted evidence. Text-guided refinement injects semantic priors to recover discriminative cues. CR-RDA transfers HR neighborhood geometry to stabilize LR ranking under mixed resolutions. Experiments on CUHK-PEDES, ICFG-PEDES, and RSTPReid show that CRST improves ultra-low-resolution Rank-1 and mAP on average by 5.7% and 5.3%, while stabilizing mixed-resolution retrieval without sacrificing high-resolution this http URL code will be made publicly available.

---


### 445. [HSAP: A Hierachical Sequence-aware Parallelism for Hybrid-Context Generative Models](https://arxiv.org/abs/2606.30460)

**<font color=#1a73e8>作者：</font>** Songxin Zhang, Zejian Xie, Zhuoyang Song 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper, we aim to combine the advantages of existing sequence parallelism paradigms and overcomes their drawbacks, the most serious of which is the incapability to correctly compute causal attention on the hybrid-context packed sequences, in a stronger sequence parallelism framework. The practical technique of packing sequences for efficiently pretraining and fine-tuning large language models causes cross-contamination problem in attention computation, which can be effectively solved when no parallelism in the sequence length dimension is taken. However, in sequence parallelism, existing approaches either ignore the scenario of hybrid-context sequences or conversely sacrifice and limit parallelism degree for supporting the scenario. To this end, we innovatively propose an efficient Sequence-Aware Parallelism algorithm to conquer the obstacles of intensive tensor transmission and partial attention computation across multiple device groups. Our algorithm utilizes JIT (Just-In-Time) compilation to optimize the communication strategy of all device groups in NCCL level. Further, we integrate existing sequence parallelism paradigms into a Hierachical Sequence-Aware Parallelism framework which benefits from our sequence-aware algorithm. We additionally elaborate on the memory and communication overhead management of the hierachical framework to optimize its performance. Through multiple experiments, we demonstrate that our proposed approach outperform other state-of-the-arts sequence parallelism approches in multiple metrics.

---


### 446. [MuonSSM: Orthogonalizing State Space Models for Sequence Modeling](https://arxiv.org/abs/2606.30461)

**<font color=#1a73e8>作者：</font>** Thai-Khanh Nguyen, Ngoc-Bich-Uyen Vo, Thieu N. Vo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> State space models (SSMs) have emerged as efficient linear-time alternatives to attention for long-sequence modeling. However, existing SSMs often suffer from instability and memory degradation over extended horizons due to poorly conditioned first-order updates and unbalanced update geometry. We introduce MuonSSM, a general framework that stabilizes SSM training by explicitly conditioning the geometry of memory updates rather than the recurrent transition matrix. MuonSSM augments SSMs with a momentum-based pathway and a lightweight Newton Schulz transformation on low-rank input injections, yielding bounded and spectrally conditioned updates while preserving parallel scan complexity. Theory shows that MuonSSM improves gradient propagation, mitigates spectral amplification, and enriches memory representations over long horizons. Extensive experiments across language, vision, and time-series benchmarks show consistent gains in accuracy, robustness, and long-context performance when integrated into diverse SSM backbones. These results establish geometric conditioning of updates as a principled pathway to stable, scalable sequence modeling.

---


### 447. [FR-DETR: Frequency and Recurrent Feature Refinement for Robust Object Detection under Adverse Weather](https://arxiv.org/abs/2606.30471)

**<font color=#1a73e8>作者：</font>** Tuan-Duc Nguyen, Duc-Trong Le  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Object detection under adverse weather remains challenging due to severe visual degradations and domain shifts. Existing enhancer-based approaches attempt to improve detection by cascading an enhancer with a detector, but they introduce redundant feature extraction and incur high computational cost with limited accuracy gains when paired with SOTA detectors. We propose FR-DETR, a detector-centric framework that refines features rather than images, focusing enhancement on regions of interest and leveraging frequency-domain cues. Specifically, we design (I) a Frequency Refinement Module that dynamically separates and reweights low- and high-frequency components to improve foreground-background discrimination, and (II) a Recurrent Focus Refinement Module (RFRM) that iteratively refines features using coarse predictions as guidance. Extensive experiments demonstrate that FR-DETR achieves superior detection accuracy under adverse weather while being significantly more computationally efficient than enhancer-based methods. Our implementation is available at this https URL.

---


### 448. [PS-MOT: Cultivating Instance Awareness from Point Seeds for Multi-Object Tracking](https://arxiv.org/abs/2606.30476)

**<font color=#1a73e8>作者：</font>** Kai Luo, Fei Teng, Mengfei Duan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce Point-supervised Multi-Object Tracking (PS-MOT) as a cost-effective alternative to traditional bounding box supervision, shifting the focus from spatial fitting to topological center-driven representation. However, PS-MOT faces challenges, e.g., spatial ambiguity and identity drift due to the lack of explicit geometric structure and scale constraints. To address these, we propose PS-Track, a hierarchical pipeline transitioning from points to instances across data, model, and loss levels. At the data level, we introduce Temporal-Feedback Prompting (TFP) to evolve points into temporally consistent pseudo-labels using negative spatial cues and motion priors. At the model level, we design the Point-Excited Wavelet Attention (PEWA) module, which leverages semantic correlations to activate high-frequency components, ``hallucinating'' object boundaries. At the loss level, Uncertainty-Guided Gaussian Learning (UGL) models pseudo-labels as probabilistic distributions, dynamically calibrating supervision intensity. Experiments on DanceTrack, EmboTrack, SportsMOT, and JRDB demonstrate that PS-Track provides a feasible and effective point-supervised alternative across diverse tracking scenarios, establishing a new state-of-the-art for point-supervised tracking. The source code is available at this https URL.

---


### 449. [PGE-SAM: Prompt-Guided Feature Enhancement for Interactive Segmentation under Degradation](https://arxiv.org/abs/2606.30477)

**<font color=#1a73e8>作者：</font>** Tuan-Duc Nguyen, Anh-Tuan Mai, Duc-Trong Le  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Segment Anything Model (SAM) has revolutionized promptable image segmentation with strong zero-shot generalization. However, its performance degrades substantially under real-world imaging artifacts such as noise, blur, and compression. Existing methods restore features globally without focusing on segmentation-relevant regions and neglect SAM's iterative refinement mechanism, leading to suboptimal performance in interactive settings. We propose Prompt-Guided Feature Enhancement SAM (PGE-SAM), a framework that explicitly leverages user prompts and prior mask predictions to spatially guide the feature restoration process toward regions of interest through a Prompt Guidance Generator. To recover fine-grained details lost under degradation, we introduce Multi-Scale Features Interaction to incorporate low-level encoder features, along with a Foreground Reconstruction Loss that restricts feature-level supervision to the segmentation target. Furthermore, we present DM-Seg, a benchmark for interactive segmentation on degraded medical images, spanning multiple imaging modalities with both general and modality-specific degradations at varying severity levels. Extensive experiments demonstrate that PGE-SAM achieves SOTA robustness on both medical and natural image domains across multiple degradation levels, while maintaining generalization to clean images and adding less than one-fifth of the parameters of prior methods.

---


### 450. [SIMAX: A Scalable and Interpretable Framework for Multi-Fidelity and Annotated Clinician-Patient Dialogue Simulation](https://arxiv.org/abs/2606.30491)

**<font color=#1a73e8>作者：</font>** Zhuhan Bao, Rui Yang, Bohao Yang 等 19 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Background. The widespread deployment of ambient digital scribes is driving large-scale capture of clinician-patient dialogues. Human coding of clinical communication data remains costly, inconsistent, and difficult to scale, motivating AI-driven communication coding systems. However, evaluating these systems requires real-world dialogues and human-coded labels, both hard to obtain at scale.
Methods. We developed SIMAX (Scalable and Interpretable Framework for Multi-Fidelity and Annotated Clinician-Patient Dialogue Simulation), a framework for generating controlled clinical dialogue data with reference behavioral annotations. SIMAX generates clinician-patient dialogues from predefined clinical scenarios, personas and voice conditions, and target communication behaviors. Behaviors are controlled using two codebooks: the Global Codebook for overall communication quality and the WISER Codebook for specific countable behaviors. We evaluated SIMAX using automated and human quality assessments and an example communication coding system.
Results. SIMAX generated 3,388 simulated dialogues across three specialties, multiple visit stages, persona characteristics, and accent conditions. Automated assessment showed mean UTMOS and WV-MOS scores of 3.03 and 2.61, WER and CER of 0.07 and 0.05, and CLAP cosine similarity of 0.41, suggesting reasonable speech naturalness, high transcription fidelity, and positive text-audio correspondence. Human evaluation showed a median MOS of 4.67 and a median clinical realism score of 3.00. Downstream evaluation suggests that SIMAX can assess how a communication coding system responds to behavioral targets and reveal insufficient sensitivity in some dimensions.
Conclusions. SIMAX generates controlled and reproducible simulated clinician-patient dialogues, providing a data foundation for developing, validating, and refining communication coding systems.

---


> [!TIP]
> 当前位于：**401-450**（第 9/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-450** | [451-489](./part-10.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
