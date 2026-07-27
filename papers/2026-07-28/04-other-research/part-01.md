# 📦 其他研究 | 2026年07月28日

> 本类共 **169** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-169](./part-04.md)

---

### 1. [Risk Is Not the Target: A Monotonic Framework for Evaluating Wildfire Operational Risk Signals](https://arxiv.org/abs/2607.21597)

**<font color=#1a73e8>作者：</font>** Nicolas Caron, Christophe Guyeux, Maxime Coulmeau 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evaluating wildfire risk systems using standard machine-learning metrics such as F1-score or IoU is fundamentally flawed: these metrics assess event prediction accuracy, not the operational coherence of a continuous risk signal. This work proposes a novel monotonic evaluation framework that measures whether increases in a predicted risk score consistently correspond to increases in observed operational load, such as number of fires, intervention time, and deployed resources. Moreover, we compare three structurally different approaches on the French Alpes-Maritimes department: the expert-based DFE index, GRU- based predictive models, and FARS, a hybrid multi-agent system combining predictive AI with LLM-based reasoning. Experimental results reveal that the DFE, despite poor classification metrics, exhibits the most balanced monotonic behavior across the full risk scale. GRU models achieve strong local monotonicity but fail to produce well-distributed risk levels. FARS inherits and reveals the structural limitations of upstream signals rather than correcting them. The central finding is a paradigm shift: a good risk model does not predict fires accurately, but one whose ordinal scale meaningfully explains operational dynamics, as proved in this paper. Code of the monotonic framework is available on github.

---


### 2. [From Frame-Level Recognition to Event-Level Confirmation: Repair Traces and Runtime Failure Analysis of Public-Space Gesture Interaction](https://arxiv.org/abs/2607.21601)

**<font color=#1a73e8>作者：</font>** M. Meng, Yansong Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Public-space gesture interaction is often evaluated as a frame-level recognition problem, but deployed systems expose a different failure boundary. In scenic kiosks, exhibition halls, and service terminals, users experience whether an intended action becomes a stable interaction event, not whether individual hand-landmark frames are correct. We call this the recognition-to-interaction gap.
This paper analyzes 8 engineering repair records from a scenic-area interactive kiosk project, covering 4 gesture tasks: two-hand bowing, single-hand fist shaking, two-hand catching control, and knowledge-graph node hovering. From these traces, we extract 20 failure instances and organize them into six non-exclusive working failure classes: model-output degeneration, temporal mismatch, geometric-scale instability, coordinate-rendering mismatch, runtime lifecycle failure, and feedback synchronization and recovery failure.
We further organize recurring repair mechanisms into an event-level runtime abstraction between the hand-landmark model and the interaction task. The contribution is deliberately bounded: a deployment-grounded failure taxonomy, an event-confirmation runtime abstraction, and case-study findings. We do not claim a new recognition model, large-scale user evaluation, or quantified accuracy gains.

---


### 3. [Analyzing Middle School Students' Dialogue and Behaviors during Collaborative AI Chatbot Development Using Ordered Network Analysis](https://arxiv.org/abs/2607.21603)

**<font color=#1a73e8>作者：</font>** Shan Zhang, Andres Felipe Zambrano, Xiaoyi Tian 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As Artificial Intelligence (AI) education has become a key component of K-12 curricula, activities such as designing and developing conversational agents are increasingly used as instructional practice. Prior work has primarily examined these activities by focusing on students' learning outcomes or the quality of final AI artifacts, offering limited insight into the collaborative processes through which learning unfolds during AI system development. Although the AIED community has a long history of studying collaborative learning in STEM and Computing education, the emergence of AI learning environments in which students build AI systems presents new opportunities to understand how collaboration unfolds in AI education contexts. Grounded in these foundational works, the current study examines collaborative interaction among middle school students engaged in the design and development of an AI chatbot. Using Ordered Network Analysis of students' dialogue and development actions, we characterize how collaboration is organized over time and how interaction patterns relate to chatbot quality and AI knowledge outcomes. Results reveal that higher-quality chatbots are associated with more integrated sequences linking explanation, testing, and refinement. Interaction patterns involving articulated reasoning and repeated testing and revision in response to chatbot output were also associated with stronger AI knowledge outcomes. These findings provide a process-oriented account of collaborative AI chatbot development and extend AIED research on collaborative learning processes to AI education contexts.

---


### 4. [Natural Language Processing in Health Professions Education: A Scoping Review](https://arxiv.org/abs/2607.21605)

**<font color=#1a73e8>作者：</font>** Javad Mohammad Alizadeh, Pegah Saebi, Mukesh Kumar Patel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Natural language processing (NLP) and artificial intelligence (AI) are rapidly transforming health professions education, yet no scoping review has systematically mapped their applications across the full spectrum of health education contexts, including public health. Following the Arksey and O'Malley framework and PRISMA-ScR guidelines, this review synthesized evidence from 64 studies published between 2015 and 2026, identified through searches of PubMed, ERIC, IEEE Xplore, and Google Scholar. Seven thematic domains were identified: automated assessment, large language models (LLMs) as student-facing learning support, virtual patients and clinical simulation, curriculum analysis and program evaluation, personalized and adaptive learning, public health and health promotion education, and educator and institutional integration. Findings reveal significant technical promise, particularly in automated assessment, clinical simulation, and curriculum analysis, alongside persistent challenges including hallucination and accuracy concerns, algorithmic bias, data privacy, digital divide, overreliance, and absence of standardized outcome measures. Only four studies explicitly addressed public health education, representing a major evidence gap. This review provides a foundation for evidence-informed integration of NLP and AI across health professions education and highlights public health education as a priority area for future research and investment.

---


### 5. [TILT: Improving Compositional Generation in Diffusion Models with a Model-Intrinsic Reward](https://arxiv.org/abs/2607.21606)

**<font color=#1a73e8>作者：</font>** Debottam Dutta, Jaehoon Hahm, Jianchong Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in powerful text-to-image generation models have made it increasingly important to develop test-time methods that modify the sampling trajectory to produce images more faithful to complex compositional prompts. We present TILT, a training-free framework for compositional text-to-image generation via test-time reward alignment. We interpret compositional failures as overlap modes between joint and single-concept distributions, and define a reward that favors samples where all concepts are jointly present. This reward is intrinsic to the base model and does not require any external supervision or reward models. This yields a KL-constrained objective with a closed-form tilted target distribution and principled guiding steps for diffusion sampling. The interaction of concept distributions together with the above reward naturally leads to two different guidance strategies while a hybrid approach that balances their respective benefits produces stronger performance. Experiments on prompts from T2ICompBench show that our method improves compositional alignment while preserving image quality compared to previous baselines.

---


### 6. [Spectral Flow Certificates for Depth-Aware Long-Range Propagation in Graph Neural Networks](https://arxiv.org/abs/2607.21607)

**<font color=#1a73e8>作者：</font>** Ranjan Veerabhadraswamy, Ajith Jubilson Emerson  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Graph Neural Networks propagate information through local message passing, but the graph topologies themselves can silently prevent any amount of training from solving long-range tasks. When we deploy GNNs on new graphs, there is currently no inexpensive way to know, before training begins, whether the graphs' structures will allow information to travel far enough between distant nodes. We address this gap by proposing Spectral Flow Certificates (SFCs), single scalars computed from the graphs' normalised Laplacians in seconds, requiring no model training and no labelled data. An SFC fuses a graph's algebraic connectivity with the chosen message-passing depth into one number that measures how much of the critical spectral bottleneck can be traversed within the available depth budget. Unlike raw spectral gaps, which are static and depth-agnostic, SFCs adapt as the number of layers increases and therefore carry strictly more diagnostic information when depths vary. Compared with classical structural statistics such as average effective resistance and graph diameter, SFCs explain more than twice as much variance in trained GNN long-range accuracy. Across twenty-five synthetic graph families spanning paths, cycles, grids, regular graphs, and random graphs, SFCs predict trained accuracy before any gradients are computed, achieving explanatory power above ninety percent at all tested depths. The same predictive relationships hold on one hundred fifty real molecular graph topologies drawn from three independent benchmark datasets, confirming that the findings are not artefacts of their synthetic construction. Taken together, these results show that a single eigenvalue computation is sufficient to flag topology-limited graphs before committing to expensive training pipelines, providing a principled first filter for GNN deployments.

---


### 7. [SCOPE and SCION: A Benchmark and an Auditable Reference Pipeline for Schema Induction and Fusion from Text](https://arxiv.org/abs/2607.21610)

