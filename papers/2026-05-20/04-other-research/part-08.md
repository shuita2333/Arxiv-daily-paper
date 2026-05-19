# 📦 其他研究 | 2026年05月20日

> 本类共 **619** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**351-400**（第 8/13 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-619](./part-13.md)

---

### 351. [Form and Function: Machine Unlearning as a Problem of Misaligned States](https://arxiv.org/abs/2605.17590)

**<font color=#1a73e8>作者：</font>** Kennon Stewart  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We formulate machine unlearning for online L-BFGS as a counterfactual state-alignment problem. Given an actual event stream and a deletion-edited counterfactual stream, the target of unlearning is the optimizer state that would have arisen had the deleted samples never been processed. We introduce state-aware metrics that separately measure parameter error, memory-operator error, combined state error, and update-direction error. The memory metric compares the inverse-Hessian actions induced by the o-L-BFGS memory, rather than treating curvature pairs as of finite influence. Under convexity assumptions, we derive a recursive bound on counterfactual state deviation. We then evaluate a state-aware benchmark of deletion interventions, including memory-only and parameter-only corrections, against an counterfactual oracle model. These results show that unlearning for online L-BFGS is not merely a parameter-correction problem: it requires alignment with a realizable counterfactual optimizer state.

---


### 352. [Error-Decomposed Class-Conditional Fusion for Statistically Guaranteed Hard-Category Robust Perception](https://arxiv.org/abs/2605.17591)

**<font color=#1a73e8>作者：</font>** Guowei Luo, Ziqi Shi, Zhao Xie  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Aggregate object detection metrics inherently mask catastrophic and repeatable failures in operationally critical, long-tail minority classes. This paper formally defines this pervasive vulnerability as the Hard-Category Reliability Problem (HCRP): the fundamental architectural challenge of strictly rectifying vulnerable categories without compromising the performance boundaries of stable classes under stringent protocols. To systematically dismantle this limitation, we propose Error-Decomposed Class-Conditional Fusion (ED-CCF), an elegant decision-layer inference framework. Diverging from heuristic global post-processing, ED-CCF projects predictions into a sophisticated quad-state error taxonomy, dynamically activating calibration pathways exclusively upon rigorous empirical justification. On a highly constrained 600-image validation benchmark, isolating cz as the critical vulnerability (HCEC=0.86, BSR=0.14), our framework achieves a targeted breakthrough: it elevates cz mAP50 from 0.089343 to 0.109353 (a massive +22.4% relative surge) while flawlessly preserving the Pareto optimality of global stability (raising all mAP50 from 0.581925 to 0.584864). Backed by exhaustive validation across 50 paired subset trials demonstrating an overwhelming 96% win rate and strict Bonferroni-corrected Wilcoxon significance (p<0.05), this work fundamentally redefines output-level fusion as an auditable, statistically guaranteed paradigm for safety-critical visual perception.

---


### 353. [Venom: A PyTorch Generative Modeling Toolkit](https://arxiv.org/abs/2605.17605)

**<font color=#1a73e8>作者：</font>** Liang Yan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern generative modeling has grown into a broad collection of related but often separately implemented paradigms, including denoising diffusion models, score-based stochastic differential equations, flow matching, variational autoencoders, normalizing flows, adversarial models, and energy-based models. For newcomers, this fragmentation makes it difficult to compare training objectives, inference procedures, sampling algorithms, and conditioning mechanisms within a single coherent codebase. We introduce V ENOM, an educational PyTorch toolkit that implements representative generative modeling families under a unified, MNIST-first interface. V ENOM emphasizes breadth, readability, reproducible entry points, and consistent training and sampling APIs rather than large-scale performance engineering. The package currently includes diffusion and score-based models, flow matching and one-step generators, variational autoencoders, normalizing flows, generative adversarial networks, and energy-based models. It provides separate training and sampling scripts, classifier and classifier-free guidance examples, bilingual tutorial notebooks, and a model-family organization that supports teaching, prototyping, and lightweight benchmarking.

---


### 354. [The Neural Tangent Kernel for Classification](https://arxiv.org/abs/2605.17606)

**<font color=#1a73e8>作者：</font>** Jonathan Plenk, Sergio Calvo-Ordonez, Alvaro Cartea 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In wide neural networks, the Neural Tangent Kernel (NTK) remains approximately constant during training, providing a powerful theoretical tool for studying training dynamics, generalization, and connections to kernel methods. However, this theory is largely restricted to regression losses. It was previously thought that training on a classification loss, or more generally losses involving nonlinear output transformations, breaks this property, leading to divergent logits and a breakdown of the linearization. In this paper, we extend NTK theory to classification by identifying conditions under which wide neural networks remain in the lazy training regime. We show that parameter-space regularization ensures a constant NTK during training for cross-entropy loss, while in the absence of regularization the regime is recovered when targets are non-degenerate, i.e. when all classes have strictly positive probability. Under these conditions, training is well-approximated by the linearized model, yielding an explicit characterization of the solution in terms of the NTK. We further analyze the distribution of trained predictors induced by random initialization and relate this notion of model uncertainty to Bayesian methods.

---


### 355. [Adaptive Generate-Rank-Verify: Inference-Time Search with Costly Verification](https://arxiv.org/abs/2605.17609)

**<font color=#1a73e8>作者：</font>** Shaddin Dughmi, Mahdi Haghifam, Yusuf Hakan Kalayci  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many inference-time language-model pipelines combine a cheap reward signal with an expensive verifier, such as exact answer checking in mathematical reasoning or hidden-test execution in code generation.
We formalize this setting using a learning-theoretic lens as generative active search: a cost-sensitive first-positive search problem in which a policy adaptively samples candidates from an unknown distribution, observes cheap scores, and pays for verifier labels until it finds a positive example. For a fixed prompt, the generator and reward model induce two unknown objects: a distribution over reward scores and a score-conditioned success function. When these quantities are known, we characterize the distribution-aware optimal policy using a dynamic programming approach. In the realistic and practical setting where both the score distribution and success function are unknown, we propose ADAP, a shellwise adaptive generate-rank-verify algorithm that progressively increases the number of sampled responses and top-ranked verifications. Under the monotonicity assumption that higher reward scores are no less likely to pass verification, we show that ADAP achieves expected cost within a constant factor of the distribution-aware optimum. We complement this result with learning-theoretic lower bounds, based on a centered star number, showing that structural assumptions on the score--label relationship are necessary. Experiments on mathematical reasoning and competitive programming validate the predicted advantage over both fixed non-adaptive policies and difficulty-adaptive baselines.

---


### 356. [GraphMind: From Operational Traces to Self-Evolving Workflow Automation](https://arxiv.org/abs/2605.17617)

**<font color=#1a73e8>作者：</font>** Yiwen Zhu, Joyce Cahoon, Anna Pavlenko 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Complex operational workflows coordinating personnel, tools, and information are central to enterprise operations, yet end-to-end automation remains challenging due to extensive requirements for human inputs and the inability to adapt over time. We present GraphMind, an end-to-end system that constructs, executes, and evolves action-centric workflow graphs without human effort. The system operates in three phases. First, a scalable offline pipeline extracts structured workflow graphs from large volumes of human resolution traces, capturing problems, actions, and their causal relationships. Second, an online multi-agent traversal engine navigates the graph to dynamically construct and execute workflows, combining graph-guided retrieval with LLM-driven reasoning at each step. Third, Adaptive Traversal Reinforcement (ATR) reinforces successful traversal paths and decays stale elements. This closed-loop mechanism enables the graph to self-optimize and adapt to shifting operational conditions. GraphMind has been deployed across four production cloud database services for incident investigation. Evaluated on production data, the system substantially outperforms a Trace-RAG baseline in mitigation reach, groundedness, and diagnostic throughput, scoring 4.95/5 in blind expert review. The ATR layer provides further gains across all metrics, demonstrating that workflow graphs can learn and improve from execution-derived feedback.

---


### 357. [Prediction of Challenging Behaviors Associated with Profound Autism in a Classroom Setting Using Wearable Sensors](https://arxiv.org/abs/2605.17618)

