# 📦 其他研究 | 2026年06月04日

> 本类共 **312** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-312](./part-07.md)

---

### 101. [FGRPO: Federated GRPO with Adaptive Aggregation on Non-IID Data](https://arxiv.org/abs/2606.03094)

**<font color=#1a73e8>作者：</font>** Pengyu Chen, Shaowei Li, Kai Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent advances in language models have established reinforcement learning as the primary paradigm for eliciting self-correction and long-chain reasoning. While group relative policy optimization (GRPO) offers superior scalability by eliminating the critic network, deploying it on a central infrastructure entails collecting a large volume of data from distributed owners, which poses significant privacy risks. To address these concerns, we introduce federated GRPO (FGRPO), a framework designed to decentralize the fine-tuning of reasoning models across heterogeneous data owners. To effectively mitigate the instability caused by divergent reward scales across heterogeneous tasks, FGRPO incorporates an adaptive aggregation mechanism based on relative performance gain. By characterizing each client's improvement relative to its personalized historical baseline, the framework dynamically prioritizes effective learning trajectories regardless of local task difficulty. FGRPO ensures robust convergence on non-IID data while preserving data privacy.

---


### 102. [AI Assistance for Discretionary Work: Increasing Feedback Provision in Higher Education](https://arxiv.org/abs/2606.03095)

**<font color=#1a73e8>作者：</font>** Romina Mahinpei, Victoria Dean, Ruth Fong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI systems increasingly shape human workflows by generating intermediate artifacts that users can adopt, revise, or ignore. While prior work has shown that AI assistance can improve the efficiency and accuracy of required tasks, less is known about whether it can increase participation in discretionary but beneficial work that users often intend to perform but frequently skip. We study this question in the context of personalized feedback provision in higher education, a pedagogically valuable but often optional practice. We conduct a mixed-methods study combining a randomized field experiment and qualitative interviews in a 300-level machine learning course with n=11 teaching assistants (TAs) and n=88 students. Student submissions were randomly assigned to either (1) a treatment condition where TAs received AI-assisted feedback drafts after grading or (2) a control condition without drafts. TAs remained fully in control and could use, edit, or ignore drafts at their discretion. We find that AI-assisted feedback significantly increases feedback provision (+10.8 percentage points, SE=1.1, p<0.001) and feedback length (+39.8 chars, SE=3.45, p<0.001) without negatively affecting student usefulness ratings or reducing time per character. Qualitative findings suggest that AI-assisted drafts function as editable scaffolds that lower barriers to initiating feedback rather than reducing overall effort. Our findings highlight AI's promise for discretionary but beneficial tasks: increasing work that might otherwise go undone while preserving human control over final outcomes.

---


### 103. [From Long News to Accurate Forecast: Importance-Aware Fusion and PRM-Guided Reflection for Time Series Forecasting](https://arxiv.org/abs/2606.03097)

**<font color=#1a73e8>作者：</font>** Mingyang Liu, Qingcan Kang, Yuke Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Incorporating news into time series forecasting is appealing because news can reveal abrupt exogenous events that historical values alone cannot recover. However, existing LLM-based news-forecasting pipelines face two practical limitations: relevant news articles often exceed the model's context window, and iterative retrieval of supplementary news is typically unguided, leading to redundant updates and slow convergence. We address these issues with a novel framework that combines importance-aware news compression and process-level retrieval supervision. First, we train an importance reward model that estimates the forecasting utility of each article and uses this signal to allocate compression budgets during sequential pairwise fusion, preserving informative content within a fixed context limit. Second, we introduce a process reward model (PRM) that ranks multiple supplementary-news candidates conditioned on the current error profile and the history of previously selected articles, replacing one-shot blind retrieval with quality-controlled selection. Both components are trained offline using historical data with ground truth; inference uses the frozen filtering logic and compression modules without any reflection loop. Experiments on finance, energy, traffic, and bitcoin forecasting benchmarks show that our method improves prediction accuracy over strong baselines, significantly reduces the number of refinement iterations compared to the iterative baseline, and remains effective when relevant articles span thousands of tokens.

---


### 104. [Zero-Shot 3D Question Answering via Hierarchical View-to-Token Transportation](https://arxiv.org/abs/2606.03100)

**<font color=#1a73e8>作者：</font>** Dongsheng Wang, Dawei Su, Hui Huang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recently, zero-shot 3D scene understanding via 2D Vision-Language Models (VLMs) has gained increasing research interest due to their promising spatial reasoning capabilities. Typically, multiple 2D views are sampled from a 3D point cloud and fed into pre-trained VLMs to answer a given question. This paradigm highlights the critical role of input context quality and raises the challenge of retaining as many task-relevant 3D details as possible under a limited input budget. We propose \texttt{KeyVT}, a hierarchical approach for input context collection at both the view and token levels. Specifically, we combine pixel features with camera parameters and assess view importance based on both semantic content and geometric position, resulting in spatially consistent and task-relevant views. Furthermore, we address redundancy among patches across selected views by identifying representative tokens under the optimal transport (OT) framework, where view tokens and key tokens are formulated as two discrete distributions in the embedding space. These key tokens are expected to cover all view features by minimizing the OT distance. We evaluate our framework on three widely used benchmarks, demonstrating significant improvements over existing tuning-free methods and performance comparable to training-based approaches.

---


### 105. [DeskCraft: Benchmarking Desktop Agents on Professional Workflows and Human-in-the-Loop Collaboration](https://arxiv.org/abs/2606.03103)

**<font color=#1a73e8>作者：</font>** Wenkai Wang, Tao Xiong, Jingchen Ni 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Real-world professional desktop workflows in specialized creative and engineering software unfold over long horizons and often require human-in-the-loop coordination, where agents proactively seek necessary information and users provide additional instructions, clarifications, feedback, or corrections as the task progresses. Yet existing desktop GUI benchmarks mostly reduce this setting to short, simplified tasks with all user instructions provided upfront. To address this issue, we introduce DeskCraft, a desktop GUI benchmark targeting long horizon creative and engineering workflows and proactive human-agent collaboration. DeskCraft organizes tasks into a multilevel difficulty taxonomy, with long horizon tasks requiring over 50 execution steps, and covers professional creative software across design, video, audio, and 3D creation. Furthermore, DeskCraft formalizes human-agent collaboration into an interaction protocol covering mid-turn and post-turn exchanges. Mid-turn interaction captures both agent-initiated clarification under uncertainty and user-initiated interruption during execution, while post-turn interaction accommodates user-driven feedback after the agent signals completion, together spanning the full space of realistic collaboration patterns. We evaluate 18 proprietary and open source agents on 538 tasks and find that GPT-5.4 reaches 31.6% on standard tasks and 27.6% on interactive tasks. Further analyses reveal persistent failures in long horizon workflow delivery and proactive clarification. We will open-source all evaluation codes, tasks, and data at this https URL.

---


### 106. [Inverting the Generation Process of Denoising Diffusion Implicit Models: Empirical Evaluation and a Novel Method](https://arxiv.org/abs/2606.03111)

**<font color=#1a73e8>作者：</font>** Yan Zeng, Masanori Suganuma, Takayuki Okatani  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper studies the problem of inverting the DDIM image generation process to recover latent variables, particularly the initial noise map, from a generated image. Existing methods often struggle with accuracy in this task. We propose a novel hybrid approach that combines direct inversion via gradient descent for the first step, followed by a fixed-point method for subsequent steps. Empirical evaluations across three datasets demonstrate that our method significantly improves the prediction of initial latent variables while achieving superior reconstruction accuracy. Additionally, we introduce a new evaluation, called the self-interpolation test, which assesses the quality of images generated from interpolated points between the true and predicted latent maps, offering deeper insights into performance. Our results reveal that while existing methods perform reasonably well in reconstruction, they consistently fail to accurately predict the initial latent variables, resulting in poor performance on the self-interpolation test. In contrast, our method outperforms all others across all metrics, providing valuable insights into diffusion models and enhancing their applications in image generation and editing.

---


### 107. [Learning to See via Epiretinal Implant Stimulation in silico with Model-Based Deep Reinforcement Learning](https://arxiv.org/abs/2606.03118)

