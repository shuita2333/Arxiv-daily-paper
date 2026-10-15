# 🧠 大模型相关研究 | 2026年10月16日

> 本类共 **313** 篇论文：已确认 **304** 篇，待复核 **9** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**101-150**（第 3/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-313](./part-07.md)

---

### 101. [VideoHarness-SRSI: Structured Recursive Self-Improvement for Video Understanding Harness](https://arxiv.org/abs/2610.19424)

**<font color=#1a73e8>作者：</font>** Zihao Lin, Haoyu Dong, Haobo Xu 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> LLM system capabilities depend not only on model parameters but also on the executable harnesses that organize information acquisition, tool use, reasoning, and memory. Recursive harness evolution can automate their design, but how it can reliably discover generalizable systems from limited, noisy, and repeatedly reused feedback remains unclear. We study this question in agentic video understanding, where rich multimodal evidence and coupled mechanisms make harness optimization challenging. We first introduce VideoHarness-BRSI, a recursive self-improvement framework that evolves video harnesses around a frozen vision-language model. Analyzing over 4,000 evolved candidates, we find it competitive with hand-engineered systems but identify three interconnected failure modes: validation overfitting, search-budget dilution, and the early-experience trap. We trace all three to a common root: the same imperfect validation evidence drives both harness revisions and the proposer's search strategy. We therefore propose VideoHarness-SRSI, an evidence-governed framework in which every search decision rests on evidence that is transferable, sufficient, and gathered before the search commits. It restricts the proposer to content-free feedback, informs exploration with instrumented warm-up experiments, and develops mechanisms in isolated probe-race branches before factorial composition and joint refinement. Across four video understanding benchmarks, VideoHarness-SRSI improves the equally weighted mean held-out score by 6.2% relative to VideoHarness-BRSI and reduces the mean validation-test gap by 37.9%. Reliable harness evolution thus depends on how search is organized and informed, not only on how well it optimizes validation performance.

---


### 102. [Evaluating Agentic Capabilities Before Post-Training: An End-to-End Approach](https://arxiv.org/abs/2610.19425)

**<font color=#1a73e8>作者：</font>** Jiarui Qin, Junjie Huang, Yunjia Xi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic capabilities are increasingly important for modern LLMs, yet remain difficult to evaluate during pretraining. Existing approaches typically rely on static trajectory-derived tasks or likelihood-based proxies, which are lightweight but provide limited visibility into how base models behave in interactive environments. We introduce ASAP (Agent Scaffold Adaptation for Pretraining Evaluation), a lightweight framework for eliciting and evaluating agentic behavior from pretrained base models on end-to-end tasks. Rather than converting base models into chat-style agents, ASAP preserves the completion interface and adapts existing agent scaffolds through structured trajectory continuation, short reference prefixes, and minimal recovery mechanisms. Across software-engineering and deep-research benchmarks, ASAP yields discriminative end-to-end performance across base models and pretraining checkpoints. Beyond aggregate scores, ASAP exposes model-generated execution trajectories, enabling analysis of exploration, editing, testing, recovery, and task completion across training stages. These trajectories provide a behavioral view of how agent-relevant capabilities change during pretraining and how execution patterns differ after post-training. Our results suggest that end-to-end agent evaluation can complement conventional pretraining benchmarks by providing a practical diagnostic of interactive model behavior.

---


### 103. [How Do LLMs Understand Legal Philosophy? Diagnosing Legal-Philosophical Reasoning in LLMs](https://arxiv.org/abs/2610.19427)

**<font color=#1a73e8>作者：</font>** Shuyuan Zheng, Yun-seo Lee, Xing Gao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Legal reasoning is a fundamental capability for large language models (LLMs) to complete legal AI tasks such as legal judgment prediction. In legal practice, this reasoning is shaped by legal philosophy: a judge's view of the nature and sources of law guides how legal materials are interpreted and applied, so judges working from the same statutes and precedents can reach different judgments. Existing research has largely overlooked whether LLMs can understand legal philosophy and apply it in legal reasoning, an ability we call \textit{legal-philosophical reasoning}. To fill this gap, we introduce LePhilBench, a benchmark for evaluating the legal-philosophical reasoning of LLMs that comprises two benchmarking tasks and a dataset. The two tasks evaluate how well LLMs understand legal philosophy and how well they apply it in legal reasoning, respectively. The dataset is manually and meticulously constructed. Its test set contains 220 U.S. Supreme Court opinions. A law professor designed fourteen annotation questions on legal philosophy, and three law-trained annotators with formal training in jurisprudence answered all fourteen questions for every opinion, yielding 9,240 legal-philosophical labels. LePhilBench takes the first step toward exploring legal-philosophical reasoning in LLMs.

---


### 104. [Recognition Is Not Grounding: Benchmarking Multilingual Financial Evidence Extraction](https://arxiv.org/abs/2610.19432)

**<font color=#1a73e8>作者：</font>** Lingfei Qian, Yan Wang, Xueqing Peng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Comparing financial disclosures across languages requires identifying shared accounting concepts and recovering all numerical facts that express them. Existing benchmarks evaluate aspects of these capabilities, but provide limited insight into whether both succeed on the same multilingual evidence. In particular, it remains unclear whether language models can recognize these concepts across languages and exhaustively recover their corresponding numerical evidence from the same contexts. We introduce MULTIFINGROUND, a benchmark designed to investigate this recognition-grounding gap in multilingual financial reports. Constructed from FY2025 disclosures of 90 issuers in English, French, and Greek, MULTIFINGROUND aligns independently authored reports through a shared accounting taxonomy and provides traceable fact-level annotations. The benchmark evaluates financial fact identification, concept recognition, exhaustive fact selection, and concept discrimination without candidate labels. Across 15 evaluated models, eight API and open-weight reference models achieve 97.3-99.4\% concept recognition accuracy, yet miss at least one target fact in 26.6-41.9\% of correctly recognized groups. Further analyses reveal substantial variation in concept discrimination and limited gains from the evaluated finance-specialized models. Our findings demonstrate that strong concept recognition can coexist with incomplete evidence recovery, highlighting the importance of evaluating semantic recognition and evidence completeness together.

---


### 105. [EvoProbe: Evaluation-Driven Benchmark Evolution for LLM Agents](https://arxiv.org/abs/2610.19433)

**<font color=#1a73e8>作者：</font>** Qianhong Guo, Wei Xie, Xiaofang Cai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Static benchmarks for large language model (LLM) agents face saturation and data contamination risks, motivating continual updates to evaluation tasks. However, aggregate scores and success rates offer limited insight into specific problem-solving bottlenecks and provide limited guidance for subsequent task design. We propose EvoProbe, an evaluation-driven benchmark evolution framework that integrates task generation, diagnostic evaluation, and feedback-driven regeneration into a closed loop. It combines verifiable subtask outcome scoring with evidence-supported multi-judge trajectory evaluation and distills phase-level bottlenecks, success patterns, and failure patterns into diagnostic feedback for generating new executable tasks. Across two rounds of cybersecurity experiments, evaluations of eight models on 66 tasks reveal phase-level performance differences and common failure patterns beyond aggregate scores. In a cross-round comparison with the Examiner model set and solver configuration held fixed, all eight models achieve lower Outcome scores on the updated tasks, with relative decreases of 11.8\% in mean Outcome and 40.0\% in mean Pass\textasciicircum{}3. These results support using fine-grained diagnostics to guide iterative task updates and probe agents' current capabilities and limitations.

---


### 106. [Progress-Aware Distillation for Mitigating Stagnation in Small Language Model Agents](https://arxiv.org/abs/2610.19439)

**<font color=#1a73e8>作者：</font>** Yuanpu Cao, Saket Sathe, Hanyu Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While LLM-based agent systems have demonstrated remarkable proficiency in reasoning and solving complex real-world tasks, they also come with substantial token consumption and inference latency, limiting their practical deployment. To enhance the efficiency of agent systems, recent efforts have focused on transferring agentic capabilities from large-scale models to small language models (SLMs) via supervised fine-tuning-based distillation. Nevertheless, as interaction trajectories grow longer, involving extended reasoning-action chains and extensive environmental feedback, distilled student agents tend to experience progress stagnation: becoming trapped in unproductive loops characterized by persistent failed strategies and difficulty making meaningful progress. Our systematic analysis shows that this phenomenon consistently occurs across diverse SLMs and task domains. To address this issue, we propose Progress-Aware Distillation (ProD), which explicitly detects and penalizes stagnation in student-generated trajectories. ProD encodes the stagnation gap between student and teacher into an adaptive margin for dynamically penalizing possible stagnation. By iteratively applying this procedure, ProD enables student agents to progressively approximate teacher behavior. Extensive experiments involving 8 SLMs, ranging from 0.6B to 8B parameters, on both in-domain and out-of-domain benchmarks, demonstrate that ProD substantially mitigates progress stagnation while enhancing both the success rates and task-completion efficiency of distilled SLM agents.