**<font color=#1a73e8>作者：</font>** Miaobo Hu, Xiaobo Guo, Shuhao Hu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Schema graphs are an upstream bottleneck of schema-grounded information extraction and knowledge graph construction, yet most extraction systems assume the schema is already available. We introduce SCOPE (Schema Construction and Ontology-induction Pipeline Evaluation), a train-text-only benchmark for corpus-to-schema induction and optional schema fusion from raw text, built from 24 public information extraction sources (15 RE and 9 EE) normalized into evaluation-only gold schema graphs; its core event-extraction target covers event types and within-event argument roles, with inter-event links reported separately. We present SCION (Schema Construction and Induction with Ontology Normalization), an auditable reference pipeline rather than a new extraction architecture; it constructs candidate spaces from train text and restricts naming, merging, filtering, validation, and conservative fusion to candidate-linked evidence under strict JSON contracts. On the SCOPE core suite, SCION-lite attains the highest F1 among released source-schema references, Text2Onto-style, LLM-only, and matched extract-then-aggregate baselines under Literal, Fuzzy, Continuous, and Graph schema-graph metrics, while the compact open-model SCION-RL variant reduces reliance on proprietary LLM schema engineers. These results are reported against normalized typed-edge targets rather than as claims that induced schemas surpass human ontology design; the release includes evidence-linked outputs, parse/fallback logs, candidate retention/merging logs, run manifests, code, and benchmark packages at this https URL.

---


### 8. [A Systematic Survey on Image Description Techniques for STEM Domains](https://arxiv.org/abs/2607.21611)

**<font color=#1a73e8>作者：</font>** Marco Cardia, Letizia Angileri, Marina Buzzi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The proliferation of visual data in Science, Technology, Engineering, and Mathematics (STEM) fields presents accessibility barrier for individuals with blindness or visual impairments. While recent advances in Artificial Intelligence (AI) offer new opportunities to generate textual descriptions of STEM images, the research landscape is fragmented and its impact on real users remains limited. This systematic survey examines 20 peer-reviewed studies on AI-based techniques for describing STEM visuals, with a specific focus on accessibility and human-computer interaction. Following the PRISMA methodology and a ROBIS-based risk-of-bias assessment, the review analyzes (i) the types of STEM visuals targeted, (ii) the AI and machine learning architectures employed, (iii) the datasets and evaluation metrics adopted, and (iv) the interaction modalities through which descriptions are delivered. The analysis reveals a shift from static, one-shot alt text toward interactive and multimodal systems that integrate conversational interfaces, keyboard navigation, and audio or haptic feedback. However, critical challenges persist, including factual inaccuracies and hallucinations, the scarcity of accessibility-first datasets co-designed with blind and low-vision users, and a heavy reliance on automatic text-overlap metrics that poorly capture perceived usefulness and trust. The survey concludes by outlining key research directions for HCI, emphasizing user-controlled verbosity, explainable and verifiable AI pipelines, and the integration of accessible description tools into mainstream STEM authoring and learning environments.

---


### 9. [FrED: External Data Influence Estimation via Domain Knowledge Graph Grounding](https://arxiv.org/abs/2607.21615)

**<font color=#1a73e8>作者：</font>** Theodoros Aivalis, Iraklis A. Klampanos, Antonis Troumpoukis 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rapid deployment of generative AI has amplified the critical need for Training Data Attribution to ensure transparency and accountability. However, current parametric approaches require computationally prohibitive access to model weights, while similarity-based methods ignore deep structural context. We propose a novel probabilistic framework that operates entirely in a black-box setting. Our method fuses continuous feature similarities with discrete, domain-specific Knowledge Graphs (KGs). This approach ensures the attribution is grounded in structural reality, explicitly rewarding highly specific historical samples while preventing generic background data from dominating the results. We evaluate our framework across two distinct domains where linking outputs to data and domain context is inherently complex: abstract artistic image synthesis and high-dimensional physical weather forecasting. Extensive benchmarking demonstrates the robust efficacy of our approach. In the artistic domain, it achieves a strong Linear Datamodeling Score that exceeds standard black-box similarity baselines, while closing much of the gap to gradient-based estimators. We additionally present a cross-domain feasibility case study in environmental forecasting, where we use domain KGs to retrieve physically consistent historical analogs for regional flood forecasts, improving geographic localisation over a latent-only baseline. Operating entirely without internal model access, our approach provides an efficient, interpretable mechanism for post-hoc influence analysis and domain-grounded retrieval.

---


### 10. [From Profiles to Steering Vectors: Global Sparse Priors and Local Semantic Calibration for Personalized Text Generation](https://arxiv.org/abs/2607.21620)

**<font color=#1a73e8>作者：</font>** Liuji Chen, Zeyu Zhang, Xinyuan Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Personalized text generation requires models to capture user-specific writing styles from historical data. Existing approaches based on retrieval, parameter-efficient fine-tuning, or activation steering either introduce inference and storage overhead or struggle to separate stylistic signals from semantic content. We propose GLASS, a training-free framework for personalized generation via Global-Local Activation Steering with Sparse priors. GLASS uses sparse autoencoders to extract a global user-style prior from historical responses and constructs local contrastive style vectors over clustered interaction scenarios. During inference, it jointly injects global and local vectors into different model layers, enabling context-aware personalization without retrieval or parameter updates. Experiments on LaMP and LongLaMP show that GLASS outperforms retrieval-, fine-tuning-, and steering-based baselines across ROUGE metrics and LLM-as-judge evaluations. Further analyses show that SAE-based representations are more robust to topic and length shifts, suggesting better disentanglement of stylistic information from semantic residue.

---


### 11. [Cloud-Native Evaluation-as-a-Service: A Microservices Architecture for Scalable AI Monitoring with Conformal Guarantees](https://arxiv.org/abs/2607.21623)

**<font color=#1a73e8>作者：</font>** Lei Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present EaaS, a cloud-native reference architecture that operationalizes AI evaluation methods as six stateless Kubernetes microservices: conformal prediction with finite-sample-corrected Adaptive Prediction Sets, calibration assessment, drift detection via RFF-approximated Maximum Mean Discrepancy, fairness monitoring with bootstrap confidence intervals, a DAG-based pipeline orchestrator, and a result storage API. We validate four key methodological concerns. First, empirical coverage is consistent with the marginal conformal guarantee across K=50 random calibration/test splits, with mean coverage within 1.4 percentage points of the nominal target. Second, all four MMLU answer tokens appear in the top-20 logprobs with 0% imputation needed, and simulated imputation at 10% produces less than 1.5% coverage impact. Third, RFF-MMD achieves 100% detection power for mild and severe drift at the median heuristic bandwidth, with Type I error between 5-8.5%. Fourth, fairness monitoring on the UCI Adult Income dataset reveals significant demographic parity disparities by race (DP gap=0.33) with stable alerts across sequential batches. Conformal prediction and calibration services achieve sub-2ms p99 latency at batch size 100; RFF-MMD requires ~500ms suited for periodic batch monitoring. A comparison with four open-source tools suggests that, to the best of our knowledge, no current platform combines conformal-prediction-as-a-service, microservice decomposition, and DAG-based orchestration.

---


### 12. [Discrete Action Space as a Prerequisite for GRPO Convergence in Small-Model Continuous Control](https://arxiv.org/abs/2607.21626)

**<font color=#1a73e8>作者：</font>** Dmytro Filatov, Valentyn Fedorov, Vira Filatova  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study whether Group Relative Policy Optimization (GRPO) can fine-tune small language models for simulated quadrotor continuous-control tasks. In our benchmark, vanilla GRPO fine-tuning of Qwen-0.5B for 25 Hz quadrotor velocity control collapses to the trivial zero action: 0 percent success rate, with entropy falling from 0.35 to 0.03 within 60 steps. Two ablations - removing the jerk-penalty term and removing the KL anchor to the pretrained prior - each prevent entropy collapse, yet neither enables learning. When the action interface is replaced by a 5-way categorical choice over PID presets, training converges. The resulting controller traces a smoothness-reliability Pareto frontier along training duration; both endpoints are reported: 98.6 percent success with 0.656 m/s3 jerk at 64 steps, and 100 percent success with 1.103 m/s3 jerk, or 0.796 under a matched velocity cap, at 256 steps. The recipe is evaluated across three pretrained language models. As context, a re-tuned classical baseline, PID with Ki = 0.30 and vmax = 2.5, reaches the same 100 percent success rate at jerk 0.736 m/s3. A high-fidelity simulation using Crazyflie 2.1 dynamics surfaces a hover-region training-distribution gap.

---


### 13. [Wavelet Phase Diffusion for Structurally and Semantically Consistent Sim-to-Real Translation](https://arxiv.org/abs/2607.21628)