**<font color=#1a73e8>作者：</font>** Jacob Lavoie, Marwan Besrour, William Lemaire 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Objective: Diseases such as age-related macular degeneration and retinitis pigmentosa cause the degradation of the photoreceptor layer. One approach to restore vision is to electrically stimulate the surviving retinal ganglion cells with a microelectrode array such as epiretinal implants. Epiretinal implants are known to generate visible anisotropic shapes elongated along the axon fascicles of neighboring retinal ganglion cells. Recent work has demonstrated that to obtain isotropic pixel-like shapes, it is possible to map axon fascicles and avoid stimulating them by inactivating electrodes or lowering stimulation current levels. Avoiding axon fascicle stimulation aims to remove brushstroke-like shapes in favor of a more reduced set of pixel-like shapes. Approach: In this study, we propose the use of isotropic and anisotropic shapes to render intelligible images on the retina of a virtual patient in a reinforcement learning environment named rlretina. The environment formalizes the task as using brushstrokes in a stroke-based rendering task. Main Results: We train a deep reinforcement learning agent that learns to assemble isotropic and anisotropic shapes to form an image. We investigate which error-based or perception-based metrics is adequate to reward the agent. The agent is trained in a model-based data generation fashion using the psychophysically validated axon map model to render images as perceived by different virtual patients. We show that the agent can generate more intelligible images compared to the naive method in different virtual patients. Significance: This work shares a new way to address epiretinal stimulation that constitutes a first step towards improving visual acuity in artificially-restored vision using anisotropic phosphenes.

---


### 108. [GuidedBridge: Training-freely Improving Bridge Models with Prior Guidance](https://arxiv.org/abs/2606.03119)

**<font color=#1a73e8>作者：</font>** Zehua Chen, Yucheng Yang, Binjie Yuan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Guidance methods, such as classifier-free guidance (CFG) and auto-guidance (AG), have advanced noise-to-data generation in diffusion models. Recently, bridge models have introduced a data-to-data generative process that can exploit an instructive clean prior. In this work, inspired by previous methods creating quality difference between denoising results as guidance, we propose a training-free bridge guidance method, termed Prior Guidance (PG). Specifically, we introduce a weak prior, which is unseen during bridge pre-training, hindering prior exploitation and thereby degrading denoising result. Then, we contrast it with the seen prior to highlight and enhance prior exploitation via a scaling factor. Moreover, we analyze the underlying mechanism of prior exploitation in the bridge process and design frequency-modulated prior guidance (FMPG), which tailors the guidance scale to low- and high-frequency bands coherent with bridge generative dynamics. To address prior exploitation in image in-painting, we develop a cascaded framework, CFG-FMPG, which first generates a noisy hidden representation via CFG and then exploits it as a generative prior with FMPG, fulfilling their complementary strengths without compromising inference efficiency. Experiments demonstrate that our PG methods consistently improve pre-trained bridge models across diverse image translation tasks.

---


### 109. [KC-3DGS: Kurtosis-Constrained Gaussian Splatting for High-Fidelity View Synthesis](https://arxiv.org/abs/2606.03120)

**<font color=#1a73e8>作者：</font>** Vivekjyoti Banerjee, Abhay Yadav, Rama Chellappa 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) enables real-time novel view synthesis by representing scenes as collections of anisotropic Gaussians optimized via differentiable rasterization. However, standard pixel-space losses (L1, SSIM) constrain only aggregate reconstruction error, permitting the optimization to redistribute error across frequency scales. This leads to oversmoothing and structural artifacts, particularly in sparse-view settings where supervision is limited. We propose KC-3DGS, which augments 3DGS training with wavelet-domain supervision based on natural image statistics. Our method combines three components: (1) a multi-scale wavelet coefficient alignment loss that explicitly penalizes missing high-frequency detail, (2) a supervised kurtosis concentration loss that encourages rendered images to match the heavy-tailed frequency statistics of ground-truth images, and (3) a cross-band covariance penalty that promotes frequency specialization. We provide theoretical analysis showing that pixel-space losses admit a family of indistinguishable perturbations under wavelet redistribution, and that our joint objective excludes degenerate solutions. Experiments across MipNeRF360, Tanks&Temples, MVImgNet, DeepBlending, and WRIVA-ULTRRA demonstrate consistent improvements in perceptual quality. On the challenging WRIVA-ULTRRA outdoor dataset, KC-3DGS achieves a 9.48% improvement in DreamSim while also improving PSNR, SSIM, and LPIPS. In sparse-view settings with only 12 training images, our method improves PSNR by up to 0.5 dB on MipNeRF360 while maintaining perceptual quality. The approach integrates seamlessly into existing 3DGS pipelines as a plug-and-play regularization strategy.

---


### 110. [TiWeaver: Unified Temporal Dynamics Modeling via Contextual Patching](https://arxiv.org/abs/2606.03121)

**<font color=#1a73e8>作者：</font>** Zhe Li, Jindong Tian, Hao Miao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multivariate time series forecasting plays a critical role in real-world applications, including weather prediction, stock analysis, and health monitoring. Due to the diversity of data sources, time series exhibit diverse temporal dynamics, often accompanied by various irregularities such as missing values and non-uniform sampling frequencies. Such irregularities lead to complex and asynchronous temporal dependencies across channels. Thus, a single model with a fixed patching scheme often fails to adapt well to diverse multivariate time series, hindering accurate forecasting. In this paper, we propose TiWeaver, a unified framework designed to handle temporal dynamics and fine-grained inter-channel dependencies adaptively. Specifically, we introduce a Graph-Guided Adaptive Tokenizer (G$^2$AT) that divides time series into high contextually coherent patches by jointly considering temporal density and representation consistency. In addition, we propose a Fine-grained Asynchronous Dependency Extractor (FADE), which is designed to model fine-grained asynchronous inter-channel dependencies while incorporating long-term historical dependencies. We evaluate TiWeaver on 12 real-world time series datasets, where it achieves state-of-the-art performance, outperforming existing methods up to 25%. These results demonstrate its robustness and effectiveness across diverse domains and data characteristics.

---


### 111. [Rethinking Neural Width for Alternating Current Optimal Power Flow Proxies](https://arxiv.org/abs/2606.03125)

**<font color=#1a73e8>作者：</font>** Dhruvi Khandelwal, Anurag Basistha, Ayushi Jolotia 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning proxies for Alternating Current Optimal Power Flow (ACOPF) lack systematic methods for determining architectural size. This paper conducts a constructive thought experiment to answer a fundamental inquiry: how wide must a neural network be to almost accurately approximate the ACOPF manifold? We introduce a Loss-Guided Neural Densification (LG-ND) algorithm that incrementally discovers necessary capacity by expanding only when the current deep neural network topology fails to improve further. Empirical results across various IEEE systems show that LG-ND achieves performance parity with literature baselines using up to ten times fewer neurons per layer. Such architectural minimalism is critical for the formal verification required in safety-critical grid operations.

---


### 112. [Think-Before-Speak: From Internal Evaluation to Public Expression in Multi-Agent Social Simulation](https://arxiv.org/abs/2606.03137)

**<font color=#1a73e8>作者：</font>** Kaiqi Yang, Tai-Quan Peng, Sanguk Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based multi-agent simulation offers a promising way to study social interaction, deliberation, and collective opinion dynamics. However, many existing dialogue simulation frameworks represent interaction mainly as observable turn exchange or aggregated outputs, leaving the internal evaluative processes behind silence, speaking intention, and public expression difficult to examine. We introduce TBS (Think-Before-Speak), an interval-based multi-agent simulation framework that separates agents' private reasoning from public utterance generation. At each interval, all agents update structured internal states based on the shared dialogue history and their own memory. These states include dissonance-related appraisal, perceived opinion climate, perceived isolation risk, response strategy, and willingness to speak. The orchestrator then resolves competing speaking intentions and commits one utterance to the public dialogue, allowing internal evaluation and public interaction to co-evolve over time.
We evaluate TBS in simulated town hall discussions on a climate-related policy issue. Results show that TBS produces coherent internal-state traces and that these traces vary systematically across turn-allocation, silence, and memory conditions. Dissonance-related appraisal increases agents' willingness to speak, whereas silence-pressure appraisal decreases it. Once speaking intention is formed, public expression is shaped mainly by turn-allocation rules. These findings suggest that TBS supports mechanism-sensitive social simulation by making the pathway from internal evaluation to public expression observable and analyzable.

