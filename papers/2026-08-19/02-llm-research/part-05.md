# 🧠 大模型相关研究 | 2026年08月19日

> 本类共 **358** 篇论文：已确认 **337** 篇，待复核 **21** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**201-250**（第 5/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-358](./part-08.md)

---

### 201. [TaoLive Digital Avatar Agent Technical Report: Training Agents to Evolve with Their Harness](https://arxiv.org/abs/2608.15763)

**<font color=#1a73e8>作者：</font>** TaoLive AIGC LLM Team, Yuhan Sun, Wenhao Lin 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> AI-powered digital-avatar streamers in live e-commerce must answer product questions, engage viewers, and execute changing business strategies in real time. This requires low latency, factual and effective replies, and rapid adaptation to updated campaign, compliance, and style requirements. We develop an evolvable Harness that decouples Skills, Hooks, system prompts, and tools from model weights, allowing runtime behavior to change without retraining. However, Harness evolution creates a moving execution environment: compact models fine-tuned on one configuration may memorize names, schemas, and prompt templates rather than follow the Harness currently provided, while stronger zero-shot models are too slow for real-time use. We address this tension with Harness-Aware Training (HAT), which makes Harness states part of the training distribution. HAT applies task-preserving Harness-State Augmentation (HSA) to Skills, tool schemas, prompt structures, and interaction constraints, and comprises three stages: HSA-based supervised fine-tuning, general on-policy distillation to recover general capabilities, and HSA-based agentic reinforcement learning in a production-informed live-room simulator. Across four evaluation sets with more than 4,500 cases, our compact 35B model scores 94.8 on real-world Live-Stream QA, versus 80.3 for the base model and 93.0 for the strongest evaluated general LLM, while scoring 94.6 on Harness-Variant QA and retaining 83.5 on IFEval. By contrast, fixed-Harness SFT reduces IFEval by 7.7 points. In a controlled complete-agent replay on one NVIDIA H20 GPU with MTP enabled, the system achieves 3.407 s P50 and 8.114 s P95 latency. These results show that HAT produces a latency-feasible compact agent that remains effective under evaluated Harness changes without sacrificing general instruction following.

---


### 202. [Broken Symmetry in LLM Refusal: Answer Release Is More Local Than Refusal Restoration](https://arxiv.org/abs/2608.15772)

**<font color=#1a73e8>作者：</font>** Yiqi Liu, Yang Wang, Songxin Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When a language model refuses to answer a prompt, it is unclear whether the correct answer is erased from its internal representations, or merely suppressed at the output layer. We investigate this mechanism using a controlled withhold setting, which yields perfectly matched answering and refusal trajectories for bidirectional activation patching. We uncover a causal asymmetry in intervention locality under matched causal interventions, which we term broken symmetry. Even when a model generates a clean refusal, the correct answer remains linearly recoverable from its hidden states. Furthermore, releasing this withheld answer is a highly local operation, requiring only a single-position patch. Conversely, the reverse operation is not equally local: reimposing suppression requires broader interventions across multiple positions, and assembling a coherent refusal sequence is more difficult still. We further demonstrate that while an average answer-to-refusal displacement vector marks the geometric difference between these states, it fails to act as a reliable, reversible linear control toggle between behaviours. Taken together, our findings show that refusal does not function as a simple symmetric switch. For safety and auditing, this implies that probe recoverability can overestimate true behavioural control, and locating refusal-relevant directions does not reliably grant the ability to steer a model from answering to coherent refusal.

---


### 203. [Routing Divergence Is Not Evidence of Behavioral Influence in Same-Weight MoE Self-Distillation](https://arxiv.org/abs/2608.15787)

**<font color=#1a73e8>作者：</font>** Cedric Caruzzo, Donggeun Yoo, Tae Soo Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Two Mixture-of-Experts (MoE) forward passes can share every weight yet route the same token through different experts. This creates a possible blind spot in same-weight self-distillation, where a demonstration-conditioned teacher supervises a query-only student. We study this mismatch in its single-step form, with frozen weights rather than as a proxy for a full training trajectory. An exact blockwise decomposition separates a routing term, which changes gates at fixed content, from a dense-like content term. Across seven open-weight checkpoints and two domains, the routing term spans only $1.6\times$ as a fraction of block output, while its residual-stream exposure spans $3.2\times$. Exposure is ordered by the routed block's share of the residual. Scaling the always-on backbone in two confirmatory models moves exposure monotonically; common-mode controls support a mass-and-coherence mechanism rather than denominator dilution alone. Preregistered PubMedQA patches on three models show that the full routing term moves outputs by less than half the natural context effect and is largely reproduced by matched-norm noise, whereas the content term is strongly direction-specific. Scale and merged-expert probes show that the narrow block-level range is not universal, although exposure remains small at the tested boundaries. Router movement alone is therefore not evidence of behavioral influence: measure exposure first, and use a behavioral intervention when the decision matters.

---


### 204. [KV-Rescue: Recovering Reasoning Language Model KV Eviction Loss via Stepwise Interleaving](https://arxiv.org/abs/2608.15797)

**<font color=#1a73e8>作者：</font>** Minsoo Cheong, Woosang Lim, Vincent-Daniel Yun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> KV-cache eviction caps the memory cost of long reasoning traces but is inherently lossy because the model decodes from a partial view of its history. Under aggressive budgets, this not only lowers accuracy but can also cause runaway degeneration, where the model produces incoherent or repetitive tokens until reaching the length limit. We characterize much of this loss as an information gapf caused by missing context, rather than a capability gap caused by limited model capacity. An evicted 7B model and a full-context 1.5B model make complementary errors, and an oracle choice between their answers recovers 79% of the accuracy gap to the full-KV 7B model. Based on this observation, we propose KV-Rescue, a training-free inference framework that bridges the information gap introduced by KV eviction using a lightweight full-context helper. KV-Rescue interleaves reasoning steps from the two models into a shared trajectory. An online detector uses entropy and compressibility to terminate the generation of incoherent or repetitive base-model candidates early. Across five math benchmarks with Qwen2.5-Math 7B and 72B, KV-Rescue recovers an average of 87% of the accuracy lost to eviction at eviction budget B=64. A decode-cost analysis further shows that preventing runaway degeneration cuts base-model token generation by 43% on average.

---


### 205. [Cross-Entropy Risk Estimation for Language Models: Inconsistency Must Be Dense, and the Holdout Method Is No Exception](https://arxiv.org/abs/2608.15798)

**<font color=#1a73e8>作者：</font>** Hanti Lin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language models are compared by their held-out per-token cross-entropy risk---the quantity scaling laws are fitted to. We show that it cannot be consistently estimated. Consistency, or convergence to the estimand, is defined relative to a \emph{possible state of the world}: a pair consisting of a data-generating distribution and a model we turn out to train. Quantifying over models as well as data-generating mechanisms is essential, because what decides whether a model's risk is estimable is a tail property of the distribution its weights induce, which no sample reveals. The per-token cross-entropy risk is hard to estimate because of a topological fact: among the possible states, finite risk and infinite risk each lie arbitrarily close to every instance of the other. Consequently no estimator---not merely the holdout average---is consistent at every state at which the risk is defined. Worse, inconsistent estimation persists under both bounding the expected sequence length and restricting to full-support models; and in that restricted setting the states at which inconsistency occurs are even dense. Two interesting ways out are identified, and neither is free. Way out 1: using a bounded context window, we can floor a model's next-token probabilities, making its risk finite exactly when the data-generating distribution has finite expected sequence length---a new, statistical rationale for a choice that was made on computational grounds, though the assumption it substitutes is itself beyond the reach of any test. Way out 2: reporting the risk only when it falls below a threshold fixed in advance restores consistency, at no cost to what model selection actually requires---but we need to recognize that the goal of estimation is revised.

---


### 206. [Using the Mimi codec for metalinguistic representations](https://arxiv.org/abs/2608.15799)

**<font color=#1a73e8>作者：</font>** Artem Saloev, Erin Pacquetet, Nicolas Ballier  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In this paper, we focus on the dictionary of 2048 tokens used in Mimi semantic token codebook, the neural codec of the Moshi language model. We show that the ABX experiment carried out with Mimi fails to capture the mapping of the semantic tokens to phone realisations. By realigning Mimi representations to the TIMIT corpus transcriptions, we show that the 2048 tokens IDs of the semantic codebook map to quadphone, triphone, biphone, phone and subphone realisations.

---


### 207. [PWLR: Pairwise Witness Local Rejection for Boundary-Aware Out-of-Distribution Detection](https://arxiv.org/abs/2608.15802)