**<font color=#1a73e8>作者：</font>** Yadhu Kartha, Conor Anderson, Jenny Foster 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autism Spectrum Disorder (ASD) is characterized by challenges with social interaction and communication and by restricted or repetitive patterns of thought and behavior, with significant variability in presentation. Approximately a quarter of children with ASD are classified as having profound autism, who often exhibit challenging behaviors, such as self-injurious behavior, aggression, elopement, or pica, that pose serious safety risks and disrupt learning in educational settings. Prior work has applied wearable sensors and machine learning to detect challenging behaviors, but has been largely confined to controlled laboratory environments. This work demonstrates that predicting challenging behavior episodes is feasible in a real-world special education classroom. We collected approximately 110.7 hours of labeled multimodal wearable data comprising accelerometry, electrodermal activity (EDA), and skin temperature from 9 children and young adults aged 10 to 21 years across standard classroom sessions. We fine-tuned state-of-the-art foundation models for multimodal wearable time-series analysis and show that challenging behavior episodes can be predicted up to 10 minutes in advance with an AUC-ROC of 0.78. These results establish a concrete foundation for developing proactive in-class intervention systems that enable teachers to minimize the safety risks of challenging behaviors in special education classrooms

---


### 358. [SynVA: A Modular Toolkit for Vessel Generation and Aneurysm Editing](https://arxiv.org/abs/2605.17620)

**<font color=#1a73e8>作者：</font>** Marten J. Finck, Niklas C. Koser, Sarker M. Mahfuz 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Intracranial aneurysms (IAs), characterized by unpredictable growth and risk of rupture, are a major cause of stroke and can lead to life-threatening hemorrhages with high mortality and long-term disability. With aging populations, the incidence and overall burden of cerebrovascular diseases are expected to increase, highlighting the need for scalable approaches to analyze complex medical data and improve population-level understanding of these conditions. While digital twins and deep learning offer promising avenues for improving diagnosis, prognosis, and treatment, their effectiveness is limited by the scarcity of large-scale, high-quality medical data and corresponding labels. We present Synthetic VAsculature (SynVA), a modular toolkit for vascular mesh generation and anatomically consistent aneurysm synthesis. SynVA combines novel flow-matching-based methods for generating healthy vessel meshes with learning-based approaches for anatomy-conditioned aneurysm mesh generation - aneurysms are computed from pre-existing vascular geometries rather than being generated in isolation. In addition, we introduce the SynVA procedural model for vascular and aneurysm synthesis based solely on physiological principles and statistical priors, which enables the generation of large-scale datasets (e.g., for the training of mesh-based generative models). To this end, we release a dataset of 50,000 fully labeled mesh samples for a variety of downstream vision tasks, such as semantic segmentation. Extensive quantitative and qualitative evaluations demonstrate that SynVA generates realistic vessel geometries and anatomically plausible aneurysms. Specifically, our experiments indicate that some methods produce aneurysm shapes more aligned with expert human perception while others perform better on quantitative similarity metrics with reconstructions of real aneurysms.

---


### 359. [Multi-task learning on partially labeled datasets via invariant/equivariant semi-supervised learning](https://arxiv.org/abs/2605.17624)

**<font color=#1a73e8>作者：</font>** Miquel Martí i Rabadán, Alessandro Pieropan, Hossein Azizpour 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We investigate the potential of invariant and equivariant semi-supervised learning for addressing the challenges of training multi-task models on partially labeled datasets with differently structured output tasks. Specifically, we use the popular FixMatch method for invariant semi-supervised learning and its equivariant extension Dense FixMatch. We evaluate their performance on the Cityscapes and BDD100K datasets in the context of the prevalent object detection and semantic segmentation tasks in computer vision. We consider varying sizes of the subsets annotated for each task and different overlaps among them. Our results for both invariant and equivariant semi-supervised learning outperform supervised baselines in most situations, with the most significant improvements observed when fewer labeled samples are available for a task and generally better results for the latter approach. Our study suggests that invariant/equivariant learning is a promising general direction for multi-task learning from limited labeled data.

---


### 360. [Verifier-Guided Code Translation via Meta-Step Decoding](https://arxiv.org/abs/2605.17626)

**<font color=#1a73e8>作者：</font>** Tianyang Zhou, Somesh Jha, Mihai Christodorescu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Test-time scaling is an important mechanism for improving large language models, especially on tasks with deterministic verifiers. Code translation is a canonical example: the source program constrains valid outputs, while compilers, type check- ers, and behavioral checks provide exact pass/fail feedback. Existing approaches typically apply these verifiers only after generation, which is inefficient because early errors corrupt the autoregressive context and are rarely corrected later. We introduce Decoding Time Verification (DTV), a framework that treats structural boundaries as meta steps for verifier-guided decoding. DTV interleaves generation with verifier calls under a state-machine controller that enforces valid prefixes, using structural-boundary checks and structure-aware rollback to prevent error propagation while reducing wasted tokens. We evaluate DTV on C-to-Rust and JavaScript-to-TypeScript translation. Using Qwen3-4B as the primary generator under matched token budgets, DTV improves pass rates from 72.3% to 82.0% on C-to-Rust and from 33.3% to 46.0% on JavaScript-to-TypeScript relative to matched self-refinement baselines, while using fewer tokens per case; the same trend largely transfers to Gemma-4-E4B. In the evaluated cost-matched grid, DTV achieves a more favorable pass-rate-cost tradeoff than post-hoc verification or sampling-based scaling. These results show that verifier-guided decoding is an effective use of inference-time compute for code translation.

---


### 361. [SparseSAM: Structured Sparsification of Activations in Segment Anything Models](https://arxiv.org/abs/2605.17633)

**<font color=#1a73e8>作者：</font>** Hoai-Chau Tran, Chi H. Nguyen, Duy M. H. Nguyen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The Segment Anything Model (SAM) achieves strong open-vocabulary segmentation, but its ViT-based image encoders dominate inference latency and memory. Existing activation compression methods, such as token merging, reduce the token length to process, yet introduce non-trivial runtime overhead and encounter catastrophic quality drop under high compression. Other methods applying Sparse Attention focus on attention alone, leaving the MLP fully dense and capping achievable speedup. We propose SparseSAM, a (i) training-free structured sparsification framework that jointly accelerates attention and MLP layers while preserving token identity. SparseSAM introduces (ii) Stripe-Sort Attention, which uses a deterministic Z-order permutation to transform dense attention into static hardware-friendly sparse patterns, eliminating dynamic masking overhead. SparseSAM further introduces a (iii) Residual-Consistency MLP that routes only informative tokens through the MLP while propagating remaining tokens through the residual pathway. Across four segmentation benchmarks, SparseSAM loses only 0.004 mIoU at a 0.4 density and 0.021 mIoU at 0.3, a 2.10x reduction in accuracy loss versus token merging advances, while achieving 2x faster inference and 2.8x memory reduction.

---


### 362. [AI Agents May Always Fall for Prompt Injections](https://arxiv.org/abs/2605.17634)

**<font color=#1a73e8>作者：</font>** Sahar Abdelnabi, Eugene Bagdasarian  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Prompt injection is the most critical vulnerability in deployed AI agents. Despite recent progress, we show that the prevailing defense paradigm (data-instruction separation) both fails to detect attacks that operate through contextual manipulation and degrades contextually appropriate behavior. We then recast prompt injection via the lens of Contextual Integrity (CI), a privacy theory that judges information flow compliance with contextual norms. This explains types of attacks that current defenses attempt to patch and predict advanced ones future agents will face. We develop unique benign and attack scenarios that force an agent to violate the norms by (1) misrepresenting the flow, (2) manipulating norms, or (3) mixing multiple flows. This reframing suggests an impossibility result: an adversary can always construct a context under which a blocked flow appears legitimate, or a defender who tightens norms will block genuinely legitimate flows. Our findings suggest that current research addresses a shrinking fraction of future attack surfaces. Instead, through CI, we offer a principled framework for evaluating context-sensitive failures, and designing CI-aware alignment for the frontier autonomous agents.

---


### 363. [WebGameBench: Requirement-to-Application Evaluation for Coding Agents via Browser-Native Games](https://arxiv.org/abs/2605.17637)

