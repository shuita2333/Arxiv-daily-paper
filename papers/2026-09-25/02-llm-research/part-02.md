# 🧠 大模型相关研究 | 2026年09月25日

> 本类共 **172** 篇论文：已确认 **158** 篇，待复核 **14** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-172](./part-04.md)

---

### 51. [EnSIMem: Entity-Structured Indexing for Long-Term Agent Memory](https://arxiv.org/abs/2609.27279)

**<font color=#1a73e8>作者：</font>** Xuanyu Meng, Xing Fan, Xinyi Fan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An agent that interacts with users over long periods must recall facts, preferences, events, and changes from a continuously growing interaction history. Existing memory systems often compress interactions into generic summaries or retrieve anonymous text chunks, making it difficult for an agent to identify the correct entity, property, and supporting evidence. We present EnSIMem, an entity-structured long-term memory architecture for an agent. During offline construction, the system organizes interactions into theme-coherent episodes and builds dialogue-grounded index entries of the form [entity][entity type][property:value]. Each entry preserves its source turns, temporal information, and available multimodal fields. During online interaction, the agent's request is decomposed into evidence requirements whose properties are aligned with the memory index. Entity-property lookup and adaptive retrieval then collect the evidence needed for point, temporal, compositional, and aggregation reasoning. The agent generates its response from the preserved source evidence rather than from lossy memory summaries. On long-term agent-memory benchmarks, EnSIMem achieves high answer accuracy while maintaining compact contexts and favorable online efficiency. These results show that entity-structured indexing and episode-level provenance provide a reliable foundation for long-term memory in agents. The code of our model is available at this https URL.

---


### 52. [Hunyuan-A13B Technical Report](https://arxiv.org/abs/2609.27284)

**<font color=#1a73e8>作者：</font>** Tencent Hunyuan Team, Ao Liu, Botong Zhou 等 75 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present Hunyuan-A13B, an open-source large language model based on a Mixture-of-Experts architecture. It contains 80 billion total parameters but activates only 13 billion during inference, balancing model capability, computational efficiency, and deployment cost. The model is pretrained on a rigorously filtered 20T-token corpus with enhanced STEM data curation, improving factual reliability and reasoning ability. High-quality supervised fine-tuning and large-scale reinforcement learning further enhance its overall performance. Hunyuan-A13B also introduces a dual-mode Chain-of-Thought framework that adapts reasoning depth to task complexity: fast thinking for routine queries and slow thinking for complex, multi-step problems. Evaluations show competitive performance across mathematics, science, programming, general language understanding, and agent tasks, often approaching that of much larger models. Its high inference throughput makes it suitable for latency-sensitive applications. We release Hunyuan-A13B to support open research and practical LLM deployment.

---


### 53. [Memory Control Signals Emerge Before Action in Long Horizon Agents](https://arxiv.org/abs/2609.27286)

**<font color=#1a73e8>作者：</font>** Mingxuan Wang, Guorun Yao, Fei Luo 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long horizon language model agents continuously accumulate interaction history, increasing computational cost while making relevant information harder to preserve and reuse. Existing context management methods mainly focus on how to compress or retrieve history, but largely leave open whether the model itself already represents the need for these memory operations before they occur. We study the hidden state immediately before each agent action and find that compression and recall needs are already encoded in the model's internal representations. These signals cannot be explained by simple context length or interaction progress, and they exhibit distinct formation patterns across model depth. We further show that most memory decision information is preserved in a compact recent context, while selectively restored historical evidence complements the long range dependencies that recent context misses. Based on these findings, we propose Preaction Memory with Evidence Retrieval (PaMER), which combines state guided compression with external evidence retrieval. PaMER+ further introduces step level evidence selection to recover only the historical information required by the current task. Experiments on WorkBuddyBench, across multiple context management baselines and model backbones, show that our framework substantially reduces context consumption while maintaining competitive task performance.

---


### 54. [SR-Fraud: An Outcome-Supervised Reflective LLM Agent Framework for Non-Stationary Payment Fraud Detection](https://arxiv.org/abs/2609.27287)

**<font color=#1a73e8>作者：</font>** Xuwei Tan, Yao Ma, Xueru Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real-time payment fraud detection is a non-stationary streaming prediction problem: adversaries adapt before supervised labels mature, and localized burst attacks can cause losses before retraining. Production systems typically rely on tabular classifiers and rules, which can struggle to capture these emerging sequential patterns before periodic retraining occurs. We present SR-Fraud, an outcome-supervised reflective LLM framework that decouples request-time decisions from offline adaptation. A frozen, stateless agent scores each transaction from a Hybrid Episodic Window to track behavioral shifts, while an offline reflection agent proposes boundary hypotheses from matured errors. A deterministic verifier then admits only supported hypotheses into an executable knowledge state. On a production payment-fraud benchmark, SR-Fraud improves all detection metrics over its frozen decision agent, obtains higher point estimates than static and periodically retrained CatBoost, and detects an emerging fraud burst.

---


### 55. [Ruby-ASR: Evidence-Preserving Supervision for Joint Orthographic and Lexical-Reading Recognition](https://arxiv.org/abs/2609.27289)

**<font color=#1a73e8>作者：</font>** Hao Shi, Yun Liu, Xuehao Yang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Conventional Japanese automatic speech recognition (ASR) is supervised by an orthographic transcript, although the same written form can correspond to different lexical readings realized in speech. Such utterances receive an identical target, so their reading distinction is absent from the supervision interface and cannot be recovered reliably by post-hoc text-only grapheme-to-phoneme conversion. We present Ruby-ASR, which refines the conventional target into a span-bound orthographic--lexical-reading sequence. Unlike separate full-sentence orthographic and phonological outputs, the ruby representation locally binds each written span to its realized reading and permits deterministic recovery of both views. We instantiate the target under subtitle-style and verbatim-style transcription conventions using a Qwen3-ASR backbone; a mora-level CTC objective provides auxiliary monotonic reading supervision. The experimental results across five Japanese benchmarks show that refining the recognition target can improve lexical-reading recovery without sacrificing readable orthographic transcription. We release the checkpoints and inference code.

---


### 56. [KITE: KV-Invariant Transformer Expansion for Efficient Agentic LLM Scaling](https://arxiv.org/abs/2609.27294)

**<font color=#1a73e8>作者：</font>** Zhiheng Hu, Yixun Wei, Jian Zhou 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scaling a language model is not only a question of final quality: the architectural choice determines how much computation is spent during training, prompt processing, and autoregressive decoding to achieve certain model quality. An ideal model architecture should lower all above computation costs to facilitate scaling to a larger model, while ensure the larger model indeed outperforms smaller baselines. We introduce KV-Invariant Transformer Expansion (KITE), a scaling paradigm that achieves this goal. It trains the model from a smaller size to a larger size (i.e., saving training costs via upcycling), while places newly added parameters in regions that do not affect attention KV. Consequently, during inference, prefilling KV only relies on the smaller part of the model, so the inference costs are saved. As a concrete instantiation, we present Step Scale Transformer (SST), a two-tower decoder in which one tower produces KV and the other reads them. At comparable cumulative training compute, SST, a 67B MoE model with 2.15B active body parameters per decode token, achieves lower training loss than 47B and 63B MoE Transformers with 1.48B and 2.02B active body parameters, respectively, while reducing estimated inference cost by 6.7% and 31.6%.

---


### 57. [StateComp: Learning When to Compress History in Long Horizon Agents](https://arxiv.org/abs/2609.27298)

**<font color=#1a73e8>作者：</font>** Mingxuan Wang, Hongyue Chen, Yinglong Guo 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon agents continuously accumulate interaction history during task execution, yet the importance of past interactions changes as the agent state evolves. Existing context management methods largely compress history based on fixed windows, periodic schedules, or current relevance, overlooking a more fundamental question: when has a past interaction become safe to replace? Premature compression may remove information still needed for future actions, while overly conservative retention leads to substantial context overhead. To address this, we propose State Conditioned Compression (StateComp), a framework that determines when historical interactions can be safely compressed according to the current agent state. StateComp constructs KEEP and READY supervision through a two-stage annotation procedure and trains an imbalance-aware router on hidden representations from a frozen language model. A bounded state representation further reduces the cost of evaluating long histories, while adjacent READY interactions are grouped into continuous spans and replaced with compact summaries during execution. Experiments on WorkBuddyBench show that StateComp reduces total agent and summarization tokens by 52.27% while maintaining task performance, and achieves a 12.67-fold speedup in representation extraction.

---


### 58. [Verifiable Hidden Dynamics Play: Generating Agentic RL Environments from Solved Mechanisms](https://arxiv.org/abs/2609.27321)