**<font color=#1a73e8>作者：</font>** Chengyao Jia, Ruixuan Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Out-of-distribution (OOD) detection remains challenging for image classifiers, especially when near-OOD samples lie close to in-distribution (ID) class boundaries. Recent vision-language detectors improve OOD detection through class semantics, local prompting, or LLM-generated outlier concepts, but seldom use language as explicit boundary evidence between confusing ID classes. We propose Pairwise Witness Local Rejection (PWLR), which uses an MLLM offline to describe visible local cues that favor one ID class over a specific rival class. These cue phrases are then screened with ID-only data under a frozen vision-language backbone, so that only reliable local verifiers are kept. At inference, PWLR first retains a small set of globally plausible classes, then checks whether any of them is locally supported against its most relevant rivals, and finally combines this pairwise local evidence with the global class score through calibration. Experiments on ImageNet-100 far-OOD, cleaner/challenging OOD and near-OOD benchmarks show that PWLR consistently improves strong vision-language baselines across multiple backbones. Source code will be released.

---


### 208. [Hallucination Span Detection with Input-Side Evidence Alignment](https://arxiv.org/abs/2608.15804)

**<font color=#1a73e8>作者：</font>** Miyu Yamada, Yuki Arase  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Hallucinations remain a major obstacle to the reliable use of large language models (LLMs) in conditional text generation. Existing methods primarily assess the factuality of an entire generated text, providing limited insight into which output spans are hallucinated or how they relate to the input. We introduce the task of hallucination span detection with input-side evidence alignment, which jointly identifies hallucinated spans and aligns output tokens with the corresponding input evidence. Our approach is based on the observation that faithful output tokens are predictable from the input, whereas hallucinated tokens are not. We therefore train an encoder-based model to predict masked output tokens from the input representation, using prediction confidence for hallucination detection while naturally producing alignments to the input. Experiments show that the proposed method effectively detects hallucinated spans and identifies meaningful input-side evidence. Human evaluation confirms the quality of the predicted alignments.

---


### 209. [A Pre-Specified Construction-Confirmation Test of Operation-Level Causal Transfer Across Finite Isomorphic Symbolic Domains](https://arxiv.org/abs/2608.15809)

**<font color=#1a73e8>作者：</font>** Xinyi Shan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Behavioral accuracy, linear decodability, and successful activation interventions do not by themselves show that a model carries an operation-level structure from one symbolic domain to another. We ask a narrower question in finite isomorphic state spaces: if the hidden-state difference between two operations is estimated separately for each source input, does adding that difference to a mapped recipient input move the model toward the corresponding recipient answer? The design compares this input-specific intervention with wrong-operation, norm-matched random, and no-op controls, and separates candidate construction from an independently isolated confirmation split. On a frozen Qwen2.5-7B-Instruct model at layers 20--21, one route--domain--operation candidate from a family pre-specified and frozen before confirmation access, transparent | integer_mod16--letters16 | successor->predecessor, passed both PyVene splits; its confirmation intersection--union p-value was 0.000198 and its 36-family Holm-adjusted p-value was 0.006943. A subsequent NNsight 0.7.0 experiment, pre-specified and frozen before its confirmation access, tested only this selected prompt route, without candidate or layer reselection. It reproduced all 12 confirmation effect estimates, confidence intervals, and exact sign-flip p-values numerically; its 36-family Holm-adjusted p-value was 0.007141. The result is therefore limited to one prompt route and one candidate, replicated across two intervention implementations on one model revision and one layer interval. It does not establish cross-model generalization, full-family backend independence, domain-general transfer, or algebraic invariance.

---


### 210. [Assessing Attack Surfaces in Generative Search Engines through Publisher Attributes: A Case Study in Political Domains](https://arxiv.org/abs/2608.15814)

**<font color=#1a73e8>作者：</font>** Riku Mochizuki, Shusuke Komatsu, Souta Noguchi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We characterize the attack surface of generative search engines (GSEs) against poisoning attacks in the political domain, from the perspectives of citation selection and personalization. GSEs integrate web search and answer generation with user preferences and backgrounds using large language models (LLMs). They play a crucial role in how users access information on the web. Because anyone can publish content on the web, GSEs are vulnerable to poisoning attacks that manipulate citations to undermine reliable information delivery. Existing studies on citation evaluation focus on how faithfully answers reflect cited content. However, they leave unexamined the two critical aspects to capture the attack surface of GSEs against poisoning attacks: which publishers GSEs prefer to cite, and how personalization affects citation behavior. To fill this gap, we introduce an evaluation framework that characterizes the attack surface of GSEs against poisoning attacks. Our contributions are twofold: (1) we propose a novel metric, \emph{content-injection barrier}, which quantifies the difficulty of injecting arbitrary content onto the web with a given level of publisher authority; and (2) we reveal how personalization affects citation behavior by embedding user profiles into GSEs. We conduct experiments on three major GSEs in the political domain of the United States and Japan. Our results show that (a) the attack surface differs across GSE models; (b) the web search functionality of GSEs shapes the attack surface; (c) ruling parties have a broader attack surface than opposition parties; and (d) user profiles have little influence on the attack surface.

---


### 211. [RLCascadeRouter: Quality-Estimator-Free Cascade Routing via Reinforcement Learning](https://arxiv.org/abs/2608.15817)

**<font color=#1a73e8>作者：</font>** Shihong Huang, Shengjie Wang, Hong Ma 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The growing ecosystem of large language models (LLMs) offers huge potential to optimize performance-cost trade-offs. However, their heterogeneous capabilities and inference costs make efficiently routing queries a significant challenge. Existing paradigms are inflexible: one-shot routers commit before observing responses, whereas conventional cascades stop adaptively but follow a fixed model order. Cascade routing removes both restrictions by reconsidering whether to stop or invoke another model after each response. Current methods use a predict-then-optimize pipeline estimating response quality and future model utility. However, prediction loss for quality or utility is not equivalent to routing-decision loss. A lower prediction error does not necessarily yield a better action; a small boundary-crossing error can reverse a ``stop'' or model-selection decision. Therefore, we propose RLCascadeRouter, a quality-estimator-free framework that formulates cascade routing as a Markov decision process with actions comprising ``stop'' and model selection. It uses trajectory returns and advantages to directly optimize the performance-cost objective. Its Cascade Policy Network models candidate complementarity for model selection and remaining-action value for stopping, eliminating independent post-hoc response-quality estimators. Evaluated across ten LLMRouterBench benchmarks with thirteen LLMs, RLCascadeRouter outperforms strong baselines and achieves superior performance-cost trade-offs. It incorporates unseen models without retraining, and ablation studies validate both policy components.

---


### 212. [Schema-Agnostic Graph Reasoning Agent for Hybrid Knowledge Graphs](https://arxiv.org/abs/2608.15834)

**<font color=#1a73e8>作者：</font>** Marius Dragic, Ruben Ifrah, Alexandre Rio  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool-calling LLM agents navigate unfamiliar codebases with a handful of generic primitives for listing, reading and searching files (ls, cat, grep). A knowledge graph admits the same interface: listing neighbours, reading node content and searching descriptions are the same operations on a different substrate. Building on this correspondence, we present GRA, a Graph Reasoning Agent that explores hybrid knowledge graphs, whose nodes are either textual concepts or relational tables, with seven generic tools, discovering everything domain-specific at run time. On UFK-M (Unified Factory Knowledge Model), an industrial benchmark of 258 analytical questions whose gold answers are produced by executing validated SQL programs, GRA beats a full-context agent by 5.1 pp (88.4% vs. 83.3%), while reading under a third of its input tokens. A graph-free control shows the gain comes chiefly from selective agentic access rather than graph topology, and that the effect depends on a model able to drive tools reliably. Seeing less, the agent answers better: selective navigation over a structured substrate beats exhaustive context.

---


### 213. [MicroVerse: An Instrument for Measuring Self-Authored Identity Drift in Long-Horizon Multi-Agent Language-Model Simulations](https://arxiv.org/abs/2608.15844)

**<font color=#1a73e8>作者：</font>** Sky Ng, Brihi Joshi, Ishan Gupta 等 47 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-horizon, multi-agent language model (LM) simulations are widely proposed for studying social behavior, yet instruments to measure whether persona-conditioned agents maintain identity fidelity under sustained pressure are lacking. We present MicroVerse, a behavioral-science instrument that measures identity drift in generative agents. Agents carry an immutable "soul file" (core values, moral boundaries, personality, goals) and inhabit a resource-scarce 50 x 50 environment where water is a non-respawning survival constraint. Scarcity is operationalized via a per-tick existence-cost gradient. The eight-verb action space maps directly to moral boundaries (trade, talk, attack, scavenge). Using a three-layer memory architecture, agents periodically revise a mutable current identity against their immutable original soul via importance-triggered reflection. To mitigate survivor bias, MicroVerse decouples measurement from behavior using uniform longitudinal engine snapshots every N ticks alongside a forced-end snapshot of all living and dead agents. Identity drift is scored offline using a paraphrase-aware, value-anchored, multi-register diff rather than raw cosine similarity. We evaluate the instrument via a controlled seed run (n = 25) and a reflection-threshold sweep (thresholds {40, 80, 150}) to determine if drift dynamics are gate artifacts or threshold-robust properties. We report two primary findings: (1) Anti-self-deception emerges unprompted as the single largest semantic category of identity modification (27 of 111 added boundaries, 24%). (2) The system is threshold-robust; lower gates accelerate and increase revision frequency but preserve drift direction. All empirical results are strictly preliminary existence proofs and effect shapes (one model, one seed per arm, n = 25) rather than statistical significance claims.