**<font color=#1a73e8>作者：</font>** Wenyu Zhang, Guoliang You, Tianlun 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Coding agents are increasingly used as application builders, yet many evaluations still focus on source code, repository-level tests, or intermediate traces rather than the delivered application. We introduce WebGameBench, a requirement-to-application benchmark that evaluates whether coding agents can turn a frozen Structured WebGame Specification into a browser-accessible game. Browser-native games provide a compact but behavior-dense testbed: even simple games require coordinated input handling, spatial mapping, rule execution, state transitions, terminal conditions, restart behavior, and visible feedback. In WebGameBench, each generated artifact is built, served, and exposed as a browser-accessible application under a unified deployment protocol. A runtime evaluator then interacts with the delivered game in a real browser and assigns a three-way label: EXCELLENT, USABLE, or UNUSABLE. On a human-reviewed subset, the runtime label is broadly aligned with human gameplay review under the Usable-rate criterion. Across 111 tasks, 12 coding agents, and 14 evaluation configurations, WebGameBench separates current systems: the best configuration reaches a 76.9% usable rate but only a 20.2% excellent rate. This gap shows that crossing the minimum playable-delivery threshold is still far from complete requirement satisfaction. To our knowledge, WebGameBench is the first requirement-to-application benchmark for browser-native game delivery that validates delivered-application runtime labels against independent human gameplay review under the Usable-rate criterion.

---


### 364. [TouchMap-OR: Multi-View 3D Mapping of Hand-Surface Contacts](https://arxiv.org/abs/2605.17638)

**<font color=#1a73e8>作者：</font>** Sophokles Ktistakis, Rui Wang, Bastian Grande 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hand-surface interactions between clinicians, patients, and medical equipment play a central role in pathogen transmission during medical procedures. However, these interactions remain largely unobserved, as current infection-prevention practices rely on manual observation and cannot reconstruct detailed contact histories. In this work we formulate the problem of identity-resolved hand-surface interaction reconstruction in operating rooms and introduce TouchMap-OR, a multi-view RGB-D vision system that models clinicians, articulated hand geometry, and the semantic structure of the clinical environment to infer when and where contacts occur. The system reconstructs globally consistent multi-person 3D skeleton tracks across cameras while estimating articulated MANO hand meshes from RGB observations aligned to depth data. Multi-view hand reconstructions are fused and associated with tracked clinicians to obtain consistent left and right hand trajectories. A semantic 3D model of the operating room is built from multi-view segmentation and depth fusion, enabling reconstructed hand trajectories to be mapped to specific surfaces, including medical equipment, movable objects, and patient body sites. Temporal hand-surface proximity is used to infer contact episodes describing which clinician touched which surface and when. We evaluate TouchMap-OR on recordings from three real anesthesia inductions with manually annotated contact events. TouchMap-OR achieves 0.75 binary contact F1, outperforming tracking-based baselines while maintaining comparable multi-person tracking accuracy and achieving 0.96 identity attribution accuracy.

---


### 365. [Temporal Decay of Co-Citation Predictability: A 20-Year Statute Retrieval Benchmark from 396M Ukrainian Court Citations](https://arxiv.org/abs/2605.17639)

**<font color=#1a73e8>作者：</font>** Volodymyr Ovcharov  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Co-citation structure is widely assumed to provide stable retrieval signal in legal information systems. We test this assumption longitudinally by constructing UA-StatuteRetrieval, a benchmark that measures co-citation predictability across 20 annual snapshots (2007-2026) of 396 million codex citations from 101 million Ukrainian court decisions. Using a leave-one-out protocol over the full bipartite citation graph, we find that Adamic-Adar MRR declines 33% on a fixed set of articles (from 0.43 to 0.29) and 47% under a train/test temporal split (from 0.51 to 0.27) confirming genuine temporal decay rather than compositional shift or evaluation artifact. The decay is non-uniform: criminal procedure maintains stable co-citation patterns (MRR ~0.40), while civil law degrades from 0.35 to 0.15, coinciding with the 2017 judicial reform. Hub articles (>100K citations) resist decay, but mid-frequency articles (1K-10K) -- the practical retrieval frontier lose half their predictability. A BM25 text baseline decays even faster (31%), and embedding drift analysis with E5-large reveals a 4.3% semantic shift in how articles are cited, providing a mechanistic explanation for the observed decay. The benchmark is released at this https URL.

---


### 366. [TabKDE: Simple and Scalable Tabular Data Generation with Kernel Density Estimates](https://arxiv.org/abs/2605.17642)

**<font color=#1a73e8>作者：</font>** Meysam Alishahi, Yan Zheng, Junpeng Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular data generation considers a large table with multiple columns -- each column comprised of numerical, categorical, or sometimes ordinal values. The goal is to produce new rows for the table that replicate the distribution of rows from the original data -- without just copying those initial rows. The last 4 years have seen enormous progress on this problem, mostly using computational expensive methods that employ one-hot encoding, VAEs, and diffusion.
This paper describes a new approach to the problem of tabular data generation. By employing copula transformations and modeling the distribution as a kernel density estimate we can nearly match the accuracy and leakage-avoidance achievements of the previous methods, but with almost no training time. Our method is very scalable, and can be run on data sets orders of magnitude larger than prior state-of-the-art on a simple laptop. Moreover, because we employ kernel density estimates, we can store the model as a coreset of the original data -- we believe the first for generative modeling -- and as a result, require significantly less space as well. Our code is available here: \url{this https URL}

---


### 367. [SAPO: Step-Aligned Policy Optimization for Reasoning-Based Generative Recommendation](https://arxiv.org/abs/2605.17648)

**<font color=#1a73e8>作者：</font>** Zaiyi Zheng, Guanghui Min, Yaochen Zhu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative recommendation treats next-item prediction as autoregressive item-identifier generation. Specifically, items are encoded as semantic identifiers (SIDs), which are short coarse-to-fine token sequences whose early tokens capture broad semantics and later tokens refine them. Recent work augments this paradigm with reasoning traces and optimizes them via reinforcement learning with verifiable rewards, typically outcome-reward algorithm with exact-match feedback on the generated SID. However, in large-catalog recommendation, exact-match feedback on the generated SID only reports whether the final item is correct; when a generated SID mismatches, outcome-reward cannot identify which SID-token prediction caused the mismatch and may penalize matched SID-token positions together with the mismatched position. We identify that the natural unit of credit assignment in this setting is a single reasoning step (one thinking block paired with one SID token). We instantiate this idea in SAPO (Step-Aligned Policy Optimization): rather than broadcasting one advantage to the whole response, SAPO computes a separate group-relative advantage for each reasoning step and applies it only to the corresponding thinking block and SID token. Across three real-world recommendation datasets, SAPO stabilizes reinforcement-learning training and consistently improves over existing generative recommendation baselines, with the largest gains where sparse exact-match feedback makes reasoning-step credit assignment important. Our results suggest that reinforcement-learning objectives for structured generation should mirror the decoder's own decomposition of the output.

---


### 368. [Reservation Based Smart Parking Management](https://arxiv.org/abs/2605.17650)

**<font color=#1a73e8>作者：</font>** Giacomo Cabri, Manuela Montangero, Filippo Muzzini 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> In the framework of Smart Cities and Intelligent Transportation Systems (ITS), efficient parking management is essential to reduce urban congestion and emissions. However, current reservation-based systems often encounter a scenario in which users find their reserved slot occupied by a previous occupant who failed to vacate on time ("No PARK" situation). This paper introduces a dual-mechanism architecture designed to enhance system reliability. A Reservation Module uses a dynamic size buffer of non-reservable slots to grant parking availability. A reputation-based Reward System exploits a "star-based" metric to incentivize punctual departures through financial penalties and access restrictions. The simulations conducted with the SUMO urban simulator are promising, showing that the dynamic buffer strategy provides a better tradeoff between parking availability and reservation success. By progressively adapting to users behavior, the proposed system mitigates "NO PARK" instances and improves resource utilization, significantly enhancing urban viability. Index Terms-Smart City, Intelligent transportation systems, Parking, Reservation systems, V2I, Reputation-based mechanisms, Smart Parking

---


### 369. [Counterfactual Explanations Under Concept Drift](https://arxiv.org/abs/2605.17651)

**<font color=#1a73e8>作者：</font>** Marcin Kostrzewa, Jerzy Stefanowski, Maciej Zięba  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Counterfactual explanations (CFEs) provide actionable recourse, but most methods assume a static framework with fixed data and a trained classifier. This assumption breaks in evolving data environments, such as data streams, where online models are repeatedly updated under concept drift. We identify CFE maintenance in this setting as a previously overlooked problem: explanations that are valid when generated may silently become invalid as the model evolves, including robust CFEs, which are not designed for continuous drift. We propose a lightweight, model-agnostic update scheme that repairs existing CFEs using local sampling to estimate validity and plausibility directions while preserving proximity to the original instance. Experiments on synthetic drifting streams show that initially created CFEs rapidly lose validity, whereas maintained CFEs preserve validity and local plausibility at a lower cost than repeated regeneration.

---


