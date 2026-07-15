# 🧠 大模型相关研究 | 2026年07月16日

> 本类共 **99** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**51-99**（第 2/2 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-99**

---

### 51. [DynTrace: Tracking Dynamic Object Evidence for 4D Spatio-Temporal Reasoning in MLLMs](https://arxiv.org/abs/2607.12503)

**<font color=#1a73e8>作者：</font>** Rongxin Gao, Yuzhi Huang, Dongxuan Liu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 4D spatio-temporal reasoning, jointly modeling 3D spatial structure and temporal evolution, is essential for understanding dynamic worlds and enabling embodied interaction. While current Multimodal Large Language Models (MLLMs) show strong capabilities in static scene understanding and coarse-grained 4D tasks, they still have notable limitations in continuous dynamic scene perception, especially in tracking dynamic object evidence for coherent 4D spatio-temporal reasoning. This shortcoming stems mainly from relying on sparse frame-level observations, fragmenting continuous dynamic cues and leaving models unable to disentangle genuine object dynamics from camera-induced apparent motion. Inspired by humans tracking dynamic cues while compensating for viewpoint changes, we propose DynTrace, a training-free framework for 4D spatio-temporal reasoning with two complementary components. Dynamic Trajectory Visualization (DTV) reprojects world-coordinate trajectories onto the image plane, providing geometry-informed visual priors that disentangle genuine object dynamics from camera-induced apparent motion. Meanwhile, the Dynamic Trace Token (DT-Token), organized into a Dynamic Trace Graph (DTG), tracks object-level dynamic cues, trace evolution, and key moments, maintaining continuous dynamic object evidence for coherent 4D reasoning. Together, these two components equip MLLMs with continuously tracked dynamic object evidence, grounded in geometry-informed visual priors and structured spatio-temporal traces. DynTrace consistently improves open-source MLLMs, achieving state-of-the-art results on Dyn-Bench, VLM4D, and DSI-Bench, validating the importance of tracking dynamic object evidence for robust 4D spatio-temporal reasoning.

---


### 52. [The Model Knows Your Project, Not You: Measuring Recognition in LLMs with NameRank](https://arxiv.org/abs/2607.12520)

**<font color=#1a73e8>作者：</font>** Bojie Li, Noah Shi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> What a frontier model recalls about a person or tool from its own weights -- before any retrieval step -- often shapes the first description a human sees, making that parametric corpus presence a measurement problem. Citations explain about a third of whether a model recognizes a researcher; we target the residual and build NameRank, a [0,1] recognition score: each of 4,685 entities in 54 cohorts is probed with one open-ended question across 36 models, and an independent judge returns a binary verdict against a curated gold -- did the model state a specific, non-guessable fact about this exact entity? -- so hallucination, context echo, and guesses earn nothing. Synthetic-null entities hold the floor near zero, and verdicts track the entity, not the model. One thesis organizes the findings: recognition is paid to named, indexable artifacts, not to credentials or titles. Every Olympic-style credential sits below a working-researcher baseline, because no named artifact ships with the medal, yet the ranking inverts at the marquee tier, where Nobel, Turing, and Fields laureates saturate the panel. For independent creators the tool out-ranks its maker, and the credential that does propagate is a named method or awarded paper. Being one of many named contributors to a celebrated artifact, by contrast, earns almost nothing -- the authors listed on a flagship model report or system card sit near the recognition floor -- because recognition attaches to the artifact's own distinctive name, not to the roster behind it. No bibliometric predicts recognition well; top-density institutions out-recognize peers at matched citations; and on 258 news events recognition loads on peak salience, not persistence. A self-report probe shows introspection reads a corpus prior, not its own knowledge.

---


### 53. [A JoLT for the KV Cache: Near-Lossless KV Cache Compression via Joint Tucker and JL-Residual Allocation for LLMs](https://arxiv.org/abs/2607.12550)

**<font color=#1a73e8>作者：</font>** Rahul Krishnan, Volker Schulz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The key-value (KV) cache has become the dominant memory cost of transformer inference. It grows with batch size, context length, and depth, and at long context it, rather than the model weights, sets the ceiling on throughput. Two families of methods reduce it. Low-rank methods factor two-dimensional slices of the cache, either per-head matrices or cross-layer feature blocks, and quantization methods lower the bit-width of every entry. Neither family exploits the fact that the cache at a layer is naturally a third-order tensor whose three axes, the heads, the tokens, and the features, carry very different amounts of redundancy. We take this tensor view directly. Our method, JoLT, applies a partial Tucker decomposition that compresses only the token and feature axes while leaving the head and layer axes intact, and then restores the energy that truncation discards with a Johnson-Lindenstrauss (JL) rotated low-bit residual. A single Lagrangian dual allocates the Tucker ranks and the residual bit-widths together, per layer group and separately for keys and values, under one byte budget. The result is a near-lossless 2-3x compression: perplexity, GSM8K accuracy, and RULER needle-in-a-haystack retrieval all stay at or within statistical noise of the uncompressed baseline on both a grouped-query-attention model (Mistral-7B-v0.3) and a multi-head-attention model (LLaMA-2-13B). At 2x, JoLT reconstructs the cache to relative Frobenius error 0.009 (K) and 0.006 (V) on both architectures, roughly an order of magnitude below cross-layer SVD and 4-bit quantization. A randomized-SVD variant, FlashJoLT, delivers a 5-13x compression-time speedup at matched quality.

---


### 54. [Gaussian Mixture Modeling for Event-Aware Visual Allocation in Long Video Understanding](https://arxiv.org/abs/2607.12557)

**<font color=#1a73e8>作者：</font>** Yifan Lu, Ziqi Zhang, Chunfeng Yuan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Vision-Language Models (LVLMs) face significant challenges in long video understanding due to the excessive computational cost and information loss associated with uniform sampling. Existing keyframe selection methods often treat video frames as atomic entities and allocate visual budgets equally, thereby overlooking high-level semantic structures and introducing substantial redundancy. To address these limitations, we propose GMM-EVA (Gaussian Mixture Modeling for Event-Aware Visual Allocation), which leverages Gaussian Mixture Models to model event-level structure from discrete frame-wise observations. A differentiated allocation strategy is then applied to preserve one primary high-resolution keyframe per event for high-fidelity detail, while utilizing lower-resolution secondary keyframes to maintain temporal context and optimize token budgets. GMM-EVA is a training-free, plug-and-play framework that generalizes robustly across various relevance measures and downstream LVLMs. Extensive experiments on multiple long video benchmarks demonstrate that our method significantly outperforms uniform sampling. Notably, GMM-EVA achieves comparable performance to baseline selection methods while utilizing only approximately half of the visual token budget, highlighting its superior efficiency and effectiveness.

---


### 55. [Agentic Service-Oriented Computing: A Manifesto for the Next Frontier of Service-Oriented Computing](https://arxiv.org/abs/2607.12619)

**<font color=#1a73e8>作者：</font>** Amin Beheshti, Rong N. Chang, Boualem Benatallah 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rapid emergence of LLM-powered autonomous and semi-autonomous agents is reshaping software systems from static, request-response components into goal-directed, adaptive, and tool-using computational actors. As these agents move from isolated cognitive prototypes into complex distributed workflows, they confront challenges that the Service-Oriented Computing community has studied for more than two decades: composition, interoperability, quality of service, lifecycle management, governance, security, and trust. Yet much of today's agentic AI ecosystem is developing these foundations ad hoc, without the engineering rigour required for dependable enterprise and societal deployment. This paper introduces Agentic Service-Oriented Computing (ASOC) as a new research and practice area concerned with engineering agents as services, orchestrating services through autonomous and semi-autonomous agents, and governing ecosystems of agents and services under constraints of trust, cybersecurity, compliance, performance, and accountability. We articulate six foundational principles of ASOC (harness-ability, composability, lifecycle engineering, trustworthiness by design, goal-driven orchestration, and observability/accountability) and organise a five-dimensional research agenda spanning: (i) agentic services foundations and lifecycle engineering; (ii) composition, orchestration, and interoperability; (iii) governance, observability, and accountability; (iv) security, trust, and risk management; and (v) evaluation, certification, and Agentic QoS. We argue that the Services Computing community is especially well positioned to provide the conceptual and engineering spine for this emerging field, transforming agentic AI from fragmented demonstrations into dependable, service-based systems worthy of human and organisational trust.

---


### 56. [Towards Vision-Free CIR: Attribute-Augmented Scoring and LLM-Based Reranking for Zero-Shot Composed Image Retrieval](https://arxiv.org/abs/2607.12621)

**<font color=#1a73e8>作者：</font>** Ryotaro Shimada, Yu-Chieh Lin, Yuji Nozawa 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent work has shown that "Vision-Free'' approaches (representing images as text) can be effective for standard image retrieval tasks. However, it remains unclear whether this paradigm can effectively handle a more complex, multimodal task, Composed Image Retrieval (CIR), due to the inherent information loss in textual descriptions. In this paper, we introduce a Vision-Free CIR framework that addresses this challenge through two key techniques: (1) Attribute-Augmented Hybrid Scoring, which compensates for lost visual details via explicit attribute matching, and (2) LLM-Based Reranking, which verifies semantic consistency of top candidates. Experiments on the open-domain CIRR dataset show that our approach outperforms existing Zero-shot CIR methods (44.04% R@1, +8.79%). On FashionIQ, our results highlight the trade-off between semantic reasoning and fine-grained visual matching. Ablation studies reveal that both attribute-augmented scoring and LLM-Based Reranking consistently improve performance.