---


### 214. [RAGas: Retrieval-Augmented Gas Optimization for Smart Contracts with Continuous Knowledge Integration](https://arxiv.org/abs/2608.15857)

**<font color=#1a73e8>作者：</font>** Yishun Wang, Wenjin Yi, Wenkai Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Ethereum is now integral to mission-critical sectors, including finance, healthcare, and supply chain management. Execution fees, commonly referred to as Gas, scale with the computational complexity of their functions. Smart contracts on Ethereum incur execution fees, known as Gas, which increase with computational complexity. Thus, optimizing Gas-intensive code while preserving functional equivalence significantly lowers deployment costs. No existing system continuously exploits evolving Gas usage patterns. We systematically analyze syntactic and semantic constructs that drive excessive Gas use. This yields six high-level categories covering twelve fine-grained antipatterns underpinning a curated knowledge base. We operationalize these insights with RAGas, a three-stage retrieval-augmented generation framework that uses a large language model to pinpoint and automatically fix Gas inefficiencies. Experiments on deployed contracts demonstrate that RAGas reduces Gas usage by up to 11% and achieves high precision and recall in detecting code snippets exhibiting Gas wastage.

---


### 215. [Beyond Visual CoT: Internalized Visual Thinking for Proactive Video Reasoning](https://arxiv.org/abs/2608.15869)

**<font color=#1a73e8>作者：</font>** Xiaoyu Zhu, Xinke Deng, Suresh Taddewadikar 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models increasingly use visual chain-of-thought (Visual CoT) to reason about spatial, temporal, and embodied environments. By generating intermediate reasoning images, Visual CoT provides an intuitive mechanism for visual foresight but introduces substantial inference overhead, which is particularly problematic for proactive video reasoning. We ask whether models can learn to think visually during training while reasoning directly at inference. We introduce Internalized Visual Thinking (IVT), a post-training framework that jointly optimizes textual prediction and next-embedding prediction over unlabeled videos. Given a partially observed video, IVT predicts latent representations of future frames together with the target textual answer, encouraging the model to capture motion, object transitions, interactions, and latent intent. At inference, IVT generates the answer directly without synthesizing or re-encoding future frames. We conduct controlled studies across target representations, decoder designs, prediction horizons, data mixtures, training curricula, and predictive objectives. IVT improves over direct-answer fine-tuning on all six evaluation settings while retaining the same inference pathway. Compared with explicit Visual CoT, IVT achieves comparable or better performance and reduces average end-to-end latency by more than 5x. Together, our findings suggest that explicit pixel-space generation at inference time, as used in visual chain-of-thought, may not be necessary for effective proactive video reasoning. Predictive world modeling can be internalized during training to produce multimodal reasoners that are both more accurate and substantially more efficient.

---


### 216. [Dear Algo: A Precision-First Agentic Intent Layer for Unified Search and Recommendation](https://arxiv.org/abs/2608.15877)

**<font color=#1a73e8>作者：</font>** Rui Wang, Jiazhou Wang, Zheng Wei 等 19 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Search and recommendation serve a shared discovery objective but encode intent differently. We study this boundary through Dear Algo on Threads, a deployed product where open-ended requests such as \emph{more NBA news} or \emph{less politics} steer subsequent feed recommendations rather than return a one-shot result list. Its agentic intent layer compiles explicit, inferred, negative, and compound intent into a grounded executable plan, then invokes conventional retrieval and optional semantic or multimodal reranking. The layer shares an intent-to-retrieval contract without requiring one model or serving path across search-like and recommendation-like modes.
We evaluate Dear Algo under a precision-first objective. In a blinded audit of 300 public request-item pairs (296 evaluable), a strict categorical LLM-as-a-judge gate achieved 94.4\% exact-Relevant precision [88.8\%, 98.9\%]. Across 72 normalized request clusters, the full configuration produced 7.73 judge-qualified candidates per 20 slots versus 6.61 for an LLM-derived-query baseline, a gain of 1.11 [0.12, 2.12]. In a candidate-randomized serving-path study restricted to the reranker path's first 72 eligible hours, the user-weighted judge-Irrelevant share among judged admissions was 2.80\% versus 4.78\% off (-1.97 points [-3.02, -0.94]), while Exact-Relevant share was 2.24 points higher [0.08, 4.41].
Together, these studies show how explicit natural-language intent can be carried into feed recommendation under a precision-first evaluation framework

---


### 217. [When Less Is Enough: Context Selection and Prompting Strategies for Bengali News Headline Generation](https://arxiv.org/abs/2608.15879)

**<font color=#1a73e8>作者：</font>** Muhammad Ashad Kabir, Kawsar Ahmed, Md. Osama  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have shown strong performance in text generation tasks, yet their effectiveness on headline generation remains sensitive to how input context is selected and presented. In this work, we investigate Bengali news headline generation as a document-level generation task that requires effective selection and presentation of salient contextual information from long-form articles. Using Gemini-2.0-Flash, Llama-3.3-70B, and GPT-4o, we systematically study the effects of context selection, prompting strategies, and in-context learning (i.e., few-shot) on the quality of headline generation. Our experiments show that providing the full article does not necessarily improve performance; instead, using selected lead paragraphs of the article can maintain, and in some cases improve, headline generation quality. We further compare Bengali Native Prompting (BNaP) and Cross-Lingual Prompting (XLP), and examine how each interacts with context-enriched prompt templates incorporating auxiliary contextual cues. Results demonstrate that prompting strategies substantially influence generation quality: XLP often yields stronger performance, particularly when combined with contextual enrichment, but its benefits are model-dependent. Additionally, few-shot prompting substantially improves Gemini, with most of the gain obtained from a single demonstration, whereas Llama shows limited benefit from additional examples. Overall, our findings highlight that effective Bengali news headline generation depends more on context relevance and prompt design than on increasing input length, offering practical insights for multilingual and low-resource LLM applications.

---


### 218. [Deploying Frontier Agentic Technology in MOOSEnger, a Multiphysics-Capable AI Assistant](https://arxiv.org/abs/2608.15881)

**<font color=#1a73e8>作者：</font>** Zaid Abulawi, Mengnan Li, Guillaume Giudicelli 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Multiphysics Object-Oriented Simulation Environment (MOOSE) is an open-source finite-element framework for building multiphysics simulation applications. Using a multiphysics environment effectively demands specialized expertise, creating a barrier for many domain scientists and engineers. MOOSEnger, developed at Idaho National Laboratory (INL), is a domain-specific, tool-enabled AI agent built for the MOOSE Framework. This work extends MOOSEnger with a harness focused on locally-hosted models. The harness gives the agent a full pipeline: it retrieves contextual knowledge from the MOOSE repository, validates and diagnoses the resulting input through interaction with the simulation executable environment, and extracts and stores lessons in a persistent memory.
The resulting framework is demonstrated on an engineering problem from the National Reactor Innovation Center Virtual Test Bed (VTB), illustrating its potential to support realistic multiphysics simulation workflows. Additionally, the agent performance is evaluated on different categories including diffusion, Navier--Stokes, phase field, plasticity, porous media flow, solid mechanics, transient heat transfer, and reactor mesh generation. Each category consists of 25 prompts/cases. We compare MOOSEnger-Gemma4 against MOOSEnger-GPT-5.2, alongside baseline Gemma4 and GPT-5.2 without agentic capabilities. MOOSEnger-GPT-5.2 shows a slight edge, achieving a 90\% success rate versus 76.5\% for MOOSEnger-Gemma4. The baseline models perform far worse, at just 5\% (GPT-5.2) and 0\% (Gemma4), underscoring the impact of the agentic harness.

---


### 219. [Bounded Agents: Delegation Security for Multi-Agent AI Systems](https://arxiv.org/abs/2608.15888)