### 370. [Beyond Transcripts: Iterative Peer-Editing with Audio Unlocks High-Quality Human Summaries of Conversational Speech](https://arxiv.org/abs/2605.17652)

**<font color=#1a73e8>作者：</font>** Kaavya Chaparala, Thomas Thebaud, Jesús Villalba López 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> There are not enough established benchmarks for the task fo speech summarization. Creating new benchmarks demands human annotation, as LLMs could embed systemic errors and bias into datasets. We test ten annotation workflows varying input modality (audio, transcript, or both) and the inclusion of editing (self or peer-editing) to investigate potential quality tradeoffs from using human annotators to summarize audio. We compare human audio-based summaries to human transcript-based summaries to track the impact of the different information modalities on summary quality. We also compare the human outputs against four LLM benchmarks (three text, one audio) to examine whether human-written summaries are less informative than highly fluent automated outputs. We find that audio-based summaries are less informative and more compressed than transcript summaries. However, iterative peer-editing with audio mitigates this difference, enabling audio-based summaries to be as informative as their transcript counterparts and LLM summaries. These findings validate iterative peer-editing among human annotators for the creation of benchmarks informed by both lexical and prosodic information. This enables crucial dataset collection even in setting where transcripts are unavailable.

---


### 371. [MUIAnno: An Expert-Annotated Dataset and Evaluation Benchmark for Mobile UI Understanding](https://arxiv.org/abs/2605.17656)

**<font color=#1a73e8>作者：</font>** Athar Parvez, Muhammad Jawad Mufti, Muqaddas Gull 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Understanding mobile user interfaces is important for building intelligent systems such as automation tools, accessibility solutions, and UI-aware agents. However, progress in this area is still limited by the lack of high-quality datasets that reflect real-world mobile applications and include reliable annotations. In this work, we introduce MUIAnno, a publicly available expert-annotated dataset for mobile UI understanding, collected from a diverse set of applications across multiple categories available on the iTunes platform. Each app was manually explored to capture representative UI screens, resulting in a collection that reflects a wide range of layouts and design patterns found in practice. To ensure annotation quality, we developed a custom web-based tool that allows UI/UX experts to label interface elements through a simple drag-and-drop process and generate structured annotations in JSON format. MUIAnno includes detailed annotations of common UI components such as buttons, input fields, navigation elements, and other key interface elements. In addition to presenting the dataset, we also provide benchmark experiments for UI element detection along with baseline results, offering a starting point for future research. We believe MUIAnno can support further work in mobile UI understanding and help improve systems that rely on accurate interpretation of interface elements.

---


### 372. [When a Zero-Shooter Cheats: Improving Age Estimation via Activation Steering](https://arxiv.org/abs/2605.17658)

**<font color=#1a73e8>作者：</font>** Erik Imgrund, Pia Hanfeld, Klim Kireev 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Different age-related regulations have been proposed to protect minors from harmful content and interactions online. Automated age estimation is central to enforcing such regulations, and vision-language models (VLMs) achieve state-of-the-art performance on this task. However, we find that the zero-shot nature of VLM-based age estimation produces an unexpected side effect we call the identity shortcut: Instead of estimating age from visual features, VLMs tend to identify the depicted person and infer their age from memorized knowledge. This phenomenon leads to substantially incorrect predictions when non-celebrities are misidentified as celebrities. It also produces deceptively high robustness to noise and adversarial perturbations on celebrity images, which dominate popular benchmarks. To mitigate this, we propose an activation steering method that suppresses the shortcut by intervening on the hidden states of the VLM. This method improves age estimation accuracy for both memorized and unseen identities, reducing mean absolute error by up to 25% across popular benchmarks.

---


### 373. [Bug or Feature$^2$: Weight Drift, Activation Sparsity, and Spikes](https://arxiv.org/abs/2605.17659)

**<font color=#1a73e8>作者：</font>** Egor Shvetsov, Aleksandr Serkov, Shokorov Viacheslav 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The design of modern neural architectures has converged through incremental empirical choices, yet the mechanisms governing their training dynamics remain only partially understood. We identify and analyze a negative weight drift induced by the interaction between standard losses and positively biased activation functions. We prove that under MSE or cross-entropy loss, the gradient with respect to positive pre-activations is non-negative in expectation at initialization, driving downstream weights toward negative values during early training. The drift is intrinsic to optimization rather than data, and persists across architectures (MLP, ResNet, ViT, GPT-nano, MP-SENe) and asymmetric activation functions (ReLU, GELU, SiLU). Coupled with ReLU, weight drift produces activation sparsity reaching up to 90\% in GPT-nano. We characterize the sparsity-accuracy tradeoff across 79 configurations and identify a sharp accuracy cliff above $\sim$70\% activation sparsity. While ReLU$^2$ achieves a good sparsity--accuracy ratio in GPT-nano, it pathologically amplifies identified activation spikes in intermediate transformer layers. Clipping resolves this while preserving the representational benefits of squaring: clipped ReLU$^2$ outperforms its unclipped version, and GELU$^2$ achieves the lowest validation loss on GPT-nano. Code is available at this https URL.

---


### 374. [Deep learning-based compression of giga-resolution whole slide images](https://arxiv.org/abs/2605.17668)

**<font color=#1a73e8>作者：</font>** Maren Høibø, Etienne Gaucher, Ingerid Reinertsen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Implementation of digital pathology leads to an increased number of whole slide images (WSIs). The large size of WSIs is challenging. Today, WSIs are compressed with codecs like JPEG resulting in several gigabytes per WSI, and large amounts of space are wasted storing glass. In this study, deep learning-based tissue segmentation for glass removal, and deep learning compression methods were explored and compared with JPEG, JPEG-2000 and JPEG-XL.
Image pyramids (N=21) with intact glass, glass replaced by single-colored pixels, and glass replaced by zero-byte tiles were created and compressed with JPEG, JPEG-XL and a deep learning model. Additionally, several compression models were evaluated on a tissue patch dataset and compared with JPEG, JPEG-2000 and JPEG-XL.
Removing glass reduced file sizes considerably for JPEG and JPEG-XL. Deep learning-based image compression reduced the WSI size by 43-72% compared to JPEG compression, whereas deep learning-based glass removal reduced the WSI size by 0.3-33%, and 6-62% using only single-colored pixels and removing all-glass tiles, respectively. Combining the two gave a small improvement to a 44-80% total size reduction which indicates that deep learning-based image compression is able to efficiently compress glass tiles, whereas JPEG is not. On the tissue patch dataset, the best deep learning-based compression models saved on average ~35-40% per patch compared to JPEG, while keeping an average SSIM above 0.95, whereas JPEG-XL and JPEG-2000 saved 17% and 14%, respectively while keeping an SSIM of 0.96. However, the deep learning models had higher decompression times than JPEG and JPEG-XL.

---


### 375. [PEIRA: Learning Predictive Encoders through Inter-View Regressor Alignment](https://arxiv.org/abs/2605.17671)

**<font color=#1a73e8>作者：</font>** Michael Arbel, Basile Terver, Jean Ponce  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Non-contrastive self-supervised learning (SSL) is an effective framework for predictive representation learning, but popular (and in practice effective) methods such as SimSiam, BYOL, I-JEPA or DINO, which rely on a form of self-distillation to train a teacher-student network, remain poorly understood as they typically do not minimize a well-defined objective. We analyze the dynamics of a variant of the Joint Embedding Predictive Architecture (JEPA) using a regularized linear regressor to predict the learned representations of two views of the data from one another, and fully characterize its stability: non-collapsed stable equilibria align with leading nonlinear canonical correlation subspaces, while collapsed equilibria may also be stable attractors. Motivated by this result, we introduce PEIRA, a non-contrastive SSL method with an explicit objective defined through the trace of the optimal linear regressor. We show that its only stable equilibria are nontrivial global minimizers and recover the same canonical correlation subspaces, with regularization selecting the effective dimension. Experiments on ImageNet-1K and CIFAR-10 show PEIRA is competitive with VICReg and LeJEPA baselines, and qualitative empirical results support the theory.

---


### 376. [A simple approach for biometrics: Finger-knuckle prints recognition based on a Sobel filter and similarity measures](https://arxiv.org/abs/2605.17673)