---


### 107. [Integrating Simulation and Chain-of-thought Reasoning in Multimodal-Language Models For Physical Reasoning](https://arxiv.org/abs/2610.19441)

**<font color=#1a73e8>作者：</font>** YingQiao Wang, Eric Bigelow, Tomer Ullman 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal language models often need to reason about the physical dynamics of the world in order to answer questions appropriately. Various methods have emerged for solving physical reasoning tasks, and in particular, two leading approaches are Chain-of-Thought reasoning and physics-grounded simulation. However, relatively little is known about which particular problems can be solved by each approach. Some tasks may benefit from computationally expensive generative video simulations, whereas others may be solved equally well (or even better) with language-based reasoning. Our work addresses this by systematically comparing simulation and language reasoning across a variety of multimodal tasks involving physical reasoning, such as answering questions about fluid dynamics and elasticity. We draw a parallel with this to resource-rational theories of human cognition, which propose that people optimally trade off simulation and reasoning depending on task demands. We present a novel cognitively-inspired hybrid model which optimally trades off simulation and reasoning to improve model performance and computational efficiency. Our model is able to decide the appropriate method to solve a physical reasoning problem at test time, and finds an optimal balance between accuracy and cost. Further, our model can be trained on a smaller vision-language model that is only 4B parameters and deployed to improve performance on much bigger base models with $>$3T parameters like Gemini 3 Pro.

---


### 108. [PFedMA: Who Should Join Next as Federated Multi-Agent Orchestration Evolves?](https://arxiv.org/abs/2610.19458)

**<font color=#1a73e8>作者：</font>** Shuai Li, Shengyuan Liu, Fan Qi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Federated Multi-Agent Systems (FedMAS) offer a promising paradigm for collaborative reasoning among LLM-based agents while keeping raw client data decentralized. However, reliable multi-round collaboration remains challenging. Agent selection must take into consideration evolving task requirements and the agent's historical reliability, while privacy rules must adapt to changing collaboration contexts and meet the client's personalized needs. To address these challenges, we propose PFedMA, a federated multi-agent framework for feedback driven multi-round collaboration under heterogeneous privacy requirements. Across rounds, PFedMA maintains historical capability and reliability states to guide agent selection, evaluates task responses before aggregation, and refines subsequent queries according to accumulated collaboration feedback. PFedMA enables bidirectional local to global and global to local private rule evolution across heterogeneous clients. Clients generalize locally updated privacy rules and selectively incorporate globally maintained rules, thereby facilitating cross-client privacy rule evolution while preserving personalized constraints. Extensive experiments across reasoning, privacy sensitive, and adversarial settings show that PFedMA improves task performance, reduces measured privacy leakage, and improves system robustness.

---


### 109. [MemCode: Discrete Semantic Representations for Long-Term Agent Memory](https://arxiv.org/abs/2610.19472)

**<font color=#1a73e8>作者：</font>** Xin Li, Liang Hu, Duoqian Miao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-term memory remains a fundamental bottleneck for large language model (LLM) agents across sessions. Existing systems typically adopt a write-then-retrieve paradigm, storing context-dependent dialogue fragments and retrieving them via nearest-neighbor search in a continuous embedding space. This design yields unstable access units and systematically misses logically related but lexically distant evidence. We propose MemCode, a long-term agent memory framework that couples retrieval-oriented writing with discrete associative retrieval. MemCode rewrites dialogue into self-contained atomic memory units (AMUs), maps AMUs into a learnable codebook with isomorphic semantic quantization (ISQ), and uses codebook co-occurrence topology as a retrieval path complementary to vector search. For long-term memory stores, MemCode separates online atomic writes from asynchronous offline consolidation. On LongMemEval-S and LoCoMo with GPT-4o-mini and Qwen3-30B-A3B-Instruct-2507 backbones, MemCode achieves the best overall accuracy while keeping per-dialogue memory construction within roughly 40~130 seconds, making it 3~21 times faster than LightMem and over an order of magnitude faster than A-MEM and MemoryOS.

---


### 110. [Beyond Retrieval: Evidence Access and Event Aggregation in Agent Memory](https://arxiv.org/abs/2610.19474)

**<font color=#1a73e8>作者：</font>** Zerui Yang, Quan Xue, Chaorui Zhang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Questions about an agent's history often require aggregating events, which retrieval alone does not resolve. We combine source-preserving evidence access with executable aggregation. Trajectory Memory (TM) retains the original trajectory and constructs a source-addressable reading view at question time. TallyMem augments it with a reusable event ledger, model-generated event specifications and deterministic execution. With a commit-specific adaptation on 776 questions from 99 held-out MINTEval repositories, TallyMem raises Qwen3-32B exact match from 35.2% to 49.0%, a 13.8-point gain over TM; gains span 12.8-13.9 points across three readers. A controlled probe with event sets parsed independently from raw logs shows an 11.0-point gain, from 82.8% to 93.8%, without routing. On full AMA-Bench, the routed system yields a smaller 1.3-point gain, from 69.8% to 71.1%. These results support executable aggregation on tasks that require combining events, with benefits dependent on the task and event specification, the largest residual system-error category in our diagnostic analysis.

---


### 111. [ActICL: Post-Training for Agentic Multimodal In-Context Learning](https://arxiv.org/abs/2610.19475)

**<font color=#1a73e8>作者：</font>** Yanshu Li, Ruixiang Tang, Junyi Jessy Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal in-context learning (ICL) is an important capability of multimodal large language models (MLLMs). Its performance is closely tied to the demonstrations it uses, making demonstration retrieval a core problem for ICL. Common methods use fixed scoring methods to retrieve all the demonstrations at once, which may introduce redundancy and noise. Context-aware retrieval methods have emerged to address this problem by allowing incremental retrieval from a growing context. However, none of them lets the MLLM learn how to judge what new demonstrations it needs and then carry out progressive retrieval on its own. To this end, we introduce ActICL, which trains an MLLM agent to acquire and use an ICL context via tool-augmented reasoning. An ActICL agent analyzes its own information gaps during iterative reasoning and tool-use actions. Based on these gaps, it performs targeted retrieval to acquire a set of initial candidates. It can then use the existing context to further filter the candidates and refine the context, or it can iteratively perform a new retrieval. When the agent judges that the context is sufficient for the task, or when the resource limit is reached with the user request met, it sends the acquired context to an answering model, either the agent itself or another MLLM. We use a two-stage post-training procedure that jointly optimizes the agent's acquisition and answering. With an adaptive number of demonstrations, ActICL improves average performance by 11.6 percentage points over standard similarity-based retrieval across seven benchmarks and three MLLMs, and by 4.4 points compared to the strongest prior baseline. The contexts acquired by ActICL agents can also be used effectively by frontier models. When GPT-5.6-Sol performs 4-shot ICL, ActICL's contexts improve its performance by 3.5 points over standard retrieval, averaged over three benchmarks.

---


### 112. [AgriJev: Efficient Agricultural Candidate Scoring with Multi-Scale Adapted Models](https://arxiv.org/abs/2610.19478)

**<font color=#1a73e8>作者：</font>** Xuechen Li  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agricultural systems make decisions over heterogeneous entity types, textual judgments, and knowledge-question options. Generating a textual answer adds decoding and extraction steps to decisions that ultimately require a candidate choice. We introduce AgriJev, a family of adapted Qwen3.5 models at 0.8B, 2B, 4B, and 9B. A shared interface conditions on agricultural text, a judgment question, and candidate definitions, returning scores and relative probabilities in one forward call. We prepare source-aware training records and frozen evaluations from existing agricultural resources, retaining original groups and annotation provenance. Comparisons include original Qwen3.5 models and matched agricultural SFT models, both evaluated through native answer generation. Across 17 external test views, AgriJev-9B reaches 75.44% mean accuracy, exceeding the original and SFT generators by 5.89 and 3.79 percentage points. It outperforms the original generator on 13 views and narrows the mean gap to hosted Jev 1.13.0. On a fixed A100 workload, its median scoring latency is approximately half that of same-scale answer generation. Task-dependent gains and failures characterize a practical choice among agricultural model weights and inference contracts.