**<font color=#1a73e8>作者：</font>** Xinjie Shen, Wei Fan, Xudong Guo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language-model agents increasingly face long-horizon tasks with evolving state, interdependent decisions, and delayed outcomes. Scaling their training requires diverse agentic environments, dependable outcome signals, and low extension cost. Existing generation pipelines commonly construct an environment before defining its outcome rule or annotating its trajectories, leaving dynamics and evaluation to be aligned post hoc. VHD-Play reverses this dependency by sampling and solving a mathematical model before a corpus-grounded setter renders its decision process as stateful tools. The executable dynamics and trajectory-scoring reference are inherited from the same solved model. The pipeline produces 3,300 diverse agentic environments at a cost of a few cents each. Training Qwen3.6-35B-A3B on three families raises its mean agentic score from 0.204 to 0.815 in a five-family diagnostic. Gains also appear on held-out instances from all three training families and eight unseen mechanism families, then extend beyond the generated substrate to external benchmarks for general function calling, travel planning, and 365-day e-commerce. On E-Commerce Bench, the trained checkpoint completes every run without bankruptcy and exceeds Qwen3.7-Max. We compare written-out problems with stateful versions that reveal or hide their parameters. The comparison shows that most of the learnable gap lies in stateful interaction rather than underlying problem solving. A frozen 35B setter realizes larger environments, and scale-matched training retains gains as mechanism size and horizon grow, indicating the potential for an evolving training substrate.

---


### 59. [Can Vision-Language Models Analyze Human-Centered Video? Mapping Model Capabilities and Human-AI Collaborative Workflows](https://arxiv.org/abs/2609.27327)

**<font color=#1a73e8>作者：</font>** Xiyuan Shen, Jiuyang Lyu, Seokhyun Hwang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video provides a rich record of human behavior, interaction, and situated contexts, offering important evidence for understanding people and conducting human-centered research. As vision-language models (VLMs) become increasingly capable of analyzing video, they offer opportunities to automate this traditionally human-intensive process. Yet a central question remains: when can VLMs analyze human-centered video independently, and when does reliable analysis still require human involvement? To address this question, we first characterize video analysis practices in human-centered research. We systematically analyze all 1,702 CHI 2026 full papers and identify 125 that annotate videos. Through iterative coding, we derive a five-dimensional taxonomy spanning analytic purpose, viewpoint, phenomenon, reasoning requirement, and annotation authority. Grounded in recurring annotation tasks captured by this taxonomy, we construct a benchmark of 15 representative tasks from open datasets to map the capabilities and limitations of a general-purpose VLM. We examine the division of labor between humans and VLMs by comparing three annotation workflows: VLM alone, human alone, and human verification of VLM outputs. Across tasks, VLM-alone annotation approaches human accuracy on average (HNS = 97.0, where 100 denotes human-alone performance), demonstrating substantial potential to automate human-centered video analysis. Human verification achieves the highest accuracy (HNS = 121.5) while reducing human annotation time by 48.9% and monetary cost by 31.3%-44.5% relative to human-alone annotation. Our findings connect real-world human-centered video analysis tasks and current VLM capabilities, and clarify how human-AI collaboration can make VLM-assisted analysis reliable and efficient.

---


### 60. [Alignment Inertia: Auditing the Durability of Training Data Influence Through Policy Override Resistance](https://arxiv.org/abs/2609.27333)

**<font color=#1a73e8>作者：</font>** Renata Barreto, Markelle Roesti, Mohammad Tahaei  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Platform operators increasingly rely on system prompts and fine-tuning to govern model behavior, yet it remains unclear how reliably these interventions override behavior inherited from prior training. We propose Override Success Rate (OSR) and alignment inertia to measure when operator interventions succeed or fail to change prior behavior. We evaluate zero-shot prompting and LoRA fine-tuning across Llama and Mistral in medical misinformation and hate speech. Alignment inertia persists across both models but varies by model, domain, and policy direction. Notably, in Mistral's restrictive hate-speech condition, LoRA increased inertia by 46.5 percentage points, showing that fine-tuning can reinforce rather than override prior behavior. We also use TRAK to test whether inertia is associated with weaker adaptation signals. TRAK achieves AUC of at least 0.85 in 7 of 8 conditions and outperforms model confidence, TF-IDF similarity, and embedding similarity as a predictor of inertia. These results provide an operator-facing audit of where prior training constrains downstream model governance.

---


### 61. [Just-in-Time Memory: Learning to Curate Task-Adaptive Memory for LLM Agents](https://arxiv.org/abs/2609.27334)

**<font color=#1a73e8>作者：</font>** Yefan Zhou, Yang Li, Zeyu Leo Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic memory systems reuse past experience to improve future performance, yet most existing designs curate memory at write time: once a task is completed, its trajectory is distilled into a fixed artifact, such as a reflection, workflow, skill, or reasoning strategy, that is later retrieved by similarity. This forces the system to decide what is worth remembering before the future query is known, irreversibly discarding information and producing a query-independent summary that must serve many possible downstream tasks. Learning such a write-time curator is also difficult because the value of a storage decision may only become apparent when a relevant query arrives, potentially many tasks later, creating a long-horizon credit-assignment problem. We instead retain raw trajectories and defer curation until read time, when the current task is known. Given the retrieved traces and the new task, a memory curator synthesizes a compact, task-adaptive payload tailored to the immediate need. Because this payload is consumed on the same task, the curator can be trained directly from immediate task success, avoiding delayed utility signals and the need to artificially group related tasks. Across ALFWorld, WebShop, and $\tau^2$-bench, our Just-in-Time Memory (JitMem) consistently outperforms no-memory agents as well as heuristic and learned write-time memory methods, improving over the strongest baseline by 16.2, 16.3, and 3.9 absolute success-rate points, respectively. Notably, even an untrained curator is already competitive with or surpasses these baselines, showing that task-adaptive read-time curation itself is a major source of the gain; training the curator further compounds the improvement.

---


### 62. [MolDesignBench: Evaluating LLM-based Agent for Scenario-grounded Molecular Design](https://arxiv.org/abs/2609.27349)

**<font color=#1a73e8>作者：</font>** Yongjun Jeong, Hanbum Ko, Ye Rin Kim 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Real-world molecular design remains challenging for large language model (LLM)-based agents. It requires them to interpret design contexts, satisfy multiple constraints, identify infeasible specifications, and reason over multi-step tool outputs. Existing benchmarks do not capture this complexity, focusing instead on explicit and narrow constraints, only feasible problems, and single-path solutions. To address this gap, we propose MolDesignBench, a scenario-grounded benchmark that more closely reflects real-world molecular design for evaluating tool-augmented LLM agents. MolDesignBench comprises 2K generation and optimization instances that combine implicit requirements embedded in design narratives with explicit property and functional-group constraints, including infeasible cases, and require the effective use of 17 specialized chemistry tools. Experiments across diverse frontier LLMs reveal low success rates--with the best achieving only $\sim43$\%--and frequent failures in implicit-constraint reasoning, infeasibility detection, and tool reasoning. The corresponding fine-grained failure-mode analysis identifies implicit constraint interpretation and infeasibility detection as the primary bottlenecks, establishing MolDesignBench as a rigorous testbed to guide future research on chemical agents. The benchmark, tool interface, and evaluation code are publicly available.

---


### 63. [Guides That Cause Actions: An Offline Study of Guide-Action Mutual Reinforcement in Multimodal Web Agents](https://arxiv.org/abs/2609.27353)

**<font color=#1a73e8>作者：</font>** Chengguang Gan, Yunhao Liang, QingHao Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Web agents are usually evaluated in live environments, where environment state and judge models drift between runs, so the same checkpoint rarely reproduces the same score, making controlled studies of training phenomena impractical. We present WebMRE, an offline benchmark of 541 tasks and 5,293 steps derived from successful WebArena trajectories, with fully audited test labels and a deterministic protocol that scores a checkpoint identically on every run without any environment. Each step pairs a human oriented guide sentence with a grounded action, enabling the first study of the mutual reinforcement effect between them in web agents. Averaged over three seeds the effect holds for both models in both decoding orders and grows with scale: jointly decoding a guide lifts element selection over an action only reference by 0.9 and 0.2 points for Qwen3.5-4B and by 1.7 and 2.2 points for Qwen3.5-9B. A mediation analysis shows that the guide is a causal channel rather than commentary: forcing the gold guide as a decoding prefix lifts action accuracy from .422 to .684, another step's guide collapses it to .055, and a paraphrase that renames the target still recovers half of the gain, so the channel carries instruction meaning and not only the label string. The same channel yields an offline reward that only a replayable protocol makes computable, though optimizing it from a strong checkpoint brings no gain yet. Our fine tuned models outperform GPT-5.5, Claude Opus 4.8, and Gemini 3.5 Flash, run zero shot, on every offline metric.

---


### 64. [Quantization-Robust Unlearning through the Lens of Retain-Forget Loss Landscapes Interaction](https://arxiv.org/abs/2609.27355)