**<font color=#1a73e8>作者：</font>** Xabier Muruaga  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based agents can act on behalf of a user to access cloud services, call tools, or invoke agents. At session start, the agent's permissions are set but remain static, and each request is evaluated independently, without considering prior actions. Within its permissions, an agent may act contrary to the delegated task, combine individually permitted actions into a prohibited outcome, or delegate authority to a sub-agent without limiting it. A prompt injection poses a risk only if the agent has authority to perform such actions; this is therefore a problem of authorization architecture, not just the model. The Agentic Principal Chain (APC) tracks delegated authority from one principal to the next. APC evaluates each request against the accumulated session state using six authorization checks. APC carries forward and restricts delegated scope and budgets. Using composition closure, APC checks requests against prior actions to prevent prohibited combinations and enforces the decision outside the model. We prove Blast Radius Monotonicity and Composition Soundness for APC implementations; Composition Soundness is limited to prohibited combinations under a complete restriction set and serialized admission. We evaluated 3,154 instances including InjecAgent, AgentDojo, and ASB. Our compromised-model evaluation tests APC independently of model behavior by inserting the ground-truth attack call after the first legitimate tool call. AgentDojo exfiltration fell from 75-100% to 0% across all four domains; APC blocked all 544 InjecAgent data-stealing cases. Intent binding reduced destruction from 38.6% to 4.0% and manipulation from 90.5% to 12.1%. Authorization latency was 0.24 ms at the 99th percentile on an idle host; across 949 AgentDojo task-injection pairs, utility was 8.6 and 13.9 percentage points lower in the two settings. Implementation, evaluation tools, and data are publicly available.

---


### 220. [Breaking and Defending LLM-Powered Social Media Bot Detection Systems](https://arxiv.org/abs/2608.15893)

**<font color=#1a73e8>作者：</font>** Nof Orenstein, Yoni Birman  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The rise of social media bots poses a persistent threat, enabling misinformation, opinion manipulation, and the erosion of trust in online platforms. To combat this, machine learning systems have been developed to detect and limit bot activity, but attackers continuously adapt through techniques such as adversarial learning and behavior imitation, fueling an ongoing arms race between bots and detection tools. Recent advances in large language models (LLMs) have significantly improved bot detection by enabling deeper semantic and contextual analysis of accounts and their content. However, this shift also introduces new attack surfaces, allowing adversaries to craft exploits that directly target the reasoning and generation mechanisms of LLM-based classifiers. Industry tools such as Anthropic's Claude Code Security similarly leverage LLMs for security-critical decisions, further motivating a careful study of their attack surfaces. In this work, we investigate both the offensive and defensive aspects of LLM-powered, threat-specific cybersecurity applications. While centered on the challenge of social media bot detection, our methodology and insights generalize to a broad class of LLM-powered cybersecurity systems, including phishing detection, email classification, and fraud analysis. We introduce two novel adversarial attack strategies that systematically exploit the semantic and contextual weaknesses of LLM-based classifiers, degrading their detection accuracy by up to 48%. To counter these threats, we propose a robust multi-LLM defense architecture designed to preserve detection reliability under adaptive adversarial conditions. Our solution, LSABRE (LLM-powered Social Adversarial Bot Recognition Ensemble), is a multi-LLM framework that substantially improves robustness across a range of attacks, maintaining 86% detection accuracy even under strong, adaptive adversarial pressure.

---


### 221. [CLARA: Clip-Level Multimodal Alignment with VLM-Derived Rationales for Hateful Video Detection](https://arxiv.org/abs/2608.15905)

**<font color=#1a73e8>作者：</font>** Yuchen Zhang, Shuang Dai, Zeyu Fu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hateful video detection has become increasingly important with the rapid growth of video-centric social media platforms, given the serious risks that hate speech poses to both individual well-being and social cohesion. Compared with text or static multimodal content, hateful video detection remains underexplored and significantly more challenging, as hateful meaning often arises from complex interactions among multimodal cues, including speech, audio, and visual content. Moreover, such signals are often brief, implicit, and temporally dependent, making them difficult to capture using conventional video-level representations. In this work, we propose CLARA, a clip-level multimodal framework for hateful video detection. Instead of treating a video as a single instance, CLARA models it as a sequence of fine-grained clips, enabling more precise capture of temporally localized hateful signals. We introduce a Mixture-of-Experts clip encoder for adaptive multimodal alignment, a local-global segment contrastive objective to jointly model short-term cues and long-range temporal dependencies, and VLM-derived rationales integrated via a gated Transformer to provide high-level semantic guidance. Extensive experiments on three hateful video datasets demonstrate that CLARA consistently outperforms state-of-the-art methods. Further ablation studies and parameter analyses validate the effectiveness of each component.

---


### 222. [UI-Mate: Advancing Open-Weight Foundation GUI Agents with In-Context Demonstrations](https://arxiv.org/abs/2608.15930)

**<font color=#1a73e8>作者：</font>** Zihan Ding, Longxu Dou, Qi Gao 等 29 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Foundation GUI agents can automate complex digital tasks, but deployment is hindered by scarce and biased training data, ambiguous prompts, and unreliable execution. Routine workflows rely on user-specific tools and tacit conventions, so unstated instructions can produce arbitrary variations across runs. We present UI-Mate, a foundation GUI agent that integrates an environment-grounded training stack with in-context demonstration learning. UI-Mate makes three contributions: A Scalable Environment-Grounded Training Stack: A closed-loop data engine automates task generation, environment construction, rollout, filtering, capability balancing, SFT, and online RL across massively parallel environments via unified task-verifier bundles. In-Context Demonstration Learning: A mechanism that transforms multimodal demonstrations into flexible subtask-level workflows, follows relevant demonstrated steps, and re-plans from the live interface. OSWorkerBench Benchmark and Insights: A benchmark of 100 long-horizon office tasks across 41 applications that supports instruction-only and demonstration-guided evaluation. Its demonstration resources separate a 33-task self-demo setting, built from successful strong-agent rollouts of the same targets, from a 45-task variant-demo setting, built from human recordings of related but non-identical tasks. Experiments show that UI-Mate-27B sets a new open-weight state of the art on general computer-use benchmarks, scoring 77.0% on OSWorld-Verified and 66.2% on WindowsAgentArena. On OSWorkerBench, it reaches 41.0% strict success and 76.9% progress, outperforming its Qwen3.6-27B base by 17.7 and 24.5 points. On the 33-task self-demo subset, one demonstration raises strict success from 17.2% to 35.4% and progress from 67.9% to 81.1%, substantially improving long-horizon reliability. Project page: this https URL.

---


### 223. [PLSQLBench: Benchmarking LLM Systems for Executable Procedural Database Programming](https://arxiv.org/abs/2608.15931)

**<font color=#1a73e8>作者：</font>** Marianne Menglin Liu, Leonid Boytsov, Daniel W. Peterson 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present PLSQLBench, to our knowledge the first benchmark for evaluating whether LLMs can write executable PL/SQL programs, with correctness measured through execution-based tests. Existing LLM evaluations largely target general-purpose code generation or declarative text-to-SQL, leaving procedural database programming underexplored. PLSQLBench contains 2,865 instances: 2,594 single-turn tasks and 271 multi-turn conversations spanning 978 turns. The benchmark combines complex schema-grounded tasks over enterprise-style Spider 2 databases, simpler schema-grounded tasks derived from Spider, and MBPP-derived procedural problems, covering varying levels of database grounding and procedural complexity. Experiments with eight LLMs reveal recurring difficulties in schema grounding, PL/SQL dialect fidelity, procedural control flow, exception handling, and cross-turn consistency. Tool-augmented LLM agents improve performance on several schema-grounded evaluations, although substantial gaps remain. These results highlight procedural database programming capabilities not directly assessed by conventional code generation or text-to-SQL benchmarks. Our code is available at this https URL.

---


### 224. [Augmenting Text to Increase Translation Difficulty](https://arxiv.org/abs/2608.15932)

**<font color=#1a73e8>作者：</font>** William Kalikman, Šimon Sukup, Michal Tešnar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As state-of-the-art machine translation models saturate standard benchmarks, the field needs more challenging evaluations to distinguish between models of varying quality. We propose augmenting existing benchmarks to increase translation difficulty by combining adversarial optimization with a differentiable translation difficulty estimator. Our Adversarial Translation Optimization (ATO) uses gradients from a combined difficulty and fluency objective to iteratively replace tokens. Because each step branches over candidate substitutions at every position, optimization becomes a tree search problem, which we address with Beam Search. ATO offers a gradient-based alternative to LLM-based dataset creation without LLM prompting, expensive human curation, or task-specific model training. Our ATO-modified benchmark lowers average translation quality (xCOMET) from 0.93 to 0.82, compared to 0.88 for paraphrasing and 0.86 for a zero-shot baseline. Human evaluation shows the modified texts are somewhat less natural than the baselines but remain reasonably grammatical and plausible while being substantially harder to translate. We release two datasets of 350 English texts each, generated by our methods, as well as the code.

---


### 225. [Token Distribution versus Data Volume: Domain Balancing in Multi-Domain Meeting Summarisation](https://arxiv.org/abs/2608.15935)