---


### 113. [Towards Efficient Simultaneous Inverse Text Normalization with Pretrained Text-to-Text Language Model and Read-Tag-Write Policy](https://arxiv.org/abs/2610.19492)

**<font color=#1a73e8>作者：</font>** Kiet Anh Hoang, Khanh Le, Bao Nguyen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Streaming Inverse Text Normalization (ITN) is vital for converting spoken-form outputs from streaming Automatic Speech Recognition into formatted written text. Existing streaming ITN methods rely on hybrid systems combining neural tagging with expert-crafted finite-state transducer rules, limiting scalability across domains and languages. While end-to-end models offer superior scalability by learning directly from data, standard encoder-decoder architectures are inherently non-streaming due to global attention. In this paper, we propose an efficient streaming end-to-end ITN system, adapting a pretrained text-to-text model to leverage its robust linguistic knowledge. To enable streaming, we introduce architectural adaptations, a specialized training strategy, a Read-Tag-Write decoding policy, and inference optimizations. Experiments on Vietnamese datasets show accuracy comparable to non-streaming baselines, outperforming hybrid methods while satisfying real-time latency requirements.

---


### 114. [Structure-Preserving Document-Level Data Augmentation via Discourse Parsing](https://arxiv.org/abs/2610.19497)

**<font color=#1a73e8>作者：</font>** Ruilin Shang, Shilong Hou, Zi Long 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Data augmentation (DA) plays a vital role in improving model performance in low-resource or limited-supervision scenarios within Natural Language Processing (NLP). Existing DA methods, such as synonym replacement and back-translation, have demonstrated effectiveness on the word or sentence level; however, they frequently neglect discourse-level coherence and logical flow, which are essential for complex tasks dependent on inter-sentential relationships. In this paper, we propose a structure-preserving document-level data augmentation framework based on large language models (LLMs) and document-level discourse structure parsing. Our approach identifies rhetorical relations between sentence pairs and extracts key phrases, which are then replaced with semantically coherent but topically shifted content while preserving the original discourse structure. Experimental results on text summarization and question answering show that the proposed augmented data provides complementary supervision and improves combined-data training across the evaluated tasks. Comparisons with a standard RST parser and controlled ablations further support the proposed discourse representation.

---


### 115. [What You Sign Is Not What You Run: The Verifiability Gap in Quantized LLM Supply Chains](https://arxiv.org/abs/2610.19498)

**<font color=#1a73e8>作者：</font>** Wei-Liang Liu, Cheng-Yen Tsai  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Model signing authenticates the full-precision weights W an LLM is released with, yet users run a quantized artifact Q whose producing transformation is not uniquely determined under current disclosure. We separate the non-environment inputs from the execution environment E and measure a quantity that, to our knowledge, has not been measured before: the Independent Verifiability Rate (IVR), the fraction of a popularity-sampled GGUF ecosystem that a third party can re-derive bit-for-bit. Across the 200 most-downloaded Hugging Face GGUF repositories (198 in scope), no artifact or model card records the build environment, so under a recorded-inputs protocol the IVR is 0/198. Yet the artifacts are not irreproducible. On four in-sample repositories that disclose their inputs, the card's information alone reproduces no Q4_K_M file, but two coordinates the card omits - the build's floating-point-contraction setting and, for hybrid models, the per-tensor quantization recipe - re-derive 7/8 target-quant files bit-for-bit on x86 (5/8 on arm64); the fp16 re-derives from the provider's checkpoint, but the calibration imatrix must be shipped and hash-bound, since recomputing it did not match. An older release additionally pins the instruction set and did not re-derive. Reproducing the divergence reported with this http URL PR #25353, we show that E is a necessary coordinate and that one compiler setting yields a unique output across the tested platforms at negligible quality cost (+0.06% perplexity). As a security characterization, benign floating-point non-determinism separates from uniformly placed nibble-flip tampering above a detection floor that grows with the environments a verifier must allow, but a targeted embedding edit evades the statistic, so the proposed protocol rests on exact re-derivation; adversarial-fp16 attacks lie outside it. We release the audit data and a re-runnable harness.

---


### 116. [Holi-Spatial 360: Generative Reconstruction from Sparse Panoramas for Spatial Rendering and Intelligence](https://arxiv.org/abs/2610.19502)

**<font color=#1a73e8>作者：</font>** Yuanyuan Gao, Zhirui Liu, Yuning Gong 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatial intelligence requires scalable 3D environments that are both photorealistic and semantically grounded, yet existing indoor datasets are dominated by room-scale captures and costly LiDAR acquisition. Online real-estate platforms offer abundant panoramas of diverse multi-room homes, but sparse viewpoints and texture-poor regions make reconstruction severely under-constrained. We introduce Holi-Spatial 360, a generative reconstruction and data curation framework for converting these panoramas into annotated multi-room 3D environments. Because reconstruction quality bounds subsequent generation, our Correspondence-Guided Geometric Optimization converts feed-forward reconstruction priors into reliable cross-view constraints and builds a coherent 3D Gaussian Splatting representation as 3D spatial memory. Adapted single-image and video priors then restore appearance and complete continuous trajectories while preserving observed content. The reconstructed scenes support arbitrary RGB-D rendering and an automated curation pipeline that combines end-to-end 3D grounding with VLM-based verification. Holi360 contains over 1K multi-room 3DGS scenes, more than 100K instance annotations, and 2M spatial question-answer pairs. We also introduce the Holi360 benchmark to evaluate the spatial understanding of VLMs in real-world, multi-room indoor environments. Experiments demonstrate superior reconstruction and curation quality under sparse panoramic inputs, while fine-tuning VLMs on Holi360 substantially improves spatial reasoning capabilities.

---


### 117. [Structure Before Intelligence: Gating What Agentic Scientific Workflows Release](https://arxiv.org/abs/2610.19507)

**<font color=#1a73e8>作者：</font>** Ashish Acharya, Aman Al Amin, Hong Qin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An agentic scientific workflow can run to completion and still release wrong results: a silent numerical error, a stale input, or a defect in a shared upstream step can contaminate several outputs while a sibling branch stays correct. We treat trust in such results as a release decision. A harness around the workflow's directed acyclic graph (DAG) decides which outputs may be used: it enforces mandatory checks, contains failures to the affected branch, recomputes from tracked versions, adds validators, and releases a result only if a risk model estimates its probability of being invalid as low. Language-model agents work inside the harness, choosing corrective actions and reviewing releases, but cannot override it. On 60 held-out paired instances of two workflows with injected faults, we switched components on and off. Each supplied a different property. Containment and recovery raised the number of correct results. Validation supplied safety: fixed rules without validation released 37 invalid results, while validating every candidate released none. Risk estimation supplied efficiency, matching that safety with 31% fewer validators at somewhat lower yield, although better targeting than random validation was not shown. Lineage evidence helped on one workflow. The language model added no measurable benefit: whether invalid results escaped depended on the harness, not the model. This proof of concept points to a practical path: placing agents inside explicit release-control structure can keep released scientific results trustworthy, and it gives more capable agents a measurable baseline to improve on.

---


### 118. [One Block Ahead: Promoting Sampler State in Diffusion Language Models](https://arxiv.org/abs/2610.19510)

**<font color=#1a73e8>作者：</font>** Yangyi Shen, Pin-Jui Ku, Nicolai Oswald 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Block-diffusion language models denoise a whole block of token positions in parallel so each forward pass can emit many tokens. However, blocks are still denoised in strict sequence, a cost that within-block acceleration leaves untouched. Here, we investigate decoding blocks concurrently and propose One Block Ahead (OBA), a training-free decoding algorithm that denoises the next block alongside the current one. We demonstrate that for uniform-state diffusion LMs, where a block's denoising progress is not visible in its intermediate tokens, concurrent decoding is advantageous if the next block's tokens are promoted together with the corresponding sampler state, including the self-conditioning signal and the denoising time. We also derive a break-even criterion that relates the benefit of OBA to the relative cost of a paired-block forward pass. On DiffusionGemma, a state-of-the-art diffusion LM, OBA increases the tokens per forward pass by 42.3% (from 15.64 to 22.25) and the single-request denoising throughput by 16.3%, averaged over ten benchmarks, with a small accuracy regression.