---


### 57. [Can Induced Emotion Bias LLM Behaviors in Sequential Decision Making?](https://arxiv.org/abs/2607.12631)

**<font color=#1a73e8>作者：</font>** Minh Khoi Ho, Zihao Zhu, Runchuan Zhu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As Large Language Models (LLMs) are increasingly deployed as autonomous agents in high-stakes domains, understanding contextual factors that may modulate their decision-making becomes critical. While LLMs are trained to perceive and resonate with users' emotions, it remains unclear whether induced emotion can influence their sequential decision-making. We investigate this question using the Iowa Gambling Task (IGT), a classic psychological paradigm for studying decision-making under uncertainty, combined with an imagination-based emotion induction procedure. We first validate the feasibility of this paradigm by confirming that LLMs can sense strong, distinguishable emotions from context and that LLM agents can learn from sequential interactions in a human-like pace. With the validated setup, we find that, different from humans, induced emotion does not significantly bias the decision dynamics of LLM agents on average. However, the effects of anger are conditioned: inducing anger makes LLM agents less sensitive to penalties for bad decisions, and in early stages of the game, anger can lower exploration, locking decisions into a few choices early. These findings reveal the subtle yet distinct effects of induced emotion on LLM decision-making compared to human behavior, and provide a tool for future research on affective modulation of LLM agents.

---


### 58. [A Learning-Rate-Gated Failure of GRPO in a Small Language and Vision-Language Model Web Agent: A Controlled Null and Its Mechanism](https://arxiv.org/abs/2607.12640)

**<font color=#1a73e8>作者：</font>** Chengguang Gan, Zhixi Cai, Yunhao Liang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards, and Group Relative Policy Optimization (GRPO) in particular, is now run routinely on a supervised checkpoint in the hope of producing a stronger agent. We ask whether it adds skill to a small language and vision-language model web agent at the 4B to 8B scale, or whether it mostly reshapes behavior the supervised model already has. Across a control grid of 18 runs that varies learning rate, KL weight, seed, initialization, and clipping, no configuration credibly improves the success rate of a strong supervised baseline on tasks the agent has largely mastered. On the text track, moderate to high learning rates make it credibly worse. The null holds under paired testing, 25 evaluation seeds, 6 training seeds, changes to the recipe, both text and Set-of-Marks screenshot observations, and scaling the backbone to 8B; the credible harm is a text-track finding and is only nominal under Set-of-Marks. To show that the null reflects the setting and not a broken pipeline, we run the identical harness, reward, and recipe on tasks whose reward is reachable by sampling, and there the success rate rises by 22 points with a paired interval that excludes zero. GRPO therefore helps only when there is headroom to climb, meaning the sampled policy already succeeds more often than the greedy one. We then explain the failure. A middle learning rate degrades the agent and a high one collapses it, and the two regimes form a double dissociation: grafting localizes the degrade regime to the attention and MLP blocks, while the collapse regime cannot be traced to any single group, and the embedding change that dominates the weight movement is causally inert. At 4B, effective rank in the late layers tracks capability in both directions; at 8B the two come apart. This coupling is specific to the smaller model, so we report it as scale-dependent.

---


### 59. [Evidence-Grounded Verified Agentic Reasoning: A Path Toward Eliminating LLM Hallucination in Empirical Inference via Tool-Attested Kernel Proofs](https://arxiv.org/abs/2607.12650)

**<font color=#1a73e8>作者：</font>** Junyu Ren  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tool access alone does not make LLM empirical reasoning governable: accepted outputs need not descend from attested evidence, and accepted deductions need not hold up under formal scrutiny. We present EG-VAR (Evidence-Grounded Verified Agentic Reasoning), a Lean 4-based tool-calling architecture in which the Lean kernel is the sole minter of Verified claims via tool-attestation axioms and declared source lifts. Every verified output structurally descends from an attested tool call (Thm. 3.1) and a kernel-checked chain of valid inference (Thm. 3.2); residual outputs are honest Abstain with a replayable audit trail. On a subcollection of TableBench numerical reasoning (n=120), EG-VAR attains 120/120 versus a 95% same-tool baseline; on counterfactual stress tests (5 domains x 2 models), EG-VAR stays 100% source-faithful while same-tool drops to 80-90% (no-tool 50-80%). With the LLM as deployment-time formalizer, residual semantic-formalization error is 3.3% on Sonnet and 1.7% on Opus. We position EG-VAR as a technical-governance interface for high-stakes empirical claims: a formal sidecar makes the target proposition, source scope, evidence boundary, proof obligation, and abstention condition auditable, eliminating unsupported Verified outputs today while turning formalization errors, lift and source-authority disputes, ambiguities, and abstentions into explicit audit targets. Over time, typed sidecars in datasets, APIs, public records, and AI-generated documents can amortize this formalization burden into reusable infrastructure.

---


### 60. [Internet of Agentic Things: Networked AI Agents for Closed-Loop IoT Orchestration](https://arxiv.org/abs/2607.12662)

**<font color=#1a73e8>作者：</font>** Quanyan Zhu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The paper introduces the Internet of Agentic Things (IoAT), an architectural framework that integrates agentic AI, IoT, cyber-physical systems, Physical AI, edge computing, and digital twins into a unified closed-loop orchestration framework. The proposed architecture consists of cloud, edge/fog, and physical IoT layers connected through autonomous AI agents that perceive, reason, coordinate, and actuate across distributed cyber-physical environments. The paper formalizes IoAT as a coupled workflow-control problem with nested strategic and tactical decision making using a hylomorphic dynamic programming framework that links agentic planning with physical execution. Smart-building orchestration is presented as a representative use case, and key research challenges related to safety, security, governance, resilience, and trustworthy deployment are discussed.

---


### 61. [Segregate, Refine, Integrate: Decomposing Multimodal Fusion for Sentiment Analysis](https://arxiv.org/abs/2607.12686)

**<font color=#1a73e8>作者：</font>** Alexios Filippakopoulos, Elias Kallioras, Nikolaos Xiros 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multimodal fusion must simultaneously refine modality-specific signals and model cross-modal interactions; two competing objectives typically entangled within the same operation. We propose \textbf{SeRIn} (\textbf{Se}gregate, \textbf{R}efine, \textbf{In}tegrate), a multimodal LM fusion scheme that enforces this separation as an architectural prior. Modality-specific representations evolve along isolated pathways, each refined against its respective encoder context, while a dedicated cross-modal pathway accumulates their joint evolution without contaminating unimodal streams. Full cross-modal interaction is deferred to a final prediction step - ablations confirm that structured interactions, not added capacity, drive the gains; gate analysis under visual corruption reveals emergent modality reweighting without explicit supervision. SeRIn achieves state-of-the-art results on CH-SIMS and CMU-MOSEI, improving all metrics on both benchmarks.

---


### 62. [Less Experts, Faster Decoding: Cost-Aware Speculative Decoding for Mixture-of-Experts](https://arxiv.org/abs/2607.12696)

**<font color=#1a73e8>作者：</font>** Jincheng Xie, Runheng Liu, Heyan Huang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sparse Mixture-of-Experts (MoE) models have become an important approach for scaling Large Language Models (LLMs), but their inference efficiency depends strongly on expert activation patterns. Speculative decoding (SD) accelerates autoregressive generation by verifying multiple draft tokens in parallel, yet existing draft selection strategies primarily optimize acceptance likelihood. In large-scale MoE models, however, selecting draft tokens also determines the union of experts activated during verification. We observe that confidence-driven SD can introduce \textit{expert scattering}: high-probability draft tokens may route to disjoint experts, increasing expert-weight memory traffic and reducing the speedup from speculation. Motivated by this observation, we revisit draft-tree selection under the non-uniform memory-cost structure of MoE inference. We propose \textsc{EcoSpec}, a cost-aware speculative decoding framework that incorporates predicted marginal expert activation cost into draft selection. With a lightweight expert predictor and a dynamic expert buffer, \textsc{EcoSpec} favors draft paths that preserve high acceptance likelihood while reusing experts already covered by the current verification set, without modifying the target-model verification rule. We evaluate \textsc{EcoSpec} on three large-scale MoE models, including DeepSeek-V3.1 (671B), Qwen3-235B-A22B, and GPT-OSS-120B, across reasoning, coding, question-answering, and dialogue benchmarks. \textsc{EcoSpec} consistently reduces active expert footprints and improves end-to-end decoding speed, achieving up to $1.62\times$ speedup. These results show that accounting for expert activation cost is important for efficient speculative decoding in large-scale MoE models.

---


### 63. [MaxSAT-Based Feedback for Guiding Vision-Language Models in Sudoku](https://arxiv.org/abs/2607.12711)