**<font color=#1a73e8>作者：</font>** Ashima Sood, Bryan Gardiner, Joan Condell  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Jointly fine-tuning an LLM on meeting-summarisation corpora of widely varying size raises a question that prior work leaves confounded: when a domain-balanced training mixture helps, is the gain due to the distribution of tokens across domains, or merely to the volume of data seen? We disentangle these factors by constructing balanced and natural (native-proportional) token mixtures at matched token budgets (2-32M) over five English meeting corpora, fine-tuning Mistral-7B with QLoRA, and evaluating per domain. Balancing redistributes quality, improving the data-scarce minority domains at a low cost to the data-rich ones. The trade favours balancing whenever the minority domains matter: their share under proportional allocation is fixed at 1-2% regardless of budget, so matching balanced quality on those domains requires far more total data. We further find that pruning low-value transcript lines removes ~15% of tokens from the conversational corpora at no measurable cost, and that balancing by tokens is not the same as balancing by examples. A two-annotator study of 741 judge-labelled facts validates our fact-level evaluation. Together these results give practitioners a basis for deciding when to balance an imbalanced multi-domain mixture, and on what unit.

---


### 226. [Aborted but Not Forgotten: KV-Cache Retention Breaks Rollback Consistency in Language Agents](https://arxiv.org/abs/2608.15939)

**<font color=#1a73e8>作者：</font>** Guijia Zhang, Harry Yang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Stateful language agents assume a rejected branch can be taken back by clearing it from the application transcript. We show this breaks when the serving session retains key/value (KV) state across the logical abort: the model can continue attending to content the application believes it discarded. We formalize the missing guarantee as rollback consistency: a complete abort must restore the state the model attends, not just the transcript. The key failure is cross-layer: a correct logical rollback need not compose with retained inference state, and the gap can remain invisible to the application. To isolate cache effects from text effects, we introduce a same-token/different-cache audit that holds decision-step tokens identical while varying only whether the cached prefix is stale or rebuilt from committed state. Across seven open-weight families (3.8B-36B), retained KV alone flips a typed protected effect in 25 of 63 audited cells, while attacker tokens are absent from the served request in all 63; rebuilding the cache closes every cell. The channel reproduces in an end-to-end session application, on the default Hugging Face Transformers cache-reuse path, and under LangGraph time-travel, where verified logical rollback can still leave attended KV stale. Susceptibility varies across models, but the underlying attended-state integrity violation is structural. We rule out position and length confounds, generalize across protected effects, policy structures, and a cache-isolated Mixture-of-Experts model, and show that transaction-local cache restoration closes the channel without requiring a global cache flush. All headline results are deterministic and reproducible from released artifacts.

---


### 227. [Navigation-Informed Embeddings: Dense-Retriever Adaptation from Agent Search Traces](https://arxiv.org/abs/2608.15956)

**<font color=#1a73e8>作者：</font>** Shrey Shah, Levent Ozgur  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic retrieval workflows produce query, retrieval, and stopping traces as a byproduct of answering questions. We study how these traces can adapt a deployed dense retriever to changing workflow distributions without new relevance labels, synthetic queries, or LLM judgments. We introduce Navigation-Informed Embeddings (NIE), a family of trace-derived objectives. NIE-Stop turns the stopping document into a soft positive; NIE-Path additionally uses preceding path documents as hard comparisons and imposes ordinal constraints with geometric decay. A BGE encoder adapted from retained source trajectories improves support Recall@20 on an independent target benchmark from 72.2 to 78.0 overall. NIE-Stop reaches 76.9 overall and 52.3 on long paths; NIE-Path raises long-path performance to 55.4, compared with 46.7 for the unadapted encoder. A shuffled-order control under the full path objective loses 3.2 points. Without public-benchmark training, the same adapter also improves nDCG@10 by 1.9 points on standard BEIR HotpotQA. NIE therefore provides a lightweight adaptation channel for settings where trajectories are already retained, with zero incremental labeling cost.

---


### 228. [SEER: Long-Context Reasoning via Selective Visual-Text Compression](https://arxiv.org/abs/2608.15962)

**<font color=#1a73e8>作者：</font>** Jiawei Xu, Zhilin Zhai, Jinrui Fang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-context reasoning remains computationally expensive for large language models due to the quadratic complexity of attention over text tokens. Visual-text compression offers a promising alternative by rendering text into images and processing them with vision-language models, often reducing token usage. However, existing approaches apply uniform compression regardless of query relevance, potentially sacrificing precision where detailed extraction is required. We present SEER, a framework that learns to select query-relevant images through visual scanning and retrieve textual content only where needed, combining the efficiency of visual compression with the precision of text-based reasoning. Through supervised fine-tuning on tool-interaction trajectories, SEER learns adaptive tool invocation for selection and retrieval. Experiments on long-context benchmarks show that SEER improves extraction precision through selective text retrieval while retaining average prompt-token savings relative to full-text baselines. On LongBench, SEER achieves 51.11% average accuracy, outperforming the visual-text baseline Glyph-9B by 2.33 points and Qwen3-8B by 3.49 points. Code can be accessed at this https URL

---


### 229. [LLMs Get Smarter from Targeted Synthetic Multilingual Data](https://arxiv.org/abs/2608.15964)

**<font color=#1a73e8>作者：</font>** Ishika Agarwal, Arkajyoti Charaborty, Tanner Sorensen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language-specific competency (LSC) is the phenomenon of a language model performing better or worse depending on the language of the prompt. In other words, a language model outputs different (and potentially incorrect) responses to the same semantic query when prompted in different languages. Prior work attributes this to an internal misalignment of semantic representation across languages. Currently, there are two main approaches to address LSC in the literature: (1) routing all queries through English, improving performance, but limiting language expressivity to English; or (2) training on language-balanced data, equalizing model performance across languages, but reducing overall performance. In this work, we take a data centric perspective and introduce HOTFIXR: Hardness Optimized Training data For Improving X-Lingual Reasoning. It is a data generation framework that uses models to probe and learn a student model's multilingual weaknesses, and generates data to mitigate them. HOTFIXR can generate multilingual synthetic training data that can improve multilingual performance. We evaluate on three in-distribution tasks, three out-of-distribution tasks, and four out-of-distribution languages. On average, HOTFIXR (1) improves in-distribution performance by 6.2%, (2) reduces catastrophic forgetting (induced by fine-tuning) on OOD tasks by 3.7%, and (3) on OOD languages by 7.1%. Overall, as many real-world applications requires multilingual LLMs, our work contributes to the efforts of making LLMs multilingually proficient. We will release code upon acceptance.

---


### 230. [Fiber Fingerprints of Hidden Learning-State Dynamics](https://arxiv.org/abs/2608.15976)

**<font color=#1a73e8>作者：</font>** Qinyou Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A learning system can occupy execution states that are indistinguishable under every declared present-behavior readout yet respond differently to future training. We formalize this through fiber fingerprints: controlled future-learning response laws restricted to present-behavior equivalence classes. Prefix-compatible finite probes induce a predictive quotient functor, a Nerode-type minimal recursively sufficient representation, and a canonical set-level predictive fiber without assuming smoothness, reversibility, finite rank, or a manifold. Under an explicit finite-dimensional Hilbert realization, response decomposes into visible, visible-mode-reuse, and irreducible-new sectors; a history-reachability bridge retains only distinctions generated by natural training histories. Conditional mechanism results then identify a graph-Hodge chronology decomposition, a regular switching class with root-mean-square scale $\sqrt{p}\eta^{3/2}$ and finite-scale corrections, and an exact Adam moment section whose immediate adaptive field is constant while common future gradients can reveal hidden moment differences. Frozen Transformer--LoRA--AdamW studies with Qwen2.5-7B and Mistral-7B-v0.3 support a local action backbone, longer-horizon first-return non-closure, and fresh visible-relative completion with output-range reuse and a low-rank irreducible sector. Stronger claims remain bounded by preregistered negative or mixed results: re-anchored transport is unresolved above its measurement floor; the strict finite-grid Hodge--$3/2$ conjunction is unmet despite prospective contraction; Qwen accessibility is not established in the frozen raw moment chart; and Mistral revelation is future-context dependent rather than bank invariant. Within these support-, scale-, metric-, and context-resolved boundaries, present behavior is not a sufficient statistic for declared future learning.

---


### 231. [ALPS: Measuring Valid Creativity in Large Language Models with Mathematical Construction](https://arxiv.org/abs/2608.15979)

**<font color=#1a73e8>作者：</font>** Eric Xie, Wenqian Ye, Aidong Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models produce outputs presented as discoveries - new proofs, conjectures, or molecules. Whether such an output that appears creative is truly original and effective is hard to establish: open-ended outputs require subjective judgment, the output may replicate something seen in training, or the task may be too simple to need creativity. We present ALPS (Austin-Law Proof-Synthesis), a benchmark that designs a task to measure valid creativity: producing a solution that is original and can be proven correct. Each instance is a single equational law, certified to require either the construction of an infinite mathematical structure satisfying the law, or a proof that no such structure exists. Submissions are verified by automated proof checking with no human involvement, and a public generator produces new instances without limit, so LLMs are never evaluated on problems they may have seen. A portfolio of eight configurations of leading automated provers resolves 2.2% of the 4,141-law evaluation pool, and a twentyfold budget increase adds 0.6%: the obstacle is not compute, but the absence of any method that produces the tailored structure each law requires. Under a fixed protocol, the strongest reasoning model we test succeeds in 14% of instances on the proof side, but none on the construction side. The remaining 97.2% of the pool is unresolved at every configuration and budget we test. We release ALPS in full: the corpus, the generator, and the automated judge.