---


### 119. [VLRLA: Deployment-Time Adaptation of Vision-Language-Action Models through In-Context Reinforcement Learning](https://arxiv.org/abs/2610.19517)

**<font color=#1a73e8>作者：</font>** Diyuan Shi, Yiqi Tang, Hongyin Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-language-action (VLA) models connect visual perception and language understanding with robot control, providing a foundation for instruction-conditioned manipulation. However, conventional pretrained VLA policies lack a mechanism for gradual adaptation through accumulated interaction experience during deployment. We therefore propose VLRLA, a general framework that equips existing VLA models with \textit{in-context reinforcement learning} capabilities for deployment-time adaptation. Our approach augments a VLA model with a reinforcement learning module that learns from historical observations, actions, rewards, and termination signals. During deployment, the policy gradually refines its action generation and progressively improves task success while keeping model parameters fixed. Our approach is also designed for general applicability and compatibility with diverse learning history construction strategies and model training pipelines. Finally, through extensive experiments, we systematically investigate the learning properties of VLRLA in simulation and demonstrate its ability to adapt to unseen scenarios during real-world deployment.

---


### 120. [Spectral World Renderer: Unified 3D Hyperspectral Unmixing](https://arxiv.org/abs/2610.19520)

**<font color=#1a73e8>作者：</font>** Chia-Ming Lee, Yu-Jou Hsiao, Ming-Ching Chang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cameras and the foundation models built on them recognize what a 3D scene contains, but not what it is made of: surfaces of the same colour can be different materials. Hyperspectral unmixing explains each spectrum as a mixture of material signatures, yet in 3D it is applied to rendered images after the views are composited, or tied to slow implicit fields, and no multi-view data with known composition exist to check the result. We present the Spectral World Renderer (SWR), which unifies world generation and unmixing. A coding agent builds executable 3D worlds that are rendered with measured spectra, so every hyperspectral image comes with exact labels and sub-pixel proportions; the resulting SWR-Bench provides eight indoor and outdoor worlds in which decompositions can be verified. SWR then unmixes inside rendering: each Gaussian of a compact 3D representation is decoded into material abundances before compositing, so one render yields spectra and material maps, and any surface can be queried by material name, a clicked pixel or a reference spectrum. Without material labels, SWR identifies materials best in all eight worlds, has the best mean PSNR on real captures, trains 3.7-12.9x faster than unmixing baselines, renders 34.9 labelled views/s and separates same-coloured materials.

---


### 121. [HyrCap: Hybrid Rank-Calibration of Action Proposals for Temporal Event Understanding](https://arxiv.org/abs/2610.19526)

**<font color=#1a73e8>作者：</font>** Rui Chen, Xingyu Chen, Pengxin Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Temporal action detection in long untrimmed videos suffers from inaccurate localization and low-quality proposals, especially with sparse annotations and ambiguous boundaries. For open-ended video understanding and LLM-driven event analysis, reliable proposals connect temporal localization, event annotation, and semantic understanding. However, conventional temporal action detection (TAD) pipelines lack explicit modeling of proposal localization quality, cross-representation support, and inter-proposal relations. We propose Hybrid Rank-Calibration of Action Proposals (HyrCap), a proposal-centric query-based TAD framework for temporal event understanding. Hybrid combines complementary video features with different localization cues, while Rank-Calibration adjusts proposal ranking confidence to reflect localization reliability and candidate competition. HyrCap treats dense query-based predictions as an over-complete temporal event hypothesis space. Cross-Representation Consensus Calibration, Localization Quality Estimation, and Proposal Redundancy Suppression improve proposal ranking reliability, localization quality, and candidate discrimination. Inspired by LLMs' capabilities in fine-grained semantic recognition, event description, and reasoning, we introduce HyrCap for Semantic Action Understanding, using calibrated proposals for standard TAD and as inputs to LLM-based semantic understanding. We define a staged evaluation protocol to separately measure event localization, segment-level semantic understanding, and combined event understanding performance. Experiments on public benchmarks show that HyrCap achieves state-of-the-art performance across multiple metrics and provides a finer-grained paradigm and evaluation protocol for query-based event segmentation and annotation.

---


### 122. [Retrieve What Helps, Only When It Helps: Agentic Reinforcement Learning for Selective Retrieval-Augmented Machine Translation](https://arxiv.org/abs/2610.19528)

**<font color=#1a73e8>作者：</font>** Shijun Li, Yang Liu, Najmeh Sadoughi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieving external knowledge can improve large language model (LLM) translation by providing supplementary information such as idiom interpretations and terminology. However, existing retrieval-augmented machine translation systems typically apply predefined retrieval strategies uniformly across all inputs. We argue that translation operates in a partial-evidence regime: LLM's parametric knowledge suffices for many inputs, while external evidence benefits a subset and usually supports rather than directly provides the desired translation. This creates two challenges: deciding when to retrieve and what evidence to acquire. We introduce Selective Retrieval-Augmented Translation (SRAT), an agentic reinforcement learning framework that learns when to translate directly or retrieve, what to retrieve, and how to integrate these decisions by optimizing final translation quality. To align evidence retrieval with downstream translation quality rather than simple semantic similarity, we further develop joint Plackett--Luce optimization and translation-quality contrastive training for retriever-training. Experiments on idiom, knowledge-intensive, and document-level translation with offline or online retrieval show that SRAT consistently outperforms never- and always-retrieve baselines, and quality-aligned retriever training provides further gains when similarity-based retrieval is insufficient. The results demonstrate the benefit of treating retrieval as a learnable translation action rather than fixed preprocessing.

---


### 123. [Typed Decision Models on Tabular Data](https://arxiv.org/abs/2610.19536)

**<font color=#1a73e8>作者：</font>** Baowen Zhang, Hangting Ye, Hongyuan Zha  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Typed decision models are language models that answer a question with a fixed set of possible answers by returning a probability for each answer instead of generating text. We study them on tabular data and compare four decision models with three large language models (LLMs) on row classification, fact verification and anomaly detection. Every request is sent in its original form and under 21 types of rewrite that keep its content, such as renaming the options or writing the table in another format. The decision models perform as well as the LLMs at a lower cost. Three of them are also far more robust to how the question is formulated. No model we test is robust to how the table is organized. For every model, at least a third of the row decisions change under some rewrite of the table or the question. The decisions to which a decision model gives low probability are the ones most likely to change. Decision models are a practical choice for tabular decisions, but their robustness remains an open problem.

---


### 124. [GraphRAG-LTM: A Layered Threat Modeling Framework for Attacks on Graph Retrieval-Augmented Generation](https://arxiv.org/abs/2610.19549)

**<font color=#1a73e8>作者：</font>** Yining Tang, Junyu Zhang, Haomiao Qiu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Graph retrieval-augmented generation (GraphRAG) uses document-derived knowledge graphs to assemble evidence for large language model (LLM) answers. Its security depends on both the seed chunks retrieved for a query and the graph evidence assembled from them, yet attacks on this evidence path remain underexplored. We introduce GraphRAG-LTM, a Layered Threat Modeling framework that tests three nested levels of attacker access. BB Query uses ranking feedback to make query edits under a semantic-similarity constraint and demote relevant seed chunks. WB Query uses retriever gradients for the same objective. Graph-aware WB keeps the white-box adversarial query and deletes bridge triplets from the query-specific evidence graph, disrupting multi-hop evidence propagation through localized graph edits. Across datasets, retrievers, and LLM backbones, rank feedback alone reduces answer quality, gradient access strengthens query attacks, and bridge-triplet deletion further impairs supporting-fact retrieval. Further analyses show how seed retrieval and graph evidence jointly contribute to these failures.

---


### 125. [LabCompiler: A Framework for Verifiable Human-Machine Laboratory Execution from Imperfect Protocols](https://arxiv.org/abs/2610.19550)