**<font color=#1a73e8>作者：</font>** E. O. Rodrigues, T. M. Porcino, Aura Conci 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The objective of this work is to propose a novel methodology for the finger knuckle print recognition, which is essentially a digital photo of the finger-knuckle region. We have employed very simple concepts of visual computing such as a filter based on the Sobel operator for finding edges and a simple noise reduction algorithm. These operations are exceptionally fast and produce binary images, which are very efficient to process and to store. Furthermore, alongside this preprocessing, some similarity measures were also regarded and evaluated for the task. After preprocessing an input finger it is compared to all the images of fingers in the dataset, one by one. We have obtained up to 17.02% of successful recognitions (true positive rate) with a large dataset.

---


### 377. [GEM: Gaussian Evolution Model for Occupancy Forecasting and Motion Planning](https://arxiv.org/abs/2605.17682)

**<font color=#1a73e8>作者：</font>** Cheng Chen, Hao Huang, Saurabh Bagchi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Future 3D semantic occupancy forecasting and motion planning are central to autonomous driving, as they require models to reason about how surrounding scenes evolve and how the ego vehicle should act. Existing occupancy world models commonly discretize scenes into latent embeddings, volumetric features, or quantized tokens, and forecast future states through fixed-step autoregressive generation. This limits temporal flexibility, obscures scene evolution, accumulates errors over long horizons, and poorly matches the continuous-time dynamics of real driving scenes. We propose GEM, a Gaussian Evolution Model for non-autoregressive occupancy world modeling, where driving scenes are represented as explicit continuous 4D Gaussian primitives with learned dynamics. Instead of rolling out future occupancy states step by step, GEM directly queries the Gaussian world representation at arbitrary timestamps and splats the corresponding conditional 3D Gaussians into semantic occupancy volumes. This enables efficient forecasting over the full horizon while retaining a compact and interpretable scene representation. By decoupling spatial geometry, temporal support, and primitive motion, GEM makes the predicted world easier to inspect, as each primitive's evolution can be followed continuously over time. The same representation also supports motion planning by predicting future ego trajectories from the learned Gaussian world. Extensive experiments show that GEM achieves state-of-the-art future semantic occupancy forecasting and strong motion planning performance, while providing flexible temporal querying.

---


### 378. [Attention-Guided Fusion of 1D and 2D CNNs for Robust ECG-Based Biometric Recognition](https://arxiv.org/abs/2605.17685)

**<font color=#1a73e8>作者：</font>** Arioua, Islameddine, Benzaoui 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Electrocardiogram (ECG)-based biometric recognition has emerged as a promising solution for secure authentication and liveness detection. However, most existing methods rely on unimodal deep learning architectures that independently process either one-dimensional (1D) temporal signals or two-dimensional (2D) time-frequency representations, limiting robustness and generalization. To address this issue, this paper proposes a hybrid framework integrating 1D and 2D convolutional neural networks (CNNs) within a unified end-to-end architecture. The 1D branch extracts temporal and morphological features from raw ECG signals, while the 2D branch captures discriminative spectral information from time-frequency representations. An attention-guided fusion mechanism dynamically weights both modalities according to input characteristics, overcoming the limitations of conventional static fusion strategies.
The framework was evaluated on three benchmark datasets (ECG-ID, MIT-BIH, and PTB), including healthy subjects and patients with cardiac pathologies, achieving identification accuracies of 99.56%, 100.00%, and 99.89%, respectively. To assess long-term biometric permanence, experiments were also conducted on the multi-session Heartprint dataset spanning ten years. The proposed approach achieved same-session accuracies of 98.54% (S1), 99.09% (S2), 94.93% (S3R), and 96.08% (S3L), while cross-session evaluations reached 56.33% (S1-S2) and 53.27% (S2-S3R), demonstrating the ability to capture stable biometric signatures over time. The optimal configuration combines InceptionTime for 1D processing, ResNet-34 for 2D analysis, and attention-based fusion. Ablation studies confirm that the proposed attention mechanism consistently outperforms conventional fusion approaches. Overall, the proposed framework provides a robust, scalable, and high-performance solution for ECG biometric recognition.

---


### 379. [Brain-inspired spike-timing plasticity for reliable label-efficient event-camera vision](https://arxiv.org/abs/2605.17686)

**<font color=#1a73e8>作者：</font>** Mohamad Yazan Sadoun, Sarah Sharif, Yaser Mike Banad  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deploying event-camera object detectors is constrained by per-frame labeling requirements and GPU compute demands. This work introduces three local spike-timing-dependent plasticity (STDP) modules, including sequence, candidate, and tube-reliability modules, that operate on a single CPU thread without GPU support. On the FRED drone benchmark, the proposed framework spans three label-efficient supervision tiers. A strict zero-label detector achieves 53.8% mAP@30, approximately 26 train-derived bits achieve 76.9% mAP@30, and an STDP candidate-reliability gate achieves 78.60 +/- 0.42% mAP@30. Under acquisition-order drift, the cohort gate outperforms streaming k-means by 2.03 +/- 0.58 percentage points across 20 of 20 positive trials, while a no-drift control falsifies the effect. STDP reduces single-model variance by 6.6 times, and one trained gate matches a 44-seed ensemble bound. The gate transfers to Intel Lava with 89% top-2 agreement. On the EVUAV benchmark, a tube-level STDP layer reduces false alarms from 454 to 331e-4 at Pd >= 88%. Dense gradient-trained detectors cannot provide this combination of gradient training, dense matrix multiplication, and local plasticity-free operation by construction.

---


### 380. [Exact Convex Reformulations of Linear Neural Networks via Completely Positive Lifting](https://arxiv.org/abs/2605.17692)

**<font color=#1a73e8>作者：</font>** Karthik Prakhya, Alp Yurtsever  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We show that the training problem of a deep linear neural network under the squared loss admits an exact convex reformulation in a lifted space over a generalized completely positive cone. The reformulation has the same optimal value as the original nonconvex problem and is linear in the lifted variables, with all nonconvexity encoded in the cone constraint. Its ambient lifted dimension depends only on the input and output dimensions, independent of the network depth and the number of data points, and the bottleneck width enters only through scalar constraints. The construction proceeds by reducing the multilayer parameterization to a bilinear factorization, lifting it to a rank-constrained semidefinite program, expressing the rank constraint via a complementarity condition, and applying a completely positive lifting. While the resulting formulation is computationally intractable in general, it gives an exact conic representation of the nonconvexity induced by linear factorization and connects linear neural network training with copositive programming.

---


### 381. [LITE-SOC: Lightweight Security Operations Center Simulator for Cybersecurity Education](https://arxiv.org/abs/2605.17703)

**<font color=#1a73e8>作者：</font>** Martin Higgins, Shawn Thompson, Cherry Mangla  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This innovative practice WIP paper describes \emph{LITE-SOC}, a lightweight web-based Security Operations Center (SOC) simulator designed for instructor-led cybersecurity education. SOC analysts must triage large volumes of alerts, separate genuine threats from false positives, and communicate decisions under time pressure. Recreating this environment in the classroom is difficult and often impractical for institutions without access to cyber ranges or enterprise security infrastructure. LITE-SOC was developed to provide a simpler alternative. The platform generates continuous streams of synthetic SOC events and offers separate student and instructor views with visualization tools, event annotation, and region-based chat. Instructors control the pacing of the exercise and can inject targeted incidents to guide the scenario. The goal is to give students a practical introduction to SOC workflows such as triage, prioritization, and decision-making without requiring a full operational SOC environment. The platform is intended for use in guided classroom exercises where students collaboratively investigate alerts and practice real-time triage and communication.

---


### 382. [Toy Combinatorial Interpretability Models Reveal Lottery Tickets in Early Feature Space](https://arxiv.org/abs/2605.17704)

**<font color=#1a73e8>作者：</font>** Alon Bebchuk, Nir Shavit  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The lottery ticket hypothesis posits that dense networks contain sparse subnetworks, ``winning tickets,'' that, when rewound to their initial weights and retrained in isolation, match the performance of the full model. We ask a more mechanistic question: what internal object does a winning ticket preserve? We work in a combinatorial, clause-structured toy setting that admits an interpretable feature-space representation with well-defined combinatorial distances between features. We show that winning tickets in weight space correspond to precursor locations in feature space that are already near, at initialization, to the final feature-channel codes. Dense SGD resolves these locations through structured selection: proximal locations either converge to final codes or are rejected, with rejection concentrated at more crowded neurons, implicating competition under superposition. A winning ticket is thus a family of compatible code locations that jointly balance proximity to final codes with low inter-feature interference. Sparse retraining often re-expresses the same clause/template family on a different row, so the preserved object is family-level rather than microscopic row identity. We validate this account with lightweight probes based on feature-space distance and motion; in our setting, these probes frequently outperform established weight-based ticket discovery methods in both accuracy and exact code recovery. Although these findings are grounded in a toy setting, they suggest that the lottery ticket structure is governed by hidden feature-space geometry rather than weight-space subnetwork identity.