---


### 232. [Whose Gold? Annotator-Pool Disagreement Is Large at the Item Level, and Hidden by Small Leaderboards](https://arxiv.org/abs/2608.15980)

**<font color=#1a73e8>作者：</font>** Anik Jha  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Preference benchmarks are built by hiring annotators, and the identity of those annotators is treated as an implementation detail. We measure what that detail buys. On the 2,885 MultiPref items where both pools are internally unanimous, so no tie-breaking convention is consulted at all, expert and crowd annotators assign a different majority label to 23.6% and name the opposite winner on 9.2%; on the 246 comparably unanimous MT-Bench cells, benchmark authors and recruited experts differ on 30.5% and reverse on 8.5%. Yet on both corpora the resulting model leaderboards are bit-identical: Kendall tau = 1.00 with zero of six models displaced.
That invariance is far weaker evidence than it looks, and we quantify how weak. Switching pools moves a model's win rate by 1.9pp (SD), one adjacent pair in our own leaderboard sits 0.8pp apart and had a 38% chance of swapping, and an item-level bootstrap displaces at least one model in 28% of resamples. The observed zero is the common outcome, not a property of aggregation: on the same measured perturbation, a ten-model leaderboard is displaced with probability 0.86 and a twenty-model leaderboard with probability 0.9997. Reporting a six-model leaderboard is safe; the safety does not generalise, and everything that consumes labels per item is not safe at any size. We make the distinction precise, show that a widely used dataset's stated assumption of no intra-group annotator variability is false, and show that an LLM judge tracks the crowd pool over the expert pool on all three models we test, including one from a different vendor. All code, per-call outputs, and pre-registered decision rules will be released upon acceptance.

---


### 233. [A Plug-and-Play 2D Motion Interface for Real-World Motion Language Models](https://arxiv.org/abs/2608.15984)

**<font color=#1a73e8>作者：</font>** Kaname Yokoyama, Norimichi Ukita  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Motion Language Models (MoLMs) typically understand human motions by tokenizing 3D motion and processing the resulting tokens using a language model. However, obtaining accurate 3D motions from monocular videos is challenging, limiting their real-world applicability. To address this issue, we introduce a plug-and-play 2D Motion Interface that enables 3D-pretrained MoLMs to accept 2D motion inputs without modifying or fine-tuning the original models.
Experiments on public datasets show that our method achieves performance comparable to 3D motion inputs across multiple MoLMs and outperforms training MoLMs from scratch on 2D motions. We further construct a monocular real-world video motion evaluation dataset and introduce a real-video adapter, demonstrating the usefulness of 2D motions over 3D motions under the evaluated monocular pose-estimation setting. These results suggest that 2D motion provides a practical interface for deploying MoLMs in real-world motion understanding settings. Code is available at this https URL.

---


### 234. [From Sequence to Structure: Relational Uncertainty Propagation for LLM Agents](https://arxiv.org/abs/2608.16002)

**<font color=#1a73e8>作者：</font>** Zhengzhao Ma. Boxi Cao, Yaojie Lu, Hongyu Lin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reliable uncertainty quantification (UQ) is essential for deploying large language model (LLM) agents in complex interactive environments. Existing UQ methods largely rely on local signals, such as token probabilities, predictive entropy, or per-step confidence, and therefore overlook the long-range dependencies through which errors accumulate across an execution trajectory. As a result, they may fail to identify agent failures whose causes originate several reasoning or interaction steps before the final answer. We propose RUPA (Relational Uncertainty Propagation for Agents), a trajectory-level UQ framework for LLM agents. RUPA represents an execution history as a directed trajectory graph in which reasoning states, tool interactions, and environment feedback are nodes connected by temporal and semantic dependency edges. It then propagates uncertainty over this graph to capture how execution risk accumulates and transfers across interaction steps. The propagated signal is combined with trajectory-level behavioral features and goal-alignment information to produce a confidence estimate for the full agent trajectory. We evaluate RUPA on representative agent benchmarks, including $\tau$-2, Terminal-Bench-2, and GAIA, using 6 open-source LLMs spanning multiple model families. Experimental results show that RUPA consistently outperforms existing UQ methods by providing more accurate uncertainty estimates, enabling earlier failure detection, and improving uncertainty-guided agent execution across diverse agent tasks. These results demonstrate that explicitly modeling relational dependency is crucial to reliable UQ for long-horizon LLM agents, providing a practical foundation for trustworthy agent execution.

---


### 235. [Prior Audit-Repair Context Shifts LLM Verifier Thresholds Toward Leniency](https://arxiv.org/abs/2608.16003)

**<font color=#1a73e8>作者：</font>** Parsa Mazaheri, Kasra Mazaheri  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated checking pipelines increasingly place one language model as the checker and another (or the same one) as the fixer. We ask whether that wiring changes what the checker reports. Measuring false alarms on human-verified-correct ProcessBench traces with the present task held byte-identical, we find that a completed audit -> repair episode already in the model's context lowers false alarms in 15 of 15 model x wording combinations, by 2.8 to 11.5 percentage points against a length-matched non-audit control, a 9 to 25% reduction relative to that control. The direction contradicts what the accumulated-message literature predicts: an episode whose audit reported an error lowers false alarms further still, at all five wordings on the model where that manipulation lands cleanly, though a negativity asymmetry predicts more flagging. Decomposing the episode finds repair content and audit verdict complementary: different components carry the effect on different model families. Signal-detection analysis locates the change in the threshold rather than in discrimination -- the criterion moves in 15 of 15 combinations and survives correction in 13 while d' survives in none, though the d' test is half as sensitive by construction -- and a hand audit of 50 false alarms finds 82% simply wrong, so at this operating point the shift need not be harmful. With reasoning enabled the effect keeps its relative size on both models tested, and the threshold reading holds there too.

---


### 236. [ReRef-3D: A Benchmark for Spatial Referring Expression-Guided 3D Scene Rearrangement](https://arxiv.org/abs/2608.16011)

**<font color=#1a73e8>作者：</font>** Mary Lynn Martin, Yifei Zhang, Martha Palmer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce ReRef-3D, a benchmark for language-guided placement in 3D scenes. It contains 33,826 instructions across 998 CLEVR-derived scenes, spanning 16 placement families and direct, one-hop, and two-hop references. Each instruction must be resolved into a valid new placement position. Given that an instruction defines a region of acceptable placements rather than one coordinate, our evaluation inserts a prediction into the scene, recomputes relations, and tests relation satisfaction and physical validity. Each instruction also includes a verified naturalized rewrite. After fine-tuning, LLaVA-3D, 3D-LLM, and PlaceIt3D produce valid placements for 68.3%, 31.6%, and 22.4% of instructions, respectively. Across models, relation satisfaction surpasses physical validity, relations such as nearest and between are the most difficult, and phrasing has minimal effect on performance.

---


### 237. [SkillWatermark: An Embedded Skill Watermark of Progressive Privacy Inference via Benign Prompts](https://arxiv.org/abs/2608.16026)

**<font color=#1a73e8>作者：</font>** Yu Li, Liqi Zhuang, Dong Wei 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Skills for large language model (LLM) agents have been widely deployed across diverse application domains. However, we observe that these skills generate specific traffic patterns during execution. In this paper, we design a pipeline that generates specific traffic patterns by inserting carefully designed skill descriptions, which we term skill watermarks, so that a passive network attacker can establish a covert channel to encode private information within observable traffic across multiple conversation turns. Specifically, we insert prompt constraint terms, referred to as watermarks, into the original skill descriptions and embed them within multi-turn conversations. The key information in the user's original prompt is thereby triggered by these watermarks, producing clearly observable encodings in the traffic. The adversary need only decode the traffic patterns to recover the encoded information. In particular, our modifications are benign in the sense that they do not directly exfiltrate any private data and do not execute any malicious instructions. Extensive experiments demonstrate that our watermarks produce highly consistent and distinguishable traffic patterns, and that the transformed skills pass existing LLM-based security auditing tools. This study highlights that generating specific traffic patterns can be exploited as a novel attack surface and offers critical insights for future security hardening.

---


### 238. [Proof-of-Execution Memory: Defending LLM Agents Against Forged-Reasoning Attacks by Verifying What Actually Happened](https://arxiv.org/abs/2608.16032)