**<font color=#1a73e8>作者：</font>** Jingyuan Li, Dongzhan Zhou, Minting Pan 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Closing the loop of AI-driven science requires reliably translating natural-language protocols into executable laboratory workflows despite protocol defects and heterogeneous hardware. Existing approaches often couple scientific interpretation with device-specific code generation, making errors difficult to localize and limiting reuse across laboratory platforms. We introduce LabCompiler, a robust protocol-to-execution framework that transforms imperfect natural-language protocols into verifiable human-machine workflows. Its protocol firewall diagnoses and repairs defects before compilation while preserving unaffected content, guided by troubleshooting knowledge accumulated through perturbation-guided self-evolution. A two-level, device-agnostic graph representation separates experimental semantics from hardware-specific implementation and supports capability-based device assignment with coordinated human execution. We further introduce a protocol recovery benchmark covering four controlled perturbation types and naturally occurring errors collected from protocols written by iGEM participants. Experiments show that LabCompiler outperforms frontier LLMs in protocol error correction while enabling coordinated human-machine execution across heterogeneous, partially automated laboratory settings.

---


### 126. [TextVerifier: Seeing Beyond Recognition to Verify Chinese Text Rendering](https://arxiv.org/abs/2610.19551)

**<font color=#1a73e8>作者：</font>** Yiyang Chen, Guo-Hua Wang, Yaoli Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image models increasingly generate readable Chinese text that still contains local rendering defects, such as a character with an extra or missing stroke or a malformed component. Such errors are invisible to OCR and vision-language models, which are trained for recognition and are therefore invariant to the very structural deviations that define a rendering error. We formalize text rendering verification as a target-conditioned problem: given a target character and an image crop, decide whether the crop is a correct rendering of that character. Our verifier TEXTVERIFIER feeds the text tower a character's Ideographic Description Sequence (IDS) rather than a single-character symbol, and is trained on 12.7M crop-IDS pairs plus label-free "same-character, different-quality" hard pairs sampled from the training trajectory of a text-region inpainting model. To evaluate this ability we build TEXTRENDERBENCH-ZH, the first per-character benchmark for generated Chinese text, annotating position, identity, and correctness for 7,358 characters. TEXTVERIFIER reaches an F1 of 0.844, far above OCR confidence (0.526), a general VLM (0.329), and TextPecker (0.590). Used as a per-character reward for Flow-GRPO post-training, it further reduces rendering errors, showing that its score can both detect and correct errors.

---


### 127. [Learning Visual Speech Representations via Cross-Modal Distillation and Joint Face-Lip Modeling](https://arxiv.org/abs/2610.19559)

**<font color=#1a73e8>作者：</font>** Jing-Xuan Zhang, Genshun Wan, Jianqing Gao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Lipreading remains challenging due to the inherent ambiguity of visual speech cues and their sensitivity to head pose and video resolution. In this work, we propose FLARE, a framework for robust visual speech representation learning via cross-modal distillation and joint face-lip modeling. FLARE leverages semantically rich Whisper representations as the acoustic teacher signal, converting them into discrete distillation targets through a random-projection quantizer and pretraining the model with a masked prediction objective. To capture complementary visual information, FLARE employs a dual-stream architecture that jointly processes lip region-of-interest (ROI) and full-face inputs, where the lip stream captures finegrained articulatory motion and the face stream encodes broader facial dynamics. During pretraining, auxiliary audio input is incorporated to facilitate cross-modal alignment, and modality dropout is applied to encourage robust visual-only representations. For downstream lipreading, FLARE serves as a visual encoder coupled with either a lightweight Transformer decoder or an LLM-based decoder. Evaluated on LRS2, LRS3, and the out-of-domain WildVSR benchmark, FLARE achieves strong lipreading performance, with word error rates of 11.7%, 13.2%, and 34.3%, respectively. A progressive design study confirms the contribution of each major component. Further analyses demonstrate that joint face-lip modeling improves robustness under degraded video resolution and large head pose variation, while yielding more phoneme-discriminative visual representations. Code and pretrained models are available at this https URL.

---


### 128. [$τ$-Emotion-Bench: Exposing the Interaction Fragility of LLM Agents through Real-World User Emotions](https://arxiv.org/abs/2610.19560)

**<font color=#1a73e8>作者：</font>** Rishitosh Kumar Singh, Amir Saeidi, Shamanthak Hegde 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In long-horizon tool-calling tasks, LLM agents can fail not only because of tool-use errors, but also because of ineffective interaction with users. Yet existing benchmarks largely assume cooperative and behaviorally stable users, leaving the effect of emotional variation on agent reliability underexplored. We introduce $\tau$-Emotion-Bench, a ten-domain benchmark for evaluating tool-calling agents under controlled emotion-conditioned user interactions while preserving the underlying task objective. To scale both benchmark construction and agent training, we introduce Tracer, a scalable agentic data-generation pipeline that constructs grounded, policy-valid tasks and collects trajectories through an interactive agent--user--environment harness. By allowing dissatisfied users to terminate inefficient interactions, the harness provides an interaction-aware signal that filters trajectories with excessive user dependence and favors effective tool use. Experiments with two user simulators show that frontier agents remain unreliable, with substantial gaps between average task success and consistent task completion. Tracer-generated supervision consistently improves Qwen3 models across scales, generalizes to unseen domains, and transfers to $\tau$-Bench and $\tau$-Trait. Behavioral analyses further show that higher task success is associated with a better balance between tool execution and necessary user follow-up. Overall, $\tau$-Emotion-Bench and Tracer provide a scalable framework for evaluating agent reliability under diverse user behaviors and improving tool-calling agents through interaction-aware supervision.

---


### 129. [REWIND: Uncertainty-Guided Trajectory Repair for Test-Time Reasoning](https://arxiv.org/abs/2610.19561)

**<font color=#1a73e8>作者：</font>** Yi Ding, Mengyu Wang, Min Zhou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> An early mistake in the generated reasoning can constrain all subsequent reasoning. Repeated-generation methods, like MCMC-based approaches, attempt to improve output quality by sampling multiple generations, but their effectiveness can be limited by randomly selecting where to regenerate. On MATH500 with Qwen2.5-Math-7B, we find that incorrect responses have substantially higher mean token entropy than correct responses, with an average within-question relative increase of approximately 112%, suggesting that entropy can signal reasoning errors. Motivated by this finding, we introduce REWIND, a training-free controller that uses entropy dynamics to propose targeted suffix regenerations. Across three model families and five benchmarks, REWIND outperforms all baselines, with gains of 0.51-10.00 percentage points over the strongest baseline. These results demonstrate the effectiveness of targeted, uncertainty-guided trajectory repair across models and tasks. Our code is available at this https URL.

---


### 130. [Frame Evidence:A Benchmark for Reference Frames and Visual Evidence in Multi-Image Spatial Reasoning](https://arxiv.org/abs/2610.19564)

**<font color=#1a73e8>作者：</font>** Chunxi Luo, Qishuai Ding, Xingchen Peng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A spatial answer depends on the reference frame specified in language and its supporting visual evidence. Item accuracy alone obscures whether correctness persists when either changes. We introduce Frame Evidence, a benchmark of 320 matched triplets and 960 Chinese multiple-choice questions from captured and rendered scenes. One family compares three grounded reference frames over fixed images. The other pairs image deletion annotated as insufficient with answer-preserving addition. Joint metrics require correct answers across all three frames and paired evidence variants. Across 20 configurations on 288 held-out questions, GPT three-shot reaches 50.00\% item accuracy, but the best three-frame group accuracy is 5/48 (10.42\%), reached by GPT two-shot. Few-shot prompting and task-specific adaptation improve item accuracy without consistently improving joint correctness. Input controls show where images support matched success, while repeated executions reveal answer instability beneath similar scores.

---


### 131. [Mission (Im)Possible: Towards Autonomous Discovery of Autopilot Logic Flaws in Open-Source Drone Frameworks](https://arxiv.org/abs/2610.19566)

**<font color=#1a73e8>作者：</font>** Ziyi Liang, Zichuan Li, Bin Yuan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Autonomous drones are increasingly deployed in safety-critical tasks, yet their autopilot software can still contain subtle logic flaws that lead to unsafe behaviors. These flaws are difficult to discover with existing techniques because they often depend on semantic relationships across modules, commands, and runtime state, and rarely manifest as crashes or detectable failures. With recent advances in LLMs, we observe that, when equipped with essential domain knowledge and carefully crafted context, LLMs demonstrate strong capabilities in understanding the high-level semantics of autopilot systems, making them suitable for logic flaw discovery. However, LLMs are limited by their context and can be biased to the vulnerabilities frequently occurs in training dataset, while logic flaws often require higher-level semantic bug oracles to identify their existence. To bridge the gap, we present Impossible Mission Finder (IMF), a multi-agent system combining static analysis, dynamic execution and log analysis, that supports fully automated identify, test, and validate logic flaws in autonomous vehicles. IMF primarily contains three LLM agents, it first uses the auditor agent to propose logic flaw hypothesis based on carefully-crafted program slicing, then it launches tester agents to write and execute test cases for each candidate, and finally it spawns the log analyzer agent to validate the execution log against the flaw hypothesis. This enables IMF dynamically validate bug oracles in a case-by-case manner, making it suitable for discovering logic flaws that do not have a unified pattern. We evaluated IMF on two widely used open-source autopilot systems, PX4 and Ardupilot, leading to 105 previously unknown logic flaws, that can cause unsafe behaviors including mission interruption failures, invalid actions, entering into restricted fly zones etc.