**<font color=#1a73e8>作者：</font>** Jialu Wang, Jianing Deng, Shuqing Luo 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Unlearning ensures LLM compliance by removing the influence of private or copyrighted training data. However, since LLM models typically undergo post-training compression, like quantization, in practical deployment, it has been observed that the unlearning effect can be substantially weakened, with the forgetting behavior degrading more severely than that of model utility. This paper proposes a quantization-robust unlearning framework that makes forgetting robust to quantization while maintaining overall model utility. We analyze this gap through the lens of loss landscape. Specifically, our analysis reveals a curvature-based criteria that pinpoints sensitive weights in the unlearned model that leads to both non-robust forgetting and reduced utility. We therefore propose sensitivity-guided noisy regularization, which is applied on the sensitive parameters to steer the model convergence towards a smoother minima of uniformly low forget and retain losses. Balancing unlearning and utility, we further propose forget-critical optimization, which updates only forget-critical layers, preserving most of the network to retain useful knowledge. Extensive experiments on the MUSE and TOFU benchmarks across multiple LLM unlearning algorithms show that our approach achieves substantially more quantization-resilient forgetting while maintaining utility.

---


### 65. [Automated Extraction of Records of Processing Activities (RoPA) Using Hybrid RAG and Locally Deployed Large Language Models](https://arxiv.org/abs/2609.27359)

**<font color=#1a73e8>作者：</font>** To Duy Hinh, Nguyen Le Quoc Anh, Phan Van Tri 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Vietnam's Personal Data Protection Law (Law No. 91/2025/QH15) and Decree No. 356/2025/ND-CP, effective January 1, 2026, require organizations to establish and maintain Records of Processing Activities (RoPA). Manual RoPA preparation is labor-intensive, while cloud-hosted large language models (LLMs) may conflict with data-sovereignty requirements. We propose RoPA Manager, a system for automated RoPA information extraction using hybrid retrieval that combines lexical ranking over tsvector, dense-vector search, Reciprocal Rank Fusion (RRF), and locally deployed LLMs. We introduce a Vietnamese RoPA benchmark with 32 organizations, 77 processing activities, 12 field groups, and 4,338 reference values. Evaluation is reported at three distinct levels. The automated scorer, tested on perturbed data without invoking an LLM, achieved F1 = 0.9493 [0.9436, 0.9548]; this measures scorer robustness rather than end-to-end extraction accuracy. End-to-end extraction achieved token coverage of 50.04-55.25% against the reference labels. Two independent experts reviewed 1,558 reference values (35.9% of the benchmark), found no incorrect values, and achieved 99.68% agreement with PABAK = 0.9936. Value-level precision was not measured. Across 32 paired scenarios on a 24 GB GPU, locally deployed Qwen3.5-27B-GPTQ-Int4 showed no statistically significant difference from cloud-based DeepSeek-V4-Flash (difference 0.20 percentage points in favor of DeepSeek, 95% CI [-0.93, 1.32], p = 0.72), while Gemma-4-31B performed significantly worse (p < 0.01).

---


### 66. [Seal, Then Sample: Sampled Layerwise Proofs for Verifiable LLM Inference from GPT-2 to 70B](https://arxiv.org/abs/2609.27367)

**<font color=#1a73e8>作者：</font>** Youki Lim, Sam Yong  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Verifying outsourced language-model inference requires a precisely identified computation and an audit whose cost a service can afford. We present Sampled Layerwise Proofs (SLP), a protocol and prototype that commits the boundary activations of every chunk of an inference trace, absorbs all commitments before any challenge is drawn, and then proves a verifier-selected subset of chunks together with the chunks that bind the prompt and the answer. Audit coverage becomes a runtime parameter over one set of commitments: on a TinyLlama-1.1B trace, proving seven of 47 chunks takes 22.0% of the time and 6.8% of the proof size of proving all 47. Because proof cost is dominated by weights rather than tokens, SLP packs concurrent requests into one trace under a block-diagonal causal mask and binds the prompt and answer of each request to its slot. Twelve packed requests are proved in 181.9 s, 6.5 times less than twelve separate proofs at the measured single-proof cost, and a simulated service proves twelve requests at 30.6 s per request with 0.6 s of verification each, rejecting a tampered answer. Disk-backed integer weights and streamed polynomial commitments let a single Llama-2-70B run complete on a 2 TB CPU host: 163 chunks sealed, five proved, a 4.34 MiB proof in 1,259 s, verified in 46.3 s without the weights. The proven object is a fixed-point canonical model; we trace a severe fidelity loss to the residual-stream bit width, repair it with an LLM-aware observer, and measure 84.8-84.9% argmax agreement with the floating-point reference over 334,705 WikiText-2 test positions. The limits are stated as precisely: guarantees cover proven chunks only, a fixed invalid chunk in the 70B setting is covered with probability 3/161, a manifest-only Fiat-Shamir schedule can be ground at 12.5 ms per attempt and needs an externally ordered challenge, and all measurements use a test reference string.

---


### 67. [Attention Routing Stabilizes Early: Working-Set Inference for Recurrent Language Models](https://arxiv.org/abs/2609.27373)

**<font color=#1a73e8>作者：</font>** Ke Wan, Chen Chen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recurrent language models repeatedly apply shared network blocks to refine latent representations, but standard inference recomputes global attention at every recurrent step. We study attention dynamics across recurrent depth and find that attention support and distributions stabilize substantially earlier than hidden states and attention outputs. This suggests a two-stage structure: early steps discover a sparse working set of relevant context, while later steps refine representations over largely the same routing support. Motivated by this structure, we introduce WISE (Working-set Inference with Support Exploitation), a training-free method that uses unrestricted global attention during early recurrence and later reuses directly discovered block-structured support while keeping recurrent depth and within-support attention computation dynamic. Controlled interventions show that recurrent discovery is important and that support-only reuse better preserves model behavior than more restrictive attention-reuse alternatives. Across multi-hop QA benchmarks, WISE largely preserves full-attention performance, while context scaling reveals increasingly sparse working sets and greater efficiency gains. Quality is largely preserved through 2K context, with a measurable loss at 4K. An optimized sparse-attention implementation achieves up to a 1.76x attention speedup over native FlashAttention at 4K and a 1.36x speedup for the full 32-step attention trajectory. Our code is available at this https URL.

---


### 68. [Planned Test-Time Scaling with Coordinated Reasoning Paths](https://arxiv.org/abs/2609.27374)

**<font color=#1a73e8>作者：</font>** Xueqing Wu, Langxing Bai, Hritik Bansal 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Test-time scaling with parallel branches is widely adopted to improve performance on challenging reasoning tasks. The predominant approach, repeated sampling, draws branches independently from a single policy, which can produce redundant attempts and thereby limit the gains from additional inference compute. To address this limitation, we propose Planned Test-Time Scaling (PTTS), which replaces independent sampling with a coordinated joint policy: a planner generates a solution outline for each branch, steering the branches toward distinct reasoning paths, and an executor produces a full solution conditioned on each outline. Formally, we show that PTTS strictly generalizes repeated sampling and, in a stylized setting, provably promotes coverage of complementary reasoning modes and yields better pass@k scaling. We instantiate PTTS on top of strong reasoning models, keeping them fixed as executors while replacing repeated sampling with PTTS inference to further enhance test-time scaling. Concretely, we develop two variants: PTTS-ZS prompts a model to jointly generate outlines for all branches in a single autoregressive pass, while PTTS-RL directly optimizes the planner against the pass@k reward using truncated execution rollouts for efficient training and a sharper reward signal. Across five mathematical reasoning benchmarks with Qwen3-1.7B and 4B, PTTS-ZS improves pass@64 over repeated sampling by up to 6.7 points, while PTTS-RL further increases the gain to up to 13.4 points. Further analysis indicates that broader coverage of distinct reasoning paths contributes to these gains. Overall, PTTS provides a general framework for improving test-time scaling by coordinating reasoning branches, with zero-shot and trainable instantiations that yield substantial performance gains.

---


### 69. [Forecast Workflow Bench: Evaluating Language-Model Decisions with Budgeted Forecast Tools](https://arxiv.org/abs/2609.27385)

**<font color=#1a73e8>作者：</font>** Shunya Nagashima  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time-series foundation models (TSFMs) provide forecasts for operational decisions, but accuracy alone does not determine their value. Evaluating agents that use these models requires measuring decision quality and forecast cost. FWBench evaluates this capability on 1,251 electricity and cycle-hire cases using fixed forecast tools and simulated capacity contracts. Agents select models, histories and horizons, then submit capacities to minimize a stated loss-cost objective. We evaluated two hosted and eight local configurations, including small language models, and tested local models with and without TSFMs. GPT-6 Astra bought inexpensive short-horizon forecasts selectively, using 2.5% of the budget, and outperformed fixed policies when the saved decisions were scored with three loss-cost weightings. FWBench enables reproducible evaluation of how language models select and use time-series forecasts to make decisions under cost constraints.

---


### 70. [PRISM-VLM: A Multi-Axis Discriminative Benchmark for Compact Vision-Language Models](https://arxiv.org/abs/2609.27395)