---


### 383. [Speed Kills: Exploring Confused Deputy Attacks Through Edge AI Accelerators](https://arxiv.org/abs/2605.17707)

**<font color=#1a73e8>作者：</font>** Datta Manikanta Sri Hari Danduri, Aravind Kumar Machiry  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI Accelerator (AIA) are specialized hardware e.g., Tensor Processing Unit (TPU), that enable optimal and efficient execution of AI applications and on-device inference. The growing demand for AI applications has led to the widespread adoption of AIAs on Edge or embedded devices on Edge or embedded devices. Unlike applications, AIAs are not bound by Operating System (OS) restrictions and have limited visibility into Application Processor (AP) security mechanisms (e.g., kernel vs. application memory, process isolation). This semantic gap can lead to confused deputy vulnerabilities, i.e., AIA can be tricked by a malicious application to perform privileged operations on their behalf. In this paper, we conducted the first in-depth study of Confused Deputy Attacks (CDAs) using AIA. We design DeputyHunt, a Large Language Model (LLM) assisted framework to extract CDA relevant information for a given AIA through a combination of dynamic and static analysis. We used this information to explore the feasibility of CDA on seven different AIAs from popular vendors, i.e., Google, NVIDIA, Hailo, Texas Instruments, NXP, AWS, and Rockchip. Our analysis revealed that CDA is feasible on six out of the seven AIAs, impacting over 128 System On Chips (SOCs) and over 100 million devices. Our findings highlight critical security risks posed by AIA on system security. Our work has been acknowledged by the corresponding vendors and assigned the CVE-2025-66425. We propose an on-demand validation defense against CDA, and evaluation on the Gem5- salam simulator shows that it incurs minimal runtime overhead (i.e., ~15%).

---


### 384. [Sometin Beta Pass Notin (SBPN): Improving Multilingual ASR for Nigerian Languages via Knowledge Distillation](https://arxiv.org/abs/2605.17710)

**<font color=#1a73e8>作者：</font>** Sewade Ogun  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Although modern multilingual Automatic Speech Recognition (ASR) systems support several Nigerian languages, their performance consistently lags behind high-resource languages like English and French. Nigerian languages present unique modelling hurdles, including acute data scarcity, inconsistent orthography, tonal diacritics, diverse accents, frequent code-switching, and localized named entities. To address these challenges, we developed a multilingual ASR framework utilizing a two-stage distillation process. First, we employ student-teacher knowledge distillation from existing monolingual models, conditioned on robust language-specific N-gram language models. Second, we perform iterative self improvement using pseudo-labelled data to further refine accuracy. Our method significantly bridges the performance gap, achieving on average a relative Word Error Rate (WER) reduction of 29 % over monolingual baselines. Our models also outperform state-of-the-art multilingual models across major benchmarks, including Common Voice and Fleurs. We introduce Sometin Beta Pass Notin (SBPN), a foundational multilingual ASR model covering Yorùbá, Hausa, Igbo, Nigerian Pidgin, and Nigerian English. SBPN is released in two sizes: SBPN-Base (120 M parameters) and SBPN-Large (600 M parameters). By releasing these as open foundation models, we aim to provide ASR resources for further research into the rich phonetic and cultural landscape of the region.

---


### 385. [From Documents to Segments: A Contextual Reformulation for Topic Assignment](https://arxiv.org/abs/2605.17714)

**<font color=#1a73e8>作者：</font>** Hoonsang Yoon, Takyoung Kim, Wonkee Lee 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Traditional topic modeling assigns a single topic to each document. In practice, however, many real-world documents, such as product reviews or open-ended survey responses, contain multiple distinct topics. This mismatch often leads to topic contamination, where unrelated themes are merged into a single topic, making it difficult to identify documents that truly focus on a specific subject. We address this issue by introducing segment-based topic allocation (SBTA), a reformulation of topic modeling that assigns topics not to entire documents, but to segments: short, coherent spans of text that each express a single theme. By modeling topical structure at the segment level, our approach yields cleaner and more interpretable topics and better supports analysis of multi-theme documents. To support systematic evaluation, we construct a SemEval-STM, a new dataset inspired by aspect-based sentiment analysis. Documents are first decomposed into topical segments using large language models (LLMs), followed by human refinement to ensure segment quality. We also propose a segment-level extension of the word intrusion task, enabling human evaluation of topical coherence at the granularity where topics are actually assigned. Across multiple models and evaluation metrics, we show that SBTA improves clustering quality and interpretability. Overall, this work provides a practical, scalable framework for fine-grained topic analysis in heterogeneous text corpora where documents naturally span multiple topics. URL: this https URL

---


### 386. [GraSP-VL: Length as a Semantic Granularity Interface for Vision-Language Representations](https://arxiv.org/abs/2605.17727)

**<font color=#1a73e8>作者：</font>** Zesheng Li, Chengchang Pan, Honggang Qi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Frozen vision-language embeddings contain signals at multiple semantic resolutions, from object identity to attributes, relations, and full-caption meaning, but they expose these signals through a fixed-length vector interface. We study whether embedding length can be turned into a controllable semantic access interface. We propose \textbf{GraSP-VL}, which learns a shared near-orthogonal prefix transform over frozen VLM embeddings. GraSP-VL instantiates a \textbf{Semantic Matryoshka} interface: short prefixes are assigned coarse semantic roles, while longer prefixes progressively expose finer language-grounded distinctions. Because the transform is shared across image and text embeddings and preserves full-dimensional geometry, prefix behavior changes without rewriting the original VLM space. On a 20,147-example COCO/Flickr30K annotation pool, GraSP-VL reaches a staircase score of 53.01 and hard-negative selectivity of 89.76, while keeping full-space drift below $10^{-6}$. It also transfers to SugarCrepe-clean with 86.03 object accuracy and 11.96 mean external emergence, and preserves full-dimensional zero-shot CIFAR-100 accuracy. These results show that frozen VLM embeddings can be reorganized into a truncatable semantic prefix interface rather than merely compressed.

---


### 387. [Domain Incremental Learning for Pandemic-Resilient Chest X-Ray Analysis](https://arxiv.org/abs/2605.17729)

**<font color=#1a73e8>作者：</font>** Danu Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning models achieved high accuracy in pneumonia detection from chest X-rays. However, their generalization across clinical domains remains limited due to variations in imaging devices, acquisition protocols, and institutional conditions. This study introduces a replay-based domain-incremental continual learning designed to enable continual adaptation to cross-domain variations without catastrophic forgetting. The proposed method incorporates a class-aware balanced replay to maintain balanced class representation within a constrained memory and a class-aware loss to dynamically reweight class imbalance during training. Experiments conducted on a domain-shifted PneumoniaMNIST dataset consisting of five simulated domains demonstrate that the proposed method achieves an average accuracy of 88.66%, outperforming Experience Replay, Fine-Tuning, and Joint Training baselines. These findings highlight the efficacy of the proposed approach in achieving robust and consistent pneumonia detection across clinical environment variations.

---


### 388. [L-Drive: Beyond a Single Mapping-Latent Context Drives Time Series Forecasting](https://arxiv.org/abs/2605.17730)

**<font color=#1a73e8>作者：</font>** Fan Zhang, Shijun Chen, Hua Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mainstream methods for multivariate time-series forecasting largely follow the Direct-Mapping paradigm. They learn a unified mapping from history to the future in the observation space to fit value-level dependencies. However, real-world systems often undergo distribution shifts and regime changes. In such cases, a unified mapping can exhibit response lag around turning points, causing error accumulation within the switching window and reducing forecasting reliability. To address this issue, we propose L-Drive, a change-aware forecasting framework. L-Drive introduces a Latent-Context, to explicitly characterize high-level dynamics evolving over time, and uses gating to modulate increment representations. This provides more timely change cues and improves adaptation to changing segments. In addition, it incorporates patch-shared relative positional basis functions to strengthen intra-segment structural modeling and reduce overfitting caused by absolute-position memorization. Extensive experiments validate the effectiveness of L-Drive and show a better overall trade-off between forecasting accuracy and computational efficiency.

---


### 389. [Divergence-Suppressing Couplings for Rectified Flow](https://arxiv.org/abs/2605.17733)