**<font color=#1a73e8>作者：</font>** Md Habibur Rahman, Jaeho Kim  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM agents are stateless and rely on external memory to carry context between steps. Because agents treat that memory as trustworthy, an adversary who can write to it can steer their behavior. The FARMA attack does this with no malicious command: it inserts fabricated entries into the agent's reasoning memory claiming a required safety step is already done, so the agent skips it. SENTINEL, the defense proposed with FARMA, scores entries against a fixed list of suspicious wordings; its authors note that an attacker who knows the list can reword the forgery and evade it, and leave this open. We show the gap is worse than stated. An automated attacker that simply asks a language model to reword the forgery evades SENTINEL on its first try, reducing its protection to zero on every model tested. We also find a capability paradox: the attack succeeds far more often on stronger models (98-100% on GPT-4o and GPT-4o-mini) than on Llama-3.1-8B (44%), because more capable agents follow reworded claims more faithfully, so the threat grows with capability. We propose Proof-of-Execution Memory (PoEM), which does not inspect memory at all. PoEM keeps a separate, tamper-evident, HMAC-chained ledger of the safety steps that actually executed, writable only by the trusted action layer, and allows a skip only if the ledger confirms real execution. An attacker can change what memory says but cannot forge a ledger entry for a step that never ran, so rewording no longer helps. Across three models and three scenarios, PoEM drives attack success to 0% while leaving legitimate operation intact (0% false positives in eight of nine cells, 1.7% in the ninth, within sampling noise), whereas SENTINEL wrongly blocks 33-50% of legitimate operations. PoEM also withstands attacks aimed at itself, adds microseconds of overhead, and works unchanged in a real LangChain agent. PoEM protects exactly the decisions it gates.

---


### 239. [$R^3$-Bench: LLMs Struggle with Resource-Rational Reasoning under Shared Budgets](https://arxiv.org/abs/2608.16033)

**<font color=#1a73e8>作者：</font>** Peisong Wang, Zhiwei Ma, Bowen Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In cognitive science, resource rationality asks how an agent should allocate limited computation to maximize expected value. Most reasoning and agent benchmarks use independent per-task budgets; existing shared-budget studies do not calibrate suite performance against the same model's demonstrated single-problem competence. We introduce $R^3$-Bench, which evaluates six-problem suites under shared budgets across mathematics, competitive programming, and abstract reasoning in tool-free and agentic settings. Matched single-problem response curves define an offline empirical oracle over observed successes. Across 72 main-table cells for six models, the oracle mean matches or exceeds the contest mean in all cells and is strictly higher in 71. Under moderate tool-free pressure, equal-allocation replay also exceeds contest performance for four of six models. Trajectory diagnostics reveal limited strategy updating and pressure-dependent failure patterns. In a three-model diagnostic under strong agentic pressure, at least one fixed scheduler exceeds the contest mean in six of nine cells, but no policy dominates across domains. These results expose a persistent gap between demonstrated competence and shared-budget realization.

---


### 240. [DuplexGen: Decoupling Content, Timing, and Acoustics for Synthetic Dialogue Speech](https://arxiv.org/abs/2608.16053)

**<font color=#1a73e8>作者：</font>** Pengcheng Wang, Sheng Li, Jiyi Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Synthetic conversational speech has become an important resource for developing and evaluating conversational speech systems. However, existing dialogue synthesis pipelines typically generate dialogue content first and then insert interruptions, overlap, and backchannels using handcrafted markers or timing rules, making conversational timing prescribed rather than interaction-driven. We present DuplexGen, a dialogue synthesis framework that explicitly decouples content, timing, and acoustics. An LLM first generates the dialogue script, and then two full-duplex conversational models perform the script while listening to each other in real time. This allows conversational timing to emerge naturally while preserving the scripted content. Finally, a high-fidelity text-to-speech model re-renders the interaction without altering its timing. As a demonstration of the proposed framework, we construct a patient--clinician conversational speech corpus with construction-time annotations, including word timestamps, speaker activity, overlap regions, and interaction events. Experimental results show that the proposed framework produces conversational dynamics closer to real dialogue than conventional stitching-based synthesis.

---


### 241. [Governance at the Boundary: How Agent Decomposition Degrades Policy Compliance](https://arxiv.org/abs/2608.16055)

**<font color=#1a73e8>作者：</font>** Bowen Li, Guojun Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing agent benchmarks ask whether the agent finished the task. We ask whether it finished it within policy. We introduce Fiducia-bench, a benchmark for the governability of financial agents---whether they escalate when obligated, abstain when required, and leave an auditable trail---and use it to study a question no prior benchmark addresses: does decomposing an agent into components degrade its governance? It does, and the mechanism is specific. Policy-relevant facts discovered by one component are attenuated at the handoff boundary before reaching the component that must act on them. In a 626-episode experiment across 100 KYC/AML task variants, two models, and three architectures, a 32B open-weights model attenuated 0% of discovered facts under a single-loop baseline, 56% under a fixed pipeline, and 85% under an orchestrator-subagent architecture (all at constraint distance 2). A stronger model (gpt-4.1-mini) attenuated 3-6% under the same conditions, suggesting the governance cost of decomposition is partly a function of model capability. Critically, the same mechanism produces both under-escalation and over-escalation, depending on whether the dropped fact was a risk signal or an exculpating one. The benchmark, all tasks, and the verification harness are open-source

---


### 242. [SiMUSation: An Interactive Visitor Experience Simulation Framework to Support Museum Exhibition Design](https://arxiv.org/abs/2608.16067)

**<font color=#1a73e8>作者：</font>** Huanchen Wang, Qiuming Chen, Zhonghao Ji 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Understanding how diverse audiences engage with narratives and content is central to exhibition design, yet designers often rely on intuition. Existing experience evaluation methods are typically retrospective, costly, and offer limited access to visitors' internal states, hindering early-stage iterative refinement. Rather than relying only on post-implementation evaluation with real visitors, we explore LLM-driven persona simulation as a reference for early-stage design. Following this idea, we present SiMUSation, an interactive framework designed to support early-stage exhibition design. SiMUSation models diverse visitor personas and simulates their exhibition experiences through a dual-layer representation that couples observable behaviors, such as movement and gaze, with corresponding internal responses, such as confusion and narrative engagement. Designers can steer simulations, inspect feedback from simulated visits, and iteratively revise layouts, content, and narrative flow to further examine how changes reshape visitor experience. We implemented a prototype and evaluated it through a user study (N=12), showing that SiMUSation provides insights for reflection and refinement in early-stage exhibition design. Our findings further highlight the potential of persona-driven simulation to support audience-informed evaluation and iterative decision-making across design tasks.

---


### 243. [CAPO: Constraint-Aware Prompt Optimization for LLM Agents](https://arxiv.org/abs/2608.16068)

**<font color=#1a73e8>作者：</font>** Victor Ye Dong, Reid Pryzant, Yi Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed as agents that rely on system prompts to use tools and complete tasks. Such deployments impose distinct operational requirements, including appropriate tool use, concise prompts and solution paths, and compliance with safety and formatting policies. For many practitioners, however, assembling domain-specific supervised data to post-train models to meet these requirements is infeasible. We introduce CAPO (Constraint-Aware Prompt Optimization), a primal-dual method that combines pool-based rewrites with adaptive constraint weighting to optimize system prompts under explicit operational constraints. Across agentic benchmarks, CAPO more reliably reaches empirically feasible operating points while improving task performance. CAPO also generalizes beyond agentic settings, achieving strong results on assistant-style evaluations with output-format and safety/privacy constraints. We further introduce DCAPO (Dynamically Trained CAPO), which trains a feedback- and dual-conditioned rewriter with pool-based GRPO while keeping the task agent frozen. Across task agents of different sizes, DCAPO produces a feasible prompt in every evaluated domain and matches or improves the task accuracy achieved by the evaluated baselines. A surrogate analysis characterizes how finite-pool and discrete-rewrite errors enter the inexact primal-dual procedure.

---


### 244. [Skill2Query: Exploiting Skill Structure to Generate Pseudo-Queries for Agent Skill Retrieval](https://arxiv.org/abs/2608.16071)

**<font color=#1a73e8>作者：</font>** Lihui Ding, Zihan Guo, Bingwei Lu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Pseudo-query generation can alleviate the supervision bottleneck for agent skill retrieval, but existing document-level approaches typically leave the rich internal relations among capabilities, parameters, and usage examples implicit. As a result, generated queries may be topically relevant to a skill while lacking capability grounding and parameter consistency, raising the question of whether explicitly exploiting a skill document's internal structure can produce more effective retrieval signals. We therefore propose Skill2Query, a framework that first parses a skill document into a Skill Knowledge Graph and then generates pseudo-queries through a three-stage process including style mimicking, query template generation, and parameter filling. The generated queries can be used for offline index augmentation, online query expansion, and retriever training. Four benchmarks (TheoremQA, LogicBench, ToolQA, and CHAMP) are used to evaluate Skill2Query with large-scale skill candidate pools across multiple downstream applications, including skill retrieval, retriever training, and end-to-end agent execution. Using nearly 30K skills across diverse domains, we generate 700K category-diverse pseudo-queries. Skill2Query consistently improves sparse, dense, and skill-routing retrieval, with an average Recall@1 gain of 6.70 percentage points across retrieval settings. Skill2Query-generated training data also achieves the best Recall@1 and nDCG@1 among the evaluated generation baselines. Further evaluations with multiple LLM backends demonstrate that improved skill retrieval translates into higher agent task success rates. Code and resources are available at this https URL.