**<font color=#1a73e8>作者：</font>** Sanghee Park, Kee-Eung Kim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Compact vision-language models (VLMs) now power a growing share of multimodal applications. The benchmarks used to compare them, however, inherit a frontier-centric design: each model is reduced to a single accuracy number, narrowing the inter-model gap on saturated suites and pressing models into low-score bands on harder ones. We introduce PRISM-VLM, a multi-axis discriminative benchmark that scores every item along seven axes covering the recurring failure modes (task quality, behavioral robustness, and capability bottlenecks) and combines them into a single PScore, with items recycled from fifteen public benchmarks. Across compact VLMs from the past two years, PScore separates model pairs more reliably than prior single-axis benchmarks under an item-level paired bootstrap, and surfaces behavioral differences these benchmarks average away. Even models with statistically indistinguishable PScores diverge sharply along the per-axis profile, particularly on sycophancy, which is nearly orthogonal to single-prompt accuracy. We will release the full pipeline, prompts, and per-item annotations.

---


### 71. [When Parallel Drafter Meets Parallel Speculative Decoding](https://arxiv.org/abs/2609.27396)

**<font color=#1a73e8>作者：</font>** Fuliang Liu, Xue Li, Kun Qian 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> DSpark-style parallel drafters have made speculative decoding highly effective, yet their draft phase remains serialized on the critical path of every round. Parallel speculative decoding (PSD) overlaps drafting with verification, yet existing methods must guess the accepted prefix and bonus token in advance: a wrong guess reverts the whole batch to serial drafting. We present DPara, a PSD framework that reuses effective parallel drafters yet guarantees backbone--verification overlap in every round, thereby eliminating this probabilistic fallback altogether. While the target verifies, DPara's diffusion backbone precomputes draft representations for every acceptance boundary with the bonus left unspecified; a lightweight autoregressive head then combines the revealed verification outcome with the matching precomputed representation to emit the next round's draft tokens almost instantly---fully parallelizing the dominant backbone forward with verification and leaving only the negligible head cost serial. Experiments on Qwen3-8B and Qwen3-14B across seven math, coding, and chat benchmarks show that DPara achieves average speedups of $3.21\times$ and $3.52\times$ over autoregressive decoding, surpassing the strongest serial and parallel speculative decoding baselines alike.

---


### 72. [Only Pay What You Must Spend: On-Demand Privacy Budget Payment for Differentially Private RAG](https://arxiv.org/abs/2609.27406)

**<font color=#1a73e8>作者：</font>** Zhonghao Sun, Zhiliang Tian, Xinyue Fang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Deploying large language models (LLMs) on sensitive data via Retrieval-Augmented Generation (RAG) introduces severe privacy risks. Recent studies apply Differential Privacy (DP) to LLMs with RAG for formal privacy guarantees. However, existing DP-RAG frameworks rapidly exhaust the privacy budget. Although recent efforts attempt to save the budget by narrowing the retrieval scope or sparsifying private generation, these methods themselves cumulatively consume the budget, whereas they could actually rely merely on public information or at a negligible one-time privacy cost. This mismatch fails to align budget expenditure with the model's actual reliance on private data, causing substantial waste on operations that require no private access. To address this, we propose SparsePay-RAG, adopting "only pay what you must spend" as its core principle. Using public information as a zero-privacy prior, it charges the privacy budget only for the private increment. Specifically, SparsePay-RAG narrows the retrieval scope via public topic-guided clustering, adaptively controls private access frequency without privacy cost through isotonic cross-layer trajectory fitting, and compresses per-access budget via DP contrastive decoding. Under strong privacy constraints, experiments show SparsePay-RAG achieves superior privacy-utility trade-offs over baselines.

---


### 73. [What Looks Like a Capability Limit in Vision-Language Models Is a Readout Limit](https://arxiv.org/abs/2609.27408)

**<font color=#1a73e8>作者：</font>** Alfredo F. Frontera Del Valle  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Benchmarks for vision-language models offer their answer choices in some convention: a letter, a color name, a pixel coordinate. That convention is treated as neutral. We find it is not, and that the limits a benchmark reports can belong to the readout rather than to the model.
On 200 COCO photographs, Qwen3-VL-4B picks the correct one of nine locations for a named object 68.5% of the time when the locations are given in English and 20.0% when the same locations are given as pixel coordinates. Chance is 11.1%. The cost arises when the answer options are coordinates; giving the model a coordinate in the question instead costs 3.5 points and is not significant. The gap holds on a 4x4 grid, under 8-bit rather than 4-bit quantization, and in every slice by object size, boundary distance and category. It also decides which model wins. Two models that tie under English names differ by 39 points in one coordinate system and by 54 in the other, in opposite directions.
On the color task, three of the four open models capable of the task show the penalty; on photographs, two of three open models do, and so does Gemini, at 11.1 points on parseable answers (p = 1e-4). GPT-4o does not. To ask whether a model reads a coordinate at all, we attach the wrong name to each one and record which the model follows. Color options written as hue angles are followed below chance; a normalized pixel convention is followed at four times chance. This tells apart conventions a model can use from ones it cannot, though it did not predict accuracy on two untried conventions. Five models also name the same color wheel five different ways, so a fixed answer vocabulary is not neutral across models either.
Five times during this work we measured a capable model as incapable because our scorer and the model disagreed about what an answer looks like. We report each case. They are the phenomenon in miniature.

---


### 74. [EviStreams: Human-in-the-Loop AI Data Extraction for Systematic Reviews in Medicine](https://arxiv.org/abs/2609.27418)

**<font color=#1a73e8>作者：</font>** Sai Karthik Kosuri, Ankita Shashikant Bhosale, Michael Glick 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Systematic reviews underpin clinical guidelines, yet their data-extraction step is a major expert-labor bottleneck bound by a protocolized workflow: two reviewers extract each study independently, an adjudicator resolves disagreements, and the team keeps an auditable record of how every value was produced. Large language models can assist with extraction, but that assistance must fit established review protocols and preserve reproducibility. We present EviStreams, a live, open-source, no-code web platform that puts review teams in control of AI-assisted extraction at three key stages: program design (a structured decomposition approved before any code runs), field specification (typed field definitions calibrated from a pilot), and extracted predictions (reviewer-blinded dual review with adjudication). Working through a form builder, a domain expert defines typed fields rather than prompts, runs extraction over uploaded PDFs, inspects every value alongside the supporting passage it came from, and resolves a reviewer-blinded dual review into an auditable consensus export. An evaluation across four clinical corpora and three frontier model families, released with the system, shows that extraction quality is shaped far more by the field specification than by the choice of model. EviStreams is live at this https URL and released under Apache-2.0.

---


### 75. [Counterfactual Constraint-Conditioned On-Policy Distillation for Multi-Constraint Instruction Following](https://arxiv.org/abs/2609.27421)

**<font color=#1a73e8>作者：</font>** Yanzhao Zheng, Yuanqiang Yu, Tianze Xu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-constraint instruction following requires a model to respond to a query under many simultaneously active constraints. Even strong instruction-tuned models still routinely violate some of them. Existing approaches either augment supervision with sequence- or token-level RL rewards from external verifiers or learned graders, or use on-policy distillation (OPD) against a single full-context teacher whose probability mass becomes diluted as more constraints become simultaneously active. We propose CC-OPD (Counterfactual Constraint-Conditioned On-Policy Distillation), which inverts the standard supervision-generation direction in distillation. Rather than enriching the teacher with information beyond what the student sees, CC-OPD ablates each constraint from the teacher's conditioning in turn, and constructs the per-constraint signal from the resulting per-token probability differentials. The resulting per-token leave-one-out log-likelihood shifts are summed, clipped, and added to the vanilla OPD reward as a token-level shaping term. All shaping terms are obtained from the frozen teacher, without an external verifier during distillation, and the reward equals vanilla OPD wherever the aggregate shift is zero. Across two Qwen model pairs and seven benchmarks, CC-OPD achieves the highest average among all evaluated student-training methods. A 1.5B student trained with CC-OPD surpasses its own 7B RL-trained teacher on the MulDimIF benchmark.

---


### 76. [A Bulletproof Business? Towards Detecting Infrastructure-as-a-Service Offerings on Telegram](https://arxiv.org/abs/2609.27428)

**<font color=#1a73e8>作者：</font>** Roy Ricaldi, Kristiyan Kyurkchiev, Irdin Pekaric  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cybercriminal operations increasingly depend on reusable digital infrastructure---including hosting, proxies, and virtual private networks (VPNs)---rented through Cybercrime-as-a-Service markets and advertised on platforms such as Telegram. We present a taxonomy for identifying Telegram messages advertising cybercriminal Infrastructure-as-a-Service (IaaS). The taxonomy comprises six service categories across compute, network, and communication infrastructure, together with three trust attributes: Bulletproof, Payment Security, and Transparency. Using 261 human-annotated messages, we evaluate keyword-based and TF--IDF classifiers and examine prompt-based large language models as exploratory baselines. We select a TF--IDF pipeline and apply it to 1,116,071 messages from 167 cybercrime-related Telegram communities. The pipeline assigns at least one infrastructure category to 207,244 messages (18.57%) spanning 113 communities. Classified advertising is highly concentrated: a single community accounts for 50.3% of infrastructure-positive messages, while the trust-attribute classifiers identify Bulletproof claims in 37.66% of those messages. These findings characterize the scale, composition, and concentration of infrastructure advertising on Telegram and can inform the prioritization of communities and actors for monitoring and investigation.