---


### 113. [$A^2$: Smaller Self-Supervised ViTs Localize Better than Larger Ones](https://arxiv.org/abs/2606.03148)

**<font color=#1a73e8>作者：</font>** Sreehari Rammohan, Huy Ha, Carl Vondrick  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robust visual classification often depends on localizing the main foreground objects in an image while ignoring contextual distractors. Surprisingly, we find that the attention maps of smaller self-supervised ViTs localize foreground objects better than those of larger ViTs. However, we still need large ViTs, because they extract richer representations from each patch. To get the best of both worlds, good localization and rich representations, we propose $A^2$, a simple method that leverages this inverse scaling finding by decoupling where to look (a small attention model) from what to extract (a large embedding model): we crop around the attention peaks of a small model and embed the crops with a larger model. $A^2$ uses entirely pretrained features, requires no group labels, and does not require per-dataset attention or backbone training. Across 5 benchmarks, $A^2$ is competitive with backbone-matched loss-level methods like DFR, and outperforms end-to-end attention training under stronger distribution shifts.

---


### 114. [A cross-domain tropical species dataset with Chinese vernacular names and CITES source links](https://arxiv.org/abs/2606.03156)

**<font color=#1a73e8>作者：</font>** Jeff Wang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We describe a versioned cross-domain dataset of 410,499 active tropical species (working snapshot 2026-04-20) spanning three applied subdomains -- tropical_plants, tropical_aquatic, and tropical_pets -- that share a commercial and regulatory life cycle but are distributed across kingdom-organised biodiversity infrastructures. The resource joins taxonomic identifiers from GBIF, Plants of the World Online, iNaturalist, NCBI Taxonomy, the Catalogue of Life and the Encyclopedia of Life, and adds three original layers: a cross-domain ontology that re-segments taxa along trade and husbandry contexts; a Chinese vernacular layer with explicit per-name provenance under a typology that excludes unverified machine-generated proposals; and a CITES source-linkage layer connecting each taxon to its Species+ entry. Chinese vernacular coverage -- the proportion of taxa carrying a CJK Chinese name distinct from the scientific binomial -- reaches 99.50 percent (408,456 of 410,499; full-population count). Coverage characterises completeness, not name-translation accuracy; the latter is bounded by the four-level provenance typology and is the subject of a preliminary internal review reported here, with a blind external audit identified as the principal open item. Upstream content is referenced by stable identifier only for the original-contribution layers, supporting CC-BY 4.0 reuse. The dataset is deposited on Zenodo (https://doi.org/10.5281/zenodo.20377811). This preprint is the canonical v1.0 description of the dataset's current state; future Data Descriptor submission is anticipated but is contingent on the validation and release-engineering items listed in the Limitations.

---


### 115. [SRENet: Spectral Re-Entry Network for Point Cloud Action Recognition](https://arxiv.org/abs/2606.03160)

**<font color=#1a73e8>作者：</font>** Qiuxia Wu, Jiarui Lan, Wenxiong Kang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recognizing human actions from point cloud sequences is critical for 3D perception driven applications such as autonomous driving and human-computer interaction. However, the irregular structure and temporal inconsistency of point clouds pose unique challenges for spatio-temporal representation learning, especially in capturing both global motion context and fine-grained temporal dynamics. We propose SRENet, a spectral-aware framework designed to explicitly learn both global context and fine-grained temporal dynamics of motion from a frequency perspective for action recognition. SRENet introduces a Spectral Decomposition Block (SDeBlock) that performs wavelet-based analysis along temporal and spatial axes, disentangling features into low- and high-frequency components with frequency-specific attention. To recover residual dynamics and re-align temporal frequency structures distorted during semantic fusion, a Spectral Re-entry Block (SReBlock) performs secondary temporal decomposition. Furthermore, a spectral-aware learning strategy is devised to enhance discriminability in both frequency subspaces via contrastive loss and a curriculum schedule that gradually shifts focus from low- to high-frequency spaces in line with coarse to detailed motion patterns. Extensive experiments on MSR-Action3D, NTU-RGBD and NTU-RGBD120 demonstrate that SRENet achieves state-of-the-art performance, validating the effectiveness of frequency modeling in point cloud-based action understanding.

---


### 116. [OpenAgenet/OAN: Open Infrastructure for Trusted Agent Interconnection](https://arxiv.org/abs/2606.03161)

**<font color=#1a73e8>作者：</font>** Jinliang Xu  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> OpenAgenet, abbreviated as OAN, is an open infrastructure project for trusted Agent interconnection. It addresses a problem that becomes visible when Agents move from isolated applications into open, multi-operator networks: before an Agent can safely discover, select, and invoke another Agent, it needs a way to verify identity provenance, governance state, discovery authorization, freshness, and pre-connection trust evidence. OAN is designed as a protocol-neutral trust layer. It does not replace Agent interaction protocols, tool protocols, model orchestration frameworks, or application-level workflows. Instead, it provides Root-governed identity admission, Registrar-assisted onboarding, Root-verified package publication, authorization-aware Discovery, and signed trusted invocation. This paper presents the motivation, architecture, roles, governance model, relationship with MCP, A2A, and ANP, deployment patterns, cooperation model, blockchain-backed authorization bulletin, prototype status, performance profile, and roadmap of OAN.

---


### 117. [OpenAgenet/OAN: Technical Architecture for Trust-Governed Agent Identity and Discovery](https://arxiv.org/abs/2606.03163)

**<font color=#1a73e8>作者：</font>** Jinliang Xu  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> This paper describes the technical architecture of OpenAgenet / OAN. OAN is a protocol-neutral trust layer for open Agent interconnection. It specifies the role architecture, identity objects, registration workflow, Root-governed lifecycle, Root-verified package model, authorization-aware Discovery, signed trusted invocation, verification requirements, state transitions, security properties, implementation boundaries, and deployment considerations. The design is intended to support heterogeneous Agent frameworks and interaction protocols, including MCP, A2A, ANP-like systems, and domain-specific Agent protocols. OAN does not define the entire business conversation among Agents; it defines how Agent identities become admissible, discoverable, verifiable, and safe to approach before protocol-specific interaction begins.

---


### 118. [Pulse Focus: Validation of the Focus Performance Score as a Behavioral Signal for Human Attentional State Modeling Toward Attention-Aware AI](https://arxiv.org/abs/2606.03164)

**<font color=#1a73e8>作者：</font>** Yisak Debele, Israel Goytom, Anwar Misbah  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence systems that model and support human cognition require reliable measures of cognitive state. We present the Focus Performance Score (FPS) from the Pulse Focus mobile Stroop application and evaluate whether it measures attentional control during color-word conflict resolution. We conduct behavioral, neural, and formula validation analyses. Behavioral results (N=466, 111,133 trials) show that FPS captures the Stroop interference effect, tracks individual differences in attentional control, and demonstrates strong test-retest reliability. Neural validation using the DMCC55B fMRI dataset (N=55) shows that the primary FPS component, mean incongruent reaction time, is significantly associated with anterior cingulate cortex activation, a key neural substrate of conflict monitoring. Formula validation identifies and resolves structural redundancy within the scoring framework and provides convergent support for the weighting design. Together, these findings establish FPS as a behaviorally valid, reliable, and neurally grounded measure of attentional control. FPS provides a defensible behavioral signal for evaluating human attentional state and supports future work on attention-aware human-AI interaction and physiological state modeling.

---


### 119. [Ask When It Pays: Cost-Aware Open-Ended Interaction for Instance Goal Navigation](https://arxiv.org/abs/2606.03175)