**<font color=#1a73e8>作者：</font>** Yimeng Min, Carla P. Gomes  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The promise of Rectified Flow rests on producing self-generated couplings whose trajectories are straight, or nearly so. In practice, trajectories generated by the base flow model can bend and intertwine, and the resulting coupling inherits this distortion. In this paper, we identify that such trajectory entanglement is often associated with regions of nonzero divergence in the learned velocity field, where local expansion or contraction distorts trajectories and steers particles away from their ideal endpoints. We then propose divergence-suppressing couplings for Rectified Flow, an offline correction that attenuate the divergent component of the learned velocity during coupling generation. The correction is paid only once per coupling pair and amortized over training, so deployment runs plain Euler at identical wall-clock cost to standard Rectified Flow. Empirically, this offline modification yields consistent improvements on 2D synthetic benchmarks and on image generation.

---


### 390. [UST-Hand: An Uncertainty-aware Spatiotemporal Point Cloud Interaction Network for 3D Self-supervised Hand Pose Estimation](https://arxiv.org/abs/2605.17742)

**<font color=#1a73e8>作者：</font>** Tianhao Han, Haoyang Zhang, Liang Xie 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Manually annotating accurate 3D hand poses is extremely time-consuming and labor-intensive. Existing self-supervised hand pose estimation methods leverage the discrepancy between input images and rendered outputs, or multi-view consistency constraints, as the driving force to optimize networks and progressively refine pose accuracy. However, these methods are highly susceptible to noisy pseudo-labels and overlook the importance of fully exploiting fine-grained spatial correlations, which undermines the stability of model training. To address these issues, we propose UST-Hand, a self-supervised learning framework that estimates uncertainty distribution of hand pose and constructs a probabilistic point cloud feature space, which enables the complex spatiotemporal relationship modeling. UST-Hand employs a conditional normalizing flow model to capture hand pose distributions and samples diverse hypotheses, facilitating robust learning under noisy pseudo-labels supervision with enhanced stability. These multi-hypothesis are mapped to a unified probabilistic 3D point cloud space for multi-view and temporal feature interaction, comprehensively exploring hand motion patterns and fine-grained spatial correlations. Extensive experiments on three challenging datasets demonstrate that UST-Hand achieves state-of-the-art performance, outperforming existing self-supervised methods by up to 37.8% in Mean Per Vertex Position Error (MPVPE).

---


### 391. [MoASE++: Mixture of Activation Sparsity Experts with Domain-Adaptive On-policy Distillation for Continual Test Time Adaptation](https://arxiv.org/abs/2605.17743)

**<font color=#1a73e8>作者：</font>** Ronyu Zhang, Aosong Cheng, Gaole Dai 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Continual test-time adaptation adapts a source-pretrained model to non-stationary, unlabeled target streams while retaining past competence, yet texture-biased backbones risk error accumulation and catastrophic forgetting. Drawing inspiration from the process of decoupling shape and texture in the human visual system, we introduce MoASE, a plug-in mixture-of-experts that disentangles domain-agnostic structure from domain-specific texture using Activation Sparsity Experts with Spatial Differentiable Dropout, forming complementary high- and low-activation pathways, while high- and low-rank bottlenecks diversify representations. The Activation Sparsity Gate produces input-adaptive SDD thresholds for precise token selection, and the Domain-Aware Router assigns per-sample expert weights using texture-sensitive cues. To curb confirmation bias on unlabeled streams and stabilize supervision, we then introduce Domain-Adaptive On-Policy Distillation to constitute MoASE++, with an EMA-anchored on-policy reverse KL distillation and an augmentation policy conditioned on entropy and confidence that aligns predictions across the same views and improves the robustness-plasticity balance. Extensive experiments on classification (CIFAR-10/100-C, ImageNet-C) and semantic segmentation (Cityscapes->ACDC) demonstrate consistent state-of-the-art performance, offering a principled, controllable approach to continual adaptation in dynamic visual environments.

---


### 392. [Agents for Experiments, Experiments for Agents: A Design Grammar for AI-Enabled Experimental Science](https://arxiv.org/abs/2605.17746)

**<font color=#1a73e8>作者：</font>** Yingjie Zhang, Chun Feng, Weizhang Zhu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI systems are becoming active participants in organizational and knowledge work. They increasingly interact with humans, coordinate workflows, and operate in multi-agent arrangements. Understanding their effects therefore requires more than measuring output accuracy; it requires evidence about mechanisms, delegation, feedback, and control. Experiments remain central to this task, but they also face a recursive challenge: we need experiments for agents to study these arrangements, and we may need agents for experiments to help search the expanding space of possible designs. Yet experimental conditions for human-AI and agentic workflows are still largely specified in prose, making them difficult to compare, reuse, or audit. We frame this as a problem of workflow representation, traceability, and governance in AI-enabled knowledge production. We introduce SEED (Structural Encoding for Experimental Discovery), a framework that represents experimental conditions as typed actor-flow graphs. SEED supports three design functions: describing conditions as interaction structures, evaluating structural novelty relative to encoded prior designs, and generating candidate designs under feasibility and governance constraints. We report a lightweight empirical feasibility test that compares graph-blind and SEEDguided generation in a medical-triage design task. In this diagnostic contrast, SEED-guided candidate designs show clearer actor-flow changes, assumptions, and governance checks, supporting the feasibility of the grammar as a design aid. The commentary closes by identifying governance tensions around novelty, replication, validity, diversity of inquiry, and accountability.

---


### 393. [Unleashing Vision Transformer Potential In Image Quality Assessment via Global-Local Adaptive Interaction](https://arxiv.org/abs/2605.17748)

**<font color=#1a73e8>作者：</font>** Yu Li, Puchao Zhou, Yachun Mi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In the field of Blind Image Quality Assessment (BIQA), accurately predicting the perceptual quality of authentically distorted images remains highly challenging due to the diverse and complex distortions present in natural environments. Although existing methods have achieved notable accuracy, their scalability is often constrained by the high cost of subjective annotation and the limited size of available datasets. Recent advances in large-scale pre-trained vision models have introduced powerful semantic and representational capabilities, yet their application to IQA tasks is hindered by substantial computational demands and suboptimal fine-tuning efficiency. To overcome these limitations, we introduce the Global-Local Interaction Adapter (GLIA), a novel framework that effectively harnesses pre-trained Vision Transformers through a dual-stream feature extraction mechanism coupled with interactive global-local fusion. By jointly retaining global semantic information and fine-grained local details, our approach delivers superior prediction accuracy and robustness while requiring significantly fewer trainable parameters. Extensive experiments on multiple benchmarks validate the effectiveness and superiority of our approach.

---


### 394. [Testable and Actionable Calibration for Full Swap Regret](https://arxiv.org/abs/2605.17749)

**<font color=#1a73e8>作者：</font>** Konstantina Bairaktari, Lunjia Hu, Huy L. Nguyen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> AI generated predictions increasingly inform decision making in critical tasks, and therefore must be trustworthy. One widely used measure of trustworthiness is calibration, which requires that the predictions match the true frequencies and can be treated like real probabilities of a given outcome. However, defining calibration is subtle, and designing good measures of calibration error has been an active topic of recent research. The first goal is to find calibration measures that are actionable, meaning they can inform decision makers about their utility loss when predictions are treated as true probabilities, which is known as swap regret. The second goal is to find calibration measures that are testable, meaning that calibration error can be measured from a small sample of predictions and outcomes. Although these are very basic requirements, there is no existing calibration measure that fully satisfies both properties, and all existing measures relax actionability by bounding a weaker notion of swap regret, or relax testability by having suboptimal estimation error. We introduce a new calibration measure, Soft-Binned Calibration Decision Loss (SCDL), which we prove is fully actionable without weakening either requirement, and testable with nearly optimal error rate. In addition, SCDL satisfies other desired properties such as continuity and consistency. We also provide a set of experiments confirming that the theoretical advantages of SCDL compared to other measures lead to better performance in practice.

---


### 395. [Bridging the Version Gap: Multi-version Training Improves ICD Code Prediction, Especially for Rare Codes](https://arxiv.org/abs/2605.17755)