---


### 132. [INTACT: Inducing Latent Reasoning on a Frozen Backbone](https://arxiv.org/abs/2610.19568)

**<font color=#1a73e8>作者：</font>** Kutay Tire, Atula Tejaswi, Haris Vikalo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Latent reasoning replaces natural-language chains of thought with compact continuous "soft-token" representations, reducing the number of intermediate tokens that must be decoded autoregressively. We use a small external encoder to induce latent reasoning in a frozen backbone model. The encoder iteratively maps the backbone's hidden states to new latent blocks, constructing a latent reasoning prefix, after which the frozen model writes its remaining reasoning and its answer as text. Our method, INTACT, trains this encoder through distillation to reproduce the effect of written reasoning steps while keeping the model's behavior close to that of the frozen backbone, and then reinforces it on answer correctness. Across four frozen backbones from 1B to 8B, INTACT improves both GSM8K and average out-of-domain accuracy, including GSM8K gains from 75.8% to 79.3% on Llama-3.2-3B and from 77.6% to 79.7% on Qwen2.5-3B. It also reduces end-to-end latency per problem by 19% on Llama-3.2-3B and outperforms the evaluated latent-reasoning baselines at the 3B and 8B scales. Beyond the mathematics setting, the same recipe trained on a multi-domain corpus improves the frozen backbone on twelve evaluation benchmarks spanning mathematics, science, and commonsense, without task-specific adaptation.

---


### 133. [LED-BENCH: A Benchmark for Large-format Engineering Drawing Understanding](https://arxiv.org/abs/2610.19571)

**<font color=#1a73e8>作者：</font>** Ke Li, Tianyi Wang, Enning You 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-world engineering drawings are often large-format and information-dense. Answering practical engineering questions therefore requires both fine-grained understanding of engineering information and complex reasoning over objects, relations, and evidence distributed across different regions or views. Existing benchmarks cover a range of engineering-drawing understanding tasks involving local regions, individual views, specific elements, or more constrained visual settings. However, systematic evaluation of understanding over realistic, large-format engineering drawings remains limited. To address this gap, we introduce LED-BENCH, a multidisciplinary benchmark designed to evaluate fine-grained understanding and complex reasoning over large-format engineering drawings, spanning the mechanical, architectural, and transportation domains. Extensive evaluation of 11 representative multimodal large language models, including 8 proprietary models and 3 open-source models, reveals substantial remaining difficulty: GPT-5.6 Sol achieves 52.65% average accuracy, performance varies across engineering domains, and all evaluated models perform worse on questions requiring broader evidence integration. These results highlight fine-grained understanding, evidence integration, and complex reasoning over large-format engineering drawings as persistent challenges for current multimodal models.

---


### 134. [Divergence-Routed On-Policy Distillation for Language Models](https://arxiv.org/abs/2610.19572)

**<font color=#1a73e8>作者：</font>** Tiantian Peng, Guannan Lv, Hongyang Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) transfers knowledge from a teacher model to a student along student-generated trajectories, typically by minimizing the reverse Kullback-Leibler (RKL) divergence. However, RKL can provide weak corrective signals for teacher-supported tokens to which the student assigns very low probability. This raises two questions: which positions are most consequential for the behavioral gap between the student and teacher, and what additional supervision is needed at these positions? Through cross-sampling, we find that divergence-based routing more effectively pinpoints positions contributing to the teacher-student performance gap than entropy-based routing. Further analysis reveals teacher-mode under-coverage at high Jensen-Shannon (JS) divergence positions, where standard OPD increases the large teacher-student probability gaps. Motivated by these findings, we propose Divergence-Routed On-Policy Distillation (DrOPD). DrOPD retains RKL supervision at all positions and selectively adds forward Kullback-Leibler (FKL) divergence supervision at positions with high JS divergence. Experiments across six math benchmarks show that DrOPD improves over standard OPD and entropy-based routing. DrOPD also reduces severe under-coverage cases by 37.9 percent relative to OPD, supporting targeted FKL as an effective complement to OPD.

---


### 135. [XferAgent: Cross-Agent Experience Transfer for Self-Improving LLM Agents](https://arxiv.org/abs/2610.19581)

**<font color=#1a73e8>作者：</font>** Weihao Li, Jun Bai, Shijie Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents can reuse experience from prior task executions to improve performance on subsequent tasks. Although existing methods enable cross-agent experience sharing, differences in agents' execution histories and task requirements make shared experiences difficult to reuse effectively. We propose XferAgent, a framework for cross-agent experience transfer that organizes reusable experience in local and shared experience graphs. XferAgent reconciles compatible contributions from heterogeneous agents while avoiding unreliable merges. For each new task, it selects shared experiences and integrates them with the target agent's local experience to support task execution. Experiments across diverse task domains show improvements over representative memory-based methods and effective experience transfer between heterogeneous agent frameworks. Cumulative task success also increases over successive task passes as agents update and reuse their experiences.

---


### 136. [Who's Behind the Text? Robust Model Authorship Attribution](https://arxiv.org/abs/2610.19583)

**<font color=#1a73e8>作者：</font>** Minseok Ko, Hyunseok Lee, Woomin Song 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) are increasingly used to generate text, their misuse has become a growing societal problem, with implications for academic misconduct, model distillation, and cyberattacks. For these reasons, Model Authorship Attribution (MAA), which identifies the source model of a given text, is important for promoting the responsible use of LLMs and improving AI safety. In practice, attribution systems must remain reliable beyond the distributions observed during training. They may encounter texts from unseen domains and writing settings, as well as generations from future versions of model families that were not available when the system was trained. However, existing MAA methods often exhibit substantial performance degradation under such distribution shifts. To address this challenge, we propose Authorship Tracing via Likelihood-based Attribution of Sources (ATLAS), which formulates MAA through source-conditioned text modeling rather than direct source prediction. ATLAS learns how text from each source family is generated and attributes a given text by comparing its likelihood under each learned source condition. We aggregate this likelihood evidence at the token level with clipping so that no single token dominates the decision. We further introduce MAABench, a broad MAA benchmark for evaluating practical OOD settings such as domain and version. Our experiments show that ATLAS consistently outperforms existing baselines across MAABench and OpenTuringBench. In particular, when both the generation domain and the model version change on MAABench, ATLAS achieves 74.27% accuracy, 9.00pp higher than the strongest baseline. Beyond MAA, ATLAS can also help identify distillation source models by measuring which source model a target LLM most closely resembles. Our extended experiments show that ATLAS recovers the known teacher of every distilled model we evaluate.

---


### 137. [JockeyBench: Evaluating LLM Agents on Horse-Racing Decision-Making](https://arxiv.org/abs/2610.19589)

**<font color=#1a73e8>作者：</font>** Zhongwei Xie, Xingsu Li, Jingqiao Yu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Repeated event forecasting requires extracting predictive signals from noisy evidence and evaluating their value across successive decisions. We introduce JockeyBench, a benchmark and evaluation protocol that studies this problem through historical Japanese horse racing. The protocol combines time-gated evidence, priced tools, paired frozen-program controls, and two workflows: executing an LLM-written predictor or acquiring evidence for a fresh per-race LLM forecast. Evaluation separates forecast quality, benchmark-specific net utility, and retrospective betting returns and risk under fixed decision rules. Across 28 model--scaffold configurations on 324 races, paired tests identify seven revision gains and two declines after multiple-testing correction. Yet every configuration has negative mean profit under capped-Kelly settlement. In a four-model comparison, the reusable-program workflow has higher mean betting profit and lower research fees, although both workflows lose on average. Further diagnostics reveal that mean probability bias reverses on selected bets and that profitable individual runs can depend on concentrated returns. These findings motivate evaluating predictive competence, adaptation, resource use, and decision value separately when assessing agents for repeated event forecasting.