**<font color=#1a73e8>作者：</font>** Xunyi Zhao, Sihao Lin, Gengze Zhou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Instance Goal Navigation (IGN) requires an embodied agent to find a specific object instance among distractors from an underspecified natural-language description. Such ambiguity often cannot be resolved from perception and language alone, making interaction with an oracle a natural mechanism for disambiguation. Prior interactive methods allow oracle queries but treat lightweight clarification and route-level guidance alike, letting agents boost success rate through repeated high-information questions rather than by resolving the underlying ambiguity efficiently. We recast interactive IGN as a cost-sensitive uncertainty-reduction problem, where the agent should ask the question whose answer provides the largest reduction in navigation uncertainty relative to its penalty. To this end, we apply an information-gain analysis on existing navigation corpora to identify which cues reduce navigation uncertainty, yielding a compact set of question types and data-derived this http URL, existing interactive navigation benchmarks do not model the cost of different question types or evaluate how efficiently agents use interaction, making them unsuitable for studying cost-sensitive interaction. Based on this taxonomy, we construct a benchmark for diagnosing interaction behavior and efficiency, together with a Weighted Success Rate metric that penalizes each query by its derived cost. We further propose a zero-shot MLLM navigator that selectively queries at each decision step only when the expected uncertainty reduction justifies the interaction cost.

---


### 120. [SenseJudge: Human-Centric Preference-Driven Judgment Framework](https://arxiv.org/abs/2606.03189)

**<font color=#1a73e8>作者：</font>** Rui Li, Junfeng Liu, Xiangwen Kong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) as judges across various scenarios such as assessing model responses is becoming an increasingly accepted paradigm. However, existing judgment approaches often rely on trained judgers using fixed preference data, which tend to overlook diverse user preferences and struggle to adapt to real-world human-AI dialogue scenarios. To address these limitations, we propose SenseJudge, a customizable judgment framework driven by human preferences and SenseBench, a diverse and challenging instruction-following benchmark derived from real-world multi-turn interactions. We applied the automatic judgment framework and benchmark to two tasks: (1) LLMs as personalized judges, and (2) model ranking. We conducted extensive experiments, and the results demonstrate that the SenseJudge framework surpasses other judgment methods and models in the LLMs-as-personalized-judges task and achieves model ranking that aligns with real human sense. Additionally, we conducted analyses on position bias and consistency, alongside ablation studies, which affirmed the robustness of SenseJudge.

---


### 121. [Focused on the User, Overlooking the Risks: Security and Privacy Understandings, Practices and Challenges of Independent Chinese AI Agent Developers](https://arxiv.org/abs/2606.03190)

**<font color=#1a73e8>作者：</font>** Shuning Zhang, Mingyao Xu, Zhixin Huang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The proliferation of AI agents empowers independent developers, defined as individual or small groups who self-initiate projects rather than fulfill client-based contracts, to create sophisticated autonomous systems, but also introduces novel security and privacy (S&P) challenges beyond traditional corporate structures. We conducted an interview study (N=28) with Chinese developers, whose extensive use of global LLM services offer valuable insights into this population. We investigate their understandings, practices and challenges of S&P challenges in their developed AI agent products. We revealed that independent developers frequently think and act from their users' perspective. They focused on user-facing safety risks such as harmful content while exhibiting low awareness of security vulnerabilities. Consequently, developers rely almost exclusively on ad-hoc, manually crafted safeguards and informal communication, with an absence of formal tools or processes for S&P practices. We found these actions are driven by various inhibitors, primarily a lack of formal training on S&P related skills, accessible security tools and actionable guidance from platforms. Our work contributed the first exploration of independent AI agent developers' S&P understanding, outlining opportunities for tailored security tooling.

---


### 122. [Private Embedding Lookup with Encrypted Compact Queries under Fully Homomorphic Encryption](https://arxiv.org/abs/2606.03191)

**<font color=#1a73e8>作者：</font>** Daehyun Jang, Jaehee Kang, Hanee Rhee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Many NLP or recommendation models begin by mapping discrete client inputs to embedding vectors. Since inputs can reveal sensitive information, the embedding step must be protected in privacy-preserving inference. Fully Homomorphic Encryption (FHE) enables inference over encrypted client data, but turns embedding lookup from simple table access into homomorphic computation. To keep the embedding table server-side and avoid transmitting encrypted embedding vectors from the client, we focus on server-side lookup: the client sends only a small encrypted index.
Prior ICML 2024 work first builds a one-hot vector from the encrypted index before multiplying with the embedding table, and this one-hot generation is the dominant cost. One-hot-based methods are expensive in FHE: they construct a p-dimensional selection vector via an equality test for each coordinate, requiring $O(p \log p)$ total homomorphic operations.
Our key observation is that private embedding lookup only requires a linearly independent representation of the encrypted index, not the one-hot basis itself. Building on it, we propose Independent Vector Evaluation (IVE). Instead of constructing a one-hot vector, IVE evaluates a linearly independent vector built from successive powers of a single encrypted value, reducing vector-generation cost to $O(p)$. It then recovers the same embedding vector via a precomputed change of basis, instantiated with an orthogonal Discrete Cosine Transform to mitigate error amplification.
Our implementation shows IVE improves amortized lookup time by up to 78.4x over prior method. We further evaluate its impact on end-to-end encrypted FastText inference, where embedding lookup is a major cost in the shallow model. On Enron-Spam dataset, replacing one-hot generation with IVE reduces the share of vector generation in encrypted inference time from 99.6% to 66.3%.

---


### 123. [Fast Organic Crystal Structure Prediction with Unit Cell Flow Matching](https://arxiv.org/abs/2606.03199)

**<font color=#1a73e8>作者：</font>** Alston Lo, Luka Mucko, Austin H. Cheng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Organic crystal structure prediction (CSP) is a requirement for computational modelling of organic solids, but traditionally costs several CPU-years per molecule. Generative models such as OXtal dramatically reduce this cost by sampling stable organic crystal structures directly. However, OXtal forgoes explicit lattice parametrization in favour of modelling large crops of the bulk material with expensive triangle layers, which can incur a computational cost of minutes per molecule. In this paper, we reduce this to seconds with Clari, a large-scale flow matching model that generates redundancy-free unit cells and replaces triangle layers with pure pair-bias attention. Clari requires only atom types and bonds as input and does not need an RDKit-sanitizable input molecule, which expands its applicability to challenging chemistries such as fullerenes, metal complexes, and atom clusters. We further ablate key design choices such as auxiliary losses, timestep distributions, noise priors, and self-conditioning. On OXtal's test sets, we surpass OXtal's solve rate while obtaining a speedup of $15$-$30\times$. Because Clari also models explicit hydrogens, it supports inference-time scaling via direct energy ranking, without any decoration or relaxation step. When generating 150 crystals and selecting the top-30 by energy, we further improve solve rate while maintaining a speedup of $5$-$8\times$. We also introduce the CSD Teaching Subset as a new test split of diverse and complex molecules for future benchmarking. Our contributions enable CSP within seconds, making large-scale virtual screening of organic solids practical. Code is available at this https URL.

---


### 124. [Reinforcement Learning from Cross-domain Videos with Video Prediction Model](https://arxiv.org/abs/2606.03201)

**<font color=#1a73e8>作者：</font>** Zhao Yang, Xinrui Zu, Jacob E. Kooi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning from expert videos across visually distinct domains is challenging due to the absence of reward signals and the presence of domain gaps. We introduce XIPER (Cross-domain Video Prediction Reward), a reward model for learning from expert videos collected in a visually different domain, where the agent's appearance differs due to factors such as color, morphology, or the sim-to-real gap. More specifically, XIPER trains a cross-domain video prediction model that maps agent observations into the expert domain and uses the prediction likelihood as a reward signal. Experiments on the DMC Color Suite (8 tasks) and DMC Body Suite (3 tasks) show that XIPER consistently outperforms baselines despite domain gaps such as differences in agent color and morphology. We further analyze XIPER on a sim-to-real transfer dataset, demonstrating that it produces meaningful reward signals for real-robot observations given only simulated expert videos. Code, pretrained models, datasets and video demonstrations can be found on our project webpage: this https URL

---


### 125. [MedCUA-Bench: A Screenshot-Only Benchmark for Clinical Computer-Use Agents](https://arxiv.org/abs/2606.03203)