**<font color=#1a73e8>作者：</font>** Pedro Orvalho, Guillem Alenyà, Felip Manyà  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision--Language Models (VLMs) have recently demonstrated promising performance on structured visual reasoning tasks, including grid-based puzzles. However, despite strong perceptual capabilities, these models lack explicit mechanisms for enforcing logical consistency and frequently generate assignments that violate underlying constraints. In this paper, we propose a neuro-symbolic approach that integrates formal constraint reasoning into the VLM solving process via a Maximum Satisfiability (MaxSAT) oracle. Rather than computing solutions directly, the symbolic component acts as a consistency validator and refinement engine. Candidate placements generated by the VLM are encoded as soft clauses in a partial MaxSAT formulation, while Sudoku constraints remain hard clauses. When inconsistencies arise, the MaxSAT solver identifies a largest mutually consistent subset of assignments, which is then translated into structured textual and visual feedback to guide subsequent refinements. We evaluate our approach on a Sudoku dataset across multiple open-source and closed-access VLMs. Results show that MaxSAT-based feedback improves logical consistency and increases the number of solved instances, particularly in full-board refinement mode. These findings demonstrate that symbolic optimisation can enhance the reliability of vision-language reasoning.

---


### 64. [LLMs Can See the Smoke but not the Fire: Evaluating Abductive Reasoning with Elenchos](https://arxiv.org/abs/2607.12733)

**<font color=#1a73e8>作者：</font>** Julius Steiglechner, Lucas Mahler, Gabriele Lohmann  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) excel at pattern recognition and text generation, but their capacity for abductive inference - inferring latent hypotheses that explain observed behavior - remains poorly understood. Here, we introduce Elenchos (named after the Socratic method of cross-examination), a generative evaluation framework that measures abductive reasoning as a structural inverse problem. Given a reference formal system, such as the lambda-calculus, and a potentially mutated counterpart, agents must determine whether a mutation has occurred and infer the rule modifications responsible for the resulting behavioral differences. Evaluating frontier and mid-tier LLMs reveals a consistent detection-attribution dissociation: models often recognize that a system has been altered but struggle to identify the latent mutations causing the observed discrepancies. Performance degrades substantially under interacting mutations, where models frequently recover only a subset of the underlying mutations. Preliminary evidence also suggests diminishing returns from increased inference-time reasoning, with only modest improvements under larger reasoning budgets, though this finding requires further validation.

---


### 65. [Epistemic Stance Flexibility Probing: Measuring Prompt-Conditioned Register Shift in Large Language Models](https://arxiv.org/abs/2607.12739)

**<font color=#1a73e8>作者：</font>** Binwen Liu, Yilin Ren  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A language model may be asked either what experts believe about a contested claim or what it believes about the claim itself. A trustworthy conversational agent should distinguish these two requests and respond in different epistemic registers: neutral attribution in the first case and stance expression in the second. Whether such a shift occurs-and whether it occurs coherently-is not directly assessed by existing benchmarks for accuracy, instruction following, or safety. We introduce ESFP, a behavioral benchmark that treats the contrast between externally attributed and self-attributed prompts as the fundamental unit of measurement. ESFP consists of 104 carefully controlled items spanning six epistemic categories and five phrasing templates, and evaluates model responses along four complementary dimensions: lexical self-attribution, representation-level responsiveness to role framing, sentence-level stance content density assessed by an LLM judge panel, and cross-condition stance consistency. Evaluating eight frontier models from five vendors, we find that epistemic flexibility is largely orthogonal to general model capability: a 27B open-weight model matches the strongest proprietary systems, the flagship model of one family underperforms its lightweight counterpart, and reasoning-optimized models do not consistently exhibit higher flexibility. Stance content density provides the strongest signal, while surface-level lexical markers such as 'I think' can change substantially without corresponding changes in expressed stance. We provide item-level bootstrap confidence intervals, weight-sensitivity analyses, and an explicit discussion of the interpretation limits of the composite score. ESFP measures a model's propensity to adapt its epistemic stance under changing attribution conditions, rather than a general competence measure.

---


### 66. [Tracing Agentic Failure from the Flow of Success](https://arxiv.org/abs/2607.12747)

**<font color=#1a73e8>作者：</font>** Samuel Yeh, Yiwen Zhu, Shaleen Deep 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Failure attribution for LLM-based agentic systems, i.e., identifying which steps in a failure trajectory caused the task to fail, is critical for debugging and improving these systems. Existing approaches either rely on prompting-based pipelines, which are computationally expensive, or require post-training on failure trajectories with step-level error annotations, which are costly to collect and difficult to scale. We argue that a practical failure attribution model should be lightweight and trainable without step-level supervision on failure data. To this end, we address unsupervised failure attribution, i.e., training exclusively on successful trajectories and identifying error steps at inference time given a failure trajectory. We propose OAT, which casts this problem as one-class learning with neural controlled differential equations, modeling the dynamical pattern of successful trajectories in latent space. At inference time, each step in a failure trajectory is assigned an anomaly score based on its deviation from the dynamics learned on successful trajectories, which is then used to form a set of error steps. With training on only 100 successful trajectories, experiments show that OAT is 200--5000 $\times$ faster than prompting-based baselines, and, at the same time, consistently outperforms them in both in-domain and out-of-distribution datasets with +20% and +7% F1 scores, respectively, demonstrating that OAT is a promising and efficient direction for diagnosing agentic system failures.

---


### 67. [Hallo4D: Multi-Modal Hallucination Mitigation for Consistent Spatio-Temporal Generation](https://arxiv.org/abs/2607.12752)

**<font color=#1a73e8>作者：</font>** Hongbo Wang, Huaibo Huang, Jie Cao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While recent advances in 3D generation have enabled impressive visual synthesis, existing methods often rely on 2D diffusion supervision without explicit mechanisms for geometric consistency, leading to spatial hallucinations such as duplicated structures and misaligned geometry. These issues become more severe in 4D generation, where maintaining consistency across viewpoints and temporal evolution introduces additional challenges, including jitter, identity flicker, and structural drift. We present \textbf{Hallo4D}, a unified and model-agnostic framework for mitigating spatiotemporal hallucinations in 3D and 4D content generation. Hallo4D introduces a generation-detection-correction paradigm that leverages large multimodal language models (LMMs) to identify and summarize spatial and temporal inconsistencies from multi-view and multi-frame renderings. These insights guide a consensus-driven image-space consistency optimization, where an LMM-based selector evaluates candidate corrections through multi-model voting, without requiring retraining or architectural modifications. To further improve temporal consistency and optimization efficiency, Hallo4D incorporates motion-aware keyframe sampling, LMM-guided initialization, and appearance alignment. We additionally introduce exposure-aware optimization and visibility pruning to enhance robustness under challenging viewpoints. Extensive experiments demonstrate that Hallo4D consistently outperforms strong baselines across diverse 3D and 4D generation settings, providing a scalable and generalizable solution for consistency-aware content generation.

---


### 68. [VisCo: Leveraging Large Language Models as Intrinsic Encoders for Visual Token Compression](https://arxiv.org/abs/2607.12756)

**<font color=#1a73e8>作者：</font>** Yupeng Zheng, Kai Zou, Bin Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) process large numbers of visual tokens, resulting in substantial inference latency and memory overhead. This has motivated extensive research on visual token compression. While training-free strategies rely on heuristic metrics and suffer significant performance degradation under high compression ratios, many training-based methods introduce external compression modules that force the VLM backbone to adapt, incurring substantial retraining cost and compromising VLMs' priors. Effective visual token compression hinges on strong information encoding, a capability already present in pretrained VLMs but underutilized by existing approaches. Motivated by this, we propose VisCo, a training-efficient self-compression framework that reuses the pretrained VLM itself as an intrinsic compressor. VisCo is a parameter-sharing autoencoder that compresses visual information using a small set of memory tokens and transfers hierarchical information from encoding to decoding. Experiments show that VisCo surpasses prior methods across all evaluated compression ratios, with larger gains under more aggressive compression, and remains stable even in the extreme single-token setting. Moreover, when combined with the original visual tokens, the learned memory tokens can even improve the base model, suggesting that VisCo captures complementary representations beyond compression.

---


### 69. [EvoGraph-R1: Self-Evolving Multimodal Knowledge Hypergraphs for Agentic Retrieval](https://arxiv.org/abs/2607.12764)

**<font color=#1a73e8>作者：</font>** Jiashi Lin, Changhong Jiang, Xiangru Lin 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) has emerged as a critical paradigm for grounding Multimodal Large Language Models (MLLMs) in external knowledge. Recent GraphRAG methods introduce structured entity-relation graphs to improve retrieval and reasoning. However, they remain limited by treating knowledge graphs as static data structures built offline and queried in a single pass. This static paradigm misaligns with the interactive, iterative nature of knowledge-intensive reasoning, creating three bottlenecks: (i) text-centric fragmentation that impedes cross-modal reasoning, (ii) frozen structures unable to incorporate new evidence or correct errors, and (iii) rigid single-pass retrieval without adaptive refinement. To overcome these limitations, we introduce EvoGraph-R1, a self-evolving GraphRAG framework that reconceptualizes knowledge graphs as dynamic environments shaped through agent interactions. We formulate retrieval as a Markov Decision Process (MDP) where the agent observes the graph state and executes actions to query (GraphRetrieve), expand (WebSearch), refine (GraphEdit), or terminate (Answer) the reasoning. These actions reshape the hypergraph structure and generate feedback signals that guide subsequent evolution. Through this closed loop, the hypergraph evolves by integrating new evidence, correcting errors, and refining structure to support multi-hop reasoning. Experiments on multimodal VQA and text QA benchmarks demonstrate substantial improvements over existing RAG baselines in accuracy, coverage, and traceability, establishing self-evolving knowledge graphs as a fundamental paradigm across modalities.