---


### 138. [L3M: A Verifiable Harness and Runtime for Self-Extending and Self-Improving Agents](https://arxiv.org/abs/2610.19591)

**<font color=#1a73e8>作者：</font>** Carson Eisenach, Robert Joseph George, Vincent Quenneville-Belair 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The lasting gains in AI have come from methods that absorb more computation, and language models already scale computation within a call. Useful work, though, happens across calls: over hours or days, through tools and external systems, among many agents and the humans they work for, and increasingly through code the agents write themselves. Whether that work compounds is enabled by the harness around it, and the harness faces a constraint the model does not: of the three participants in such a computation, the human, the model and code, only the human's attention does not scale, so the computation can grow only if the human is not in every loop. L3M is a runtime built on that premise, written in Lean 4 so that one language implements the harness, states its invariants, and is the language agents extend it in. One computation spans humans, agents, models and code, and all of its state lives in Git: a rich state trajectory -- rather than a chat conversation -- is an object the runtime can resume, rewind, fork, compare and merge. Waiting, communication, delegation and undo are primitives, not patterns the model reasons through each time. When an agent works out a procedure, it can write it once as a sealed Lean program whose type is its permission request, and the harness offers it back as a tool -- machinery for the model to use. To take the human out of the loop, L3M uses reversibility to decide where that is safe: a tool's review tier follows from how far its effects can be undone, so agents act freely where the runtime can recover. Because the machinery can change, the properties that make this safe are stated as kernel-checked theorems about the code that runs. On Terminal-Bench, an untuned L3M reaches about two thirds of its (unsafe) shell-equipped pass rate using only safe (not needing human review) tools.

---


### 139. [PA1-OPD: One-Step Prefix-Augmented On-Policy Distillation for Language Model Pretraining](https://arxiv.org/abs/2610.19601)

**<font color=#1a73e8>作者：</font>** Zhenhe Wu, Jian Yang, Yaping Jin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Knowledge distillation (KD) improves language-model pretraining by matching teacher distributions at corpus prefixes, but provides no direct supervision at contexts induced by student predictions. We introduce PA1-OPD, which augments corpus-path distillation with teacher feedback after one student-sampled transition per selected prefix. This expands the supervised states while retaining next-token prediction and corpus-path KD. Data-anchored roots support parallel sampling, and differentiable tree attention shares prefix computation without changing inference. In two continued-pretraining settings, full coverage improves held-out cross-entropy over KD across C4, PG-19, and Pile at every evaluated checkpoint. In Stage2, selecting the 10% of roots with highest student surprisal adds 48.85% to KD's Macro cross-entropy gain over next-token training. Gains remain when branch supervision excludes successor states already on the corpus path, supporting the value of feedback beyond observed contexts. Additional depth or breadth improves aggregate results at unchanged per-term supervision weight, with benefits varying by corpus. These findings support local student-induced supervision as a complement to pretraining distillation.

---


### 140. [PN-Mix: Pair-Norm Guided Mixed-Precision Key Cache Quantization for Efficient Long-Output LLM Inference](https://arxiv.org/abs/2610.19605)

**<font color=#1a73e8>作者：</font>** Gil Jae Song, Sungjoo Yoo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-output inference in large language models suffers from severe KV cache memory and bandwidth bottlenecks. While KV cache quantization alleviates this issue, low-bit quantization (e.g., 2-bit) severely degrades model accuracy. Recent mixed-precision key-cache quantization methods mitigate this degradation by allocating higher precision to important key channels, but estimate channel saliency using only key statistics. Through attention logit perturbation analysis at the RoPE channel-pair level, we show that quantization errors in channel pairs with large query--key pair-norm products contribute significantly to logit variation. Based on this insight, we propose PN-Mix, a mixed-precision key-cache quantization method for RoPE-based decoder-only LLMs, which allocates higher precision to salient channel pairs identified once during the prefill stage and reused throughout decoding. Across standard reasoning, code-generation, and AIME benchmarks, PN-Mix with 2.26-bit average precision achieves comparable or better average accuracy than prior mixed-precision methods using 2.32--2.39 bits. Furthermore, in our Pareto sweep, PN-Mix degrades gracefully down to 1.5 bits, whereas the compared baselines exhibit sharper performance drops below 2.25 bits.

---


### 141. [A Graph-Based Analysis of Comparability, Scale, and Attribution in Private Transformer Inference](https://arxiv.org/abs/2610.19607)

**<font color=#1a73e8>作者：</font>** Souvik Das, Ariful Azad, Nitesh Saxena  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Rising privacy concerns around large language models have accelerated research in private Transformer inference (PTI). Synthesizing the empirical claims in this line of research, however, is hindered by multi-dimensional cryptographic progress and inconsistent evaluation contracts. In this work, we systematize the field by constructing an empirical graph of 62 PTI systems, mapping system attributes to node features and evaluation compatibility to edges. A three-tiered analysis of this graph illuminates the state of private inference. Node-level attribution shows that cryptographic progress drives performance gains across most systems, yet always co-occurs with other factors (model fidelity, hardware, cost accounting). Edge-level auditing shows that only 1 of 1891 candidate system pairs is directly comparable under shared assumptions. Finally, graph-level analysis shows that the scaling frontier of private inference has plateaued at 13B parameters and projects the cost of deploying current PTI techniques on production-scale Transformers. Overall, this graph-based framework equips the community to evaluate PTI claims transparently and channel technical speedups into deployment-scale private inference.

---


### 142. [CORE: Contrast-and-Reflect for Self-Supervised Prompt Optimization in Anomaly Synthesis](https://arxiv.org/abs/2610.19610)

**<font color=#1a73e8>作者：</font>** Haoxiang Rao, Fang Zhao, Zhao Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Industrial anomaly detection (AD) is bottlenecked by the scarcity of anomalous samples, making high-fidelity anomaly synthesis crucial for improving downstream performance. However, existing methods either rely on scarce real anomaly references or auxiliary data, while lacking complex reasoning and iterative optimization capabilities for generating realistic defects in open-set scenarios. To address these challenges, we propose CORE, a cost-efficient and training-free prompt optimization framework based on Large Multimodal Models (LMMs), which unifies zero-shot and one-shot anomaly synthesis. CORE first introduces an Anomaly Context Grounding module to transform sparse user context into defect-aware generation context, which is subsequently instantiated as structured anomaly prompts that disentangle normal-region preservation from anomaly-specific variation, enabling controllable and faithful defect generation. Furthermore, CORE autonomously refines prompts through a self-supervised contrast-and-reflect mechanism. This design empowers general-purpose LMMs to synthesize realistic anomalies under both zero-shot and one-shot settings without task-specific training. Extensive experiments on MVTec-AD and VisA demonstrate that CORE synthesizes realistic and diverse anomalies, yielding superior improvements in downstream AD performance. Furthermore, its model-agnostic and plug-and-play paradigm enables effortless integration with diverse LMMs, facilitating adaptation to unseen open-set scenarios.

---


### 143. [What Breaks in Multi-Image Schema Application? Factorial Oracle Interventions Reveal an Instance-Information Bottleneck](https://arxiv.org/abs/2610.19611)

**<font color=#1a73e8>作者：</font>** Yiliu Xu, Xinjin Li, Yu Ma  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern vision-language models can accept multi-image contexts, but aggregate accuracy rarely reveals where a multi-image reasoning pipeline fails. We study a controlled schema-application task in which a model must locate two target characters in a 16-image sequence, identify their visual attributes, consult an item-specific visual codebook, and compose two ordered nonce code names. We introduce a within-item 2-by-2 factorial Oracle design: Oracle-A supplies a verified textual schema, Oracle-B supplies a verified ordered target-appearance representation, and both interventions retain the original images and final question. Across 72 new items and 1,188 analyzed model responses, Oracle-B increased strict exact accuracy by 54.6 percentage points (95% confidence interval: 46.3 to 63.0) and outperformed Oracle-A by 60.6 points (Holm-adjusted p-value no greater than .0002). An auxiliary retrieval diagnostic reached only 49.1% ordered-appearance accuracy even after removing code-name generation. Providing both Oracle sources yielded 100% accuracy across all models. These results localize the dominant recoverable deficit to upstream ordered instance recovery rather than primarily to downstream schema use and composition.

---


### 144. [Divergent Paths: Learning an Outcome-Predictive Representation of LLM Agent Trajectories](https://arxiv.org/abs/2610.19614)