**<font color=#1a73e8>作者：</font>** Jia Yu, Zilong Wang, Xinyang Jiang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Computer-use agents could automate repetitive screen-based clinical work, but their reliability in medical graphical user interfaces remains largely unvalidated. Existing benchmarks focus on general web or desktop tasks and underrepresent medical software, which requires domain knowledge, exhibits markedly different UI design from mainstream applications, lacks public testing environments, and demands safety validation beyond task completion. We introduce MedCUA-Bench, an interactive benchmark for clinical computer-use agents. It covers 18 clinical scenarios across 10 medical domains, reconstructed from real product manuals and open-source medical systems to capture authentic clinical interfaces while avoiding licensing and privacy constraints. Each task ships with paired intent- and step-level goals to disentangle clinical reasoning from UI execution, and is evaluated by a deterministic checker over task completion and five clinical safety dimensions. Across 23 agents, the best closed-source model reaches 54.2% strict success, while all models remain below 9% on the real OpenEMR. Open-source agents average only 2.5%, with the best reaching 16.2%. MedCUA-Bench exposes the gap between current agents and reliable clinical software use, providing a reproducible testbed for future research.

---


### 126. [Bayesian Tensor Decomposition with Diffusion Model Prior](https://arxiv.org/abs/2606.03212)

**<font color=#1a73e8>作者：</font>** Zerui Tao, Qibin Zhao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-rank tensor decomposition (TD) is usually effective on clean, fully observed data, but it often degrades under severe missingness or noise. Low-rankness is itself a useful but limited structural prior, and additional handcrafted priors (e.g., sparsity or smoothness) still fall short of capturing the rich statistics of real-world data. To compensate for this weak inductive bias under heavy corruption, one would like to inject a learned, data-driven prior; however, the state-of-the-art diffusion models are not readily compatible with current TD and tractable posterior inference. To address these challenges, we introduce DiffBCP, a hybrid-prior Bayesian CP decomposition framework that couples a cumulative shrinkage process prior over the CP factors for automatic rank selection with an off-the-shelf pre-trained diffusion model as an implicit data prior on the reconstructed tensor. To make posterior inference tractable despite the coupling among the likelihood, low-rank constraint, and diffusion prior, we develop a split Gibbs sampler: CP factors admit conjugate updates, while the diffusion block is sampled via low-rank-guided denoising. A noise-adaptive coupling schedule further reduces sensitivity to hand-tuned annealing. Experiments on image inpainting and denoising, including high-resolution out-of-distribution images, show consistent gains over Bayesian, nonlinear, and plug-and-play TD baselines.

---


### 127. [Effect of Demographic Bias on Skin Lesion Classification](https://arxiv.org/abs/2606.03214)

**<font color=#1a73e8>作者：</font>** Ralf Raumanns, Gerard Schouten, Veronika Cheplygina 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In this study, we evaluate the performance of skin lesion classification using ResNet-based convolutional models, focusing on the impact of demographic bias in training data, particularly variations in patient sex and age. We use linear programming to generate datasets with controlled demographic characteristics, allowing systematic investigation of bias effects. Three learning strategies are evaluated: a single-task model, a reinforcing multi-task model, and an adversarial learning scheme. Our sex-based analysis indicates that sex-specific training datasets optimise model performance. Notably, including male patients in the training data improved performance for the male subgroup, even in female-majority cases. Reinforcing and adversarial learning schemes narrowed or eliminated bias gaps in balanced and female-majority datasets. However, these strategies proved less effective in male-majority settings, where models continued to perform better for males than females. The two learning schemes showed marginal bias reduction compared to the baseline model in predominantly male patient populations. Age-based analysis demonstrates comparable baseline performance across the three model approaches, with performance declining across age categories. Younger groups consistently achieve the highest performance, regardless of training data distribution. Although balanced training yields optimal results for the youngest age category, performance decreases in older categories. We find that sex biases arise mainly from data imbalances, while age biases consistently favour younger groups regardless of distribution. These distinct mechanisms require targeted mitigation strategies. Additionally, cross-dataset validation on two external datasets revealed that domain shifts notably affect performance and patterns of demographic bias.

---


### 128. [Generative AI-Enabled Refund Fraud in Chinese E-Commerce: Investigation on Merchants and Platform Workers](https://arxiv.org/abs/2606.03215)

**<font color=#1a73e8>作者：</font>** Shuning Zhang, Eve He, Xiao Zhan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> E-commerce dispute resolution typically relies on the security assumption that digital evidence truthfully reflects physical reality. Generative AI (GenAI) invalidates this threat model, enabling attackers to fabricate hyper-realistic evidence of product defects at negligible cost. Through semi-structured interviews with merchants (N=17) and platform workers (N=13) in the Chinese e-commerce market, we characterize this shift toward GenAI-enabled scalable fabrication. We outline a taxonomy of four GenAI-enabled threat vectors across the transaction, dispute, logistics and communication phases, highlighting how attackers exploit GenAI to synthesize physically plausible product defects at scale. To mitigate these threats, platforms and merchants are adapting verification strategies, relying on AI tools for automated screening and adversarial interrogation (e.g., requesting multi-angle videos) to increase attack complexity. However, we find several challenges that hinder the adoption of these defenses, including implementation hurdles like structural platform constraints and fundamental limitations regarding the technical sophistication of GenAI. We conclude by outlining design implications for privacy-preserving cross-platform fraud databases, and traceability mechanisms such as embedding verifiable material anchors into the product.

---


### 129. [The Role of Domain-Specific Features in Malware Detection: A macOS Case Study](https://arxiv.org/abs/2606.03218)

**<font color=#1a73e8>作者：</font>** Biagio Montaruli, Andrea Oliveri, Savino Dambra 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Despite the growing popularity of macOS among end users and enterprise systems, malware research has primarily focused on Windows and Android operating systems, leaving the problem of macOS malware detection relatively unexplored. Indeed, the specificity of the operating system and the unique characteristics of the Mach-O file format can play a fundamental role in the classification of unknown samples, drastically increasing the detection rate. In this work, for the first time in the literature, we employ new domain-specific features, i.e., static features specific to macOS binaries, such as embedded certificates, entitlements, persistence techniques and key system APIs, to train a machine learning malware detector. We perform a comprehensive experimental evaluation on a novel dataset of 41,129 samples, comprising 11,413 benign and 29,716 malicious executables, and demonstrate that our solution achieves state-of-the-art detection performance (98.50%), outperforming all existing approaches, with an average improvement of 16% in terms of detection rate. We also provide an in-depth analysis of the importance of the individual features, showing that our detector effectively leverages the new domain-specific features. Then, in order to evaluate the generalization capabilities of our detector over time, we perform a real-world evaluation on a new dataset of 9,000 fresh macOS executables. The results show that (i) our detector maintains a very high detection rate (99.50%), (ii) outperforms the state-of-the-art by 50%, and (iii) the domain-specific features are crucial for generalizing to novel malware samples, as their removal leads to a 15.92% drop in detection performance. Finally, we also release our dataset to the research community.

---


### 130. [Sample-Size Scaling of the African Languages NLI Evaluation](https://arxiv.org/abs/2606.03219)

**<font color=#1a73e8>作者：</font>** Anuj Tiwari, Oluwapelumi Ogunremu, Terry Oko-odion 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> African languages have very little labelled data, and it is unclear if augmenting the quantity of annotation data reliably enhances downstream performance. The study is a systematic sample-size scaling study of natural language inference (NLI) on 16 African languages based on the AfriXNLI benchmark. Under controlled conditions, two multilingual transformer models with roughly 0.6B parameters XLM-R Large fine-tuned on XNLI and AfroXLM-R Large are tested on sample sizes of between 50 and 500 labeled examples and average their results across random subsampling runs. As opposed to the usual belief of monotonic increase with increased data, we find a strongly language sensitive and often non-monotonic scaling behavior. Some languages show early saturation or decrease in performance with sample size as well as high variance in low resource regimes. These results indicate that the volume of data is not enough to guarantee stable profits to African NLI, creating the necessity of language sensitive datasets creation and stronger multi-lingual modelling strategies.

---


### 131. [Learning Temporal Causal Structure via Smooth Differentiable Optimization](https://arxiv.org/abs/2606.03227)