---


### 70. [Learning Mechanistic Reasoning for Chemical Reactions with Large Language Models](https://arxiv.org/abs/2607.12771)

**<font color=#1a73e8>作者：</font>** Xingyu Dang, Haocheng Tang, Junmei Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reaction mechanisms consist of the step-by-step sequences of elementary reactions that explain chemical transformations. Learning the mechanism logic is therefore essential for enhancing the fundamental chemical intelligence of large language models (LLMs). The stepwise deduction of reaction mechanism aligns naturally with the reasoning paradigms of reasoning LLMs. However, current chemical LLMs primarily emphasize coarse-grained name reactions for product prediction and retrosynthesis, often leading to physical inconsistencies and hallucinations. In contrast, specialized small-scale generative models for mechanism inference typically suffer from restricted generalization capacity across diverse chemical spaces. To overcome these limitations, we built a novel, large-scale reasoning dataset of reaction mechanisms. Furthermore, we established the FukuyamaBench, a difficult benchmark derived from Fukuyama's Advanced Organic Reaction Mechanism book, to rigorously evaluate model performance on hierarchical mechanism reasoning. Our fine-tuned Qwen3-30B-A3B achieves 8.3% exact pathway match on FukuyamaBench Set~A, surpassing the specialized FlowER model (5.1%), demonstrating that mechanism-aware training substantially enhances chemical reasoning in language models.

---


### 71. [MBTI: A Multi-Branch Efficient Fine-Tuning Framework for Hyperspectral Image Classification with Foundation Models](https://arxiv.org/abs/2607.12782)

**<font color=#1a73e8>作者：</font>** Mingzhen Xu, Haonan Guo, Di Wang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hyperspectral foundation models learn transferable spectral-spatial representations from large-scale unlabeled data. They provide an effective paradigm for adapting to downstream hyperspectral image (HSI) classification tasks with limited labeled samples. However, spectral band configurations vary substantially across sensors, which makes direct model transfer difficult. Existing adaptation strategies often compress, select, or reshape the original spectra to match model-specific input requirements. These operations may discard useful spectral information and weaken local spectral continuity. To address this problem, we propose MBTI, a Multi-Branch efficient fine-tuning framework for Hyperspectral Image classification. MBTI adapts hyperspectral foundation models to downstream classification tasks while preserving full-band spectral information. First, we introduce a spectral-continuity-preserving multi-branch preprocessing strategy. The original HSI is divided into multiple continuous spectral subsets, and a band reuse mechanism is used when the remaining bands cannot form a complete branch. This avoids invalid padding and unnecessary spectral loss. Second, independent Low-Rank Adaptation (LoRA) modules are inserted into each branch. They enable different spectral intervals to learn task-specific discriminative features while keeping most pre-trained parameters frozen. Finally, a multi-branch channel attention fusion module adaptively recalibrates and integrates features from all spectral branches. Experiments on three public hyperspectral datasets show that MBTI achieves competitive and superior performance compared with representative classification methods. Under the final rank-8 configuration, only about 2.33\%--2.36\% of the parameters are trainable. The code will be available at this https URL.

---


### 72. [ExtraGS: Enhancing Endoscopic View Extrapolation via Diffusion-Guided 3D Gaussian Splatting](https://arxiv.org/abs/2607.12785)

**<font color=#1a73e8>作者：</font>** Cheng-Tai Hsieh, Jiwei Shan, Han Fang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robot-assisted minimally invasive surgery (MIS) critically depends on reliable endoscopic perception for navigation and safety. However, conventional endoscopes provide only a limited field of view, leaving large portions of surrounding anatomy unobserved. Recent neural rendering approaches, such as Neural Radiance Fields and 3D Gaussian Splatting, enable novel view synthesis from endoscopic videos, but their reliance on sparse observations often leads to severe artifacts when extrapolating beyond the training this http URL this work, we propose ExtraGS, a framework for enhancing endoscopic view extrapolation via diffusion-guided 3D Gaussian Splatting. Starting from an initial reconstruction, we introduce an uncertainty-guided virtual camera sampling strategy to actively explore blind spots and maximize information gain. The rendered views from these sampled locations are refined using a diffusion model to recover plausible anatomical structures, producing pseudo observations that guide further optimization. To prevent the generated content from degrading reliable regions, we adopt a confidence-weighted fine-tuning strategy when incorporating these pseudo this http URL experiments on multiple public endoscopic datasets demonstrate that ExtraGS significantly reduces extrapolation artifacts and achieves state-of-the-art performance in endoscopic novel view synthesis.

---


### 73. [CoRe: A Comprehensive Framework for Cross-Image Comparative Reasoning in Vision-Language Models](https://arxiv.org/abs/2607.12786)

**<font color=#1a73e8>作者：</font>** Lin Peng, Cong Wan, Zeyu Guo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-image comparative reasoning remains challenging for vision-language models (VLMs), especially when correct prediction requires fine-grained attribute grounding and globally consistent reasoning. We present CoRe, a unified framework for this problem. CoRe includes: (i) CoRe-20K, a large-scale triplet-based training set automatically constructed from structured visual metadata through a multi-expert collaborative pipeline, covering counting, depth, distance, and spatial relations; (ii) TriSR, a structured reward framework that jointly supervises attribute grounding, judgment alignment, and triplet consistency under GRPO optimization; and (iii) CoRe-Bench, the first benchmark dedicated to fine-grained cross-image comparative reasoning. Experiments show that CoRe substantially outperforms existing VLMs on CoRe-Bench while remaining competitive on standard multimodal benchmarks, achieving a 28.2-point gain in partial accuracy over the strongest baseline.

---


### 74. [Do We Really Need Multimodal Emotion Language Models Larger Than 1B Parameters?](https://arxiv.org/abs/2607.12787)

**<font color=#1a73e8>作者：</font>** Kaiwen Zheng, Junchen Fu, Wenhao Deng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in multimodal large language models (MLLMs) have significantly improved the performance of multimodal emotion recognition (MER) and enabled interpretable description generation by jointly modeling video, audio, and language, etc. However, these performance improvements are often accompanied by an increase in model parameter size (e.g, at least 7B), which simultaneously incurs high computational costs and reduces inference efficiency, thereby hindering real-time deployment on resource-constrained platforms such as robots and mobile devices. This raises a fundamental question: do we really need the multimodal MER model larger than 1B parameters for high-quality MER?
In this paper, we challenge the assumption that larger models are inherently necessary and proposes a lightweight MER framework (called Light-MER), which achieves better and faster multimodal sentiment understanding and recognition through knowledge distillation. It can transfer knowledge from a strong, large-scale teacher model to a lightweight sub-billion-parameter student model, aiming to preserve rich multimodal emotion reasoning and recognition while substantially improving deployment efficiency. Specifically, we introduce two new optimization strategies to enhance knowledge transfer: (1) a new optimal transport loss that combines Sliced Wasserstein Distance with hidden-state alignment, and (2) a new multi-reward optimization strategy based on GRPO that balances MER performance and efficiency, aimed at further enhancing the learning capabilities of student models. Extensive experiments on nine benchmark datasets demonstrate that Light-MER achieves state-of-the-art performance while significantly improving inference efficiency. This highlights the strong potential of small multimodal emotion language models for future research. Code is available at this https URL.

---


### 75. [Who Grades the Grader? Co-Evolving Evaluation Metrics and Skills for Self-Improving LLM Agents](https://arxiv.org/abs/2607.12790)

**<font color=#1a73e8>作者：</font>** Xing Zhang, Guanghui Wang, Yanwei Cui 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-evolving agent systems improve by creating, revising, and retiring their own skills, but every such loop rests on a hidden assumption: a reliable evaluation metric already exists. In many real applications it does not. We make three claims. First, metrics can be \emph{evolved}: our metric loop searches compositions of small drawback detectors under a full evolutionary lifecycle, trained to agree with a ten-item anchored reference set, regularized by consensus over unlabeled outputs, and audited against a held-out anchor it never reads, yielding a transparent, inspectable metric rather than an opaque judge. Second, since no metric exists to beat, the yardstick is recovering what an accurate metric would have enabled, and \emph{Double Ratchet}, our co-evolution of the metric with a lifecycle-managed skill loop, does so: across code generation (MBPP+), enterprise text-to-SQL (Spider~2.0-Snow), and reference-free report generation, it retains 88--110\% of the held-out lift achieved by the same skill loop driven by ground truth or the best available rubric. Third, safety comes from anchor discipline plus outer audits: removing anchor guards collapses the metric into a vacuous detector while removing the lifecycle does not; and when evolved skills gamed the report rubric, an independent judge caught it, one detector repaired it, and a task-aware judge then preferred the evolved outputs over the pre-evolution baseline in 77\% of decided pairs. We argue this failure-expecting architecture is the right default wherever no reliable automatic verifier exists.

---