**<font color=#1a73e8>作者：</font>** Kaiwen Wang, Frank Bieder, Yinzhe Shen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Simulation-to-reality translation must bridge the appearance gap between synthetic and real domains while preserving structural and semantic consistency. Conditioning-based methods achieve spatial alignment but introduce computationally expensive control modules. Paired-data methods achieve realism but rely on complex synthesis pipelines, often altering scene geometry and semantics. Training-free editing methods avoid both constraints but lack a learned appearance prior, limiting their perceptual quality. Recently proposed phase-preserving diffusion presents a promising alternative, but Fourier-domain formulations are constrained by global spectral coupling. This coupling induces spatial artifacts such as ringing and boundary leakage, thereby degrading structural and semantic consistency. We introduce Wavelet Phase Diffusion, which addresses this through two components. First, we operate in the Dual-Tree Complex Wavelet Packet Transform domain, whose localized wavelet packets enable spatially adaptive phase injection without global spectral interference. Second, Low-Frequency Randomization (LFR) replaces the low-frequency packet, decoupling the model from the synthetic illumination prior and enabling in-distribution real-world appearance. Both components train on unpaired open-domain data, and introduce negligible inference overhead. The spatial locality further enables instance-level translation, where individual objects or regions are translated to photorealistic appearance independently while the surrounding scene remains untranslated. On vKITTI $\to$ KITTI image translation, ours outperforms prior methods in realism and semantic consistency while maintaining competitive structural alignment. For CARLA video translation, ours approaches the realism of paired-data methods while reducing VLM planner ADE and FDE by $5.4\%$ and $5.1\%$, respectively.

---


### 14. [On the Depth Scalability of Logic Gate Networks](https://arxiv.org/abs/2607.21633)

**<font color=#1a73e8>作者：</font>** Taegun An, Dohun kim, Haebeom Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Logic Gate Networks (LGNs) implement computation through compositions of Boolean operations, yet unlike classical Boolean circuits, existing LGNs do not reliably benefit from increased depth. We identify two distinct causes: optimization collapse in deep relaxed LGNs and a topology-induced limitation that persists even when skip-biased initialization and straight-through estimation stabilize training. Thus, trainability alone is insufficient; deeper layers must also receive information that supports useful computation.
We introduce Input-Anchored Logic Gate Networks (IALGNs), in which each gate combines an evolving hidden feature with a direct input anchor. This topology preserves a computational spine while conditioning every layer on the original input. We show that a depth-D path can depend on up to D+1 input bits and establish a strict path-wise depth hierarchy. Random-k anchor relaxation further improves anchor selection without relaxing the spine.
Across MNIST, CIFAR-10, and CIFAR-100, IALGNs achieve consistent fixed-width depth--accuracy improvements beyond 100 layers, whereas alternative LGN topologies saturate or degrade. Layer-wise probes, topology ablations, and effective-depth analysis show that input anchoring produces progressively more informative representations and preserves longer computational paths. These results demonstrate that scalable depth in LGNs requires both stable optimization and an information-access pattern that supports input-conditioned refinement.

---


### 15. [MotifRole-Diff: Risk-Optimal Role-Aware Corruption for Masked Molecular Graph Diffusion](https://arxiv.org/abs/2607.21634)

**<font color=#1a73e8>作者：</font>** Tasfia Nuzhat Ornee, Elias Hossain, Ivan Garibay 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Masked discrete diffusion for molecular graph generation typically applies a uniform corruption schedule to all tokens in a lossless graph-to-sequence representation, implicitly treating structurally heterogeneous molecular components as equally difficult and equally important to reconstruct. However, different molecular graph token roles exhibit substantial variation in denoising difficulty and their influence on the decoded molecule, motivating role-specific corruption strategies. We introduce MotifRole-Diff, a role-aware corruption process that allocates masking rates according to empirically measured denoising difficulty and graph-level perturbation impact while preserving the model architecture, clean sequence space, and lossless molecular-graph decoder. We formulate schedule selection as the risk-optimal allocation of a fixed masking budget across token roles. Our theorem characterizes optimality for the modeled role-weighted residual risk, while downstream generation performance is evaluated empirically. Under matched architecture, training budget, and sampling compute, MotifRole-Diff improves validity on QM9 from 0.905 to 0.944 while reducing FCD from 1.701 to 1.609, and on MOSES improves validity from 0.920 to 0.938 while reducing FCD from 2.125 to 1.850. Role-wise diagnostics further show improved reconstruction across molecular graph token categories. Together, these matched-compute results indicate that structurally informed corruption is a more effective masking strategy than uniform schedules for serialized molecular graph diffusion.

---


### 16. [Measuring the Dependency Gap: Diagnosing Inter-Column Fidelity in Tabular Generative Models](https://arxiv.org/abs/2607.21636)

**<font color=#1a73e8>作者：</font>** Jie Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Synthetic tabular data is valued for preserving not only each column's marginal distribution but the dependencies between columns -- structure that carries much of the discriminative signal for minority classes in imbalanced domains such as fraud and clinical risk. Yet the metrics most commonly used to certify synthetic tabular data are, we show, largely blind to inter-column dependency: a baseline that models every column independently (and therefore destroys all dependency) is judged indistinguishable from real data by the logistic-regression C2ST, and the pairwise Trend score is only partially sensitive. We introduce a dependency-aware fidelity diagnostic that decomposes a strong classifier two-sample test (XGB-C2ST) into marginal, dependency, and numerical-categorical cross components, anchored between a worst-case fully-factorized reference (all dependency destroyed) and a best-case real-data oracle. Applying it to a state-of-the-art flow-matching generator (TabbyFlow/EF-VFM), we find a real dependency gap that standard metrics miss; destroying dependency outright collapses minority-class utility, and the generator's residual gap carries a smaller, consistent utility cost. We then ask whether this gap reflects a structural limitation of mean-field generative objectives. It does not: consistent with recent recovery results for variational flow matching, the objective is asymptotically exact. Yet the gap is stubborn -- a 16x increase in model capacity does not close it -- pointing to the absence of direct dependency supervision rather than a capacity or structural limit. Consistent with this, and because the residual gap is higher-order, no cheap intervention closes it: not an in-model dependency mechanism, not post-hoc copula correction, and not the 16x capacity increase -- a caution for a field that assumes such fixes help.

---


### 17. [Quasi-Monte Carlo Initialization for Meta-Reinforcement Learning](https://arxiv.org/abs/2607.21637)

**<font color=#1a73e8>作者：</font>** Julian G. Soltes  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper explores the efficacy of quasi-Monte Carlo (QMC) weight initialization for meta-reinforcement learning within modern benchmark environments. Various sampling methods are used to bound a population-based search and aggregate an optimal prior from a baseline set of tasks. The QMC meta-priors show improvements in training convergence compared to modern orthogonal (SB3) defaults when extrapolated to similar unseen continuous control environments. In dissimilar tasks, the orthogonal orientation was globally superior for an unbiased search.

---


### 18. [StajChain: A Hyperledger Fabric-Based Multi-Party Internship Agreement System](https://arxiv.org/abs/2607.21643)

**<font color=#1a73e8>作者：</font>** Rampia Perente  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Many administrative processes, such as internship agreement processes, often rely on manual approval workflows and centralized record-keeping. This makes the process susceptible to delays and unauthorized modification while introducing limited traceability. This study presents StajChain, a permissioned blockchain-based multi-party internship management system developed using Hyperledger Fabric. The proposed system implements the complete internship agreement lifecycle through smart contracts and enforces role-based authorization using Hyperledger Fabric CA. The architecture consists of a React frontend, a this http URL backend, an off-chain SQLite database, and the on-chain Fabric ledger. Users such as students, companies, faculty internship committee members, and the central internship unit can perform specified operations according to their role and identity. The agreement lifecycle follows predefined sequential steps, and at each step, the ledger status is updated and recorded securely. Furthermore, the system was evaluated using functional and performance tests, indicating acceptable throughput and latency for verifiable administrative workflows. This implementation demonstrates how permissioned blockchain technology can improve transparency, integrity, and accountability while preserving controlled access to institutional data and providing a working prototype that can be used in various future systems.

---


### 19. [Toward Goal-Agnostic Joint-Embedding Predictive Control of Partial Differential Equations](https://arxiv.org/abs/2607.21644)