**<font color=#1a73e8>作者：</font>** Tong Zhao, Ce Guo, Wayne Luk 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Causal discovery with instantaneous effects in multivariate time series is challenging, as the instantaneous structure must be acyclic. Prior methods enforce this by either separating instantaneous and lagged estimation into multi-stage pipelines or imposing algebraic acyclicity constraints via complex augmented Lagrangian optimization, both of which incur high computational cost. In this work, we propose a different approach: we learn a differentiable permutation of variables using the Gumbel--Sinkhorn operator and triangularize the instantaneous coefficient matrix of a Structural Vector Autoregressive (SVAR) model in the learned order. This converts acyclicity from a hard constraint into a parameterization and keeps it valid throughout optimization. In doing so, our method enables unified, continuous optimization with gradient-based learning, leading to improved efficiency in time--series causal discovery. Across three real-world benchmarks, our method achieves the best overall performance compared with 12 baselines in both discovery accuracy and efficiency. On the large-scale benchmark, it further demonstrates strong scalability, achieving more than a 6x speedup over competing methods.

---


### 132. [GFFMERGE: Efficient Merging of Graph Neural Force Fields and Beyond](https://arxiv.org/abs/2606.03232)

**<font color=#1a73e8>作者：</font>** Parth Verma, Parv P. Singh, Vipul Garg 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Neural Networks (GNNs) have revolutionized Neural Force Fields for atomistic simulations, achieving near-quantum accuracy at reduced cost, yet adapting these models to new chemical systems requires expensive retraining of foundation models. Inspired by model merging in vision and language processing, we introduce GFFMERGE, the first principled framework for closed-form model merging in GNNs. We exploit the linear structure of message-passing layers and formulate merging as a convex embedding-alignment problem with an analytical solution. Through the first systematic benchmarking of model merging for GNNs, we show that existing methods designed for vision and language catastrophically fail on force field regression, while GFFMERGE recovers performance approaching gold standard joint training. Across molecular (MD17, MD22), solid-state (LiPS20), and large-scale graph benchmarks, GFFMERGE and GNNMERGE (its generic GNN counterpart) achieve 5-27$\times$ speedups while enabling modular composition of specialized models. Remarkably, our closed-form solution alone outperforms all baseline methods before fine-tuning and provides superior initialization for faster, data-efficient convergence.

---


### 133. [Solipsistic Superintelligence is Unlikely to be Cooperative](https://arxiv.org/abs/2606.03237)

**<font color=#1a73e8>作者：</font>** Rakshit S Trivedi, Natasha Jaques, Logan Cross 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI's central challenge is shifting from capability to coexistence. The dominant paradigm in AI research focuses on developing powerful agents that treat the world as an exogenous and stationary source of feedback. We contend that superintelligence, an extremely capable task solver, born out of such a solipsistic approach to AI design, is unlikely to be cooperative. Deploying AI systems induces endogenous non-stationarity, resulting in a train-test-deploy gap where historical distributions diverge from the deployment context. We refer to this as the self-undermining property of unilateral optimization. Closing this gap requires AI that participates in cooperation: the equilibrium-selection process through which multiple actors navigate their interdependence. We call for a non-solipsistic research paradigm that treats this interdependence as a core design principle rather than approaching cooperation as a task to solve. This entails building dynamic evaluation testbeds involving adaptive counterparties, treating institutions as design primitives, and preserving human agency as a structural feature of the systems we build.

---


### 134. [ARBOR: Online Process Rewards via a Reusable Rubric Buffer for Search Agents](https://arxiv.org/abs/2606.03239)

**<font color=#1a73e8>作者：</font>** Zheng Liu, Longxiang Zhang, Xintong Wang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM-based search agents are trained predominantly with outcome-only reward, leaving the search process itself unsupervised. This signal degenerates on outcome-homogeneous groups where all sampled trajectories share the same correctness, yielding zero within-group advantage and no gradient. Existing process supervision either trains a costly verifier or generates per-query rubrics that are inconsistent across queries and discarded after one use. We propose ARBOR (Adaptive Rubric Buffer for Online Reward), a reusable process-reward framework that maintains a rubric memory shared across queries. Query-local drafts induced from contrastive trajectories are admitted, consolidated into cross-query common rubrics, and retired as the policy evolves. A small active subset of common rubrics scores trajectories via sparse pairwise judging, and the resulting scores are added to the base reward, providing process-level gradient even when outcome reward is uniform. ARBOR consistently outperforms GRPO and DAPO baselines on four multi-hop QA benchmarks, raising average LLM-judge accuracy by up to 4.2 points and converting up to 42% of otherwise-zero-gradient training groups into informative ones.

---


### 135. [Benchmarking Speech-to-Speech Translation Models](https://arxiv.org/abs/2606.03241)

**<font color=#1a73e8>作者：</font>** Alkis Koudounas, Hayato Futami, Quentin Jodelet 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speech-to-speech translation (S2ST) has advanced rapidly, but offline evaluation lacks a unified protocol: studies report non-overlapping metric subsets, preventing direct comparisons. We introduce COMPASS, a unified and reproducible benchmarking framework integrating 46 metrics across eight dimensions, and deploy it on 1,248 model-language configurations from FLEURS and CVSS, spanning cascaded and end-to-end architectures over ten language pairs. Architectures exhibit complementary strengths: best-vs-worst gaps exceed 30\% on naturalness and speaker preservation but remain within a few points on translation quality, so single-metric rankings systematically misrepresent system quality. Correlation filtering reduces 46 metrics to 10 per direction, with three axes requiring different metrics across X$\to$EN and EN$\to$X (e.g., TER/UTMOS vs. ChrF++/NISQA-MOS); these subsets preserve rankings (Spearman's $\rho>0.80$) while cutting evaluation time by $\approx 2.5\times$. Human validation across dubbing, podcasts, and medical domains shows standalone MOS predictors fail to predict listener preference, while top domain-specific metrics correlate with human judgment ($\rho \geq 0.90$). We release COMPASS as a foundation for domain-aware S2ST evaluation.

---


### 136. [MemoGen: Can Past Experience Improve Future Text-to-Image Generation?](https://arxiv.org/abs/2606.03243)

**<font color=#1a73e8>作者：</font>** Wenshuo Chen, Kuimou Yu, Bowen Tian 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern text-to-image models have achieved strong visual synthesis, yet remain unreliable when prompts require implicit visual constraints, relational reasoning, or external knowledge. Existing retrieval-augmented and agentic generation methods mitigate this issue by acquiring external knowledge, references, or refined prompts for the current request, yet they typically treat each generation as an isolated episode and do not systematically preserve past successes or failures for future use. In this work, we ask whether a text-to-image system can continually improve from its own generation experience without updating the underlying generator. We propose MemoGen, a training-free framework that augments existing image generators with an agentic evolution layer. For each task, MemoGen explicitly infers visual requirements, retrieves external evidence and references when necessary, translates them into executable generation constraints, evaluates the generated result, and stores task understanding, reference choices, visual feedback, successful strategies, and failure lessons as reusable experience memory. Across evolution rounds, the agent retrieves relevant experience to improve similar future generations, selectively repairing previously failed cases while preserving successful ones, thereby enabling test-time self-evolution without parameter updates. Extensive experiments on knowledge-intensive and reasoning-oriented benchmarks demonstrate the effectiveness of this paradigm: after only two evolution rounds, MemoGen built upon the open-source Qwen-Image backbone surpasses strong proprietary systems such as Nano Banana Pro and GPT-Image-1 on WISE and Mind-Bench, showing that explicit experience memory can serve as a powerful continual learning signal for reliable text-to-image generation.

---


### 137. [When Does Complexity Conditioning Help a Frozen Sentence Embedding? A Controlled Study of Per-Sentence and Pair-Level Difficulty Adaptation](https://arxiv.org/abs/2606.03244)

**<font color=#1a73e8>作者：</font>** Suhwan Hwang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A common intuition is that sentence embeddings should adapt to the difficulty of the input. We test this intuition in a controlled, multi-seed setting: a lightweight post-encoder adapter attaches to a frozen Qwen3-Embedding-0.6B encoder, accessing only its final pooled embedding, and is evaluated on four paraphrase and semantic-similarity tasks (PAWS, MRPC, QQP, STS-B). The naive form of the idea fails: surface-based per-sentence complexity is nearly uncorrelated with frozen-baseline error (Pearson approximately 0.05) and provides no advantage over constant or shuffled controls, while degrading a saturated baseline. Even when the target is aligned to a non-circular pair-difficulty signal, the per-sentence gate still cannot reliably capture difficulty because difficulty is primarily a property of the pair, not the individual sentence. In contrast, a small pair-level residual gated by a held-out cross-encoder difficulty signal yields consistent gains on the larger and graded tasks, including +0.022 Spearman on STS-B and +0.037 on QQP, while remaining anchored to the frozen baseline across all seeds. Because this useful form operates on sentence pairs rather than individual sentences, the resulting model is best understood as a lightweight re-ranker over cached frozen embeddings, not a replacement single-vector embedding; we make no state-of-the-art claim. Our contribution is a controlled account of when difficulty-aware adaptation helps and when it fails, together with a pre-training diagnostic that predicts the available headroom.