---


### 245. [Learn What's Left, Not What's Mastered: Saturation Aware Advantage Reweighting for Multi-Reward Policy Optimization](https://arxiv.org/abs/2608.16072)

**<font color=#1a73e8>作者：</font>** Yixuan Wang, Yifei Chen, Haichao Zhang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) with group-relative advantages has become the de facto standard for post-training language model reasoners. However, when optimizing multiple reward objectives, existing methods typically scalarize the reward vector with a fixed weighted sum before group-wise standardization. We show that this design leads to two fundamental problems: rollouts with distinct reward profiles can receive identical advantages, and all objectives are optimized with fixed relative weights regardless of their current level of saturation. As a result, training continues to allocate gradient budget to already-solved objectives instead of focusing on those with greater remaining headroom. We introduce \textbf{Saturation Aware Advantage Reweighting for Multi-Reward Policy Optimization} (SA-MRPO), which standardizes each reward objective independently and adaptively discounts its contribution according to a batch-level estimate of objective saturation. This dynamically reallocates optimization effort toward under-optimized objectives while empirically maintaining performance on those that are already well satisfied. We further show that saturation-aware reweighting can reverse the sign of an update, rather than merely rescale its magnitude. Across mathematical reasoning with two- and three-objective reward combinations, SA-MRPO improves the harder correctness objective over GDPO in 12 of 15 benchmark comparisons, with gains of up to $5\%$ on AIME24. On adaptive reasoning it improves accuracy on all five benchmarks, by $3.8\%$ on average and up to $9.2 \%$ on AMC23, and on coding benchmarks it improves pass rate by up to $2.3\%$, while in all settings maintaining the easier objectives near their already satisfied levels.

---


### 246. [SafeGesture: Evaluating Fine-Grained Hand Gesture Understanding in Vision-Language Models through Scenario-Conditioned Safety Interpretation](https://arxiv.org/abs/2608.16081)

**<font color=#1a73e8>作者：</font>** Taegang Kim, Saleh Afroogh, Junfeng Jiao  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-weight and frontier vision-language models (VLMs) perform well on general image understanding, but their ability to interpret fine-grained hand gestures in safety-critical operational contexts remains largely unexamined. We introduce SafeGesture, a benchmark that evaluates whether a model can infer scenario-appropriate safety actions from hand gestures. It pairs six HaGRID gestures with eight operational scenarios for 4,800 items and evaluates Qwen2.5-VL-7B, LLaVA-NeXT-7B, InternVL2-8B, Phi-3.5-Vision, and GPT-4o. Results reveal a perception-reasoning decoupling: GPT-4o achieves 98.4% gesture accuracy but 53.3% safety accuracy, while Qwen2.5-VL reaches 84.9% and 39.5%, yielding gaps of 45.0 and 45.4 percentage points. Four of five models rarely or never use the uncertainty label, and failure directions differ substantially across models. Accuracy also obscures label bias: a scenario-majority policy with no visual input reaches 58.3%, above every evaluated model, while only GPT-4o exceeds this prior under macro-F1. Visual input improves safety accuracy by 11.2 to 30.2 percentage points, but providing the ground-truth gesture as text improves performance by only 0.4 to 3.2 points, and no model exceeds 56.2%. These results indicate that the main bottleneck is scenario-conditioned safety reasoning rather than gesture recognition.

---


### 247. [Nexus: Structured Synergy for Efficient Text-to-Image Generation using Rectified Flow Model](https://arxiv.org/abs/2608.16104)

**<font color=#1a73e8>作者：</font>** Yizhao Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion and flow matching models have made significant progress in text-to-image generation, yet high computation, quadratic complexity, and large memory footprint hinder high-resolution synthesis and edge deployment. We propose Nexus, which integrates sparse architecture, linear complexity, and low-bit quantization. It combines MoE feed-forward layers, gated DeltaNet attention, and per-expert low-bit training to reduce computation and memory. Their joint optimization allows Nexus to achieve generation quality comparable to mainstream models such as SDXL and SD3 while delivering markedly higher inference efficiency. Experiments on COCO and LAION validate its effectiveness.

---


### 248. [HyperSkill: Self-Evolving LLM Agents via Hypergraph-Structured Skill Memory](https://arxiv.org/abs/2608.16114)

**<font color=#1a73e8>作者：</font>** Ruiyao Xu, Tiankai Yang, Wei-Chieh Huang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As agentic tasks grow in complexity, LLM agents increasingly rely on experiential memory to reuse procedural knowledge across tasks. Effective memory design must jointly address what to store, how memory is structured and retrieved, and how memory evolves. Existing systems tackle each only partially: they store trajectories, insights, or workflows as isolated entries, discarding compositional relationships among subtasks and reusable skills; retrieve by flat embedding similarity that ignores relational signals; and maintain memory without leveraging its relational structure. We propose HyperSkill, a hypergraph-based memory framework that jointly improves all three. HyperSkill represents memory as a hypergraph with two node types, subtask steps and reusable skills, where each hyperedge links the subtasks and skills from a single trajectory. Dual-path retrieval queries both subtask and trajectory levels, ranking skills by co-occurrence across retrieved trajectories. Periodic structure-informed maintenance prunes low-utility nodes and merges redundant skills via quality-weighted propagation. Across xBench, GAIA, and WebWalkerQA with GPT-4o and Qwen3-30B-A3B, HyperSkill outperforms ten memory baselines, yielding gains of up to +11.51 on GAIA and +11.18 on WebWalkerQA.

---


### 249. [Assessing LLMs' mathematical abilities requires understanding the various mechanisms of mathematical creativity](https://arxiv.org/abs/2608.16118)

**<font color=#1a73e8>作者：</font>** Silvère Gangloff  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> How should we assess whether large language models can perform mathematical invention? I argue that this question is currently underspecified: mathematical creativity is not one capacity but several mechanistically distinct modes of meaning-making - reflexive introspection on mathematical practice, analogical import from the sciences, problem-driven construction, and the bridging of distant domains - together with a further, cross-cutting distinction between meaning pursued because a pattern was observed and meaning pursued because it is strategically wanted, a distinction I develop through the case of conjecture-formation. These mechanisms are likely non-substitutable, so that competence in one does not transfer to the others. Grounding each in a historical case study and in an architecture-level account of current transformer-based systems, I suggest that today's models concentrate their competence in modes shaped by recombination and search over existing building blocks; if that description holds, the remaining modes are out of reach in principle, not just slower - though whether it holds is itself the open, empirical part. Because proof is getting cheaper as AI improves at generating it - a shift the field's own leading voices are now diagnosing - mathematical value is migrating toward the modes current systems cannot yet perform, and evaluations of AI mathematical ability should be organized around this taxonomy rather than around aggregate benchmarks that conflate it.

---


### 250. [TRCA: Transition-wise Rubric Credit Assignment for Long-horizon LLM Agents](https://arxiv.org/abs/2608.16156)

**<font color=#1a73e8>作者：</font>** Huan Zhang, Mingju Chen, Dongxu Zhou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon large language model (LLM) agents are typically optimized with sparse terminal outcomes, making fine-grained credit assignment across multi-step interactions difficult. Existing approaches either rely on process evaluators, which incur annotation and inference costs, or derive step-level credit from successful trajectories. However, successful trajectories are extremely scarce during early-stage reinforcement learning, substantially weakening anchor-based methods. We propose Transition-wise Rubric Credit Assignment (TRCA), which derives step-level supervision directly from action-induced transitions without learned evaluators or successful anchors. TRCA evaluates each transition using Evidence, Execution, and Invalidity rubrics to capture task-relevant information acquisition, valid task execution, and invalid or regressive behavior. From these judgments, Foundational Rubric Reward measures local transition quality, while Breakthrough Rubric Reward tracks newly covered Evidence and Execution conditions to reward incremental task progress. Combined with terminal outcomes, these signals produce fine-grained step-level advantages for policy optimization. Experiments on ALFWorld, WebShop, and seven search-augmented question-answering benchmarks show consistent improvements over the evaluated baselines. With Qwen2.5-7B-Instruct, TRCA improves the WebShop score by 6.0%-12.6%; with Qwen2.5-3B-Instruct, it improves the average SearchQA score by 1.9%-18.3%. These results demonstrate the effectiveness of transition-wise rubric credit assignment for long-horizon tasks with sparse successful anchors.

---


> [!TIP]
> 当前位于：**201-250**（第 5/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-358](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