**<font color=#1a73e8>作者：</font>** Jonathan Gallagher, Roberto Guglielmi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present a goal-agnostic control framework for partial differential equations (PDEs) built around a joint-embedding predictive architecture (JEPA). The small 2D ViT encoder and action-conditioned latent dynamics are trained offline without a reward or downstream goal, frozen, and reused by a model-predictive path integral (MPPI) controller. We find that when available, the control objective is better applied to an explicit physical observable (provided injectivity) than to minimizing raw Euclidean distance ($L^2$) in the learned latent space. For a learned linear kinetic-energy (KE) probe on frozen latent rollouts we can reproduce held-out trajectories with $R^2=0.989$, while requiring no change to the underlying world model. On the PDE Control Gym 2D Navier--Stokes benchmark, using KE-probe planning improves the matched 50-episode native reward from $-12.08\pm0.86$ for latent-$L^2$ planning to $-10.90\pm0.91$ (95\% CI), while lowering last-quarter velocity-field RMSE from $0.0765$ to $0.0692$. Across three intentionally withheld, dissimilar, aperiodic targets, KE planning lowers late field RMSE by $53\%$ relative to latent-$L^2$ planning ($0.0220$ versus $0.0469$), winning all 30 paired episodes. The same frozen model also supports controls targeting stabilization around a steady configuration via direct regulation of KE achieving $2.7\%$ mean relative error. While the latent probe is brittle to measurement noise and missing pixels, we believe the results support the claim that latent dynamics can remain both dynamic and goal-agnostic while calibrated observables (granted they guarantee unique continuation) may be a better objective for state control

---


### 20. [Multi-Horizon Consistency as Geometry: When Latent Dynamics Contract, and When They Do Not](https://arxiv.org/abs/2607.21645)

**<font color=#1a73e8>作者：</font>** Kavya Bhand, Aadi Joshi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-horizon latent consistency is a common training knob in video predictors and world models, but practitioners rarely know what it does to transition geometry. We treat lambda, the weight on multi-step latent agreement, as a diagnostic control and measure an empirical expansion proxy L20,q95 together with horizon-20 prediction error E20. On Moving-MNIST (n=6 seeds at the critical pair), raising lambda from 0 to 0.8 cuts L20 from 4.96 +/- 2.01 to 1.01 +/- 0.06 (paired t p=0.005, Wilcoxon p=0.031) and halves E20 (0.365 to 0.177, paired t p=1.1e-13). Four of six seeds cross L<1 at lambda=0.8. The same loss does not produce population L<1 on action-conditioned Pendulum-v1 or CartPole-v1, nor on KTH Actions video, even when E20 improves. An associational mediation analysis on MMNIST gives r-hat=0.94 (95% CI [0.88, 1.00], n=27, B=2000); lambda was not randomized. Defensive checks (architectural baselines, exogenous stress, WorldTest, MPC, scaling) mostly support a narrow claim: soft consistency can push passive video toward a near-contractive band, and that band is domain-limited. A stochastic-forcing law L20 ~ 1.23 + 1.82 eta at lambda=0.8 (bootstrap slope CI [1.73, 1.92], R^2=0.96) unifies control domains on the same curve via calibrated eta_eff. Complete joint slices at lambda in {0.4, 1.2} (30/30 cells, 5 eta x 3 seeds) show comparable linear L20(eta) slopes (~1.69 and ~2.00); we do not fit a continuous (lambda, eta) surface. We do not report DreamerV3 or TD-MPC2 returns.

---


### 21. [Adjustment Speed as a Safety Constraint for Nonstationary Reinforcement Learning](https://arxiv.org/abs/2607.21646)

**<font color=#1a73e8>作者：</font>** Timothy Tomashevskiy  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Ensuring safety in reinforcement learning under nonstationarity requires determining whether a learning system can safely adapt to forecasted environmental change within the required recovery horizon. Existing safe reinforcement learning methods typically assume stationary environments and do not explicitly consider adaptation speed as a safety concern. However, when environments evolve over time, delayed adaptation may result in transient unsafe behavior.
This paper proposes adjustment speed as a safety constraint for nonstationary reinforcement learning. The central idea is to define safety in terms of adaptation feasibility: future states or regions may become unsafe when the adaptation required to remain safe exceeds the learning system's calibrated recovery capacity. The proposed framework uses learned context representations and short-horizon context forecasts to estimate adaptation demand and compare it with the agent's achievable adaptation capacity.
When predicted adaptation demand exceeds the calibrated recovery capacity, the framework proactively tightens the admissible action set and activates an action-level shield to reduce unsafe behavior before violations occur.
Experiments in a nonstationary driving environment show that the proposed approach primarily reduces safety violations in short-horizon windows aligned with context changes. Ablation studies further show that shielding is more conservative for peak- and tail-risk suppression, while optimization-level adjustment provides additional reductions in short-horizon switch-conditioned violations.
These results support adaptation feasibility as a practical safety principle for reinforcement learning under nonstationarity and demonstrate that proactive intervention can improve safety during periods of environmental change.

---


### 22. [A Drift Stable Quantum Federated Learning for Intelligent Services](https://arxiv.org/abs/2607.21647)

**<font color=#1a73e8>作者：</font>** Shanika Iroshi Nanayakkara, Shiva Raj Pokhrel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Quantum federated learning enables distributed clients to train quantum neural networks without sharing local data, making it promising for privacy-aware intelligent services. Intelligent services in this context refer to privacy-sensitive distributed decision systems, such as fraud detection and genomic classification, where reliable and fair client-level learning is as important as the accuracy of the aggregate model. However, heterogeneous client data and noisy quantum optimization often cause unstable local updates, client drift, and unfair performance between clients. This paper proposes DUQFL-Prox, a drift-stable quantum federated learning framework based on deep-unfolded local optimization. Instead of using a fixed local optimizer, each client performs adaptive unfolded SPSA updates, while a proximal term keeps the local model close to the global model. A lightweight controller learns step-specific optimization parameters to improve post-aggregation performance. Experiments on financial fraud and genomic classification tasks show that DUQFL-Prox improves stability, generalization, and client fairness compared with standard QFL baselines. The results suggest that deep-unfolded quantum federated learning can support more reliable and fair intelligent services in heterogeneous distributed environments.

---


### 23. [Shallower ReLU Network Representations via Exact Linear Algebra](https://arxiv.org/abs/2607.21651)

**<font color=#1a73e8>作者：</font>** Kilian Rueß, Gennadiy Averkov, Florestan Brunck 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We prove that the maximum of $n$ real numbers is exactly representable by a ReLU network with two hidden layers for every $n\le 10$. The constructions are obtained by reducing the problem to exact rational linear algebra: after a symmetry reduction, the necessary cancellations are encoded in finite linear systems over $\mathbb{Q}$, which we solve and verify computationally. The representation of $\max_{10}$ has a structured first hidden layer consisting only of pairwise maxima, a feature that allows it to be recursively substituted into larger networks. We use this to show that for every $n>10$, the maximum $\max_{n}$ can be exactly represented with $\lceil{\log_5 (n / 2)\rceil}+1 < \log_5(n) +1.5694$ hidden layers. Via the generalized hinging-hyperplane representation [Wang, Sun, IEEE Trans. Inf. Theory 2005], the same depth bound holds for all continuous piecewise-linear functions on $\mathbb{R}^d$, with $d+1$ in place of $n$. In particular, every continuous piecewise-linear function on $\mathbb{R}^d$ for $d\le 9$ admits a two-hidden-layer ReLU representation. Our results improve on [Bakaev, Brunck, Hertrich, Stade, Yehudayoff, STOC'26]. In that work, the authors established a two-hidden-layer representation for $\max_{5}$ and an upper bound of $\lceil{\log_3 (n-2)\rceil}+1$ hidden layers for $\max_{n}$.

---


### 24. [Defining AI-Native Systems: Autonomy as Revision Authority](https://arxiv.org/abs/2607.21659)

**<font color=#1a73e8>作者：</font>** Cheng Tan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI has begun to write systems code: agents now synthesize, verify, and deploy system components. Despite this shift, "AI-native" remains a marketing term with no precise technical definition. This paper gives it one. We define AI-nativeness along a single axis---authority over the system's own decisions rather than by the capability of the underlying AI models. Building on a decision-level model of a system, we distinguish occupancy (who executes a decision) from revision authority (who may change it), organize revision authority into a ladder---self-tuning, self-rewriting, self-architecting and define a system as AI-native when an AI autonomously rewrites the system's own implementations. The definition further requires an escalation detector, a verification procedure, and a verified fallback, while leaving purpose and correctness human-owned.

---


### 25. [Physically Constrained Federated Additive Models for O-RAN SLA-Risk Prediction](https://arxiv.org/abs/2607.21665)