---


### 138. [MariData: One-Step Unpaired Image Translation for Maritime Environments](https://arxiv.org/abs/2606.03246)

**<font color=#1a73e8>作者：</font>** Santeri Henriksson, Mehdi Asadi, Amin Majd 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The development on robust perception systems for Maritime Autonomous Surface Ships (MASS) is heavily constrained by the scarcity of diverse training data, particularly for adverse weather and low-light conditions. Because collecting paired images in dynamic maritime environments is physically impossible, synthetic data generation via unpaired image-to-image translation offers a critical solution. However, existing generative models suffer from failing to preserve the fine structural details of small navigational objects due to latent compression bottlenecks. In this paper, we introduce a framework for generating synthetic maritime data using CycleGAN-turbo, a one-step unpaired translation architecture. By incorporating zero-convolution skip connections to bypass the Variational Autoencoder (VAE) bottleneck, our approach explicitly preserves small object details (e.g., distant vessels and sea marks) during translation. We compiled a dataset of 7,000 maritime images to train and evaluate models for Day-to-Foggy, Day-to-Sunset, and Day-to-Night domain translations. Qualitative evaluations and variable-strength inference studies demonstrate that our method effectively synthesizes realistic atmospheric conditions while maintaining the underlying semantic structure of the scene. The Day-to-Foggy and Day-to-Sunset models exhibit great structural retention, whereas the Day-to-Night model highlights the challenge of semantic hallucination, such as generating artificial coastal lights, induced by unbalanced training distributions. Ultimately, this work establishes an efficient, structure-aware data synthesis pipeline that directly addresses the data scarcity bottleneck in autonomous maritime navigation.

---


### 139. [Structures Facilitate Retrieve, Rerank, and Generate](https://arxiv.org/abs/2606.03247)

**<font color=#1a73e8>作者：</font>** Yeqin Zhang, Haomin Fu, Xujie Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Document-grounded dialogue systems (DGDS) utilize knowledge from external documents to answer domain-specific user questions. Existing solutions typically divide documents into independent passages for retrieval and response generation. This approach, however, neither makes good use of structural information within documents nor provides enough (document) context for knowledge selection and responses. This paper proposes SF-Re2G to address such issues systematically. Firstly, we seek to improve a passage representation by contrasting it with others of the same section, thus improving the retrieval performance. Secondly, a structure-enhanced reranker is built, leveraging the fact that multiple grounding passages of one dialog turn tend to be in the same neighborhood. Specifically, candidates from the retrieval are grouped into subgraphs according to the document structure. The reranker will rescore the candidate integrating its group information. Finally, the chosen passages are used for responses, taking into account the subgraph context for better generation. Experimental results on two DGDS datasets validate our method for both Chinese and English.

---


### 140. [Do Real-World Datasets Contain Natural Experiments? An Empirical Study Using Causal Feature Selection](https://arxiv.org/abs/2606.03251)

**<font color=#1a73e8>作者：</font>** Gautam Gare, John Galeotti, Michael Mozer 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In nature, events that affect some individuals or groups but not others constitute an implicit intervention and are known as natural experiments. For example, the COVID-19 pandemic was an intervention by the coronavirus on the sub-population infected with COVID. We ask, do natural experiments occur in existing real-world datasets? If yes, how should we treat them? To detect natural experiments in data, we use causal discovery to recover the underlying causal graph and perform feature selection based on causal links. If downstream performance improves by treating the data as interventional rather than observational, we argue that this suggests the dataset contains natural experiments. We first validate this hypothesis by simulating datasets with and without natural experiments using synthetic graphs. We then perform a systematic empirical evaluation on a large suite of real-world datasets. Our results indicate that real-world datasets do contain natural experiments and we can take advantage of those natural experiments to improve model performance using causal inference. Our work represents the initial foray into this area, offering a preliminary exploration within a limited scope.

---


### 141. [FreeStreamGS: Online Feed-forward 3D Gaussian Splatting from Unposed Streaming Inputs](https://arxiv.org/abs/2606.03254)

**<font color=#1a73e8>作者：</font>** Ruiyang Chen, Feiran Li, Chu Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feed-forward 3D Gaussian Splatting (3DGS) allows efficient and high-fidelity novel view synthesis (NVS) from an offline recorded image sequence. However, achieving online NVS from streaming and unposed image inputs remains challenging. Although online feed-forward geometric estimation methods have been proposed for streaming depth and point cloud recovery, they cannot be adapted to NVS due to severe rendering artifacts. This is because NVS demands stricter multi-view consistency in Gaussian scales and pose-geometry alignment; even minor deviations would accumulate over time and visibly degrade rendering quality. To this end, we propose FreeStreamGS, a robust online feed-forward framework for efficient and high-quality NVS. We introduce two key mechanisms: a Decoupled Intrinsic Recovery Head that removes cumulative camera intrinsic bias and prevents scene scale jitter during long-term streaming, and a Dynamic Point Refinement Offset strategy that relaxes rigid unprojection to correct coupled pose-depth drift. Extensive experiments show that FreeStreamGS achieves rendering quality competitive with state-of-the-art offline feed-forward 3DGS methods, despite operating without access to future frames.

---


### 142. [Beyond "To whom it may concern": Tailoring Machine Translation to Audience and Intent](https://arxiv.org/abs/2606.03259)

**<font color=#1a73e8>作者：</font>** Raphael Merx, Ekaterina Vylomova, Trevor Cohn  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Translation quality depends on purpose: the same source text demands different translations depending on audience, tone, and communicative intent. Yet MT models and metrics treat translation as a fixed mapping from source to target. LLMs enable users to explicitly specify purpose alongside source text, yet this capability has not been evaluated at scale. We introduce a systematic evaluation of purpose-driven MT across 50 languages, 5 model sizes and 8 text domains. We find that (1) explicit instructions substantially improve translation adaptedness, with larger gains on informal domains (conversation, social media), for larger model sizes and for higher-resource languages; (2) instructions outperform semantically-matched few-shot examples and paragraph-level context; (3) traditional MT metrics fail to capture adaptation quality, often penalizing adapted translations; (4) when curated instructions are unavailable, models can self-generate them from surrounding document context, closing up to 80% of the adaptedness gap to curated instructions. Our results establish that purpose-adapted MT is a viable and measurable capability of LLMs, while highlighting the need for purpose-aware metrics.

---


### 143. [EqGINO: Equivariant Geometry-Informed Fourier Neural Operators for 3D PDEs](https://arxiv.org/abs/2606.03260)

**<font color=#1a73e8>作者：</font>** Sungwon Kim, Juho Song, Seungmin Shin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning surrogates for 3D Partial Differential Equations (PDEs) often fail to generalize across geometric transformations because they depend heavily on specific coordinate systems. While equivariant networks offer a solution, they typically rely on local operations in the spatial domain, making the global receptive field, which is essential for PDE dynamics, computationally expensive. Conversely, Fourier Neural Operators (FNOs) efficiently capture global interactions, yet establishing 3D equivariance within them remains impractical due to the prohibitive cost of spectral group convolutions. To bridge this gap, we introduce EqGINO, a geometrically robust framework that enforces isotropy in the spectral domain. By design, EqGINO guarantees exact equivariance to the discrete symmetries inherent to the discretized computational domain. Beyond this discrete guarantee, our structural prior enables effective generalization to arbitrary continuous orientations even with a limited number of SE(3)-transformed training samples. Consequently, our method robustly models coordinate-invariant physical laws on complex irregular 3D geometries. Our code is available at this https URL

---


### 144. [Let There Be Light: Reflection, Refraction and Scattering for Neural Operators](https://arxiv.org/abs/2606.03262)