---


### 77. [Latent evolving World Action Model](https://arxiv.org/abs/2609.27455)

**<font color=#1a73e8>作者：</font>** Xueji Fang, Boqiang Duan, Hua Wu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World Action Models (WAMs) jointly model action generation and environment dynamics and are mostly built on pretrained Video Diffusion Models (VDMs). In VDM-based WAMs, observations are first encoded by a VAE, and the resulting compressed latents are then processed by large video diffusion backbones to extract effective features for action generation. However, this paradigm ties WAM performance and training cost to large-scale video generation pretraining, limiting WAM efficiency and scalability. In this paper, we theoretically and empirically investigate how visual representations affect action generation in WAMs. Our results show that predictive embeddings from Joint-Embedding Predictive Architecture (JEPA) encoders better support action generation than compressed VAE latents, with I-JEPA performing best in our encoder comparison. Based on these findings, we propose LeWAM, which conditions action generation on JEPA embeddings and models environment evolution by predicting future embeddings in the same space, without relying on a video diffusion backbone. We further find that imitation learning matches demonstrated actions but does not distinguish better actions from worse ones, even though small action deviations can greatly affect task success. To address this limitation without additional environment interaction or the human oversight required for resets and safety, we introduce Demonstration-Guided DPO (DemoDPO), an offline preference refinement stage that derives preference supervision directly from this http URL only 0.4B trainable parameters, LeWAM achieves an average success rate of 92.28\% on RoboTwin 2.0, comparable to that of state-of-the-art VLAs and WAMs, and maintains practical effectiveness on real-world manipulation tasks.

---


### 78. [Beyond Balanced Accuracy: A Resolution and Parity-Controlled Benchmark for Vision-Language and Vision-Only Defect Assessment in UAV Power-Line Inspection](https://arxiv.org/abs/2609.27457)

**<font color=#1a73e8>作者：</font>** Linghao Zhang, Siyu Xiang, Junwei Kuang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) are often reported to outperform task-specific vision backbones for unmanned aerial vehicle (UAV) power-line defect assessment. We test that claim on ElecVQA-Bench, a 56,972-item benchmark derived from the public InsPLAD dataset, across six evaluation choices: partition, evaluated item set, label space, replication, input resolution, and side information. On a matched partition, a Swin Transformer and the strongest adapted VLM differ by only 0.03 points at binary screening. At seven-way defect typing, increasing the vision backbones from 224 px to the measured pixel budget of the VLM preprocessor narrows the gap against InternVL3.5-8B from +20.53 to -0.57 points for ResNet-50 and from +23.67 to +4.70 points for Swin-T. A pixel-budget audit shifts Qwen3-VL-8B macro recall by 10.78 points, yet a source-pixel-matched InternVL control still leaves Qwen ahead by 7.43 to 13.61 points while using 56% fewer visual tokens, so neither source pixels nor token budget explains the difference between the two VLMs. A two-seed global replication changes Qwen binary accuracy and seven-way macro recall by 0.86 and 1.02 points. After split-specific retraining, Qwen does not lead at crop or image level, and a 14-tower, three-seed replication reverses the sign across seeds, giving mean common-six macro recall of 0.9085 for Qwen against 0.9509 for ResNet-50. No split regime yields a family-level advantage that survives multiple-comparison correction. The study supports a benchmark-audit contribution rather than a general claim of VLM superiority.

---


### 79. [Invisible in Space, Visible in Time: Motion Vision CAPTCHA against GUI Agents](https://arxiv.org/abs/2609.27461)

**<font color=#1a73e8>作者：</font>** Zeyu Zhang, Dingyi Rong, Zijian Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Most existing visual CAPTCHAs remain spatially solvable: the required information is exposed by static appearance, local structure, and interface state. This assumption is weakened by advances in multimodal large language models (MLLMs) and Graphical User Interface (GUI) agents, which exhibit strong visual perception, reasoning, and browser interaction capabilities. We propose Motion Vision CAPTCHA (MVCAP), a hierarchical motion-based CAPTCHA framework in which target semantics are instantiated as motion-defined foreground structures and become recoverable only through temporal segregation from a dynamically evolving background. Built on this shared principle, MVCAP is instantiated in three perceptually progressive levels: coherent motion, structural motion, and biological motion. To evaluate this framework, we introduce MVCAP-Bench, a browser-based benchmark with 600 live CAPTCHA instances, together with a matched foreground-only control benchmark, MVCAP-Bench-FG. We evaluate humans, Browser Use agents, native computer use agents, and a supplementary offline VQA setting derived from the same instances. Results reveal a substantial human--agent gap: on the full MVCAP-Bench, human accuracy reaches 99.6%, whereas the best GUI agent achieves only 16.8%, close to the six-way chance level. The foreground-only control further shows that the key difficulty comes from dynamic background camouflage rather than answer format or browser interaction alone. These findings identify a measurable human--agent perception gap and position MVCAP-Bench as a benchmark for studying motion-defined perception in current agents.

---


### 80. [CereVLA: Cerebellum-Inspired Consequence-Aware Residual Governance for Efficient Vision-Language-Action Execution](https://arxiv.org/abs/2609.27468)

**<font color=#1a73e8>作者：</font>** Shuai Zeng, Yuxuan Liang, Hangmiao Hu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Action-chunked vision-language-action (VLA) policies improve inference efficiency, but limited feedback within committed action chunks can lead to accumulated execution errors. Residual adaptation can correct such deviations without retraining the VLA; however, existing corrections are typically optimized for reference-action consistency without explicitly considering their downstream consequences. To address this limitation, we present Cerebellum-Inspired Consequence-Aware Residual Governance (CereVLA), a unified framework that integrates lightweight residual refinement and predictive consequence evaluation into frozen VLA execution. Corrective actions are first generated by flow-based residual refinement, and their short- and interval-horizon consequences are then evaluated by a recurrent state-space model and a history-aware classifier. Residual corrections predicted to be unfavorable are selectively suppressed by a lightweight governor. Comparisons with state-of-the-art methods on LIBERO-10 and LIBERO-GOAL demonstrate the effectiveness of CereVLA. On SO-101, CereVLA increases task success from 57.5% to 90.0% and reduces mean control steps by 19.6% among successful trials, relative to the frozen SmolVLA baseline.

---


### 81. [DeltaS: Reading the Gated Linear Attention State for KV Cache Eviction in Streaming Video](https://arxiv.org/abs/2609.27470)

**<font color=#1a73e8>作者：</font>** Taeyoun Kwon, Seungjin Kim, Hyeonyu Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent video-language models increasingly adopt hybrid architectures that interleave linear and full attention layers for efficient long-context processing. While the recurrent state of linear attention remains fixed in size, the KV cache of full attention continues to grow with the video stream, making eviction necessary under a bounded memory budget. The key challenge in streaming is that eviction must occur before the question arrives, so what to retain has to be decided without the question. Existing eviction methods derive token scores from the KV cache itself, using position, attention, or key-value representations, and attention-based scores further require proxy queries or extra computation. Hybrid backbones offer another source of signal. In gated-delta linear attention, the recurrent state is updated by the residual between each input and what can already be retrieved from the state, so its change over a chunk of frames reflects how much new information the chunk brings. We propose DeltaS, a query-agnostic, training-free method that retains video chunks inducing larger normalized state change, or state drift. In a controlled comparison with the budget and retention policy held fixed, state drift outperforms position-, attention-, and key-value-based signals. With a signal costing only 1.9% of the forward pass, DeltaS surpasses the strongest query-agnostic bounded-memory baseline by 2.1 points on average across six long-video benchmarks and by 5.6 points on the longest benchmark. These results suggest that the two memories of hybrid architectures can work cooperatively. Code is available at this https URL.

---


### 82. [Uncheatable Eval: Dynamic Compression-Based Evaluation of Language Models](https://arxiv.org/abs/2609.27510)

**<font color=#1a73e8>作者：</font>** Kaifeng Tan, Yudong Li, Linlin Shen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Modern large language models are pretrained on massive datasets, making it difficult to prevent benchmark data from entering their training sets and undermining the reliability of evaluation results. Reliable evaluation is particularly challenging for base models, whose limited instruction-following ability complicates task-based assessment. We introduce Uncheatable Eval, a dynamic benchmark that regularly collects newly published text to evaluate base language models and reduce the risk of data contamination. Drawing on the relationship between a model's predictive ability and its ability to compress data losslessly, we use compression rate to evaluate how well models predict new text. We evaluate 80 models across 14 text categories, study how compression changes with context length, and examine the correlation between compression rate and zero-shot MMLU accuracy. Our results yield three main findings: (1) compression performance follows a consistent scaling trend with model size; (2) attention-based, hybrid, and recurrent models differ in how their compression performance changes as more context becomes available; and (3) lower compression rates are strongly associated with higher zero-shot MMLU accuracy. Code is available at this https URL.