**<font color=#1a73e8>作者：</font>** Aubida A. Al-Hameed, Mohammed M. H. Qazzaz, Maryam Hafeez 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Proactive service assurance in O-RAN requires predicting per-slice SLA violations before they occur. The prediction model must be auditable by operators and must train across base stations without pooling per-slice KPIs, which are commercially sensitive because slices are leased to individual tenants. Neural additive models (NAMs) offer auditability because each KPI contributes through a visible shape function. However, visibility alone does not guarantee physical validity. On the ColO-RAN testbed dataset, unconstrained NAMs learn effects that contradict wireless physics, for example predicting higher risk when channel quality improves. This failure appears under both local and centralized training, and non-IID federated averaging worsens it. We present Monotone FedNAM, a federated additive model in which KPIs with unambiguous physical direction are represented as monotone splines whose constraints survive FedAvg aggregation by construction, while contestable KPIs remain unconstrained. The model trains and operates as a Non-RT RIC rApp and is compact enough for deployment as a Near-RT RIC xApp. Monotone FedNAM eliminates all monotonicity violations, raises constrained shape consistency from 0.71 to 1.00, generalizes to an unseen scheduling policy, and reduces uplink traffic by 65%, at a cost of 0.04 to 0.07 AUC. These results show that physically constrained federated additive models can support auditable SLA risk inference for multi-tenant O-RAN service assurance

---


### 26. [Neural Feature Governance: Extending Atom Prevalence](https://arxiv.org/abs/2607.21671)

**<font color=#1a73e8>作者：</font>** Idris Karel Seunda Ekwe, Patrick Tenga Shako, Ernest Parfait Fokoué  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural network compression and interpretability remain open challenges in modern deep learn- ing, where billion-parameter architectures deliver impressive accuracy at the cost of trans- parency, computational efficiency, and reliable uncertainty quantification. This paper introduces Neural Atom Prevalence (NAP), a principled Bayesian framework for structured node-level model selection in feedforward neural networks. NAP introduces the neural atom (activation unit) and functions as a hybrid method operating through a four-phase pipeline: Bayesian Lottery Ticket (BLT) identification via Iterative Magnitude Pruning (IMP), soft variational training of the Spike and Slab Independent Gaussian (SS-IG) model, Poisson-Binomial (PB) optimal layer-size selection, and Bayesian fine-tuning to produce a sparse, stable, interpretable, and accurate model. Extensive empirical validation across simulated nonlinear regression, two UCI benchmark datasets (Concrete, YearPredictionMSD), and the MNIST image classification task demonstrates that NAP achieves state-of-the-art structural sparsity, reducing active nodes to as few as 8% of the original dense architecture on MNIST, while well-calibrated probabilisti- cally: the aleatoric-epistemic uncertainty decomposition reveals that model ignorance accounts for only 3 to 4% of total predictive variance across all experiments, and regression reliability diagrams confirm a near-nominal predictive interval coverage (93.4% observed against a 95% target). These results establish NAP as a reliable, theoretically grounded, and computation- ally tractable solution to the simultaneous pursuit of sparsity, accuracy, interpretability, and uncertainty quantification in Bayesian neural networks.

---


### 27. [Self-Poisoning in Adaptive Out-of-Distribution Detection: A Sharp-Threshold Theory and Certified Label-Free Calibration](https://arxiv.org/abs/2607.21673)

**<font color=#1a73e8>作者：</font>** Vishnu Bindu Balachandran  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Test-time adaptive out-of-distribution (OOD) detectors update a memory bank from the unlabelled stream. We show this adaptation obeys a provable dynamical law. Modelling bank impurity as a generalized Pólya urn, we prove almost-sure convergence to a mean-field equilibrium whose slope acts as a reproduction number. Below one, impurity stays benign. Above one, the bank is fully poisoned and the detector collapses. The measured admission kernel is affine ($R^2 \ge 0.996$) with slope just below one in every encoder family (a protocol signature), so this detector class is near-critical by design, and across 96 settings the predicted threshold matches the empirical collapse, where ungated dictionaries lose up to $0.163$ AUROC. We then prove that a certified admission gate, reading only a frozen reserve, severs the feedback loop and removes the transition at every contamination rate, even adversarially, while controlling false positives label-free. For the complementary static-calibration failure under drift we give CDC, which restores nominal FPR label-free on all tested drift-affected cells. Finally we prove a two-world impossibility theorem. Drift and contamination are indistinguishable without labels, forcing a closed-form power ceiling our procedure approaches. Together these give a complete possibility/impossibility characterization of label-free adaptive OOD detection.

---


### 28. [CARNet Cycle-Conditioned Core Aggregation and Redistribution for Multivariate Time Series Forecasting](https://arxiv.org/abs/2607.21681)

**<font color=#1a73e8>作者：</font>** Awsaf Tausif Adib, Md. Shahria Sarker Shuvo, Md. Estehaar Ahmed Emon 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurately modeling cross-variate dependencies remains a key challenge in multivariate time series forecasting, particularly in the presence of strong periodic patterns. Many existing approaches rely on attention-based mechanisms that incur quadratic complexity and scale poorly with increasing numbers of variates. Recent attention-free aggregation models address this issue through linear-complexity core-based interactions, but they do not explicitly leverage the global periodic structure present in the data. To overcome this limitation, we propose CARNet, a Cycle-Conditioned Core Aggregation and Redistribution framework that integrates global recurrent cycle information into efficient core based interaction modeling via Multihead Core Aggregation. Extensive experiments on multiple real-world multivariate forecasting benchmarks demonstrate that CARNet consistently outperforms strong transformer and non-attention baselines across diverse prediction horizons while preserving linear-complexity modeling of cross-variate dependencies.

---


### 29. [Evaluation design conditions the expert-vs-auto MeSH gap: a controlled comparison of bag-of-words and BiomedBERT on the Cohen benchmark](https://arxiv.org/abs/2607.21685)

**<font color=#1a73e8>作者：</font>** Samuel M. Okoe-Mensah  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A systematic review begins with someone reading thousands of abstracts to identify the few that are relevant, and classifiers are used to prioritise that reading. Their inputs are often augmented with Medical Subject Headings (MeSH), assigned either by expert indexers weeks or months after publication or by automatic tools at once. To our knowledge the two have not been compared directly as classifier features, and no previous work has asked whether that comparison's outcome depends on how the classifier is evaluated. Using the Cohen et al. (2006) drug-class benchmark on three topics, we characterise a bag-of-words logistic regression classifier (seven reruns) and BiomedBERT (five seeds), then examine how the Statins result changes under alternative designs. Under the canonical 5-fold full-corpus design, the bag-of-words expert-vs-auto gap on Statins is +0.096 WSS@95%. Matching the corpus size to the smaller topics (n = 803) reduces it to +0.033 (95% bootstrap CI includes zero), and 10-fold cross-validation at full size to +0.021 (CI narrowly excludes zero). Under canonical evaluation BiomedBERT gives +0.020, within sampling noise of the bag-of-words 10-fold result. A power analysis indicates a Statins-sized effect would not have been detectable at the Opioids or ADHD variance, so those nulls are design-limited rather than informative. A representation asymmetry remains: 15.1% of Statins inputs exceed BiomedBERT's 512-token limit when expert MeSH terms are appended, so truncation may contribute to the smaller transformer gap, although this cannot be separated from training volume here. In screening pipelines using transformers or 10-fold bag-of-words, the gap on the topics tested is about 0.02 WSS@95%, with CIs spanning zero on at least one bound. More broadly, benchmark conclusions about feature sources can change substantially under reasonable changes to the evaluation design.

---


### 30. [A method of Risk Analysis and threat management using analytic hierarchy process](https://arxiv.org/abs/2607.21691)

**<font color=#1a73e8>作者：</font>** Manvi Sahni, Sumanta Kumar Das  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Efficient risk analysis and threat management are essential requirements of modern air defense (AD) systems. The paper is halfway between the analytic hierarchy process (AHP) and practical reasoning to model and analyze the risks and threats associated with military AD applications. The models are applied for decision-making tasks of AD command and control (C2) for assessing and prioritizing the threat from hostile targets for efficient risk management. The paper presents a method for threat assessment using fuzzy set theory, the AHP, and the technique for order preference by similarity to ideal solution (TOPSIS). The target threat attributes are first represented using fuzzy set theory. The experts' subjective opinions on different alternatives are quantified and ranked using the AHP process. These AHP solutions are obtained through the TOPSIS for prioritization. The models are implemented in a simulated environment. The simulated system runs without any human intervention and represents the state-of-the-art model for the C2 system. The use of fuzzy set theory, AHP, and TOPSIS for decision-making tasks is particularly useful from the point of view of futuristic risk and threat management in the battlefield. This method is easy to implement in practice and good for real-time applications.

---


### 31. [Learning What Matters: Supervising Sparse Attention Routing with Causal Evidence Sets](https://arxiv.org/abs/2607.21692)