### 76. [The One-Word Census: Answer-Choice Conformity Across 44 Language Models](https://arxiv.org/abs/2607.12796)

**<font color=#1a73e8>作者：</font>** Tapan Parikh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When a language model must pick one answer from a large space of equally valid options, which does it pick -- and how often is it the same answer every other model picks? Asked to "pick a word -- any word," 44 models chose "serendipity" 41% of the time. We characterize this convergence with a deliberately minimal instrument: 31 single-turn prompts, each naming a category with many valid one-word answers ("Name a tree."), asked four times per model with no system prompt. Analysis is exact-match on normalized tokens -- no embeddings, no judge -- at about a dollar per model. That models converge is well documented; our contribution is the instrument itself -- the One-Word Census -- and what it reveals about the structure of the convergence. We score each model by answer-choice surprisal: the average $-\log2$ probability of its answers under the pooled answers of all other models, leave-one-out. Convergence is extreme -- in 7 of 31 categories one answer takes over 80% of all answers -- yet conformity varies more than fourfold across models, and the variation is structured. Persona- and community-tuned models are the most divergent; the newest mainline flagships are the most conformist, producing almost no answer no other model gave. Within four lineages (Claude, GPT, Qwen, Grok) conformity rises with each generation -- but reverses for the latest flagship Claude and GPT models, a possible early signal of repositioning at the top tier. Rankings are robust to roster composition (leave-one-family-out rho = 0.985). Against human category-production norms, the field is more concentrated than people in 18 of 20 shared categories. All prompts, transcripts, and code are public.

---


### 77. [Visual Access Boundaries in Vision-Language Model Reasoning](https://arxiv.org/abs/2607.12815)

**<font color=#1a73e8>作者：</font>** Hiroto Osaka, Shohei Taniguchi, Gouki Minegishi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Chain-of-Thought (CoT) prompting is widely used as a test-time scaling strategy for Vision-Language Models (VLMs), but it remains unclear what is extended when VLMs generate longer reasoning traces. We ask whether CoT requires continued access to image tokens, or whether it mainly operates over visual information already made available earlier in the forward pass. We introduce Visual Access Sweep, a causal intervention that masks attention from generated-token queries to image-token keys along layer depth and generation time, and define the Visual Access Boundary (VAB) as the minimal access region that preserves task accuracy. Across six model configurations from Qwen2.5-VL and InternVL3, both no-CoT direct answering and CoT prompting exhibit finite VABs. In Qwen2.5-VL-32B and InternVL3 at 14B and 38B scales, when CoT is evaluated against the no-CoT full-access target, its VAB layer differs from the no-CoT boundary by at most two layers, despite substantially longer generations. This suggests that CoT does not primarily improve performance by prolonging direct image-token access throughout the reasoning trace, but by extending language-side computation over image-derived hidden-state information. We further show that CoT gains are constrained by perceptual readout. CoT helps when the queried visual attribute can be reliably read out by the model, but not when that readout is unreliable. A symbolic-attribute oracle shows that CoT can improve counting once ground-truth attributes are supplied as text, while a single-object probe-vs-decode check shows that hard attributes can be linearly recoverable from hidden states yet difficult for the model itself to output. Together, these analyses place the bottleneck at readout rather than counting.

---


### 78. [AVSCap: Orchestrating Audio-Visual Synergy for Omni-modal Video Captioning](https://arxiv.org/abs/2607.12820)

**<font color=#1a73e8>作者：</font>** Yanghai Wang, Jiahao Wang, Jiafu Tang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Omni-modal video captioning is not merely combining visual captioning with audio transcription: a useful caption must describe how visual actions, speech, music, and sound effects co-evolve. Existing large multimodal models often fail at this relational step, treating audio and visual streams as loosely coupled observations, relying on automatic speech recognition, and under-specifying non-speech sounds and their links to visual events. We present AVSCap, a framework for audio-visual captioning centered on explicit cross-modal event binding. First, we construct AVSCap-130K, a tri-modal training corpus generated by a decoupled-then-fused pipeline that anchors visual and acoustic evidence before composing grounded omni-modal captions. Second, we train AVSCap-7B, a 7B captioner with a two-stage strategy: supervised fine-tuning establishes baseline capabilities, while sample-efficient reinforcement learning uses hybrid rewards to optimize acoustic completeness and audio-visual synergy. Our scaling analysis shows that reinforcement learning brings larger gains than increasing SFT data. Third, we introduce AVSCapBench, a benchmark that decomposes captions into visual, audio, and synergy events and evaluates them with fine-grained event recall. Experiments on AVSCapBench and external benchmarks show that AVSCap-7B improves non-speech audio coverage and cross-modal binding, delivering the best overall performance among evaluated open-source models.

---


### 79. [Accelerating Masked Diffusion Large Language Models: A Survey of Efficient Inference Techniques](https://arxiv.org/abs/2607.12829)

**<font color=#1a73e8>作者：</font>** Daehoon Gwak, Minhyung Lee, Junwoo Park 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion large language models (dLLMs) offer a theoretical advantage in parallel generation over standard autoregressive models. However, parallel generation alone does not guarantee practical speedups. Realizing this efficiency requires specialized inference mechanisms, such as diffusion-aware caching and reuse. Consequently, as inference efficiency becomes a prerequisite for practical deployment, recent research has actively explored acceleration techniques across algorithms, architectures, and systems. However, rigorous comparisons remain difficult, as end-to-end latency stems from intricate trade-offs between algorithmic, architectural, and system-level factors that are often conflated in existing benchmarks. In this survey, we introduce a unified latency decomposition framework for dLLMs to disentangle these factors and analyze their impact on inference speed in real deployments. Guided by this framework, we categorize acceleration techniques along three axes covering algorithmic innovations, architectural and system optimizations, and inference-time scaling. Finally, we provide guidelines for reproducible benchmarking and highlight open challenges for realizing the full potential of parallel generation.

---


### 80. [Knowledgeless Language Models: Suppressing Parametric Recall for Evidence-Grounded Language Modeling](https://arxiv.org/abs/2607.12831)

**<font color=#1a73e8>作者：</font>** Roi Cohen, Yvan Carré, Nick Lechtenbörger 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models encode substantial factual knowledge in their parameters, which can lead to unreliable behavior when this knowledge is outdated, incomplete, or misaligned with the provided context. In this work, we study whether modifying the pretraining signal can systematically shift models away from parametric recall and toward evidence-grounded reasoning. We introduce Knowledge--''Less'' Language Models (KLLMs), a fundamentally different epistemic training paradigm for LLMs, which are pretrained on corpora in which named entities are anonymized, thereby removing a primary channel for entity-linked factual supervision. This intervention substantially reduces closed-book factual recall, while often improving performance on tasks where relevant information is provided as context. Across multiple model scales, KLLMs consistently outperform matched baselines on contextual question answering, fact verification, and hallucination detection benchmarks. Crucially, in retrieval-grounded settings with imperfect evidence, KLLMs show improved robustness and achieve up to 20--25\% relative gains over standard language models. They further exhibit better calibration, with improved ECE, Brier score, and AUROC, as well as more reliable abstention behavior. Our results demonstrate that suppressing entity-linked supervision during pretraining induces a shift in epistemic behavior: KLLMs rely less on parametric knowledge and more on external evidence, leading to improved reliability under realistic conditions. This suggests that pretraining-time control over knowledge acquisition can complement retrieval-augmented and tool-based systems by providing a more evidence-sensitive base model.

---


### 81. [Can LLMs Write Reliable Rubrics? A Meta-Evaluation for Experiment Reproduction](https://arxiv.org/abs/2607.12835)

**<font color=#1a73e8>作者：</font>** Hanhua Hong, Yizhi Li, Jiaoyan Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Rubric-based evaluation is a promising approach for assessing open-ended outputs from LLM-based research agents, particularly in paper reproduction, where direct paper-to-repository comparison is prone to hallucination. However, constructing paper-specific rubrics requires substantial expert effort, limiting the scalability of benchmarks such as PaperBench. In this work, we present, to our knowledge, the first systematic meta-evaluation of LLM-generated rubrics for paper reproduction. We reformulate rubrics into a checklist-style format and evaluate four generation settings across two backbone models. We meta-evaluate generated rubrics intrinsically by semantic similarity and extrinsically by score alignment with ground-truth rubrics. Our results show that the augmented settings substantially improves downstream evaluation alignment, with the strongest setting approaching the human baseline, while intrinsic gains are more modest. Further analyses reveal that LLM-generated rubrics are often overly fine-grained, biased toward high scores, and less adaptive to paper domains, highlighting both the affordances and limitations.

---


### 82. [Verifier-Based Reinforcement Fine-Tuning of Reasoning Models for Thermal Energy Storage Control](https://arxiv.org/abs/2607.12856)