---


### 83. [NV-Reason-CT: 3D Visual Language Model for CT Analysis](https://arxiv.org/abs/2609.27511)

**<font color=#1a73e8>作者：</font>** Andriy Myronenko, Dong Yang, Yucheng Tang 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present NV-Reason-CT, a generative vision--language model for chest and abdominal CT combining native 3D visual encoding with radiologist-guided reasoning. The model couples a native 3D vision transformer with a language model, passing all visual tokens and their explicit 3D coordinates into language decoding without further spatial token merging. This retains volumetric spatial information within the vision encoder and through the language model's positional encoding during joint processing with text.
We train on a curated corpus of approximately 550,000 multimodal instruction examples from 70,111 unique CT image inputs, combining standardized reports, abnormality-focused and anatomy-specific questions, multi-turn interactions, and radiologist-authored reasoning from recorded and transcribed expert CT interpretations. Expert annotations provide direct supervision and guide additional report-grounded synthetic reasoning. End-to-end supervised fine-tuning (SFT) is followed by Group Relative Policy Optimization (GRPO), with verifiable rewards over chest and abdominal abnormality sets.
The model supports abnormality classification, report generation, and interactive reasoning with reviewable observations, differential diagnoses, and uncertainty. Evaluation spans public CT benchmarks and a held-out NIH cohort. On CT-RATE, NV-Reason-CT achieves a macro-F1 of 0.614 and macro-AUROC of 0.871 without a task-specific classification head; generated reports achieve a report-derived macro-F1 of 0.592. In a preliminary study with expert radiologists, AI-assisted review received favorable confidence ratings and was associated with a 50% reduction in average reported interpretation and reporting time. We release the model and training code to support reproducible research on explainable AI for volumetric medical imaging.

---


### 84. [Not What You Meant: Can LLMs Follow a Specified Negation Semantics?](https://arxiv.org/abs/2609.27517)

**<font color=#1a73e8>作者：</font>** Qiming Bao, Agnieszka Mensfelt, Michael J. Witbrock 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Negation does not carry a uniform interpretation across domains. In legal, regulatory, and medical reasoning, the intended interpretation depends on the reading in force -- open- versus closed-world, two- versus three-valued, and credulous versus skeptical. We study which reading of negation large language models adopt by default and whether they can override that preference when a different reading is explicitly specified. To this end, we introduce NAFBench, a procedural generator of solver-certified instances spanning four semantic viewpoints: SLDNF, well-founded semantics (WFS), and credulous and skeptical reasoning under stable-model semantics. The generator emits ground normal logic programs with controlled depth, width, and cycle structure. Each program is solved under all four viewpoints using SWI-Prolog, a well-founded semantics solver, and clingo, yielding up to four divergent labels. The programs are then verbalized into natural language under multiple framings and rule orderings that leave the answer invariant. The results expose a consistent gap. Across open-source models, following a specified negation semantics remains unsolved: the strongest models score 59--74% across the four semantic viewpoints, while the weakest score 31--67%. All models are order-sensitive on more than half of logically identical rule shufflings, while the two weaker models frequently overcommit on well-founded "undefined." Two frontier models reach 100% on the main fixed-complexity evaluation set, and a third, o4-mini, is near-perfect, falling only to 81% on well-founded "undefined." Delegating reasoning to a solver, fine-tuning on certified traces, or forcing an explicit three-valued verdict each partly closes the gap.

---


### 85. [ProCredit: From Outcome Rewards to Progress Credit in Agentic Reinforcement Learning](https://arxiv.org/abs/2609.27532)

**<font color=#1a73e8>作者：</font>** Ming Ma, Yi Zhu, Yiran Zhong 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-horizon agentic tasks require an agent to modify an environment through a sequence of tool calls, with success determined by the final state. The standard recipe assigns a single outcome reward at the end and compares trajectories sampled for the same task. As a result, a group with no successful trajectory yields no training signal, failed attempts cannot be told apart by how close they came to completion, and turns that advance the task receive the same credit as turns that only query the environment. Prior work refines the unit of comparison from the trajectory to the step, or trains a reward model to supply intermediate signal: the former still derives its signal from final success alone, and the latter estimates it with a model. We observe that the acceptance checks that decide success can also be run on intermediate states, so progress is as verifiable as the outcome. We propose ProCredit, which turns this verified progress into credit: it reruns the acceptance checks after each turn, rewards the turn by its change in progress, and uses these rewards to assign credit both across attempts at the same task and across the turns within a trajectory. Starting from Qwen3.5 base models at three scales on AppWorld, ProCredit outperforms outcome-reward baselines and progress-based baselines in task completion rate at every scale on both test sets, exceeding the strongest outcome-reward baseline by 4.1 percentage points at 4B, and results in a second environment show the same direction of improvement. Ablations show that adding the final progress to the trajectory score alone does not improve performance: the gain comes from crediting progress to the turn where it occurs.

---


### 86. [Control-Token Injection Suppresses Chain-of-Thought and Defeats Reasoning-Based Oversight in Tool-Using Agents](https://arxiv.org/abs/2609.27542)

**<font color=#1a73e8>作者：</font>** Muhammad Usama, Khair Un Nisa, Summer Yeoreum Jung  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The safety of a tool-using language model agent is usually treated as a property of the model alone. We give controlled, full-precision evidence that it is instead a joint property of the model and the software that renders its chat template and parses its tool calls, the decoding harness, and that both halves are attackable from untrusted input. On the released gpt-oss-20b reasoning model under its published tool sandbox, appending a single string of the model's own channel-control tokens to a user message makes the tokenizer render a reasoning turn that is already complete, so the model writes no chain-of-thought and proceeds directly to the tool call. Across forty tasks the model already completes, the reasoning channel falls from a mean of 52.5 tokens to zero on every trial while the this http URL still fires on every trial. A rule monitor and a cross-family language-model monitor detect the unsafe request on all plain trials and no forged trials, and on overtly malicious requests the attack converts 39.6% of the model's refusals into completed exfiltrations. Separately, whether an identical tool-call generation fires is decided by the harness parser, not the model: a truncation-tolerant regular expression fires a call whose closing token is missing while a strict one drops it, and two parsers shipped for the Gemma agent give opposite outcomes on identical greedy generations, firing on all twenty-four trials and on none. We show the suppression can be delivered indirectly and characterize its dependence on the chat template across two more reasoning models, and we evaluate input sanitization, parser hardening, and empty-reasoning detection as defenses; flagging an absent trace catches the basic attack but not an adaptive benign decoy. All measurements use greedy decoding on publicly released models. Code and per-trial logs: this https URL

---


### 87. [CCR: Towards a Common, Quality-Gated CACAO Integrations Registry for European Cybersecurity Automation](https://arxiv.org/abs/2609.27567)

**<font color=#1a73e8>作者：</font>** Mateusz Zych, Vasileios Mavroeidis, Gudmund Grov  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Standardised, machine-readable cybersecurity playbooks provide a basis for portable, shareable, and reusable incident-response logic. OASIS CACAO provides a vendor-neutral representation for such playbooks, but not the product-specific integration artefacts needed to invoke external products and services. We introduce the Common CACAO Registry (CCR), an open, provenance-aware registry of CACAO HTTP-API connector envelopes. Each envelope captures an API operation's command, inputs, target, authentication-related information, provenance, validation evidence, and maturity metadata. CCR is \emph{quality-gated}, with acceptance requiring both CACAO v2 schema validity and a mean back-validation score of at least 0.8 against the source OpenAPI operation, while a six-level maturity model records progressively stronger evidence and distinguishes gate acceptance from operational readiness. To seed CCR, we develop a hybrid OpenAPI-to-CACAO pipeline. Deterministic code extracts source-derived interface facts, generates identifiers, wires cross-references, and validates structure, while a constrained LLM provides bounded semantic enrichment, including action naming, authentication interpretation, and CACAO activity annotation. Evaluation across eight security APIs yields 713 CACAO-schema-valid envelopes with a mean back-validation score of 91.5\%, of which 675 produce well-formed, dispatchable HTTP requests in a local harness. Comparison with a deterministic rule-based baseline shows that mechanical API structure is preserved more reliably through rule-based translation, while the LLM contributes bounded semantic enrichment, most notably CACAO activity annotation. Together, these results support CCR as reusable integration infrastructure for CACAO action steps and as an initial foundation for a broader common European registry.

---


### 88. [DCRL: Decoupling and Coupling Reinforcement Learning via Policy-Reward Manifold Alignment](https://arxiv.org/abs/2609.27572)