**<font color=#1a73e8>作者：</font>** Jim Allchin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparse attention reduces the cost of long contexts by allowing each query to read only selected parts of the input. These selectors are often trained by distilling the attention patterns of a dense teacher, assuming that attention reveals which context the teacher actually uses. We test that assumption on retrieval tasks where the evidence for each answer is known exactly. By masking parts of the context and measuring whether the answer changes, we find that attention and causal dependence often disagree, and distilled selectors inherit the mismatch. Teachers attend to outdated facts they have learned to ignore, and their attention can vary across training runs even when they rely on the same evidence. In a two-step reference task, attention at the answer skips the intermediate step because it was resolved earlier in the forward pass: a selector trained on attention achieves 41% accuracy, while the same selector trained on causal evidence reaches 99% and matches the teacher. These evidence sets require no annotation: recovered from a frozen teacher by masking alone, they train selectors to the same accuracy. We find the same conflict in pretrained models: Qwen2.5-3B gives more attention to an outdated fact than the current one on 58% of conflicting-fact examples despite answering correctly, while Gemma-2-9B rises from 56% to 99% accuracy when restricted to the two relevant sentences. Attention shows where a model looks, not necessarily what its answer depends on; across the regimes we tested, that dependence matched or outperformed attention as a training target.

---


### 32. [An Introduction to Bayesian and Frequentist Simulation-Based Inference with Machine Learning](https://arxiv.org/abs/2607.21702)

**<font color=#1a73e8>作者：</font>** Maximilian Dax, Theo Heimel, Gilles Louppe  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Simulation-based inference (SBI) with machine learning is an increasingly important tool for solving inverse problems in science and engineering, including parameter inference and the inversion of detector effects. We provide an overview of the Bayesian and frequentist statistical frameworks, describe how machine-learning-based SBI methods, such as neural posterior estimation and neural likelihood estimation, can be used for parameter estimation within these frameworks, and show that the same methods can also be applied to Empirical Bayes or unfolding tasks. We also discuss how to validate inference results and the limitations of SBI with machine learning.

---


### 33. [A Defense of the Quadratic Model](https://arxiv.org/abs/2607.21716)

**<font color=#1a73e8>作者：</font>** Alexandru Meterez, Pranav Ajit Nair, Depen Morwani 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Due to the complexity of neural network loss landscapes, optimization theory is forced to rely on idealized models, and there is generally a tradeoff between how theoretically tractable the model is, and how accurately it describes the true optimization dynamics. In this work, we stress test the simplest possible model of optimization -- the quadratic model -- and show that it can be surprisingly predictive in an LLM setting with 150M parameters and 3B training tokens. Specifically, we show that Taylor expanding the model and the loss function at intermediate checkpoints through training can accurately predict the optimization dynamics over windows that can last up to 10\% of training. Having established this agreement, we then turn to analyzing the structure of these local quadratic optimization problems through two lenses: the Hessian spectrum and local stability. Using Lanczos quadrature with extremely deep probes, we are able to estimate the Hessian spectrum deep into the tail, and we find a surprising amount of structure in both the eigenvalues and eigenvectors, which depends on the batch size, preconditioner, and training time. We also empirically test local linear stability at intermediate checkpoints and compare it to theoretical predictions to demonstrate that optimization in LLMs typically occurs at a stochastic edge of stability, whose nature is also determined by batch size. Our results indicate the quadratic model may be a theoretically tractable proxy for pretraining optimization dynamics.

---


### 34. [RED-PIM: Reducing Data Movement for Transformers using Processing-in-Memory](https://arxiv.org/abs/2607.21731)

**<font color=#1a73e8>作者：</font>** Zahra Yousefijamarani, Alaa Alameldeen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformers are widely used across many domains, including natural language processing, computer vision, web search, and DNA sequence analysis. Given their broad applicability, improving the performance of transformer models is critical. However, the high volume of data movement between processing units and memory during attention operations significantly limits their efficiency. Processing-In-Memory (PIM) mitigates this issue by performing computations directly inside memory. While prior work has proposed PIM-based transformer implementations, they suffer from costly inter-bank communication, and struggle to scale due to the limited capacity of memory banks. As a result, attention-related data must be split across banks, diminishing the potential benefits of PIM.
In this work, we propose RED-PIM, an algorithm-architecture co-design that reduces attention latency by minimizing inter-bank data movement from O(N^2) to O(N) and shrinking intermediate attention matrices from N x N to d x d. By reorganizing matrix operations, performing computations locally, and employing an optimized data transfer strategy, RED-PIM significantly reduces computation cost and interconnect traffic. Compared to baseline PIM implementation, RED-PIM achieves inference time reductions ranging from 16.05% to 99.99% (geometric mean of 66.42%), with the largest gains on longer sequences. On real-world datasets, RED-PIM improves performance by 99.60% for long documents and 13.44% for shorter ones, while maintaining or improving accuracy. These results demonstrate RED-PIM's effectiveness for scalable and efficient transformer inference.

---


### 35. [Charting the Moral Universe: Capturing Virtues and Values of Data Visualization Practice](https://arxiv.org/abs/2607.21732)

**<font color=#1a73e8>作者：</font>** Chloe Hudson Prock, Enrico Bertini, Michael Correll  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> What do we value in our visualizations, and in the people who design them? Despite a growing body of work on critical data visualization, the conception of what it is to do ethical data visualization work can often be narrow (for instance, holding that our ethical duties are discharged merely by avoiding overtly lying or manipulating data), or entangled with potentially problematic implicit value structures (such as the assumption of the objectivity and neutrality of data, and so the designer's role being merely the passive conveying of numbers as efficiently as possible). Yet, what it means to act ethically in data visualization is broad and multifaceted, and the virtues to which we should aspire as data visualization researchers and designers are worth explicating. We conducted an interview study with a broad spectrum of 20 experienced data visualization researchers, practitioners, and data artists to solicit their values and ethical considerations around doing visualization work. We report on a list of 68 values, organized into nine virtue clusters, that we encountered in our interviews. These virtues and values together describe a diverse space of matters of care and concern in data visualization: from the unease around the best use of visualization as a tool for persuasion, to the tightrope that visualization practitioners often walk between their professional responsibilities and their personal moral commitments. The virtues themselves, as well as our interviewees' reflections on ethical practice, offer practitioners, researchers, and educators in data visualization a richer vocabulary for ethical reflection and provide a broader foundation for considering and applying visualization ethics.

---


### 36. [What AI Red-Team Evaluations Can and Cannot Prove](https://arxiv.org/abs/2607.21735)

**<font color=#1a73e8>作者：</font>** Bandana Kaur  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Red-team evaluations of AI models support some claims and not others, and the boundary between the two is calculable rather than merely a matter of judgment. We define the evidential ceiling of an evaluation as the largest factor by which one result can move belief under a fixed testing budget, derive it in closed form for the benchmark null result, and use it to locate that boundary exactly. We find that above a calculable harm rate, a benchmark of modest size certifies a category to a stated evidentiary standard, and a clean sheet is then the stronger of the two possible observations, outweighing a single reproduced failure. Below that rate, no passive benchmark of feasible size provides the specified evidence of safety under the fixed scoring rule and approximately independent trial structure. The crossing between the two regimes has a closed form. The bound is not specific to benchmarks: written in terms of a procedure's hypothesis conditioned elicitation rates, it covers adaptive and automated red teaming as well, and shows that discrimination between the hypotheses rather than attack success is what determines evidential worth. Auditing eight evaluation suites against the boundary, we find that current benchmarks are adequate for high-frequency harm categories and several orders of magnitude short for rare, catastrophic ones. Safety benchmarks are not uninformative. They are informative about a specific and computable set of propositions, and the discipline they need is to state which.

---


### 37. [Parameter-free Adaptive Sparse Attention via Compression-Based Content Selection](https://arxiv.org/abs/2607.21752)

**<font color=#1a73e8>作者：</font>** Debarshi Kundu, Swaroop Ghosh, Vasant Honavar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data-adaptive sparse attention masks substantially outperform fixed patterns (e.g., BigBird and Longformer) and can even exceed dense attention on long sequences. Existing adaptive approaches---including SBM-Transformer, Dynamic Mask Attention, and NSA---typically require additional learnable parameters, custom gradient estimators, or specialized CUDA kernels.
We show that classical data compression provides an effective masking signal with \textbf{no additional parameters}. By computing per-block gzip compression ratios, we identify non-redundant content blocks and route long-range attention selectively through them. Intuitively, blocks that gzip cannot compress contain information not predictable from local repetition, making them natural long-range attention targets. Because the compression profile is input-dependent, the resulting sparse mask adapts dynamically to content without learned parameters, auxiliary losses, or custom kernels.
On PG-19 byte-level language modeling at 92M parameters with 8K context, our method achieves 1.71 bits-per-byte (BPB), outperforming dense attention (2.89), BigBird (2.34), Longformer (3.21), and a reimplemented SBM-Transformer (3.38)---the only learned-mask baseline---by up to 1.67 BPB while adding no parameters. The advantage grows with sequence length, with the gap over BigBird widening from 0.05 BPB at 4K context to 0.63 BPB at 8K, while convergence is 3.3$\times$ faster.