**<font color=#1a73e8>作者：</font>** Jinghui Liu, Anthony Nguyen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Clinical coding maps clinical documentation to standardized medical codes, an essential yet time-consuming administrative task that could benefit from automation. Current models on ICD coding are typically optimized for codes from a specific ICD version. However, in reality, ICD systems evolve continuously, and different versions are adopted across time periods and regions. Moreover, ICD coding suffers from the long-tail problem, and rare code performance can be a bottleneck for developing implementable models. We examine whether it is viable to train version-independent models by combining data annotated in different ICD versions, which may help address these challenges. We add ICD-9 data to the training of a modified label-wise attention model for ICD-10 prediction, and find that despite the version mismatch, adding ICD-9 yields a 27% increase in micro F1 for 18K rare ICD codes compared to training on ICD-10 alone. On 8K frequent ICD-10 codes, the multi-version training also substantially improves macro metrics, with far fewer model parameters.

---


### 396. [OSCAR: Offline Spectral Covariance-Aware Rotation for 2-bit KV Cache Quantization](https://arxiv.org/abs/2605.17757)

**<font color=#1a73e8>作者：</font>** Zhongzhu Zhou, Donglin Zhuang, Jisen Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> INT2 KV-cache quantization is attractive for long-context LLM serving, but it remains difficult to make both accurate and deployable. Simple rotations such as Hadamard transforms reduce outliers, but still degrade at INT2 because they are not aligned with downstream attention. We propose OSCAR, an Ultra-low-bit KV Cache quantization method that estimates attention-aware covariance structures offline and uses them to derive fixed rotations and clipping thresholds for quantization. In this way, it aligns KV quantization with the covariance structures that attention actually consumes. More importantly, we not only provide theoretical justification but also develop a fully deployable OSCAR system with a custom INT2 attention kernel that remains compatible with paged KV-cache serving and fused kernel pipelines, enabling seamless integration into modern LLM serving frameworks such as SGLang and vLLM.
We evaluate our methods on recent reasoning models with reasoning traces of up to 32k tokens across 5 tasks. On Qwen3-4B-Thinking-2507 and Qwen3-8B, OSCAR reduces the BF16 accuracy gap to 3.78 and 1.42 points, respectively, while naive rotation INT2 collapses to nearly zero. We further scale OSCAR to Qwen3-32B and GLM-4.7 (358B params), where it remains effectively on par with BF16. On long context - RULER-NIAH up to 128K, OSCAR remains robust on both Qwen3 models, while naive rotation INT2 collapses. System-wise, OSCAR reduces KV-cache memory by approximately 8x, improves throughput by up to 7x at large batch sizes under the same memory budget, and accelerates batch-size-1 decoding by up to 3x over BF16 due to reduced memory bandwidth overhead.

---


### 397. [Memisis: Orchestrating and Evaluating Synthetic Data for Tabular Health Datasets](https://arxiv.org/abs/2605.17758)

**<font color=#1a73e8>作者：</font>** Nitish Nagesh, Mahdi Bagheri, Arshia Harish Puthran 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Synthetic data is widely used in healthcare to create datasets that are similar to original data but without the privacy concerns. Generating and evaluating synthetic data across privacy, utility and fairness is crucial for facilitating high quality data availability for downstream prediction tasks and clinical decision making. We present Memisis, a tool that orchestrates and evaluates synthetic data by leveraging existing synthetic data tools, the power of large language models and state-of-the-art evaluation metrics. Our tool creates a unified workflow for data generation, validation and evaluation. Users have control over the training size, training epochs and the number of synthetic rows to sample. Instead of knobs to tune synthetic data, the interactive agent allows users to specify their synthetic data generation goals and the tool will orchestrate the workflow by leveraging existing tools while performing the requisite evaluation. For the demo, we use an open source schizophrenia dataset with protected attributes related to race and gender, three different synthesizers and a local language model to orchestrate the workflow. We observe that CTGAN, TVAE and GaussianCopula have comparable performance across fairness and utility metrics. The workflow allows users flexibility and control over the data generation and evaluation process.

---


### 398. [FrequencyBooster: Full-Frequency Modeling for High-Fidelity Pixel Diffusion](https://arxiv.org/abs/2605.17759)

**<font color=#1a73e8>作者：</font>** Lichen Ma, Zipeng Guo, Yu He 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> To circumvent the inherent fidelity bottlenecks and optimization misalignment of VAE-based latent diffusion, pixel-space diffusion models have emerged as a compelling end-to-end paradigm. However, existing pixel diffusion models often struggle to balance computational efficiency with the preservation of high-frequency details. They frequently resort to patch-based compression or restricted local decoding, leading to a "spectral compromise" where high-frequency and fine-grained pixel information are suppressed. To address these challenges, we propose \textbf{FrequencyBooster}, a novel framework designed to empower pixel diffusion with full-frequency modeling capabilities without prohibitive overhead. The core of our method is a high-capacity decoder that specializes in extracting exhaustive high-frequency details and low-frequency semantics, the latter of which is derived from a Diffusion Transformer (DiT) backbone. Unlike prior works that sacrifice global context for local refinement, FrequencyBooster leverages high-dimensional feature representations to maintain global structural integrity while achieving superior pixel-level precision. Extensive experiments on ImageNet demonstrate the effectiveness of our approach: our model achieves a state-of-the-art FID of \textbf{1.60} at $256 \times 256$ resolution within only 320 epochs. Furthermore, at $512 \times 512$ resolution, FrequencyBooster attains an FID of \textbf{1.69}, significantly outperforming existing pixel-space and latent-space generative models.

---


### 399. [Surface-Form Neural Sparse Retrieval: Robust Fuzzy Matching for Industrial Music Search](https://arxiv.org/abs/2605.17762)

**<font color=#1a73e8>作者：</font>** Paul Greyson, Zhichao Geng, Wei Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Music search at the scale of Amazon Music presents a unique challenge: queries frequently deviate from indexed metadata due to misspellings, transpositions, and phonetic variations, yet the retrieval system must operate under strict millisecond-level latency constraints. Our existing learning-to-retrieve system, the High Confidence Index (HCI), learns query-entity associations from customer behavior, relying on continual ``exploration'' to choose candidates. Traditional n-gram matching enables this exploration but suffers from poor semantic robustness and high noise, limiting the system's ability to learn from long-tail queries. In this work, we present a \textbf{robust neural sparse retrieval system} designed to maximize exploration efficiency. We adapt a state-of-the-art \textbf{inference-free} sparse retrieval architecture to the music domain, combining it with an effective \textbf{domain-specific granular subword tokenization strategy}. Our approach utilizes short-length token constraints (max 3 chars) to enforce the learning of surface-form robustness over lexical memorization. By pre-computing the neural embeddings and term expansions during the offline indexing phase, online processing is reduced to minimal tokenization and IDF weighting, achieving effectively zero latency overhead for query encoding. Evaluations on a 6M-document production corpus show an aggregate \textbf{91.4\%} recall@10 (vs. \textbf{57.7\%} for trigrams) at comparable throughput. Simulation of the HCI feedback loop demonstrates improved exploration efficiency, with \textbf{+0.8\%} higher stabilized recall than production trigrams. Ablation studies indicate that our sparse training methodology drives the performance gains, while domain-specific pretraining provides a cost-effective alternative to large-scale general-purpose pretraining.

---


### 400. [Towards Universal Physical Adversarial Attacks via a Joint Multi-Objective and Multi-Model Optimization Framework](https://arxiv.org/abs/2605.17772)

**<font color=#1a73e8>作者：</font>** Ziyang Liu, Hongyuan Wang, Zijian Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Physical adversarial attacks often overfit single surrogate models and optimization objectives. While ensemble attacks can mitigate this, existing methods struggle with severe gradient conflicts within restricted physical texture spaces, significantly degrading cross-model transferability. To bridge this gap, this paper proposes a Joint Multi-Objective and Multi-Model Optimization Framework (JMOF) that leverages quantitative similarity analysis to select the optimal surrogate model ensemble. Within JMOF, a dual-level mechanism jointly suppresses prediction outputs and flattens intermediate feature distributions, balancing attack efficiency with deep generalization. Additionally, an Orthogonal Gradient Alignment (OGA) strategy resolves cross-model gradient conflicts, transforming mutually repulsive gradients into synergistic optimization directions. Extensive simulated and real-world experiments demonstrate that JMOF outperforms state-of-the-art baselines against diverse black-box detectors. Crucially, JMOF exhibits substantial cross-vision-task generalization, generating attacks capable of simultaneously deceiving object detection and semantic segmentation or monocular depth estimation models. This research advances the generalization limits of physical adversarial attacks, providing a robust framework for evaluating visual AI vulnerabilities in real-world deployments.

---


> [!TIP]
> 当前位于：**351-400**（第 8/13 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | [601-619](./part-13.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