**<font color=#1a73e8>作者：</font>** Henan Sun, Zehua Li, Haitao Hu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) has emerged as a key paradigm for improving the reasoning capabilities of large language models (LLMs). However, existing reward systems, such as rule-based and reward-model-based, often exhibit issues such as unstable optimization and reward hacking. In this work, we revisit the general reasoning of LLMs from a geometric perspective, conceptualizing it as a coupled manifold composed of three interdependent sub-manifolds: logical deduction, evaluation, and representation. Based on this perspective, response generation in RL can be interpreted as a decoupling process from the evaluation manifold, while reward estimation corresponds to a decoupling process from the logical deduction manifold. The limitations of rule-based and reward-model RL systems can be geometrically interpreted as the mismatch of policy-reward manifolds during RL process. To address the aforementioned misalignment, we propose Decoupling and Coupling Reinforcement Learning (DCRL) framework, which incorporates two key components: (1) a syllogistic logic-based prompt evolution mechanism that dynamically refines reward rubrics to enhance the expressiveness of the reward manifold; and (2) a policy-reward re-coupling mechanism that jointly updates the reward and policy models, ensuring consistent evaluation and mitigating manifold mismatch during training. Theoretical analysis and extensive experiments across multiple reasoning domains demonstrate that DCRL consistently outperforms both rule-based and reward-model baselines. Notably, a Qwen3-4B model trained under DCRL surpasses a Qwen3-32B baseline and approaches the performance of a Qwen3-235B model, highlighting superior effectiveness and generalization in RL.

---


### 89. [Does Step Law Transfer to Small-Scale Language Models? An Empirical Recalibration Below 59M Parameters](https://arxiv.org/abs/2609.27581)

**<font color=#1a73e8>作者：</font>** Egor Romanyukov, Timofey Novikov, Timur Shokarov 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Step Law gives power-law formulas for the optimal peak learning rate eta* and batch size B* when pre-training language models. It was calibrated on models between 59M and 1B parameters; the small-model regime N < 59M was never tested empirically by its authors. This regime matters for single-GPU training, interpretability research, educational experiments, and settings where larger models are infeasible on memory or cost grounds.
We test whether Step Law transfers to small language models. We consider three outcomes: H1, the original coefficients work directly; H2, the power-law form holds but with different coefficients; and H3, a power law does not describe the optima in this regime. All experiments use a single nanoGPT/TinyStories pipeline with a 2048-token BPE vocabulary, AdamW, and a warmup-cosine schedule. The optimum for each (N, D) cell is extracted from the loss surface L(eta, B) via a local quadratic approximation in log-log coordinates over the smoothed training loss.
The final dataset contains 29 unique (N, D) cells and 935 analysis-ready runs. The main refit uses 25 cells (815 runs) in the working range 4 <= D/N <= 600. On the pooled data we accept H2: the functional form is preserved, but the coefficients differ from the original. We obtain eta*(N, D) = 0.0985 N^(-0.508) D^(0.238) (R^2 = 0.834) and B*(D) = 3.6 x 10^(-4) D^(0.931) (R^2 = 0.950).
Step Law's structural claim that B* is independent of N is reproduced (p = 0.87), but the growth of B* with D is nearly twice as steep as in the original work. Direct transfer of Step Law systematically overestimates the optimal learning rate: the median ratio eta_SL / eta* is approximately 4.0x, with a range of 2.4x to 6.6x.

---


### 90. [MWE-ECL: Recoverable Long-Range Context Does Not Always Override Local Lexical Priors](https://arxiv.org/abs/2609.27590)

**<font color=#1a73e8>作者：</font>** Wei He, Aline Villavicencio, Rodrigo Wilkens 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-context evaluations often test whether a model can recover distant evidence, but recoverability does not guarantee behavioral influence. We test the prediction that a distant discourse anchor can remain explicitly recoverable yet fail to change the locally preferred reading of a familiar multiword expression; such failures should concentrate when the model's no-anchor default conflicts with the anchor, while prior-correct decisions remain largely preserved. We introduce Multiword Expression Effective Context Length (MWE-ECL), a bilingual diagnostic whose matched anchor-retrieval, no-anchor prior, and interpretation prompts measure explicit recoverability, model-observed defaults, and anchor-conditioned decisions, respectively. Across eight English deployment panels on a shared 0-128K grid, retrieval-control accuracy on prior-conflict items is 0.989-1.000, prior-conflict override spans 0.806-1.000 (0.809-1.000 after conditioning on correct retrieval), and preservation of prior-correct decisions remains 0.977-1.000. A same-call control querying retrieval and interpretation in one prompt reproduces the gap for DeepSeek V4 Pro (1.000 retrieval versus 0.900-0.920 interpretation), showing that separate invocations are not its sole explanation; smaller or absent gaps in the other two models bound its generality. For DeepSeek V4 Flash, separate prompt-fit tests retain perfect retrieval with lower interpretation at 512K and 1M, while foil-consistent cues shift the no-anchor prior far more than retrieval; cross-model cue effects are heterogeneous. A separately reported 10-family Chinese subset shows similar descriptive gaps, but imperfect retrieval for some models prevents an integration-only attribution. MWE-ECL therefore evaluates whether explicitly recoverable distant context changes a competing local semantic decision.

---


### 91. [Hidden not Deleted: How Networks Suppress Entangled Features](https://arxiv.org/abs/2609.27593)

**<font color=#1a73e8>作者：</font>** Akash Samanta, Manish Pratap Singh, Debasis Chaudhuri  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Concept erasure methods that operate via linear projection assume that features occupy separable subspaces. We show this assumption fails under dense superposition: when two features are forced into an antipodal pair sharing a single subspace, state-of-the-art linear erasure destroys both, not just the target. Networks trained with gradient descent instead solve this problem non-linearly, but not uniformly: they converge to one of two distinct circuit-level solutions depending on initialization, which we call mirror and shadow solutions. We map this bifurcation as a function of feature entanglement, show it reflects a stable attractor structure rather than an artifact of our setup, and use targeted causal interventions to demonstrate that both solutions leave a substantial, measurable trace of the erased feature's representation intact, recoverable through a single scalar patch rather than requiring any further training. This mirrors a failure mode recently observed empirically in LLM unlearning, where suppression rather than deletion allows forgotten knowledge to resurface; our results offer a mechanistic, causally-validated account of why that failure mode occurs.

---


### 92. [When Context Misleads: In-context Learning with Jurisdiction in Large Language Models](https://arxiv.org/abs/2609.27603)

**<font color=#1a73e8>作者：</font>** Pei-lin Li, Qingle Liu, Junyang Feng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In-Context Learning (ICL) has become a cornerstone of modern LLM deployment. However, existing ICL post-training methods have a critical blind spot: they excel at extracting patterns from demonstrations while often neglecting context authority, the ability to determine whether contextual information should govern the final answer. To benchmark this capability, we introduce FakeContextBench, which contains pseudoscientific claims across seven domains. Our evaluation of commercial and open-source models shows that large-scale pre-training alone is insufficient for reliable context-authority discrimination. Moreover, prevalent ICL fine-tuning methods can increase susceptibility to misleading context, reducing reality accuracy by up to 14.95 percentage points relative to the base model. To address this trade-off, we propose Jurisdiction In-Context Learning (J-ICL), a post-training framework that incorporates context validation into the training objective. Across four model backbones, J-ICL improves ICLEval by an average of 5.84 percentage points and reality accuracy by 9.20 points over the corresponding base models. It also raises the Reality Rate by an average of 18.09 points relative to MetaICL and Symbol Tuning. These results demonstrate that ICL capability and resistance to deceptive context can be improved together. The benchmark is available at this https URL.

---


### 93. [State-Grounded Conditioning: Wrapping User-Facing LLM Agents Where Direction Depends on Live State](https://arxiv.org/abs/2609.27606)

**<font color=#1a73e8>作者：</font>** Qi Liu, Xiaoyang Yuan, Yubin Ruan 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce State-Grounded Conditioning (SGC), a design principle for user-facing LLM agents that must condition on live user state (game state, session history, live inventory), and a distinct failure class we call direction drift: task-complete responses whose chosen direction misaligns with the current state. SGC externalises state-dependent control into rule kernels over structured inputs and three primary state slices, via Perception, Grounding, and Interaction wrappers with explicit conditioning dependencies. We evaluate SGC on a 200-session anonymised benchmark ($\approx$1,000 assistant model turns) from an in-game conversational coaching agent that guides players through consecutive competitive matches, reporting mean first-token latency and five human-annotated dialogue-quality metrics that jointly cover factual grounding and coach-like guidance progression. The Perception wrapper holds mean first-token latency at 1.5s (vs. 6.1s for PE-Agent inside a production tool-use harness); enabling all three wrappers lifts turn-level grounded accuracy from 61.1%/69.8% (Prompting / PE-Agent) to 96.7% and session-level grounded accuracy from 20.0%/26.5% to 83.5%; session-level grounding-failure incidents drop by $\approx$78% relative to the strongest baseline. A cumulative ablation shows complementary incremental gains as the wrappers are added. These results inform approximate state-slice orthogonality, without establishing independent per-wrapper effects.

---


### 94. [FLEET: From Logits Entropy to Enhanced Trajectories in Text Generation](https://arxiv.org/abs/2609.27657)