**<font color=#1a73e8>作者：</font>** Takumi Shioda, Kohei Terashima, Tatsuo Nagai  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Buildings are expected to shift cooling loads in response to grid conditions. Thermal energy storage (TES) enables this shift, but scheduling it well requires planning hours ahead under storage constraints. Model predictive control (MPC) and reinforcement learning are difficult to scale across buildings. This study instead adapts an open-weight reasoning model through reinforcement learning with verifiable rewards (RLVR). We convert exact offline dynamic-programming (DP) action values into dense rewards for every candidate action. Using only 30 training prompts, reinforcement fine-tuning (RFT) trains the model as an upper-level scheduler that outputs hourly heat-pump setpoints from text-based states and forecasts. Evaluation uses a deliberately simple office-building TES benchmark where exact DP is tractable and the optimum is known. RFT reduces the open-weight model's emissions from 70.5 to 61.2 kg-CO2, close to the DP optimum of 60.8 kg-CO2. GPT-5 nearly matches DP and MPC without task-specific training, while GPT-4o, a non-reasoning LLM, produces higher emissions than the no-storage baseline, so inference-time reasoning appears important. Trace analysis shows that RFT mainly stabilizes observable planning patterns (candidate comparison, look-ahead, and feasibility checking) rather than creating a new strategy. Robustness and generalization tests clarify what transfers: the reinforced planning patterns persist under forecast errors and an unseen TES condition and carry over to a battery task, but its different structure limits the gains. DP-based verifiable rewards offer a practical way to adapt open-weight reasoning models to building storage scheduling. These results motivate higher-fidelity tests of whole-building control and scalable verifiers for city-scale energy management.

---


### 83. [Metric-Guided Synthetic Image Data Rendering for Deep Learning compatible with Agentic AI](https://arxiv.org/abs/2607.12874)

**<font color=#1a73e8>作者：</font>** Martina Radoynova, Samuel Pantze, Trina De 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning computer vision for scientific applications requires collecting and annotating large datasets in a laborious, expensive and error-prone process. Synthetic data generation through 3D modelling and rendering may simplify this process and increase the accuracy of annotations by generating them programmatically. However, minimising the domain gap between real and synthetic images visually is subjective and lacks systematic quantitative guidance. We present GraNatPy, a Python package with metrics to guide improvement of the rendered scene. We show that quantifiable increase in realism, diversity and size of rendered dataset correlates with improved visual perception of the scene and higher zero-shot performance of an object detection model. Furthermore, we demonstrated using photographs of virological plaque assays that gradient similarity affects performance on small object detection, which can be improved by mixing real and synthetic data. Finally, we turn procedural data rendering into an agentic skill (SynthClaw) to automate the procedural parameter optimisation.

---


### 84. [MetaInfer: A Knowledge Only LLM Inference Engine Generator SKILL Toolbox](https://arxiv.org/abs/2607.12875)

**<font color=#1a73e8>作者：</font>** Zhenwen Miao, Honglin Wang, Mingheng Mi  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> As LLM technology advances, the space of model families, compute hardware, quantization schemes, parallelization strategies, and specialized optimization kernels continues to expand, sharply increasing the code complexity and maintenance cost of general-purpose inference frameworks. Conventional software engineering uses multiple layers of abstraction to support diverse application scenarios, but these abstractions also increase system complexity and may introduce additional performance overhead. This paper presents metainfer, an 'LLM-as-Compiler' approach in which users specify only the runtime constraints of an inference program. An LLM-driven multi-agent collaboration system, coupled with a contract knowledge base, then automatically generates a compact customized inference framework that satisfies these constraints. We evaluate metainfer from three perspectives: the effect of source-code reference, the runtime behavior and performance profile of engines generated under the zero-reference constraint on CKB-covered targets, and knowledge-base evolution for new model and platform scenarios. The results show that metainfer organizes generation constraints, validation feedback, and knowledge consolidation into a continuous closed loop, enabling runnable customized inference solutions to be generated from explicit knowledge. The code is publicly available at this https URL.

---


### 85. [Evaluating Large Language Models on Misconceptions in Multi-Turn Medical Conversations](https://arxiv.org/abs/2607.12884)

**<font color=#1a73e8>作者：</font>** Monica Munnangi, Saiph Savage  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Patients seeking medical information often ask questions that embed incorrect assumptions or misconceptions. In such cases, safe medical communication requires not only answering the question, but identifying and correcting the underlying false belief. These interactions naturally unfold over multiple turns, a pattern now mirrored in interactions with LLMs. Yet current evaluation frameworks do not capture model behavior in these settings, where misconceptions can emerge, persist, or evolve over the course of a conversation. Whether LLMs can reliably correct such misconceptions over time remains largely unexamined. To study this, we introduce ThReadMed-QA, a multi-turn medical dialogue dataset of 2,437 patient-physician conversation threads comprising 8,204 question-answer pairs, derived from real patient interactions on AskDocs. This dataset enables systematic evaluation of whether models can detect and correct misconceptions under a multi-turn context. We evaluate five LLMs using a rubric-based LLM-as-a-Judge framework that scores responses based on their ability to identify and correct misconceptions. Our experiments reveal a consistent pattern: even frontier models that can address misconceptions in a single interaction degrade substantially over subsequent turns. GPT-5 and Claude-Haiku correct these false presuppositions around 85% on initial questions but drop to roughly 50% within two follow-ups. An oracle analysis replacing prior model outputs with physician responses shows that much of the degradation is driven by error propagation, while performance remains imperfect even under correct context. Even when models tend to correct misconceptions initially, their performance degrades substantially over later turns, leading to inconsistent and potentially unsafe guidance in patient-facing settings and highlighting the need for evaluation frameworks that capture multi-turn behavior.

---


### 86. [LLM Judges Can Be Too Generous When There Is No Reference Answer](https://arxiv.org/abs/2607.12885)

**<font color=#1a73e8>作者：</font>** Chalamalasetti Kranti, Sowmya Vajjala  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM judges are increasingly being used to evaluate open-ended model responses, often in no-reference settings where a ground-truth answer is unavailable. However, can they reliably assess in such evaluation setups? We explore this question in this paper through a two stage pipeline with a) calibration experiments that assess the judge model's knowledge of the task it is evaluating, and b) sensitivity experiments that assess how the judge model's performance is impacted by the presence and positioning of the reference answer in the prompt. Across experiments covering three languages, we show that the judge models we evaluated tend to over-credit incorrect answers in the absence of a reference answer, and adding reference answer information to the prompt flips the judge model's correct/incorrect decisions by as much as 85% in some experimental settings. Comparison with a subset of human annotations shows that these reference-driven changes generally align with human judgments. Our results emphasize the need for calibrating the LLM judges with a sample with reference-aware evaluation before using them in reference-free setups reliably, and our methodology provides a blueprint for researchers and practitioners in doing such calibration of LLM judges for other tasks.

---


### 87. [A Multi-Agent System for Autonomous, Fine-Tuning-Free Clinical Symptom Detection: Development and Validation Study](https://arxiv.org/abs/2607.12886)

**<font color=#1a73e8>作者：</font>** Cameron Cagan, Pedram Fard, Jiazi Tian 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Clinical notes contain many of the signs and symptoms that bring patients to care, yet this information rarely reaches structured fields. Existing extraction approaches either rely on context-insensitive rules that generate false positives or on supervised models that require substantial fine-tuning. We present Pythia, a multi-agent system that autonomously writes and optimizes extraction prompts for clinical concepts without manual prompt engineering or fine-tuning. Running on a locally hosted open-weights model, Pythia keeps clinical notes on local infrastructure and selects prompts using development-set sensitivity and specificity. We compared Pythia with a curated lexicon across 72 signs and symptoms from 400 clinical notes representing 387 patients. Development (n=300) and validation (n=100) sets were partitioned independently for each concept. Pythia achieved mean sensitivity of 0.76 and specificity of 0.95, compared with 0.82 and 0.76 for the lexicon, and matched or exceeded the lexicon on both metrics for 20 of 62 directly comparable concepts. For 14 concepts where the lexicon labeled every note positive, Pythia recovered mean specificity of 0.97 by requiring a present-tense, patient-attributed finding rather than any textual mention of a term. Specificity transferred from development to validation with minimal degradation across prevalences, whereas sensitivity transfer weakened below 5% prevalence, reaching a mean gap of 0.25 below 2% prevalence. A BERT classifier fine-tuned per concept on the same development set achieved mean sensitivity of 0.23 and collapsed to zero sensitivity for concepts below roughly 5% prevalence. These findings suggest that autonomous, fine-tuning-free prompt optimization can produce symptom extraction prompts that generalize effectively from development to validation while remaining deployable on local infrastructure.

---


### 88. [Hy-Embodied-VLM-1.0: Efficient Physical-World Agents](https://arxiv.org/abs/2607.12894)