**<font color=#1a73e8>作者：</font>** Keke Wu, Yixuan Zhang, Jingrun Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural operators learn mappings between infinite-dimensional function spaces and provide a data-driven surrogate modeling paradigm for parametric partial differential equations (PDEs). Existing architectures typically obtain expressivity by parameterizing integral kernels in prescribed transform domains or by applying attention-like interactions over discretized spatial points. While these approaches have achieved substantial progress, they often face a persistent trade-off among physical interpretability, nonlocal spatial communication, mesh scalability, and computational cost. We propose a Light-inspired neural operator(LiNO), an operator-learning architecture whose latent evolution is decomposed into three mechanisms motivated by elementary light transport: reflection, refraction, and scattering. Reflection and refraction act as adaptive pointwise transformations in latent feature space, enabling local feature reorientation and anisotropic modulation, whereas scattering performs input-dependent nonlocal propagation over the physical domain. We first formulate scattering as a normalized pairwise kernel with relative positional bias, and then develop an efficient scattering variant that replaces explicit pairwise interactions with positive-feature global propagation and a local diffusion branch, reducing the dominant spatial complexity from quadratic to linear. This yields a structured neural operator that separates local feature modulation from global spatial communication while retaining a modular and interpretable latent evolution.

---


### 145. [ReforMe: Re-Shaping Documents with Contextual Prompting and Layout-Aware Propagation](https://arxiv.org/abs/2606.03266)

**<font color=#1a73e8>作者：</font>** Nabin Khanal, Tongyan Wang, Jui-Cheng Chiu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Digitizing complex documents with handwritten content, irregular tables, and heterogeneous layouts remains challenging, as traditional Optical Character Recognition (OCR) systems fail to capture writing nuances, author-specific conventions, and document structure, and recent LLM-based approaches lack mechanisms for precise, scalable correction. We present an interactive document digitization system that integrates layout-aware parsing, OCR, and LLM-based reconstruction with user-driven refinement. The system is informed by a formative study that identifies key challenges and interaction needs in real-world digitization workflows. It supports both direct edits and natural-language instructions, and introduces a layout-aware propagation mechanism that generalizes user corrections across structurally similar regions. This enables not only efficient error correction but also document re-shaping into structured, analyzable representations. We evaluate the system through a within-subjects user study (n=12) on real-world documents. Results show improved correction efficiency and reduced repetitive effort, demonstrating more effective and controllable document digitization procedure.

---


### 146. [VistaHop: Benchmarking Multi-hop Visual Reasoning for Visual DeepSearch](https://arxiv.org/abs/2606.03273)

**<font color=#1a73e8>作者：</font>** Hang He, Chuhuai Yue, Chengqi Dong 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual DeepSearch requires multimodal large reasoning model (MLRM) agents to answer complex visual queries by repeatedly inspecting image regions, grounding intermediate reasoning in visual evidence, and connecting fine-grained clues across long reasoning chains. However, existing benchmarks mainly focus on single-step visual understanding or static image-question answering, offering limited evaluation of iterative image inspection, visual-anchor grounding, and multi-hop evidence integration. In this work, we introduce VistaHop, a benchmark for evaluating vision-centric search and multi-hop visual reasoning in Visual DeepSearch. VistaHop contains 300 high-resolution images, 25 visual search scenarios, and 350 multi-hop QA tasks that require models to follow evidence chains from visual anchors or fuse information across multiple image-grounded reasoning paths. We further develop VistaArena, a unified evaluation environment that supports tool-augmented reasoning with text search, image search, image cropping, and evidence-based answer validation. Experiments on seven representative MLRMs show that current models remain far from solving VistaHop: the best model, SenseNova-MARS-32B, achieves only 24.31% Pass@1. These results reveal persistent limitations in visual grounding, evidence revisiting, long-chain reasoning, and multi-anchor information fusion, highlighting the need for stronger benchmarks and training methods for Visual DeepSearch.

---


### 147. [A Geometric Lens on Physics-Aligned Data Compression](https://arxiv.org/abs/2606.03279)

**<font color=#1a73e8>作者：</font>** Aleix Segui, Wesley Armour  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In AI for Science, physics-informed losses are increasingly used to train learned compressors for scientific data, but their rate-distortion implications remain poorly understood. At fixed bitrate, these objectives often improve preservation of a target physical observable while degrading standard reconstruction fidelity. We develop a local geometric theory showing that this tradeoff is governed by the interaction of latent-space sensitivities induced by the entropy model, the physical observable, and the distortion metric. At each operating point, these induce preferred directions along which compression noise should be suppressed, yielding an anisotropic error-allocation mechanism. When these directions are misaligned, improving the observable at fixed rate necessarily worsens standard distortion, establishing a fundamental limit on simultaneous preservation. We formalise this through a local tangent-space rate-distortion law and introduce a practical alignment diagnostic based on dominant eigenspace overlap. Experiments across scientific domains test the theory and validate that the alignment diagnostic correlates with observed data- and physics-space trade-offs.

---


### 148. [A Negative Result on Cross-Model Activation Transfer in a Pythia Multi-Hop Setting](https://arxiv.org/abs/2606.03280)

**<font color=#1a73e8>作者：</font>** Peiyan Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent work shows that language models can transmit behavioural traits through hidden signals in generated data during training. We ask whether a more direct and stricter channel is also viable: can one language model communicate useful intermediate reasoning state to another at inference time by translating and injecting hidden activations, rather than by passing natural-language text? We test this question in a controlled Pythia-160M to Pythia-410M multi-hop reasoning setting. A linear translation layer learns a strong normalized-space map between sender and receiver hidden states, with normalized cosine similarity near 0.97 across seeds. However, when the translated activations are injected into the receiver at inference time, they do not improve downstream answering. Low-strength additive injection remains near the no-injection baseline, with confidence intervals that cross zero. Replacement-style injection is consistently destructive, and rescaling translated vectors to the receiver hidden-state norm does not rescue performance. The result is therefore a scoped negative result: in this setting, offline representational alignment is not sufficient for useful causal communication inside the receiver.

---


### 149. [SEA-NLI: Natural Language Inference as a Lens into Southeast Asian Cultural Understanding](https://arxiv.org/abs/2606.03284)

**<font color=#1a73e8>作者：</font>** Peerawat Chomphooyod, Jian Gang Ngui, Yosephine Susanto 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Frontier LLMs perform well in Western contexts, but remain poorly tested on underrepresented cultures such as those in Southeast Asia (SEA). Existing NLI benchmarks are largely Western-centric, translation-derived, or monolingual, limiting their ability to measure culturally grounded reasoning. We introduce SEA-NLI, a native, culturally grounded NLI benchmark covering eight SEA countries in English and native regional languages, verified by native speakers. Across 17 encoder and decoder models, we observe a low performance from all models, especially for knowledge-intensive categories such as Languages and Science and Technology. Our analysis shows that failure cases mainly stem from missing SEA cultural knowledge: SEA-adapted models and culture-aware prompting improve performance, while CoT prompting offers limited gains.

---


### 150. [BA-T: An Iterative Transformer for Two-View Bundle Adjustment](https://arxiv.org/abs/2606.03287)

**<font color=#1a73e8>作者：</font>** Ganlin Zhang, Weirong Chen, Daniel Cremers 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feed-forward models for 3D reconstruction have achieved strong performance using deep cross-view attention to exchange information across images. However, these approaches often depend on heavy decoder stacks and lack a structured mechanism for geometry refinement, resulting in poor multi-view consistency. We address this by drawing inspiration from classical bundle adjustment (BA), which can be viewed as an iterative information propagation process between poses and local geometry. Inspired by BA, we propose BA-T, an iterative Transformer that implements BA-style structured updates as a repeatable layer in implicit token space. Instead of relying on deep attention stacks, BA-T refines predictions based on latent residual by a single lightweight layer. Experiments demonstrate that BA-T progressively improves pose and reconstruction accuracy across iterations, achieves stronger cross-view consistency than conventional decoders, and matches or surpasses substantially larger models while using only 16% of their decoder parameters. BA-T provides a compact, efficient, and structural alternative to depth-heavy attention, enabling accurate 3D reconstruction within a lightweight architecture. The code will be made publicly at this https URL.

---


> [!TIP]
> 当前位于：**101-150**（第 3/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-312](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