**<font color=#1a73e8>作者：</font>** Oleksii Streltsov, Oleksandra Vitko  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Solutions based on large language models (LLMs) often rely on temperature sampling to improve accuracy and stability by aggregating multiple samples from the completion distribution. However, this memoryless approach is inherently suboptimal: because it lacks awareness of prior generations and their evaluations, it produces an increasing proportion of semantically duplicate answers as more samples are drawn, leading to diminishing returns. To address this limitation, we introduce FLEET, a novel method that integrates a memory mechanism into the generation process. FLEET represents each generation as a sparse trajectory through states whose entropy exceeds a predefined threshold and uses these trajectories to infer per-token utility scores that adjust the logits. Benchmark evaluations demonstrate that FLEET achieves the same accuracy as the repeated sampling baseline, with a 3x speedup, and substantially improves accuracy on complex coding tasks (LiveCodeBench Pass@32 increases from 59.9% to 66.2%) under the same budget. Furthermore, in the greedy-decoding configuration evaluated here, the approach is deterministic and uses a single calibration pass to derive its principal hyperparameters, requiring only minimal modifications to existing LLM pipelines.

---


### 95. [The Path Matters: Evaluating Small Language Models Beyond Answer Accuracy in KGQA](https://arxiv.org/abs/2609.27669)

**<font color=#1a73e8>作者：</font>** Eduin E. Hernandez, Sergio A. Diaz, Luis F. Garcia 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Small language models (SLMs) are increasingly paired with knowledge graphs (KGs), yet end-to-end KG question answering conflates graph access, search, navigation, reasoning, and answer generation. This coupling makes it difficult both to determine whether an SLM can faithfully execute the reasoning path implied by a question and to attribute failures to navigation rather than to other stages of the pipeline. We isolate this capability by employing the THESEUS navigation and traceability framework and using frozen, off-the-shelf SLMs as local action policies. At each hop, the environment exposes the legal outgoing graph actions, and the model selects one executable graph action and decides whether to stop, without task-specific parameter updates, model-controlled beam search, or free-form answer generation. This controlled setting allows us to evaluate terminal-answer accuracy with Hits@1 together with path fidelity, using Path Edit Distance (PED) as the primary trajectory metric. Across the Kinship and MQuAKE-ST KGQAs, similarly sized local models differ substantially in answer accuracy and path fidelity, with the two metrics sometimes favoring different models. This model-dependent behavior also extends to prompting, as a single demonstrated trajectory can improve or degrade navigation depending on the model. These results motivate evaluating SLM graph reasoning beyond endpoint accuracy alone.

---


### 96. [Same Scores, Different Decisions: Evaluating JEV and Language Models for Legal Document Understanding](https://arxiv.org/abs/2609.27678)

**<font color=#1a73e8>作者：</font>** Fan Zhang, Yankai Chen, Zhuohan Xie 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Contract inference requires multiple judgments about a shared document, but aggregate accuracy can conceal changes in the individual decisions. Repeated agreement is also insufficient: a model may consistently return the wrong answer. In this paper, we compare Jev with nine language models on ContractNLI, evaluating inference cost, response time, average correctness, and correctness across repeated request conditions. Controlled comparisons vary hypothesis visibility, requested outputs, and output order while keeping the contract and target judgment fixed. Jev has the lowest cost and median response time among the evaluated configurations, while hosted language models achieve higher baseline accuracy. Rankings by baseline accuracy differ from rankings by correctness across every condition and repeat, although small differences in the latter do not establish a general stability advantage. Development diagnostics further reveal compensating corrections and regressions, as well as persistent errors. These findings motivate evaluating cost and response time alongside whether individual judgments remain correct as the request configuration changes. Code: this https URL

---


### 97. [Gender Bias in Vision-Language In-Context Learning](https://arxiv.org/abs/2609.27682)

**<font color=#1a73e8>作者：</font>** Tong Xiang, Noa Garcia, Yuta Nakashima  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In-context learning (ICL) enables large vision-language models (LVLMs) to perform tasks by following patterns from in-context examples, yet its potential to amplify societal biases remains underexplored. We systematically investigate how ICL influences gender bias in LVLMs through VL-BICLE, an evaluation framework comprising six ICL settings, three tasks, and four datasets. Our experiments on six LVLMs reveal that gendered ICL demonstrations act as a directional force, shifting model bias toward the demonstrated gender through a cross-gender mechanism that disproportionately degrades performance on the opposite gender. This effect appears in image captioning and pronoun prediction but not in visual question answering, indicating that gendered ICL influences bias only when the task output involves gendered language. Similarity-based retrieval methods inherit the training pool's gender imbalance and offer no debiasing advantage, while standard quality metrics remain blind to these bias shifts. To mitigate this bias, we replace real in-context images with synthetic ones from stable diffusion models while keeping captions unchanged. This simple intervention reduces gender bias without degrading caption quality.

---


### 98. [Consequential Behaviour and Representational Fairness in the Validation of Synthetic Research](https://arxiv.org/abs/2609.27690)

**<font color=#1a73e8>作者：</font>** Florian Kutzner, Celina Kacperski, Laura de Molière 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Researchers in industry and academia use synthetic survey respondents powered by large language models as substitutes for human samples. These synthetic populations require validation against real-world data, so researchers often address them using ad hoc comparisons with human surveys. Inspired by the intention-behaviour gap in behavioural science, we argue that these validations test the wrong thing for most applied cases where decision makers commission synthetic research to anticipate consequential behaviour. To address this problem, we propose a validation framework with two requirements. First, every validity claim must state its level of correspondence with human data: does the sample predict what the represented people do, which of four diagnostics (location, dispersion, response process and structure) does the validation address, and does the validation compare against experimental effects? Second, researchers must report validity claims for subgroups, since these groups are often the most affected by consequential decisions and aggregate accuracy hides their misrepresentation. Our validation framework operationalises three justice dimensions (distributional, procedural, and recognition) as measurable quantities and defines within-persona counterfactual experiments as a validation requirement. We then apply the framework to electric vehicle charging tariffs, before closing with a reporting checklist that researchers can use to make convincing validity claims.

---


### 99. [FFM-CP: Cross-Backbone Fusion of Vision-Language Foundation Models for Few-Shot Computational Pathology](https://arxiv.org/abs/2609.27710)

**<font color=#1a73e8>作者：</font>** Anh-Tien Nguyen, Trung DQ. Dang, Nghiem Tuong Diep 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pathology vision-language foundation models vary in performance across diseases and tasks, with no single model consistently performing best. The high cost of expert pathology annotation can also limit the labeled data available for task-specific adaptation. Combining complementary pretrained representations is a potential approach to these limitations, yet learning an effective fusion from few labeled examples remains challenging. We introduce Few-shot Fusion Foundation Models of Computational Pathology (FFM-CP), which is a framework that combines multiple pathology vision-language models in the few-shot learning setting. The framework first aligns heterogeneous representations using a closed-form Orthogonal Procrustes transformation estimated from corresponding support images. This alignment preserves within-model feature geometry without training an additional alignment network. Within the aligned space, a unified graph enables information exchange across backbones by jointly refining support-image features and visual and textual class prototypes. These refined representations support complementary text-prototype and case-retrieval branches that capture semantic class knowledge and within-class visual variation, respectively. Each branch learns to combine predictions from all ordered backbone pairs, allowing queries encoded by one model to draw on evidence represented by another. We evaluate three backbone combinations on six histopathology datasets at 4, 8, and 16 shots per class. FFM-CP achieves higher mean macro-F1 than the strongest individually adapted member of each fused set in 50 of 54 comparisons. These findings suggest that combining complementary pretrained representations can improve histopathological classification when annotations are limited.

---


### 100. [SkillGym: Internalizing Human Skills into LLMs for Real-World Problem Solving](https://arxiv.org/abs/2609.27717)

**<font color=#1a73e8>作者：</font>** Zhilong Ge, Yuting Shao, Yutao Yang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Human-written agent skills encode rich workflows for real-world problem solving, but are typically used as external inference-time instructions rather than internalized as reusable model capabilities. We introduce \texttt{SkillGym}, a framework that transforms these skills into executable, verifiable training environments for large language model agents. Its skill-to-task pipeline instantiates concrete tasks, verifies outcomes with code-based checkers, and assesses empirical skill dependence through contrastive executions. We construct and release 2,756 environments across 12 categories and collect 8,364 successful trajectories from multiple models and harnesses, averaging 49 tool calls and over 60k logged text tokens. These resources support supervised fine-tuning on verified workflows and reinforcement learning with outcome-based rewards. Under Claude Code, supervised fine-tuning improves Qwen3.5-35B-A3B by 199 Elo on GDPval-AA v2, 19.10 percentage points on Terminal-Bench 2.1, and 28.13 and 12.38 points on SkillsBench v1.1 with and without skills, respectively. Our 35B \texttt{SkillGym-Agent} reaches 51.47\% on skill-assisted SkillsBench, exceeding reported scores for Claude Sonnet 4.6, GPT-5.4 Mini, and DeepSeek V4 Pro. Without skills, it also surpasses skill-assisted bases under Codex and Claude Code, suggesting reusable procedural competence.

---


> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-172](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