**<font color=#1a73e8>作者：</font>** Ziyi Wang, Xumin Yu, Yongming Rao 等 22 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Building capable embodied agents requires not only multimodal perception and understanding, but also agentic capabilities for reasoning about actions, adapting to evolving situations, and interacting with the physical world. In this report, we introduce Hy-Embodied-VLM-1.0, an efficient and powerful embodied foundation model specifically designed for embodied agents operating in the physical world. To cultivate such capabilities from the pre-training stage onward, we define an action-centric capability taxonomy comprising three progressive dimensions: Action-Relevant State Understanding, Action-Transition Reasoning, and Sequential and Adaptive Reasoning. Guided by this taxonomy, we develop a systematic data pipeline and curate data mixtures spanning both pre-training and post-training. To deliver strong physical-world understanding and interaction capabilities while supporting latency-sensitive deployment, we build our model on the Hy3-A3B language backbone and the Hy-ViT2 vision encoder. Its efficient Mixture-of-Experts architecture combines strong model capacity with high inference efficiency. We evaluate Hy-Embodied-VLM-1.0 on a comprehensive suite of 38 benchmarks covering embodied perception, physical-world understanding, and embodied reasoning. The model achieves the best performance among similarly sized models on 19 of the 38 benchmarks and substantially outperforms strong competitors, including Qwen3.6-A3B and Cosmos 3. Compared with the previous-generation Hy-Embodied-0.5 MoT-2B, Hy-Embodied-VLM-1.0 improves average performance by 8.4%. Despite activating only 3B parameters, it achieves performance close to that of the previous-generation model with 32B activated parameters. Beyond static benchmark evaluation, Hy-Embodied-VLM-1.0 also demonstrates strong performance on embodied agentic tasks requiring multi-turn interaction and long-horizon reasoning.

---


### 89. [UniMedSeg: Unified In-Context Learning for Multi-Paradigm 2D/3D Medical Image Segmentation](https://arxiv.org/abs/2607.12896)

**<font color=#1a73e8>作者：</font>** Yunzhou Li, Jiesi Hu, Yanwu Yang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical image segmentation foundation models are expected to generalize across diverse clinical scenarios, yet existing universal methods remain fragmented by prompt paradigms and spatial dimensions. Visual in-context learning, interactive segmentation, and language-guided segmentation are typically handled by paradigm-specific models, while 2D and 3D images are also modeled separately. Such isolation prevents heterogeneous annotations and data from being jointly absorbed by a single scalable model and limits cross-paradigm knowledge transfer. To address this bottleneck, we propose UniMedSeg, a Transformer-centric universal segmentation framework that maps visual examples, geometric interactions, language instructions, and 2D/3D images into a shared sequence space, enabling heterogeneous medical supervision to be jointly learned through a unified in-context interface without prompt- or dimension-specific branches. To overcome the long-sequence memory bottleneck caused by visual contexts, we introduce Decoupled Split Attention, which reduces attention complexity to linear while preserving hardware-friendly computation and focused context-target interaction. Extensively trained and evaluated on a large corpus curated from 27 public datasets, UniMedSeg achieves state-of-the-art performance across visual in-context, interactive, and language-guided segmentation without task-specific fine-tuning, demonstrating strong generalization on diverse held-out tasks. The code and model weights are publicly available at this https URL

---


### 90. [Rank-1 Identity Consensus Predicts Gallery Enrollment in 1:N Face Matching More Accurately than Score Thresholding](https://arxiv.org/abs/2607.12903)

**<font color=#1a73e8>作者：</font>** Gabriella Pangelinan, Aman Bhatta, Michael C. King 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In operational 1:N face identification, a crucial question arises for each probe: is this person enrolled in the gallery or not? The stakes are high and asymmetric. Rejecting a mate-present (MP) probe loses a valid lead; accepting a mate-absent (MA) probe makes every returned candidate a false identification, at worst a wrongful arrest. Most approaches threshold match scores, but scores shift substantially with image quality and gallery size and composition, making thresholds fixed before deployment brittle under realistic conditions. Our prior work introduced 1-consistency, the only method based on rank consensus across multiple independently trained matchers: a probe is labeled MP if all matchers return the same rank-1 identity. This work stress-tests 1-consistency across 36 (gallery, probe quality) scenarios spanning four quality levels and two structural axes: images per identity and total enrolled identities. We benchmark against two score-thresholding methods that bracket what any deployed threshold could achieve. Fixed Score-Thresholding (FST), calibrated once on baseline conditions, collapses asymmetrically as quality degrades: MP recall falls below 2% while MA recall holds near 100%. Oracle Score-Thresholding (OST), re-tuned per scenario, is the best any threshold could theoretically do, yet for degraded probes 1-consistency matches it with zero tuning. The two differ mainly in error type (OST favors MP recall, 1-consistency favors MA recall), but on one axis 1-consistency does not merely match the oracle: when it labels a probe MP, it returns the correct mate 97-100% of the time versus OST's 66-84% under severe degradation. In short, 1-consistency delivers oracle-level accuracy without the impossible requirement: it sets no threshold, so it needs no advance knowledge of the conditions a probe will arrive in, which is what makes it usable.

---


### 91. [Open-KNEAD: Knowledge-grounded Nutrition Estimation via Agentic Decomposition](https://arxiv.org/abs/2607.12911)

**<font color=#1a73e8>作者：</font>** Bruce Coburn, Jingbo Yue, Jinge Ma 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) are increasingly used for dietary assessment from meal images, where retrieval-augmented grounding was shown to sharpen nutrition estimates. However, we find this premise no longer holds for current MLLMs. A modern MLLM's direct estimate now matches or surpasses the full retrieval pipeline. This raises a question: if retrieval no longer improves the overall estimate, can it still deliver the two things clinicians value, accurate portions and a traceable, item-by-item record? We pursue this while preserving what matters for clinical adoption: minimal user burden (a single, unannotated meal image), explainability (an auditable record), and privacy (locally hosted inference). We introduce Open-KNEAD, a knowledge-grounded agentic framework for meal nutrition estimation that is training-free and locally deployable. Each decomposed food item is grounded to a Food and Nutrient Database for Dietary Studies (FNDDS) code via selective, nutrient-aware retrieval, composing an auditable per-item record. Across two open MLLM families and three cuisines, Open-KNEAD improves portion estimates over both prior grounding methods and direct estimation in most backbone-dataset settings. An agent-internal recipe-prior step further recovers the invisible cooking-added energy that biases estimates on non-US cuisine. The advantage is largest on the dietitian-verified ACETADA dataset, where the local open agent surpasses the direct portion estimates of two frontier closed models by roughly $30\%$ and $53\%$, all while keeping every meal image on local hardware. We release the Open-KNEAD framework and its agent-ready FNDDS knowledge base.

---


### 92. [CD-MED: Cross-Domain Multimodal Emotion Descriptor for Visual Comparison of Digital Objects](https://arxiv.org/abs/2607.12958)

**<font color=#1a73e8>作者：</font>** Elnara Kadyrgali, Muragul Muratbekova, Pakizar Shamoi  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Digital objects express emotions through different modalities. For example, a movie may include visual scenes, audio, dialogue, and facial expressions, while a song may contain melody, rhythm, lyrics, and vocal tone. Because existing emotion recognition models are usually modality-specific, it is difficult to compare such objects directly. This paper proposes CD-MED, a Cross-Domain Multimodal Emotion Descriptor for representing heterogeneous digital objects in a common emotional space. Each modality can be processed by its own emotion recognition model, and the resulting emotional outputs are transformed into a shared descriptor. The descriptor preserves information from individual modalities while also allowing an integrated emotional profile of the object. For interpretation, CD-MED is visualized in the valence-arousal space: position represents affective coordinates, color denotes emotion category, size indicates intensity, and shape shows the modality. This unified representation enables emotion-based comparison, retrieval, recommendation, and visualization across different domains such as movies, songs, images, and books.

---


### 93. [ViCo3D: Empowering LiDAR-based Collaborative 3D Object Detection with Vision Foundation Models](https://arxiv.org/abs/2607.12959)

**<font color=#1a73e8>作者：</font>** Haojie Ren, Songrui Luo, Lingfeng Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> LiDAR-based collaborative 3D perception in Vehicle-to-Everything (V2X) systems typically relies on fusing bird's-eye-view (BEV) features across agents. However, current BEV representations, typically extracted by LiDAR backbones trained from scratch, are geometry-dominated and lack general semantic priors, inherently limiting the efficacy of feature-level collaboration. Meanwhile, vision foundation models (VFMs) pretrained on large-scale image data have demonstrated strong capability in learning general-purpose and informative visual representations for 2D tasks, and have the potential to enhance agent-wise LiDAR BEV representations for collaboration. Despite this potential, adapting VFMs to LiDAR-based 3D detection remains challenging due to the substantial image-point cloud modality gap. To bridge this gap, we propose ViCo3D, a collaborative 3D object detection framework powered by VFMs. Specifically, ViCo3D adapts VFMs to LiDAR-based collaborative perception from three aspects: First, ViCo3D projects point clouds onto the BEV plane as three-channel images, enabling DINOv2 to extract BEV-space visual features from LiDAR inputs. Besides, to effectively integrate these DINOv2-derived features with LiDAR geometric features, ViCo3D introduces a multi-scale BEV fusion module within the single-agent encoder. In addition, ViCo3D adopts an ego-centric cross-agent fusion strategy to aggregate complementary information from multiple agents. Experiments on DAIR-V2X and V2XSet demonstrate that ViCo3D achieves state-of-the-art 3D detection performance. Remarkably, it delivers up to 1.8x greater collaborative gains than prior methods on DAIR-V2X. The code will be made public available for future investigation.

---


### 94. [FormalAnalyticGeo: A Neural-Symbolic Based Framework for Multimodal Analytic Geometry Problem Generation](https://arxiv.org/abs/2607.12982)