---


### 38. [Humanly: A Configurable and Traceable Environment for Human-AI Collaborative Writing](https://arxiv.org/abs/2607.21758)

**<font color=#1a73e8>作者：</font>** Shenzhe Zhu, Haoqian Zhang, Xu Yang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Teachers, conference chairs, and public readers all judge writing from limited evidence, seeing only a finished document and not the process that produced it. Final text alone cannot reveal whether a document was produced through human typing, AI generation, or mixed human-AI collaboration. Existing process-tracking tools help, but many are tied to host-document histories, provide coarse activity records, and offer limited control over the writing environment. Humanly is a writing platform that makes the writing process itself the evidence. Users configure writing environments for personal documents or assigned tasks and draft in a workspace that records writing activity and in-platform AI assistance. Humanly can package a completed session into a sealed writing certificate with configuration-aware anomaly behavior review. It can support writing scenarios such as course assignments, peer review, and personal certification. Our user study shows that Humanly is helpful across roles, and a red-teaming study shows that the Humanly Typing Detector distinguishes human hand typing from automated typing.

---


### 39. [Every Model Cheats: Prompt-Level Mitigation of Cheating on Offensive Cyber Tasks](https://arxiv.org/abs/2607.21763)

**<font color=#1a73e8>作者：</font>** Michael Kouremetis, Ads Dawson, Raja Sekhar Rao Dheekonda 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents routinely cheat on cybersecurity benchmarks, inflating reported pass rates far beyond genuine capability. Prior audits of Cybench found cheating in 0.3-3.4% of traces, implicating only a handful of models. We present a controlled prompt-ablation study across 22 frontier models from 7 providers on 23 Cybench capture-the-flag (CTF) challenges under three prompt conditions (no anti-cheat, standard, severe). All 1,518 task traces were individually audited through a four-stage pipeline combining LLM-as-a-judge classification, programmatic verification, judge-verifier reconciliation, and human review. We find cheating is far more pervasive than previously estimated: under baseline conditions, 37.1% of passes involved cheating, 21 of 22 models cheated, and scores were inflated by up to 5x. Anti-cheat prompts reduce cheat propensity from 33.0% (baseline) to 17.8% (standard) to 8.5% (severe) without degrading, and sometimes improving, solve rates. However, even under the most restrictive prompt condition, eight models still produced cheated passes, four showed backfire effects, and cheating escalated from web search toward infrastructure probing. We introduce the "solve rate" metric (clean passes only) to distinguish genuine capability from cheated outcomes, and argue it should be standard practice in any evaluation where cheating vectors are available. Anti-cheat prompts are an effective and essentially free first layer of defense, but they are not a substitute for environmental controls.

---


### 40. [From Grasping to Speaking: Generative AI-Based Environment-Grounded VR Communication Training for Autistic Individuals](https://arxiv.org/abs/2607.21769)

**<font color=#1a73e8>作者：</font>** Ziming Li, Roshan L. Peiris  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Autistic individuals often face barriers in workplace communication, where soft skills are embedded within ongoing tasks and surrounding environment context, not in isolated verbal exchange. Recent work has introduced LLM-driven agents into VR-based communication training and proposed prompting schemas that let agents generate dialogue grounded in the VR environment and the user's hand-based interactions. Building on this work, we explore how different levels of environmental grounding influence the training experience of autistic trainees and job coaches. We conducted an exploratory study with 9 autistic trainees and 7 job coaches across three modalities: conversation-only (C), conversation with environmental objects (C+O), and conversation with objects and grasp interactions (C+O+G). Usability and workload were comparable across modalities, while both trainees and coaches preferred the more interactive and environment-grounded condition (C+O+G). Participants viewed C+O+G as helpful for sustaining engagement and integrating communication practice into task performance. We discuss design considerations for more flexible, interactive, and workplace-relevant VR communication training for autistic individuals.

---


### 41. [Smart predict-then-robustly-optimize](https://arxiv.org/abs/2607.21773)

**<font color=#1a73e8>作者：</font>** Aakil Caunhye, Xuefei Lu, Belen Martin-Barragan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this paper, we propose and study a robust variant of the smart predict-then-optimize approach that accounts for prediction shifts due to disturbance in the covariate feature space. While traditional integrated-learning-and-optimization models assume that side information is perfectly revealed, empirical data-driven features are frequently corrupted or noisy at the time of decision-making, leading to fragile operational policies. To bridge this gap, we integrate principles of robust optimization directly into the predictive-prescriptive pipeline via a smart predict-then-robustly optimize loss and establish a computationally tractable convex surrogate, designed to hedge against worst-case feature perturbations. On the theoretical front, we formalize the structural validity of this surrogate by proving its approximation error probability decays exponentially according to a sub-Gaussian concentration profile. Furthermore, we establish that under mild assumptions, the surrogate is Fisher consistent with high probability. We also prove necessary conditions under which our framework outperforms standard smart predict-then-optimize and maintain its superiority even when the standard method is equipped with regularized upstream predictions. Numerical experiments validate that our robust framework consistently yields significant performance improvements over standard methods, both in out-of-sample terms and in training stability.

---


### 42. [Physiological Signals as a Forensic Modality for Talking-Face Deepfake Detection](https://arxiv.org/abs/2607.21776)

**<font color=#1a73e8>作者：</font>** Othmane Harraq, Tamer Aldwairi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Talking-face (TF) deepfake generation synthesizes photore- alistic facial video from a static source image and an au- dio signal, producing forgeries that current image-based detectors consistently fail to identify. Unlike face-swap ma- nipulation, TF synthesis has no underlying real video from which to inherit physiological characteristics, making re- mote photoplethysmography (rPPG) a uniquely motivated detection modality for this forgery category. We propose a detection framework that extracts per-video rPPG wave- forms via RhythmFormer and trains a suite of lightweight classifiers to distinguish real from synthesized physiologi- cal signals. Evaluated on the TF subset of Celeb-DF++ un- der a strict subject-independent protocol, where test identi- ties are completely separated from training identities, our 1D ResNet achieves an AUC of 0.806 and EER of 27.8%, placing it within 2.4 points of the best published general- purpose detector (Effort, ICML 2025) while operating ex- clusively on the physiological channel. We document a con- trolled reproduction study of DeepFakesON-Phys, the rep- resentative prior rPPG detector, demonstrating degrada- tion from AUC 0.999 on legacy face-swap data to 0.622 on the TF subset of Celeb-DF++. We further show that detec- tion difficulty is strongly method-dependent: AUC ranges from 0.985 (Real3DPortrait) to 0.690 (IP-LAP) across the seven TF generators, with the ranking remaining perfectly stable across all evaluation protocols. This spread reflects an interpretable physiological property of each generator rather than evaluation noise, and constitutes the primary theoretical contribution of the work.

---


### 43. [AI-Integrated Scientific Inquiry: A Practice-Centered Vision for Science Education](https://arxiv.org/abs/2607.21777)

**<font color=#1a73e8>作者：</font>** Arne Bewersdorff, Matias Rojas, Xiaoming Zhai  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence (AI) has become part of scientific inquiry. Scientists use AI to observe and measure phenomena, to identify patterns in data, and to build models. As AI moves into scientific inquiry, it gains relevance for science education: students should learn how AI is changing scientific practices, ideally by engaging in AI-integrated scientific inquiry themselves. How to design such instruction, grounded in authentic scientific practice rather than taught as a standalone topic, remains an open question. In our vision, which we describe in this article, AI is treated as a set of scientific instruments that students use within the scientific practices described by the Next Generation Science Standards. Each instrument is a genuine scientific tool, pedagogically bounded: its controls are simplified while its core scientific function is preserved. The approach has two aims: engaging students in authentic scientific inquiry, and building an understanding of how AI is used in science and where it can mislead (discipline-based AI literacy, DAIL). In the article, we focus on the investigative core of inquiry, namely observing, analyzing, and modeling, and describe one exemplary AI instrument for each: computer vision for observing, clustering for analyzing, and generative modeling for modeling. We argue that every AI instrument in science education should carry a distinct reflection point that prompts critical evaluation of the AI instrument itself. Finally, we describe how agentic AI, operating across the whole inquiry rather than a single practice, could be represented, arguing that students should first build a foundational understanding of scientific inquiry and AI instruments before relying on agentic AI.