**<font color=#1a73e8>作者：</font>** Alexander Gill, Guram Gogia, Francisco Guzmán  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this work, we reframe agentic trajectories as paths through a shared embedding space of actions and environmental observations. We show that successful and failed rollouts of the same task separate in this space, with simple per-task discriminators predicting held-out rollout outcomes at up to 0.95 AUROC across three agent benchmarks and three policy models. To exploit this signal across tasks, we introduce Precog-RM, a transformer-based model that meta-learns a representation in which outcome prediction can be performed in a few-shot setting. We show that Precog-RM generalizes to unseen tasks and models, and gives confident predictions of trajectory success long before termination. Deployed as an early stopping controller for Group Relative Policy Optimization (GRPO) on Tau2-Bench, Precog-RM cuts training FLOPs by up to 47.3\% while maintaining performance comparable to baseline GRPO.

---


### 145. [DAGFormer: Global Topology Prediction for Transformer Cross-Layer Connections](https://arxiv.org/abs/2610.19625)

**<font color=#1a73e8>作者：</font>** Xiaocong Yang, Yuren Hao, ChengXiang Zhai  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We propose DAGFormer, a Transformer language model whose cross-layer connections are planned by a jointly trained topology predictor. Beyond the residual connections in a standard Transformer, DAGFormer adds direct connections from earlier layers to later ones, and the predictor controls the strength of every connection based on input tokens. Unlike existing cross-layer routing architectures, which set each layer's connections separately, DAGFormer plans the routing of the whole model at once. On matched OLMo-2 pairs from 75M to 1B parameters, DAGFormer lowers WikiText-2 perplexity by 17% to 25% over the vanilla Transformer, and a 1B DAGFormer trained on 5B tokens outperforms the vanilla model trained on 10B. Against four routing baselines with the same data and budget, it reaches the lowest perplexity at 75M, 300M and 1B. The gain carries over to 13 commonsense, science, reading and math evaluation tasks (2.0 to 2.5 points higher mean accuracy at 300M and 1B) and to instruction finetuning (63% to 70% AlpacaEval win rate against the vanilla Transformer, leading every routing baseline), and under structured pruning DAGFormer degrades the least in five of six settings.

---


### 146. [Sparse Autoencoders Are a Shared Coordinate System for Symbolic Matching](https://arxiv.org/abs/2610.19636)

**<font color=#1a73e8>作者：</font>** Xiaocong Yang, Xuanyu Meng, Yuji Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) hold broad knowledge in one set of weights, but lack interpretability and trustworthy reasoning, especially in high-stakes use cases. A neuro-symbolic model, with its interpretable architecture and System 2 reasoning capacity, is a promising alternative if built at the scale of LLMs; however, its symbolic backbone is usually constructed with human effort, so existing neuro-symbolic models are bottlenecked by the scope of the symbol component and usually domain-specific. A data-driven method could instead build a larger symbolic system by aligning and merging existing ones. We target its first, foundational step: matching units across these heterogeneous systems. Our method, SAE-IDF, encodes a symbol in its native context into a sparse code with a sparse autoencoder (SAE), re-weights each dimension by its rarity and matches across systems. On 12 tasks across 6 kinds of symbolic system, SAE-IDF outperforms the same LLM's dense baseline on all tasks with Gemma-2-9B and all but one with Llama-3.1-8B, by up to 45 points, consistently across SAE layers and configurations. SAE-IDF is also interpretable: every dimension of the sparse code has a human-readable meaning, so each match decomposes into named concepts (features). Our work paves the way to a universal symbolic backbone.

---


### 147. [J-tau: A Fully Localized Japanese Benchmark for Tool-Agent-User Interaction](https://arxiv.org/abs/2610.19638)

**<font color=#1a73e8>作者：</font>** Chihiro Yano, Jun Hirako, Hiroaki Yamagiwa 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present J-tau, the first publicly available Japanese benchmark for evaluating tool-using LLM agents in interactive customer-support scenarios. While tau-bench is widely used to evaluate LLM agents, it is English-centric and cannot evaluate agents in other languages. Existing multilingual extensions offer no public Japanese version and rely primarily on machine translation, leaving locale-specific entities such as addresses and currencies inconsistent with the target region. To enable reliable evaluation in Japanese, we carefully localize tau-bench through machine translation, entity adaptation, and human review. During this process, we also uncover and fix two flaws in the original tau-bench: invalid tasks and a score aggregation error that inflates certain models' results. Experiments show that J-tau yields fewer evaluation errors than a naively machine-translated counterpart and that our fixes resolve both flaws.

---


### 148. [Model What Matters: Decision-Guided Selective World Modeling for Language Agents](https://arxiv.org/abs/2610.19642)

**<font color=#1a73e8>作者：</font>** Maolin Ran, Minda Chen, Di Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning provides a direct mechanism for optimizing task objectives in large language model-driven agents, but task rewards are typically sparse trajectory-level signals that only evaluate task success, without directly supervising action-conditioned environment transitions, leaving the model with limited explicit understanding of action consequences and environment dynamics. Recent work introduces auxiliary supervision through policy and world modeling co-training, yet typically treats complete environmental observations uniformly as world modeling targets, overlooking the varying decision relevance of observation content. We propose DGS-WM (Decision-Guided Selective World Modeling), a decision-guided policy-world modeling co-training approach for language agents. DGS-WM employs a Decision-Guided Observation Selection component that filters observation units with decision value as world modeling targets based on their support for subsequent policy responses, and a Confidence-Adaptive Weighting component that adaptively adjusts supervision strength according to the model's prediction confidence on selected targets. Together, these components form a decision-aware auxiliary world modeling loss, jointly optimized with the RL loss on the same policy model. Across multiple benchmarks covering single-hop/multi-hop question answering and interactive web tasks, DGS-WM achieves consistent improvements under different model scales and RL algorithms, demonstrating more stable and effective performance compared to full-observation world modeling methods.

---


### 149. [Selective Reasoning for Typed Decision Models: When to Start, Read, and Stop](https://arxiv.org/abs/2610.19644)

**<font color=#1a73e8>作者：</font>** Bin Zheng, Zheng Chen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Typed decision models need an interface that can use additional reasoning while retaining candidate outputs. We train a shared candidate-answer reader on a frozen Qwen3.5-4B backbone to unify direct decisions with on-demand, interruptible reasoning. The reader returns distributions from empty and partial reasoning prefixes. A benefit gate starts reasoning, a natural-state trigger requests explicit reads, and an entropy rule accepts acquired answers and cancels generation. Measurements distinguish answer-query work, generated output, and pipeline time. Across 768 questions from ProofWriter, LogiQA 2.0, and ARC-Challenge, accuracy rises from 70.96% for direct reading to 84.38%. Relative to 512-token terminal reading, accuracy improves by 7.29 percentage points with 2.25% more mean output work. Relative to 1,024-token terminal reading, pipeline time falls by 46.30% with an accuracy difference of -1.17 points. Exact-prefix controls isolate the saving from interruption, while read-scheduling controls distinguish reduced observation work from shorter response time.

---


### 150. [SPECTRA-VLA: Base-Fine Hyperspectral Token Transfer at Frozen Vision-Language-Action Interfaces](https://arxiv.org/abs/2610.19651)

**<font color=#1a73e8>作者：</font>** Chih-Chung Hsu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hyperspectral imaging distinguishes RGB-similar objects, but a pretrained vision-language-action model needs a state its frozen decoder can use. SPECTRA-VLA provides a native-width spectral upgrade without retraining the visual encoder or action decoder. A learned continuous residual enriches each target token through its own normalized false-color reference; projection, norm control and validation-calibrated injection regulate the change. Across 86 held-out acquisitions, category balanced accuracy rises from 0.812 to 0.883. With identical residuals and scale, own-token addition improves reuse of an external category-derived probe on frozen decoder logits: 0.701 versus 0.590 with pooled replacement, at similar image-disjoint recognition. Five grouped tests covering the same 86 acquisitions recover within-category spectral shape with $R^2=0.802/0.337$ from continuous and posterior-code states. Category-matched spectral swaps further show that own-token composition approximately doubles the target-specific recovery increment after frozen decoding. Spectral enrichment and receiving-token preservation thus work together at the pretrained interface.

---


> [!TIP]
> 当前位于：**101-150**（第 3/7 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-313](./part-07.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