**<font color=#1a73e8>作者：</font>** Ruoran Xu, Wending Gao, Qiufeng Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Math reasoning has achieved significant progress with the rapid advancement of Multimodal Large Language Models (MLLMs), however analytic geometry remains largely underexplored, primarily due to the scarcity of annotated samples. Existing diagram generation approaches struggle with analytic geometry: template methods cannot handle constraint-driven layouts, and generative models lack the geometric precision to render annotated conic curves correctly. We present FormalAnalyticGeo, a scalable framework for fully automatic generation of multimodal analytic geometry problems. Leveraging the rigor of formal languages, we design the framework around CDL (Condition Description Language), a formal intermediate representation that bridges free-form problem text with precise diagram rendering via a Signed Distance Field (SDF) engine. The framework employs four specialized LLM components in sequence: a Generator that produces diverse analytic geometry problems, a Formalizer that converts each problem into CDL for SDF-based rendering, a Measurer that extracts ground-truth answers through vision-based measurement on the rendered diagrams, and a Quality Verifier that checks outputs at three stages. Structured feedback from the Quality Verifier drives automatic retry, forming a closed loop that eliminates any need for human annotation. Applying FormalAnalyticGeo at scale yields AnalyticGeo7K, a dataset of over 7K verified multimodal problems, each with aligned text, diagram, formal annotation, and ground this http URL show that the generated problems achieve a median ground-truth relative error of 0.70\%, with 82.3\% of answers falling within 5\% of the exact symbolic solution. Our framework and dataset will be publicly released.

---


### 95. [Resist and Update: Counterfactual Report Coordinates for Incentive-Compatible LLMs](https://arxiv.org/abs/2607.12985)

**<font color=#1a73e8>作者：</font>** Sen Yang, Yuen-Hei Yeung  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Aligned language models routinely misreport under non-evidential incentive pressure: they agree with a confident user or overstate certainty even when their internal belief is unchanged. We cast this as a failure of internal incentive-compatibility (IC) and present a method for learning and certifying counterfactual report mediators that hold a model's reports to a causal contract: invariant to forbidden influences (pressure, prestige, restyling) and responsive to licensed ones (genuine evidence). These two demands, resist and update, pull in opposite directions. We study them on a Bayesian-witness benchmark with known posteriors, in which the same user disagreement is licensed evidence or forbidden pressure purely by stated source reliability. We (i) causally identify, by interchange interventions rather than probe accuracy, low-rank report coordinates for answer, confidence, and caveat that are near-orthogonal and independently controllable, and (ii) introduce a training-free counterfactual report-coordinate (CRC) clamp that references the model's own report under a counterfactually incentive-neutralized context. On the witness benchmark the two-pass clamp attains resist and update of 1.00 jointly (Wilson 95% CI [0.99,1.00]), a causal certificate under a constructible reference, not a deployed solution. Global decoding and steering show a single-parameter tradeoff; output-level fine-tuning matches both objectives only when both are enumerated; resist-only training loses evidence-responsiveness. The deployable single-pass compilation is lossy (0.73/0.97). The mechanism and clamp reproduce across three model families and transfer to a natural sycophancy benchmark (SycophancyEval). Our contribution is the interface and certification method: activation-level counterfactual incentive-invariance as a structural primitive for internal IC.

---


### 96. [Win by Silence: Deletion Non-Monotonicity, Autonomous Exploitation, and Typed-State Gating in LLM Plan Evaluation](https://arxiv.org/abs/2607.12986)

**<font color=#1a73e8>作者：</font>** Aleh Manchuliantsau  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Plan evaluators can reward a strategic plan for becoming less explicit. This paper studies that failure in a staged expected-value scorer for LLM-generated venture routes. Proposition 1 gives the score change from deleting an interior transition while retargeting its predecessor and retaining downstream value: Delta_k = (prod_{i<k} p_i)[c_k + (1 - p_k)R_{k+1}]. On a frozen 26-route cohort, all 57 admissible deletions matched the analytic identity and threshold sign, and every route had at least one score-improving deletion. A score-seeking optimizer, allowed to restructure routes but not told the exploit mechanism, found baseline-beating uncovered structures in 21/26 routes. GATE refused score release for 26/26 silenced routes with 0/26 honest suspensions; after refusal, 47/54 next revisions repaired to a covered structure, and strict covered improvement rose from 1/26 to 13/26. An adaptive compiler-aware co-author exposed the registry-provenance boundary: obligation-channel evasions remained 6/6 across all four v1/v1.5 conditions, while delta-indexed cost floors reduced beat-honest routes from 6/6 to 3/6 and fundability-by-silence from 5/6 to 0/6 without establishing semantic completeness. If a plan scores better only because it omits necessary work, the plan did not improve; the evaluation created an omission incentive. PCSC detects and neutralizes post-hoc omission splices over model-mediated typed-state records. In the cooperative setting tested, GATE acts as a deterministic search-shaping constraint, not merely a post-hoc filter. It does not verify the semantic completeness or real-world quality of arbitrary LLM-generated strategies.

---


### 97. [Audio-Native Speech Recognition with a Frozen Discrete-Diffusion Language Model](https://arxiv.org/abs/2607.13013)

**<font color=#1a73e8>作者：</font>** Harsha Vardhan Khurdula, Abhinav Kumar Singh, Yoeven D Khemlani 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automatic speech recognition is dominated by autoregressive decoders that emit one token at a time. We ask whether a discrete diffusion language model can transcribe speech instead, refining a whole transcript in parallel over a small number of denoising steps. We train an audio-native interface for DiffusionGemma, a 26B mixture-of-experts model that generates text by uniform, random-token discrete diffusion rather than the absorbing-mask scheme common to recent diffusion language models. A frozen Whisper encoder supplies acoustic features, a lightweight projector maps them into the model embedding space, and low-rank adapters let the frozen backbone attend to the new modality.
About 42M parameters are trained, which is 0.16 percent of the backbone. We find that the natural training objectives fail to ground the audio because their gradient reaches the projector only through attention that has already dismissed it. A connectionist temporal classification loss applied through the frozen output head breaks this deadlock. The resulting model reaches 6.6 percent word error rate on LibriSpeech test-clean, transcribes in roughly eight parallel steps regardless of utterance length, and uses a single adapter trained on six languages, which we evaluate here on English, Hindi, and Mandarin.

---


### 98. [PalmClaw: A Native On-Device Agent Framework for Mobile Phones](https://arxiv.org/abs/2607.13027)

**<font color=#1a73e8>作者：</font>** Hongru Cai, Yongqi Li, Ran Wei 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) agents have moved beyond generating responses to executing multi-step tasks by calling tools, observing the results, and iteratively deciding the next action. Most agent systems run on desktops or servers, which support tool use and task automation. Mobile devices are also important agent environments because they are widely accessible and contain users' data, sensors, and daily-use applications. Existing mobile agents mainly operate smartphones through graphical user interface (GUI) actions such as tapping, swiping, and typing, which often form long, interface-dependent sequences, cannot directly access device capabilities, and make execution boundaries difficult to define. We present \textbf{PalmClaw}, an open-source agent framework that runs natively on mobile phones and manages the sessions, memory, skills, tools, and agent loop directly on the device. PalmClaw exposes device capabilities as device tools with explicit arguments, structured results, and clearly defined execution boundaries. This design enables agents to use mobile capabilities directly while keeping each action explicit and controlled. Experiments show an 11.5\% relative improvement in task success and a 94.9\% reduction in completion time over the strongest baseline, with lower setup burden and traces illustrating how execution boundaries are applied. Code is available at this https URL.

---


### 99. [Do AI Agents Know When a Task Is Simple? Toward Complexity-Aware Reasoning and Execution](https://arxiv.org/abs/2607.13034)

**<font color=#1a73e8>作者：</font>** Junjie Yin, Xinyu Feng  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents increasingly automate multi-step engineering and informatics workflows, yet they rarely ask how much effort a task actually requires. They often follow a maximum-context-first strategy--re-reading files and dependencies they have already seen--turning a one-line edit into a small code-base audit. We argue the missing capability is task-aware execution-scope estimation: judging a task's difficulty, the information it truly needs, and the shortest reliable path before committing budget. We formalize minimum-sufficient execution and the Agent Cognitive Redundancy Ratio (ACRR), and propose E3 (Estimate, Execute, Expand): the agent estimates an initial operating point, executes a minimum viable path, and expands scope only when verification fails. On MSE-Bench--a deterministic benchmark of 121 edits in a capability-controlled simulator--E3 matches the strongest baseline's 100% success while cutting cost by 85%, tokens by 91%, and inspected files by 92%, and further beats a strong adaptive retrieval baseline by 16%; the gains survive held-out instruction wording and essentially every cost weighting. A companion real-model harness (LLM-Case) corroborates the effect on a live gpt-4o agent editing a real open-source library, with every candidate patch graded by actually running the project's real pytest suite against a measured oracle: the over-reading is milder but real, and E3 is the leanest and fastest policy at comparable task success--its one shortfall a provider rate-limit, not a wrong edit. We frame this as a controlled probe of execution redundancy, not a measurement of any deployed agent, and position task-aware execution as a step toward engineering-grounded AI (EGAI)--agents whose effort is anchored in the engineering reality of the task. We release the framework and benchmark.

---


> [!TIP]
> 当前位于：**51-99**（第 2/2 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-99**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