---


### 44. [From Seasonality to Semantics: Benchmarking a Hybrid Probabilistic Forecasting System for Roadblocks in Bolivia](https://arxiv.org/abs/2607.21785)

**<font color=#1a73e8>作者：</font>** Rodrigo Vargas Sainz, Christian Berón Curti  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Roadblocks in Bolivia are a social conflict phenomenon with devastating economic impacts, estimated at losses equivalent to 4% of the national Gross Domestic Product. Despite their recurrence and impact, there is a lack of local predictive systems to anticipate these events for logistical decision-making. This paper presents a hybrid probabilistic forecasting system that integrates time series decomposition (Prophet) with natural language processing (NLP) techniques applied to a six-year corpus of Bolivian news coverage. The methodology employs vector semantic embeddings and zero-shot classification models to capture signals of discursive escalation prior to the materialization of the roadblocks. Using an expanding walk-forward validation scheme applied over 1,762 days and seven forecasting horizons (H+1 to H+7), seven internal configurations and four external benchmarks were compared, including SARIMA and LightGBM. The results demonstrate that the hybrid configuration (Prophet + NLP, C6) consistently outperforms purely statistical models, achieving an AUC-ROC of 0.677 at H+1 and reducing the Brier Score by 10.9% relative to the baseline temporal model (0.220 vs. 0.247), maintaining a statistically significant error reduction across all evaluated horizons ($p < 0.02$). This research validates that the integration of semantic news signals allows for the detection of social tension peaks not captured by historical inertia, providing a technical tool for risk management in critical transport corridors.

---


### 45. [Risk-Routed Implicit Boundary Refinement for Robust Ultrasound Image Segmentation](https://arxiv.org/abs/2607.21787)

**<font color=#1a73e8>作者：</font>** Jingguo Qu, Xinyang Han, Xiang Wang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical ultrasound (US) image segmentation faces significant challenges due to speckle noise, low-contrast boundaries, acoustic shadowing, and acquisition variation across operators and clinical centers. Although encoder-decoder and transformer-based networks have achieved strong performance, many methods recover boundary details through dense decoders or larger backbones, which may still produce over-smoothed contours or unstable predictions under external distribution shifts. In this article, we propose Risk-routed Implicit Boundary Refinement (RIBR), a compact segmentation framework that uses implicit neural representation as a risk-routed residual correction rather than an unconstrained full-mask predictor. RIBR combines boundary-refinement implicit residuals, risk-routed residual control, and geometry- and speckle-aware boundary regularization to refine uncertain contours while suppressing non-boundary oscillations. Evaluation on nine US datasets covering lymph nodes, breast lesions, thyroid nodules, and prostate shows that RIBR achieves the best overall macro-average and consistently reduces boundary error across grouped and organ-specific comparisons under a compact parameter budget. These findings suggest that controlled implicit residual learning is a practical strategy for resource-constrained and boundary-sensitive US segmentation. Source code is available at this https URL.

---


### 46. [What Happens to Accuracy When Photo Lineups Contain Non-Mated Rank-One Images From Large Galleries?](https://arxiv.org/abs/2607.21792)

**<font color=#1a73e8>作者：</font>** Genesis Argueta, Kevin W. Bowyer, Michael King 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> One-to-many facial identification is commonly used to match a probe image from surveillance video against a gallery of driver's licenses and/or booking photos. The algorithm's rank-one image from the gallery, or a human examiner's selection from the algorithm's top-ranked images, may then be placed in a photo lineup shown to a witness. Witness selection of the gallery image in the photo lineup may then lead directly to the person in the gallery image being arrested. This facial identification process is involved in at least 9 wrongful arrests. This work specifically examines whether the probability of a witness making an incorrect identification increases with the size of the gallery searched. We compare photo lineup accuracy when the "suspect" image is drawn from galleries of 500, 5,000, and 24,000 images. We find that larger galleries increase both the likelihood of a witness making an incorrect identification and their confidence in that (incorrect) identification. These results raise questions of whether an image resulting from such a facial identification process should be used in photo lineups and of whether results of a photo lineup alone should constitute probable cause for arrest.

---


### 47. [QLPO: Quadrant-weighted Sampling for Length-aware Policy Optimization](https://arxiv.org/abs/2607.21793)

**<font color=#1a73e8>作者：</font>** Siwei Chen, Siqi Chen, Xupeng Miao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent large reasoning models often develop long chain-of-thought responses during reinforcement learning (RL), resulting in high inference latency and deployment cost. Existing methods for response length control typically rely on explicit length penalties or additional control modules, which require careful tuning and may compromise reasoning quality. We propose Quadrant-weighted Sampling for Length-aware Policy Optimization (QLPO), a simple resampling-based variant of GRPO that introduces implicit length control without modifying the reward function. QLPO first over-generates candidate responses and then resamples the training group by preserving the empirical correct/incorrect ratio while favoring short correct responses and long incorrect responses. This reshapes the training distribution and implicitly encourages shorter model outputs. Across models ranging from 1.5B to 32B parameters, including both base models and strong reasoning models, QLPO consistently improves the accuracy-length trade-off. It reduces response length by 30% to 70% while preserving reasoning performance. These results suggest that structured resampling provides an effective and robust approach to efficient reasoning.

---


### 48. [Adversarial Prompts for Acceptance Collapse in Speculative Decoding](https://arxiv.org/abs/2607.21804)

**<font color=#1a73e8>作者：</font>** Run Wang, Chaoyi Zhou, Xi Liu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Lossless acceleration schemes, such as speculative decoding, promise significant inference speedups by relying on dynamic token-level alignment between a draft and a target model. However, this guarantee of semantic equivalence masks a severe operational vulnerability: draft-target alignment can be systematically attacked. In this paper, we introduce ADSD, which, to the best of our knowledge, is the first prompt-suffix attack that collapses verifier acceptance by pushing draft probability mass toward tokens the target is unlikely to accept. ADSD uses Soft-Collapse, a verifier-aligned surrogate derived from the asymmetric speculative acceptance rule, together with a target-preservation objective that discourages obvious task corruption. ADSD successfully generates highly effective adversarial suffixes. On the GSM8K dataset, our attack increases the mean sample time by 62.3% while preserving the task quality. We further show that this vulnerability exists across different domains, speculative decoding strategies, and model architectures.

---


### 49. [Bounding the Causal Impact of ML-assisted Decision-Making via Counterfactual Correctness](https://arxiv.org/abs/2607.21806)

**<font color=#1a73e8>作者：</font>** Jonathan Zhang, Erik Skalnes, Jacob Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predictive machine learning (ML) models are increasingly used to aid human decision-makers across various high-risk domains such as healthcare and criminal justice. There is a growing recognition of the need to evaluate the causal impact of deploying these systems on downstream outcomes, such as patient survival or crime recidivism. Randomized control trials (RCTs) can provide high-quality evidence on the impact of a deployed model, but they run into a challenge: it is often infeasible to run repeated trials when models are updated or retrained to improve predictive performance. In this work, we present a partial-identification approach to using prior RCT data to construct bounds on the causal effect of a new model. The core innovation in our approach is to leverage assumptions relating fine-grained predictive accuracy to downstream outcomes. We do so via two monotonicity assumptions: first, on individual-level `counterfactual correctness' (all else being equal, a correct prediction leads to non-inferior outcomes); and second, on the relation between subgroup predictive performance and outcomes, interpretable as an assumption regarding trust in model outputs. We demonstrate our method with a simulation study, illustrating how incorporating this information can lead to more informative bounds compared to prior work.

---


### 50. [Adaptive Driving Style for SAE Level-2 Driving Automation: Minimizing Preference Mismatch](https://arxiv.org/abs/2607.21819)

**<font color=#1a73e8>作者：</font>** Kumar Akash, Zhaobo Zheng, Teruhisa Misu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Driving style is a key factor in the comfort and acceptance of automated vehicle (AV) features. In SAE Level-2 automation, where the driver must supervise the system and remain ready to intervene, mismatches between the automation's driving style and the driver's preference can reduce trust and trigger takeovers. This paper proposes an adaptive driving-style control framework that minimizes such preference mismatch. In a driving-simulator study, we compare fixed, trust-based, and preference-based adaptation heuristics and analyze their effects on preference mismatch and trust. We then train a driving-preference prediction model and use it in an implicit adaptation policy that selects among bounded driving styles for upcoming events. A validation study shows that the predictive policy achieves equal or lower preference mismatch than comparison baselines, particularly when starting from a less defensive style, while also yielding higher average trust. The results provide a step toward developing human-aware driving automation that can implicitly adapt its driving style to the driver's preferences.

---


> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-169](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
