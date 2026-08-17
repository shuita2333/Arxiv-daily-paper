# 🧠 大模型相关研究 | 2026年08月18日

> 本类共 **144** 篇论文：已确认 **138** 篇，待复核 **6** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**51-100**（第 2/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-144](./part-03.md)

---

### 51. [MemoryLake on MemoryArena: A Matched Study of Agent Memory Backends](https://arxiv.org/abs/2608.13883)

**<font color=#1a73e8>作者：</font>** Chaoqun Zhan, Qiang Zhou, Guannan Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Most agent-memory benchmarks test post-hoc recall, whereas MemoryArena evaluates whether memory supports interdependent, multi-session task completion. We compare MemoryLake, a structured multi-track memory backend, with Mem0, text-embedding-3-small vector RAG, and a long-context control across all five MemoryArena domains. The systems share the same agent framework, requested gpt-5-mini model alias, task samples, and scoring code; the memory integration is the intentionally changed component. Because each backend bundles write, retrieval, consolidation, budgeting, and prompt-assembly choices, the study is a matched system-level comparison, not a representation-only ablation or a cost-matched experiment. On the shared evaluation sets, MemoryLake has the highest observed success rate (SR) in mathematics (9/40), physics (12/20), and progressive retrieval (4/20). Every system has zero SR in travel planning, and web shopping yields a single bundle-level success (long context, 1/150); MemoryLake ranks third on both the travel soft process score and shopping step match. Following MemoryArena's suite-level convention, a post-hoc equal-weight average over the five SRs is 20.5% for MemoryLake versus 13.6% for the best comparator. These are point estimates: sample sizes are modest, confidence intervals overlap, and we do not report paired significance tests. A separate MemoryLake-only run over all 221 progressive queries yields a failure-counted SR of 26.7% (59/221) and is not a baseline comparison. The results support a workload-dependent view of memory backends and an observed lead among the four evaluated systems on the shared sets; they do not establish benchmark-wide state of the art or a causal advantage of representation structure.

---


### 52. [Consensus-gated Multi-Agent Neural Architecture Search for Seismic Fault Segmentation](https://arxiv.org/abs/2608.13889)

**<font color=#1a73e8>作者：</font>** Shehram Baig, Ahmad Mustafa  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Neural networks for seismic fault segmentation are often borrowed from computer vision and medical imaging domains where they train under relatively much larger labeled data resources. Optimizing their architecture under tight labeled data budgets as are common in geophysical applications is not a trivial problem. Manually designing data-optimal architectures is time-consuming while classical neural architecture search (NAS) is restricted to hand-crafted search spaces and large compute budgets. We present an agentic NAS system in which a panel of three large language models (Claude, GPT-5.1, and Gemini~2.5~Pro) debates each candidate architecture to unanimous consensus, authors the complete PyTorch implementation, cross-reviews it, and submits it to an automated validate-train-score loop with a hard 450K parameter budget, keep-or-revert lineage, and a memory of failed mechanisms. Operating on source code rather than a predefined operation menu, the search ran on a single consumer GPU and trained only eight candidates. It discovered \ours{}: a 425K-parameter encoder-decoder with a strip-pooling bottleneck, squeeze-and-excitation gating, an asymmetric one-conv decoder, and a feature-pyramid fusion neck. Trained under a protocol identical to all baselines on sections derived from the Thebe fault dataset, it attains the highest F1 (0.578) and IoU of all models tested while being the smallest, outperforming a published-capacity U-Net (31M parameters, F1 0.484), DeepLabV3-ResNet50 (39.6M, 0.516), an Attention U-Net(1.83M, 0.502). The search cost 101 LLM calls ($\sim$1.15M input / 0.39M output tokens) and roughly one GPU-day, making consensus-gated LLM panels a practical, low-cost route to domain-specific architecture discovery.

---


### 53. [MedMix: Specialization-Consistent Federated Sparse MoEs under Modality Heterogeneity](https://arxiv.org/abs/2608.13911)

**<font color=#1a73e8>作者：</font>** Adiba Orzikulova, Dong Min Kim, Jaehong Yoon 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated multimodal medical AI faces modality heterogeneity at both the client and sample levels: clients may systematically lack access to specific modality types, while individual records within the same client may contain different partial modality subsets. Sparse Mixture-of-Experts (MoE) architectures are a promising remedy for modality-adaptive computation, but their use in federated learning is fragile under cross-client modality heterogeneity, where locally learned routing policies can diverge across clients and drive experts toward incompatible specializations. Different clients may assign the same observed modality configuration to different experts, or train similarly indexed experts on different missing-modality configurations, causing standard aggregation to misalign or overwrite the expert specialization that sparse MoEs are intended to learn. To address this challenge, we propose MedMix, a semantic-alignment framework for federated multimodal sparse MoEs that coordinates cross-client routing and expert specialization using modality context. At the client side, MedMix uses modality-context-aware routing to guide expert selection using each token's modality identity, position, and incompleteness context. Across clients, it uses consensus-guided routing alignment to construct server-side consensus anchors for shared modality patterns and align local routing distributions across clients. Complementing these routing mechanisms, client-adaptive expert aggregation leverages client-specific modality-pattern prototypes to match and aggregate functionally similar experts across clients. Experiments on real-world multimodal medical datasets show that MedMix achieves the best average F1 across diverse modality heterogeneity and modality incompleteness settings, with especially clear gains under severe heterogeneity.

---


### 54. [When Personal Memory Has No Single Answer: Evaluating LLM Agents under Irreducible Conflict](https://arxiv.org/abs/2608.13921)

**<font color=#1a73e8>作者：</font>** Lu Yang, Shusheng Xu, Zhuoran Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents increasingly maintain personal memory across sessions, but it can conflict. Preferences depend on context, behavior evolves, and sources can conflict. When a query lacks context, time, or source authority to interpret conflict, treating one memory as definitive converts unresolved conflict into an unjustified, overconfident action. Existing benchmarks recover one answer from conflicting evidence, overlooking whether agents recognize underdetermination, preserve alternatives, seek missing information, and choose appropriate actions. We introduce \underline{T}esting \underline{A}gents' \underline{N}avigation of \underline{G}enuine, \underline{L}atent, and \underline{E}ntangled Memory Conflicts (\textsc{TANGLE}), a benchmark for genuinely unresolvable memory conflicts. It comprises 541 instances across 40 personas and three types: Context-Partitioned Conflict (CPC), Behavior-Oscillation Conflict (BOC), and Source-Contradiction Conflict (SCC). We evaluate two tracks---an oracle track with curated memory and a pipeline track that extracts memory from multi-session dialogues---on five dimensions: conflict perception, causal reasoning, confidence calibration, clarification seeking, and memory faithfulness. Experiments reveal pipeline challenges. With curated memory, models recognize conflicts more reliably than they calibrate actions or seek targeted clarification. With end-to-end pipeline memory, extraction fails to preserve conflict-bearing relations needed for downstream reasoning. Policy comparisons show fixed rules are insufficient when actions must reflect conflict. These findings motivate Conflict-Aware Action Policy (CAAP), which adapts actions to each conflict using available evidence. \textsc{TANGLE} frames conflict handling as recognizing underdetermination, retaining conflicting evidence, and acting without forcing a definitive answer.

---


### 55. [CForce: Boosting Parallel Decoding for dLLMs via Consistency Forcing](https://arxiv.org/abs/2608.13925)

**<font color=#1a73e8>作者：</font>** Yuji Ren, Chenkai Xu, Zhuocheng Gong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion large language models (dLLMs) accelerate language generation by predicting multiple masks in a single forward pass. However, existing dLLMs can suffer from unreliable predictions in early denoising stages under aggressive parallelism strategies, leading to errors that can propagate to later stages. To tackle this issue, we present Consistency Forcing (CForce) for dLLMs, a distillation method to force the mask predictions of early stages to align with those of later stages. CForce trains the model on pre-collected self-rollout trajectories, thereby improving training-inference alignment. We introduce Confidence Adaptive KL Divergence as a distillation objective to conjoin the merits of forward and reverse KL. We further provide a theoretical analysis for the consistency objective to explain why CForce can approximately minimize the prediction error of early stages. Critically, the same formulation applies to both mask-to-token decoding and edit-capable decoding; in the edit-capable case, later token-to-token refinements provide additional supervision for earlier masked-state predictions. Experiments on non-edit and edit-capable LLaDA models show improved speed-quality trade-offs, especially under high-parallelism decoding budgets. Code is available at: this https URL.

---


### 56. [Never the Number: Structural Abstention for AI Systems Whose Answers Are Consumed as Fact](https://arxiv.org/abs/2608.13926)

**<font color=#1a73e8>作者：</font>** Zhelun  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models have made natural language interfaces to databases (NLIDB) newly credible, but LLM text-to-SQL systems fail in a way that matters for deployment: a hallucinated column or a mis-aggregated total yields a fluent wrong answer, indistinguishable at the point of use from a right one. Where the consumer cannot inspect the generated query, as in enterprise AI deployments and operational dashboards, and increasingly where the consumer is a tool-using agent rather than a person, accuracy alone is insufficient: nothing marks which answers to distrust. This is a reliability problem before it is an accuracy problem.
We propose an architectural pattern for such systems, a trusted kernel with a generative shell, resting on one invariant: a component that can fabricate may influence which question the system answers, never which value it returns. A generative shell interprets underspecified input and phrases replies; a deterministic kernel matches fully specified questions against a bounded set of answerable question shapes and compiles them to queries by deterministic execution. The two meet at a confirmation the user reads before any value is computed, and requests the kernel cannot express are declined rather than approximated. We call this structural abstention, and distinguish it from the statistical abstention of selective prediction and calibrated confidence: refusal here needs no confidence estimate, because unanswerable requests are unrepresentable.
We specify the pattern implementation-independently, give a five-decision recipe and work it across three domains, extend the invariant from returned values to the actions of agentic systems, and report a two-year production case study alongside two generative alternatives, a fine-tuned parser and a tool-retrieval agent. We close against enterprise and reliability benchmarks published since.

---


### 57. [CoSA: Context-Aware Severity Assessment via Context Analysis with Large Language Models](https://arxiv.org/abs/2608.13928)

**<font color=#1a73e8>作者：</font>** Jinfeng Jiang, Yikun Li, Chengran Yang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Accurate vulnerability severity assessment is essential for prioritizing remediation, yet manually assessing Common Vulnerability Scoring System (CVSS) base metrics remains labor-intensive. Existing automated approaches often fail to capture the repository-level evidence required for assessing many CVSS base metrics. Such repository-aware assessment is challenging because relevant evidence is scattered across the entire repository under heavy noise.
To address these challenges, we present CoSA, a Context-aware vulnerability Severity Assessment approach that infers CVSS base metrics from repository artifacts. CoSA constructs a code property graph (CPG) and applies a two-stage repository-pruning strategy: lightweight static pruning to preserve structurally proximal context, followed by an agentic large language model (LLM)-guided pruning step to retain CVSS-relevant context while collecting supporting evidence. The LLM then consolidates the retrieved repository context into compact, CVSS metric-wise textual summaries, which are fed into a lightweight transformer predictor. We also construct a higher-quality repository-level dataset comprising 6,816 CVSS labeled instances spanning 90 Common Weakness Enumeration (CWE) types.
Experiments on real-world vulnerabilities show that CoSA consistently outperforms function-level and pure-LLM baselines. It improves prediction accuracy by 14.4% and Macro-F1 by 15.3% over the best-performing baseline, suggesting that explicit, metric-oriented repository context retrieval is crucial for practical and reliable automated severity assessment.

---


### 58. [Extracting and Verifying Illicit Bitcoin Addresses from Underground Forum Discussions](https://arxiv.org/abs/2608.13930)

**<font color=#1a73e8>作者：</font>** Abdoul Nasser Hassane Amadou, Arnaud Legout, Imane Fouad 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Existing labeled Bitcoin datasets are largely derived from community-reported abuse, blockchain heuristics, incident-specific collections, or proprietary labeling processes. Their construction methods are rarely publicly reproducible and often provide limited evidence that an address was directly involved in illicit activity. We present a reproducible pipeline for constructing evidence-backed Bitcoin labels from HackForums, an underground cybercrime forum with fifteen years of archived activity. The pipeline combines LLM-assisted screening, expert review, and on-chain validation to identify Bitcoin addresses explicitly associated with illicit transactions discussed on the forum. Each released label is supported by contextual evidence from underground discussions and validated on-chain. The resulting dataset contains 2,438 manually verified illicit Bitcoin addresses spanning 2010-2024 and twelve cybercrime categories assigned during LLM screening. We release the dataset, temporal metadata, and the complete extraction pipeline to support reproducible research on cryptocurrency-facilitated cybercrime.

---


### 59. [AI Research Preference Models](https://arxiv.org/abs/2608.13940)

**<font color=#1a73e8>作者：</font>** Thomas Simon Foster, Bassel Al Omari, Tingchen Fu 等 33 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI research agents (AIRA) can now propose, implement, and evaluate their own machine learning experiments, but progress on frontier tasks is throttled by cost: a candidate solution can be written in minutes, whereas evaluating it can take hours to days of GPU time. An agent can therefore propose far more candidates than it can afford to run, and its progress depends on its research preference: how it allocates a fixed execution budget across many candidates. We introduce AI Research Preference Models (RPMs) that predict which of multiple candidate solutions are most worth executing, without paying the cost of executing them all. We build RPMs from frozen pretrained language models (with no task-specific training), in two forms: an inference-only model that reasons over candidate plans, code, and prior executed solutions, and an agentic model that additionally runs small-scale pilot experiments before deciding. We integrate both into the AIRA-dojo search agent and evaluate on AIRS-Bench, a recent benchmark of machine learning research tasks for AI research agents. The two variants raise the average normalized score from 0.684 to 0.711 and 0.729 respectively, and reach the unguided agent's 24-hour performance in roughly 15 hours, using less than two-thirds of its execution budget. Our best RPMs also yield new state-of-the-art results on two AIRS-Bench tasks.

---


### 60. [Musical Mirrors: The LLM as Sounding Board in Songwriting](https://arxiv.org/abs/2608.13944)

**<font color=#1a73e8>作者：</font>** Xiao Xiao  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This paper examines a use of AI in creative practice as an interpretive sounding board for human-generated material, rather than the more familiar pattern of AI generation followed by human curation. Through the lens of resonance as theorized by Hartmut Rosa, I present a first-person case study of songwriting from July 2025 to March 2026, drawing on 16 original pieces in English, French, and other languages along with piano solos. I describe a configuration in which resonance is not located between user and model, but in the author's deepening contact with their own material, mediated through the model. This kind of resonance was supported rather than inhibited by AI when sounding-board behavior was cultivated through sustained calibration by the user. Two failure modes appeared when calibration was absent: sycophantic drift and magical overinterpretation. This account suggests both the potential and the risks of AI as an interpretive partner in creative practice.

---


### 61. [Scaling Creative Writing Beyond Story-Centric Data with Attribute-Guided Genre Expansion](https://arxiv.org/abs/2608.13947)

**<font color=#1a73e8>作者：</font>** Hwan Chang, Yongil Kim, Heuiyeen Yeen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> High-quality creative writing data for large language models (LLMs) remains dominated by story-centric data, limiting models' ability to follow the structural and functional conventions of diverse creative formats. We propose an attribute-guided genre expansion framework for scaling creative writing data beyond story generation. By separating thematic breadth from genre-form control, our framework leverages human-authored story prompts as diverse creative seeds, while utilizing manually curated genre attributes to enforce distinct structural, stylistic, and formatting conventions. We combine these to prompt strong LLMs for genre-faithful query-response pairs, which are then quality-filtered. Applying this framework, we construct the Multi-Genre Collection, a 50K-example corpus spanning 13 creative genres, including story, rap, lyrics, scripts, game design, character design, and other creative formats. Experiments across out-of-distribution writing benchmarks and held-out genre diagnostics demonstrate that models fine-tuned on our data consistently surpass not only base models and writing-specialized baselines, but also models trained on existing writing corpora. Genre-count ablations further indicate that controlled genre expansion, rather than story-centric scaling alone, is a key driver of robust creative writing capability.

---


### 62. [Implementing Computational Law in Wolfram Language for the Governance of Artificial Intelligence](https://arxiv.org/abs/2608.13958)

**<font color=#1a73e8>作者：</font>** James K. Wiles  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> How do we govern AI systems whose reasoning we cannot fully inspect? Governance does not require understanding a system's reasoning. It requires stating what the system is obliged, permitted, and forbidden to do, and checking whether it complied. I present an implementation of Reified Input/Output Logic, the formalism behind the DAPRECO knowledge base, in Wolfram Language: the core I/O axioms, obligations, permissions, constitutive norms, reified eventualities, and temporal operators. I then test whether GPT-4 can translate English legal statements into the formalism, and report the failures: hallucinated functions, omitted temporal scope, deviation from the formalism, and (in the worst cases) code that runs, reads plausibly, but silently encodes the wrong norm. A case study, an AI guard dog operating under a computational contract, shows how formalized rules can extend from a contract directly into the operational code of an embodied agent, producing symbolic, auditable justifications for its behaviour. I argue that computational law can be used as a governance tool and that a desirable goal would be to formalize the law that can and ought to be programmatically executable.

---


### 63. [QUASAR: Lowering the Loss Floor of Quantization-Aware Training with Loss-Aware Reconstruction](https://arxiv.org/abs/2608.13966)

**<font color=#1a73e8>作者：</font>** Vincent Counathe, Ben Athiwaratkun, Christopher De Sa 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As large language model inference shifts toward lower precision, post-training quantization (PTQ) becomes increasingly brittle, making quantization-aware training (QAT) essential for preserving model quality. However, QAT computes the loss and surrogate gradients using a lossy reconstruction of latent full-precision weights, while applying updates to the latent weights themselves. This mismatch can lead to suboptimal training trajectories and a higher loss floor. Second-order PTQ methods mitigate a similar gap by minimizing loss-aware reconstruction error, but doing it once for a frozen model can take hours; repeating this process throughout QAT as the weights evolve is impractical. We introduce QUASAR, a QAT method that continuously performs lightweight, loss-aware reconstruction in the training loop to lower the loss floor and improve the resulting low-bit model. At each training step, QUASAR uses the exponential moving average of squared gradients as online saliency estimates, searches over a small set of clipping ranges, and fits affine dequantizers via saliency-weighted least squares. Our analysis shows that the loss-aware reconstruction error is the only reconstruction-dependent term in the QAT convergence bound and controls the loss of the final quantized model, establishing QUASAR's objective as a principled optimization target. QUASAR modifies only the training procedure and supports standard deployment formats, including integer quantization and NVFP4, with no inference-time changes or overhead. Across Qwen3 and Llama-3.1, QUASAR achieves the lowest held-out KL divergence among competitive QAT methods at 2, 3, and 4 bits, reducing KL by at least 10% at 3 and 4 bits and by 29% at 2 bits. At 2 bits, it improves average accuracy across eight tasks by 3.5-4.3 percentage points over strong QAT and PTQ baselines.

---


### 64. [PPOM: Marginalizing Patch-Grid Phase for CLIP-Based Generalizable Vision-Language Prompt Tuning](https://arxiv.org/abs/2608.13969)

**<font color=#1a73e8>作者：</font>** Liang Wang, Haoyang Li, Chao Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Prompt tuning adapts CLIP-based vision-language models with few trainable parameters, yet its predictions remain sensitive to the spatial sampling imposed by a frozen vision transformer. In particular, non-overlapping patch tokenization makes predictions depend on the alignment (phase) between image and the patch lattice. To reduce prediction sensitivity to patch-grid alignment, we introduce Patch-Phase Orbit Marginalization (PPOM), a training-free inference operator that treats phase shift as a nuisance variable. Given a patch stride, PPOM evaluates the identity view and reflection-padded translations, pairs opposite shifts into horizontal, vertical, and diagonal antithetic families, and assigns equal mass to these families and the identity prediction to avoid view-count bias during phase integration. In summary, PPOM provides a deterministic interface between prompt adaptation and patch-grid sensitivity. Across multiple prompt-learning hosts, PPOM improves host performance without re-training.

---


### 65. [ProFocus: Interpreting Affective Experience in Artistic Images with Progressive Visual Focusing](https://arxiv.org/abs/2608.13974)

**<font color=#1a73e8>作者：</font>** Zhiyan Zhang, Zicheng Yan, Jianqi Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Interpreting the emotional responses triggered by images is central to achieving emotional intelligence. Compared with natural images, visual art is intentionally created to elicit emotional responses from its viewers through abstract concepts and visual metaphors, making affective interpretation particularly challenging. However, most existing methods rely on general-purpose visual embeddings (e.g., CLIP), failing to capture the nuanced cues underlying artistic emotion. To address this gap, we propose \textbf{ProFocus}, a novel framework that models affective experience in artistic images via progressive visual focusing. The key idea is to model visual representation learning inspired by a hierarchical cognitive theory of human aesthetic appreciation. Technically, ProFocus contains two core components: a Hierarchical Art Critic (HAC) and a Progressive Hint Fusion (PHF) module. HAC leverages multimodal large language models to generate structured linguistic priors at three cognitive levels--atmospheric style, narrative subjects, and concrete details--thereby translating artistic perception into coherent semantic guidance. Building upon these priors, PHF departs from conventional cross-modal fusion by sequentially injecting the hierarchical hints into visual features, enabling a progressive focusing process that mirrors human perception. This design allows the model to capture subtle affective cues and produce more faithful explanations. Extensive experiments on the ArtEmis v1.0 and v2.0 datasets demonstrate that ProFocus consistently outperforms state-of-the-art methods in both emotion recognition and affective explanation. Project page: this https URL.

---


### 66. [FIRM: Fine-Grained Intra-Token Representation of Masks for Remote Sensing Reasoning Segmentation](https://arxiv.org/abs/2608.13980)

**<font color=#1a73e8>作者：</font>** Weidong Tang, Kaiyu Li, Yikai Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reasoning segmentation requires multimodal large language models (MLLMs) to translate implicit instructions into precise pixel-level masks. MLLMs encode an image as visual tokens, each of which merges a group of image patches. In remote sensing images, small targets, thin structures, and adjacent instances can occupy different parts of the same visual token. Assigning a single binary mask label to such a token loses its internal spatial structure, causing nearby targets to merge and object boundaries to become coarse. To bridge this representational gap, we introduce FIRM, a Fine-grained Intra-token Representation of Masks. For each visual token, FIRM predicts a mask code that specifies an $r\times r$ binary sub-cell pattern rather than a single foreground/background label. Given a target identified by the MLLM, the complete grid of mask codes is predicted in one mask pass. Fixed lookup converts the predicted codes into a discrete sub-cell mask, while marginalizing the code distribution yields a soft structural field. To further recover fine-grained boundaries within each sub-cell, we introduce a lightweight continuous renderer that refines this field using pre-merge visual features and image details. Across five reasoning and referring segmentation benchmarks on satellite and UAV images, FIRM achieves leading results, including $70.5/80.5$ gIoU/cIoU on LaSeRS and a $3.0$-point average gain on EarthReason. These results demonstrate the value of explicitly representing intra-token mask patterns for fine-grained MLLM segmentation.

---


### 67. [Batch-wise Adaptive Pruning: Periodic Neuron Activation-Aware Weight Pruning for Language Reasoning Model](https://arxiv.org/abs/2608.14003)

**<font color=#1a73e8>作者：</font>** Yongmin Kim, Shota Takashiro, Yusuke Iwasawa 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Reasoning Models (LRMs) achieve strong performance on complex tasks through extended chain-of-thought generation, but incur substantial computational costs during inference. In production settings, batched inference is essential for high throughput, yet the existing training-free adaptive pruning methods we evaluate severely degrade in this regime. Because a batch must share a single pruning mask, these methods aggregate activations across samples and then apply threshold-based selection; the threshold, calibrated offline on unaggregated activations, no longer matches the aggregated distribution, so the realized sparsity ratio drifts and accuracy on reasoning tasks collapses under batched inference.
In this work, we propose a training-free adaptive pruning method designed specifically for batched inference in LRMs, built on two components. First, we replace threshold-based selection with periodic top-k selection over the aggregated importance scores, which is unaffected by the shift that aggregation induces in the activation distribution, and which runs selection once per update period rather than at every token, preserving the speedup. Second, based on the observation that important neurons re-fire periodically during long reasoning generation, we introduce an activation memory that accumulates importance across update phases so that recurring neurons are retained.
Experiments on diverse reasoning benchmarks demonstrate that our method outperforms the previous state-of-the-art adaptive pruning method by 39.7 percentage points in average accuracy at batch size 4 with 50% target sparsity on DeepSeek-R1-Distill-Qwen-7B, and reaches 1.40x speedup over dense inference at 50% actual sparsity.

---


### 68. [Identifiability and Order-Dimension Limits of In-Context Learning on Partial Orders](https://arxiv.org/abs/2608.14004)

**<font color=#1a73e8>作者：</font>** Faizanuddin Ansari, Debanjan Dutta, Swagatam Das  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In-context learning is commonly formalized as inference from examples of a function. Partial orders instead combine transitivity, antisymmetry, and incomparability, so a finite prompt may not determine a queried comparison. We develop a theory of in-context learning on partial orders that separates logical identifiability, prompt teaching cost, structural complexity, and the exact capacity of a formal coordinate-decoder class. A version-space semantics makes background knowledge and open- versus closed-world assumptions explicit. For finite open-world prompts with positive and negative comparisons, we prove an exact completion trichotomy: after taking the reflexive transitive closure of the positive demonstrations, a query is forced true, forced false because every true completion creates a cycle or violates a negative demonstration, or remains genuinely ambiguous. For a known $n$-element universe, we characterize the open-world teaching number as the number of covers plus a blocker-set hitting number, prove that its maximum over all $n$-element posets is $n(n-1)$ and is uniquely attained by the antichain, and identify the blocker term as the exact cost of open-world rather than complete-Hasse semantics. We formalize prompt-dependent $s$-coordinate decoders and use the classical coordinate-order equivalence to obtain an exact representation boundary: dimension at most $s$ is necessary and sufficient, while width at most $s$ is a convenient sufficient condition.

---


### 69. [Buy the Rumor, Sell the News: When Is News Priced In?](https://arxiv.org/abs/2608.14014)

**<font color=#1a73e8>作者：</font>** Alireza Kargarzadeh, Nariman Khaledian, Navid Parvini 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Two old market sayings hold that news is already priced in by the time it is published, and that the rumor is bought while the news is sold. Both place the price move associated with a piece of news before and at publication rather than after it. Whether the claims hold, for which kinds of news, and by how much are basic questions about how fast markets absorb public information. We test them on 4.57 million financial news articles covering roughly 3,000 US stocks (2023-2026). A large language model teacher, distilled into a compact classifier through active learning, assigns each article one of 17 event tags and five attributes; articles are clustered into stories to separate first reports from follow-up coverage; and beta-adjusted abnormal returns are measured around the resulting 1.68 million stock-day events, with 364,405 neutral-sentiment events as a placebo group. Three results follow. First, the price move associated with news concentrates before and at publication: pooled across all signed events, the cumulative move in the news direction by the close of publication day is 2.8 times its value 20 days later, and for rumor-flagged events the rumor day captures the entire move while the subsequent confirmation contributes nothing. Second, measured against the placebo of comparable stocks, markets underreact to numbers and overreact to stories: quantified fundamental news (earnings, dividends, guidance, analyst actions) keeps drifting in the direction of the news for weeks, while soft story-driven news (launches, macro commentary, leadership) gives back its move. Third, news carries width as well as direction: publicity raises volatility before the publication day, and volatility declines once the news is out, because publication resolves uncertainty. The study also produces a table of measured drift for each event tag, usable as a prior in news-conditioned forecasting models.

---


### 70. [Content Based Video Narration of Gameplay with Vision Language Models](https://arxiv.org/abs/2608.14016)

**<font color=#1a73e8>作者：</font>** Mathew Varghese  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Live game commentary is scarce: it exists for professional esports broadcasts and almost nowhere else. We present a content-based video narration system that produces spoken, esports-style commentary for arbitrary gameplay recordings using a general-purpose vision-language model (VLM) and a text-to-speech back end, with no game-specific instrumentation, no engine telemetry, and no task-specific training. Three mechanisms carry the system. Temporal mosaic packing arranges nine uniformly sampled frames into a single 3x3 image, letting an image-native VLM reason about motion while consuming one image payload per segment instead of nine. Context-conditioned prompting replays the K most recent narrations as assistant-role history, suppressing the repetition that dominates per-segment captioning of static scenes. Duration-conditioned generation and elastic alignment constrain narration length in the prompt, then time-scale or symmetrically pad the synthesized audio so each utterance fills its segment slot exactly, giving frame-accurate muxing without a forced aligner. The implementation supports either cloud TTS or a 6-bit quantized 4B-parameter on-device TTS model on Apple silicon, making the speech stage fully local. We report a qualitative case study on real-time strategy footage, a cost model showing the mosaic reduces per-minute image payloads by 9x, and a candid account of observed failure modes - hallucinated game state, resolution loss from mosaicking, and prosody artifacts from time-scaling. We release the system as a reproducible baseline, with an evaluation protocol for the quantitative study a full version will report.

---


### 71. [SSP: An Event-Matched Syn2Sim2Phy Cross-Domain Evaluation Framework for Autonomous Driving VLA Models](https://arxiv.org/abs/2608.14024)

**<font color=#1a73e8>作者：</font>** Haojie Feng, Peizhi Zhang, Xinrui Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language-action (VLA) models for autonomous driving jointly produce scene interpretation, language-based reasoning, and driving trajectories. Existing evaluations often use independently selected synthetic, simulated, and physical data, so measured performance gaps can be confounded by changes in scenario content rather than genuine domain sensitivity. We propose SSP (Synthetic-Simulation-Physical), an event-matched Syn2Sim2Phy evaluation framework that anchors cross-domain comparison to the same safety-critical interaction. Starting from a synthetic long-tail video, SSP builds a validated event specification that preserves road topology, participant roles, relative motion, conflict evolution, passing order, response constraints, and event phases. Platform-specific realizations are then constructed in CARLA and on a closed proving ground and are evaluated only after transfer audits confirm preservation of mandatory event properties. SSP maps heterogeneous outputs from OpenEMMA, LLaViDA, and Alpamayo-R1 into common semantic slots and a 1 s trajectory window to assess output validity, semantic accuracy, critical-interaction recognition, trajectory quality, and risk response. Across Cut-in and vulnerable-road-user crossing cases, the macro-averaged Integrated VLA Capability Scores are 0.259, 0.291, and 0.325 in the Synthetic, Simulation, and Physical domains, respectively, while the best domain varies by scenario. Alpamayo-R1, OpenEMMA, and LLaViDA obtain scores of 0.405, 0.338, and 0.131. SSP provides a reproducible scene-transfer chain and an evidence-qualified evaluation of VLA behavior without assuming that the Physical domain is universally superior.

---


### 72. [Agent-Orchestration in Autonomous Chip Design](https://arxiv.org/abs/2608.14035)

**<font color=#1a73e8>作者：</font>** Linyang Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent developments in large language models (LLMs) and tool-using agents encourage people to explore the potential of using agents in chip design. The core question is what kind of AI we really need in such a sophisticated industry.
To this end, we bring the idea of modeling a chip-design superintelligence as an enormous \textit{AI-organization}.

---


### 73. [Demystifying Agent Skills: Why They Work-Until They Don't](https://arxiv.org/abs/2608.14036)

**<font color=#1a73e8>作者：</font>** Zhiyuan Jiang, Fangrui Huang, Hanwen Xing 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Skills have emerged as a practical and effective approach for enhancing LLM agents at inference time through structured packages of knowledge. However, existing evaluations largely measure whether skills improve aggregated task success, leaving a more fundamental question underexplored: \emph{\textbf{When do skills help, why do they work, and where do they fail?}} Through controlled experiments across various benchmarks, agent harnesses and LLMs, we isolate the effects of representation, outcome annotation, retrieval difficulty, and cross-framework robustness of skills. To further answer this question, we design a contrastive study that combines controlled quantitative experiments with paired trajectory analysis. We normalize 8,135 trial records from controlled experiments and retain 238 valid unique labels from 240 open-coded records. We consolidate these observations into a taxonomy of three high-level categories and twelve skill-use modes: skills work when noisy trajectories become procedural anchors that stabilize execution. Skills improve over Workflow Memory by 6.06 points in matched comparisons. Procedural anchoring accounts for 65.7\% of skill cases, versus 4.5\% for explicit knowledge injection, showing that skills stabilize action rather than inject missing facts. Retrieval is a separate bottleneck: as pools grow from 5 to 100, actual-use precision falls from 29.6\% to 3.3\%. Confusable distractors impair offline identification, yet downstream success remains stable; exact ground-truth invocation is neither sufficient nor necessary. Skills fail under brittle assumptions, incompatible contexts, or insufficient adaptation. These findings move evaluation beyond aggregate success rates and guide reliable self-evolving agents.

---


### 74. [Beyond Text Conditioning: A Systematic Study of MLLM-DiT Fusion for Video Generation](https://arxiv.org/abs/2608.14043)

**<font color=#1a73e8>作者：</font>** Yanbo Ding, Yijia Fan, Caihua Shan 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion Transformers (DiTs) have become the dominant paradigm for high-fidelity video generation, yet their ability to perform high-level semantic planning remains limited. While hybrid architectures integrating MLLMs with diffusion backbones have shown strong advantages in image synthesis, such designs remain underexplored in video generation, where existing approaches often treat MLLMs primarily as frozen feature encoders rather than semantic generators. To fill this gap, we systematically study how an MLLM should be integrated with a DiT for video generation by answering three questions: what intermediate representation should bridge the MLLM and DiT, how the MLLM should generate it, and how the DiT should incorporate it during diffusion rendering. Our analysis reveals three key findings: (1) discrete semantic visual tokens produced by an EMA-based tokenizer provide a stable and expressive interface, (2) autoregressive causal modeling is effective for generating these tokens, and (3) explicit visual-token conditioning is more effective than prompt refinement or latent bridging. Based on these findings, we propose BiVidGen, a hybrid framework where an MLLM first generates semantic visual tokens and a DiT renders videos conditioned on both text and these tokens via multi-layer cross-attention. Extensive experiments show that BiVidGen improves semantic alignment and temporal coherence over a fine-tuned DiT baseline, achieving stronger performance on VBench-Long. These results demonstrate that explicit MLLM-based visual planning provides an effective intermediate interface for text-to-video generation beyond text-only conditioning.

---


### 75. [Model-agnostic Retrieval-Augmented Extended Forecasting for time series](https://arxiv.org/abs/2608.14054)

**<font color=#1a73e8>作者：</font>** Juan Pablo Villa Serna, Rohan Asthana, Vasileios Belagiannis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time series forecasting with pretrained foundation models has demonstrated strong zero-shot capabilities. However, achieving optimal performance on time series with short or negligible historical data in domain-specific applications typically requires adaptation via either fine-tuning or RAG. While fine-tuning is effective, it incurs substantial computational costs. This work explores RAG within univariate time series (Retrieval Augmented Generation) as a more efficient alternative, in particular RAF (Retrieval Augmented Forecasting), and introduces RAEF (Retrieval-Augmented Extended Forecasting), a model-agnostic method built upon RAF. RAEF incorporates key refinements to the retrieval and aggregation mechanisms: (1) direct retrieval in input-space rather than embedding-space, reducing inference overhead, and (2) concatenation-based aggregation that preserves temporal structure instead of averaging. Empirical evaluation across multiple benchmark datasets demonstrates that RAEF outperforms RAF in both accuracy and inference overhead. Furthermore, comprehensive comparisons with zero-shot and fine-tuned foundation models show that RAEF achieves competitive or superior performance to fine-tuning while avoiding its computational burden, establishing it as a practical and scalable approach for domain adaptation in time series forecasting.

---


### 76. [HERMES: a multi-agent framework for structured knowledge extraction from ultra-long documents in geoscience](https://arxiv.org/abs/2608.14055)

**<font color=#1a73e8>作者：</font>** Ziqi Song, Zongyuan Xiang, James G. Ogg 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Authoritative scientific knowledge in geoscience remains largely trapped in legacy monographs and historical literature, where unstructured text and complex layouts hinder computational access. We introduce HERMES, a scalable multi-agent framework that extracts structured data from ultra-long scientific documents. Using a coordinating large language model, HERMES integrates domain constraints, validation rules and evidence tracing within a unified document-level extraction process that incorporates parsed text, tables, figures and captions. Applied to the 55-volume Treatise on Invertebrate Paleontology, the system produced a structured database of 32,277 fossil taxonomic entities and 451,878 attributes, released online at this https URL. Extraction performance remained stable across fossil groups (average F1 scores of approximately 0.90 for entities and 0.91 for attributes), improving per-volume efficiency approximately sixfold relative to the tested fully manual baseline. Evaluation in palaeomagnetism and geochemistry, conducted without additional model training, demonstrated transfer across distinct geoscience domains. This work provides a practical pathway to transform historical scientific literature into FAIR-oriented structured data, offering a sustainable infrastructure for data-intensive disciplines and large-scale knowledge integration.

---


### 77. [InstructVVT: Instruction-Driven Video Virtual Try-On without Auxiliary Spatial Priors](https://arxiv.org/abs/2608.14070)

**<font color=#1a73e8>作者：</font>** Dingbao Shao, Song Wu, Xinyu Chen 等 21 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video virtual try-on is a highly constrained editing task requiring the precise replacement of a target person's clothing while strictly preserving the original video's spatial structure and temporal dynamics. Existing methods heavily rely on auxiliary handcrafted spatial priors (e.g., masks, poses) for editing control. However, these priors are prone to failure in unconstrained real-world videos and often compress rich visual context into incomplete structural signals. Furthermore, standard reconstruction objectives fail to fully capture try-on-specific human preferences. To address these challenges, we propose InstructVVT, an instruction-driven and reference-guided video virtual try-on framework based on a Diffusion Transformer (DiT) that operates without inference-time spatial priors. Our core insight is to recover fine-grained control directly from the input triplet (source video, reference garment, and instruction) via a dual-level reference conditioning scheme. Specifically, an MLLM infers semantic edit tokens for target disambiguation and structural preservation, while a lightweight conditioning pathway explicitly injects fine-grained visual garment details. Finally, we design a try-on-specific reward and utilize the DiffusionNFT algorithm to align the model with human preferences. Extensive experiments on ViViD-S and TripVVT-Bench demonstrate that InstructVVT outperforms state-of-the-art open-source methods in garment fidelity, structural preservation, and temporal consistency, despite requiring fewer inference-time controls.

---


### 78. [Scaling Domain Data Repetition in LLM Pretraining](https://arxiv.org/abs/2608.14071)

**<font color=#1a73e8>作者：</font>** Jingwei Li, Xinran Gu, Rui Dai 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As large language models scale, their training-token budgets must also increase to maintain an appropriate tokens-per-parameter ratio (\(\mathrm{TPP}\)). However, high-quality domain data is much harder to scale than general web data. As model size and the training-token budget increase, its fraction in the training mixture tends to decrease. Repeating the available high-quality data provides an effective way to counteract this dilution, but excessive repetition may lead to overfitting. We study this trade-off under practical LLM scaling, where the training-token budget grows proportionally with model size. For a fixed domain, we first find that, surprisingly at a fixed \(\mathrm{TPP}\), the optimal repetition count mildly increases with model size. Across different domains, we find that the optimal repetition count is strongly negatively correlated with the final validation loss of a domain: domains with lower loss can generally benefit from more repetitions. In contrast, the amount of unique domain data is only weakly related to the optimal repetition count. These findings suggest that repetition counts tuned on smaller proxy models with the same \(\mathrm{TPP}\) can provide a practical estimate for larger models.

---


### 79. [Regime-Conditional Verification: Correctness Estimation for Adapting and Monitoring Safety Classifiers](https://arxiv.org/abs/2608.14089)

**<font color=#1a73e8>作者：</font>** Thiago Sandoval, Ufuk Topcu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Safety classifiers deployed with large language models often fail for two reasons: their decisions reflect the policy learned during training rather than the deployer's desired policy, and their performance degrades as deployment traffic evolves. We present Regime-Conditional Verification (RCV), a lightweight wrapper that adapts an off-the-shelf safety classifier without retraining it. RCV estimates, from the classifier's internal representations, the probability that each prediction disagrees with the deployer's policy, and selectively corrects predictions likely to be wrong. The same correctness estimates also provide a label-free signal for detecting distribution shift, enabling a maintenance loop that updates the correctness estimation layer and resorts to classifier fine-tuning only when necessary. Across three off-the-shelf safety classifiers and two benchmark datasets, RCV improves adherence to the deployer's policy in every classifier-dataset combination, catching up to 0.81 of previously missed unsafe content without modifying the underlying classifier. In a deployment study with ten attack campaigns, each a harm category held out of RCV's training, RCV detects every campaign in a dedicated injection panel; in the maintenance census most drift episodes are repaired without updating the classifier, and the fine-tune is reserved for the residual episodes that repair does not restore.

---


### 80. [AppLooper: An Agentic Application Engineering Loop for Accountable Release with Virtual-User Feedback](https://arxiv.org/abs/2608.14093)

**<font color=#1a73e8>作者：</font>** Zihong He, Chen Liang, Hai-Ning Liang  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Much existing research on coding agents organizes application development as an iterative loop of requirement interpretation, implementation, tool execution, evaluation, and repair. As these loops run longer, requirements may drift; users may lose awareness of the current state and rationale for changes; and generated applications may remain insufficiently grounded in target users' contexts and needs. Application engineering therefore requires a mechanism connecting owner intent, target-user experience, development changes, and responsibility for release. We present AppLooper, a human--coding-agent--virtual-user application engineering loop for accountable release. An application owner confirms frozen requirements, supplies feedback, inspects candidates, and retains final release authority. A development agent produces and revises versioned candidates. A virtual-user agent cohort executes interface scenarios grounded in target users and contexts of use. Besides, an owner-intent simulation agent retests only requirements, constraints, and feedback explicitly confirmed by the owner, abstaining when evidence is insufficient. A testing agent performs read-only developmental checks by reproducing reported failures, running existing regression tests, and exercising the current candidate through its browser interface. The orchestration layer groups the resulting findings and routes them into development revision, targeted retesting, and owner inspection. AppLooper binds requirements, feedback sources, interface targets, development changes, retesting outcomes, owner interactions, and release decisions to specific versions. It thereby extends sustained coding-agent iteration into a traceable and reviewable lifecycle in which humans retain final responsibility for release. Source code is available at this https URL.

---


### 81. [P2Skill: Privacy Preserving Skill Distillation for Cloud-Local LLM Inference Systems](https://arxiv.org/abs/2608.14094)

**<font color=#1a73e8>作者：</font>** Myunghoon Ryu, Geunpyo Park, Sungjoon Lee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cloud-local LLM inference systems have the potential to use the reasoning capability of large cloud models while protecting sensitive user data on personal devices. Cloud-bound requests must exclude personally identifiable information (PII) to prevent external data leakage. Existing privacy-preserving methods rely on prompt perturbation, entity masking, or model fine-tuning, but these approaches may distort contextual semantics or require additional training. This paper proposes P2Skill, a prompt-based skill distillation method in which a local small language model (SLM) autonomously performs decomposition, PII-aware routing, paraphrasing, and reconstruction by following the skill prompts. Skills are iteratively refined from execution failures by a cloud LLM, enabling the local SLM to generalize beyond memorized PII patterns, and therefore P2Skill requires no privacy-specific fine-tuning or learned auxiliary detectors. Evaluation on a four-domain benchmark shows that P2Skill achieves $1.69\times$ and $3.66\times$ higher privacy-preserved inference quality than previous baselines.

---


### 82. [A Graph-Based Reinforcement Learning Framework for Structured Drift Diagnosis and Recovery in Autonomous LLM Agents](https://arxiv.org/abs/2608.14109)

**<font color=#1a73e8>作者：</font>** Ismail El Hamraoui, Sagar Jose, Nicolas Bureau 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous LLM agents are increasingly deployed in complex real-world workflows, yet they remain vulnerable to runtime behavioral drift, a silent deviation from the original task that can lead to irreversible side effects on external systems. Existing approaches address drift at the prompt level but lack structured mechanisms for step-level detection, risk assessment, and recovery decision. Because the main task-executing agent is often a large and expensive model that cannot be re-trained on every deployment, this work targets a plug-and-play recovery module instead. It introduces a graph-based framework in which a single small language model is trained via reinforcement learning to specialize at each node of a recovery graph, external to the main agent. Each node has a precise role\,: drift classification, operation detection, risk evaluation, or final decision and the model learns to produce structured XML-formatted reasoning adapted to that role. Training combines rule-based structural rewards with an LLM-as-judge semantic-quality signal, so that the model is graded both on how it answers (schema and length) and on what it says. Experiments on the public AppWorld benchmark show that the method generally exploits information about the suspected drift onset to issue correct recovery decisions using a small language model. In addition, the trained small language model reliably respects the prescribed output schema and produces semantically appropriate content in each field according to its assigned node role.

---


### 83. [Search or Chat? Comparing How We Learn About Debated Topics](https://arxiv.org/abs/2608.14113)

**<font color=#1a73e8>作者：</font>** Ran Yu, Alisa Rieger, Rabia Karatoprak Ersen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) become more integrated into everyday information platforms, chat-based systems are emerging as a popular alternative to traditional web searches, especially for informational search and informal learning tasks. Despite this shift, little is known about how different tools affect learning outcomes. Our work aims to improve the understanding of how chat-based information access supports and impacts learning performance in informal learning settings. In this paper, we present the results of a crowdsourcing user study (N = 194) that compares learning about debated topics using a traditional search interface versus an LLM-powered chat interface. Through our analysis of learning outcomes, user characteristics, and interaction patterns, we found no significant differences in user learning gain or critical reflection on our study tasks. Our observations from the analysis of further exploratory variables suggest that, in the context of longstanding debated topics, user characteristics such as their attitude strength and level of intellectual humility might be more important in shaping immediate learning outcomes than the information access tool.

---


### 84. [Act2Intention: A Benchmark For Developing Active Mobile Agents Through Inferring User Intention from GUI Actions](https://arxiv.org/abs/2608.14132)

**<font color=#1a73e8>作者：</font>** Xiaokai Yan, Jingtao Ding, Yong Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Mobile GUI Agents powered by multimodal large language models (MLLMs) show promise in human-computer intelligence. However, current research primarily focuses on reactive task execution while lacking a comprehensive understanding-prediction-execution process for user intentions, which are the core requirements of active agents. In this paper, we propose the Act2Intention framework that builds an active mobile agent by integrating understanding, predicting user intentions, and executing decisions. First, we construct the Act2Intention Bench through data collection and validated generation, comprising 72,511 intentions and over 700,000 actions across 52 apps, thereby establishing the first benchmark for evaluating proactive agents via continuous intention-action trajectories. We further develop the Act2Intention Agent, achieving proactive services through Proactive-oriented Intention Understanding, Personalized Proactive Intention Prediction, and Experience-guided Intention Execution. Experimental results show that supervised fine-tuning on Act2Intention Bench yields absolute improvements of +32.0 Acc-S, +10.25 Acc-S, and +6.9 SSR points over non-fine-tuned counterparts under the same agent framework for intention understanding, prediction, and execution, respectively. This success underscores the necessity and value of the Act2Intention Bench, which establishes a standardized platform for developing and evaluating proactive agents and consequently paves the way for research on intention-driven human-computer interaction.

---


### 85. [Self-Supervised Visual On-Policy Distillation](https://arxiv.org/abs/2608.14144)

**<font color=#1a73e8>作者：</font>** Yijiang Li, Yijun Liang, Yunjie Tian 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual on-policy distillation relies heavily on an informative teacher-student asymmetry, through either a larger, stronger teacher or privileged supervision, such as reference answers or ground-truth regions of interest. This raises a fundamental question: where can informative asymmetry come from when nothing privileged is available? We answer this by inverting where the asymmetry comes from. Rather than adding privileged information to the teacher, we subtract information from the student. This asymmetry creates the same effective learning signal for free as a teacher with access to information unavailable to the student, without ground-truth annotations, rewards, or a separate stronger teacher model. Building on this principle, we introduce Self-Supervised Visual On-Policy Distillation (S$^2$VOPD), a simple yet effective method that constructs on-policy learning signals from asymmetric augmented views. S$^2$VOPD distills the teacher's distribution conditioned on the original image on-policy into the student distribution conditioned on a strongly augmented view of the same image. We systematically explore a broad design space of visual augmentations and uncover that (1) asymmetry matters: all four augmentation families improve performance, while symmetric self-distillation degrades it; (2) strength matters: performance peaks at a moderate strength; and (3) the gap must remain task-consistent: augmentations that completely remove the question-relevant evidence can induce large but uninformative discrepancies. Across six fine-grained perception benchmarks, S$^2$VOPD improves Qwen3.5-4B from 70.7% to 77.4%, above all open-source models compared, up to Qwen3-VL at 235B, and surpasses GPT-5.4. While holding training data the same, it recovers 96% of the improvement achieved by methods with privileged information. Website is at this https URL

---


### 86. [Leading-Silence Augmentation and Multi-Stage Synthetic Supervision for the Second MLC-SLM Challenge](https://arxiv.org/abs/2608.14150)

**<font color=#1a73e8>作者：</font>** Kexin Shi, Renhe Sun, Yuge Huang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The second Multilingual Conversational Speech Language Model (MLC-SLM) Challenge evaluates two tasks over complete, unsegmented multilingual conversations: speaker diarization and recognition (Task 1) and conversational speech understanding (Task 2). Neither task provides oracle utterance boundaries or speaker labels at evaluation, and Task 2 provides no question-answer training set. For Task 1, we fine-tune VibeVoice-ASR-7B with random leading-silence cropping, consistent timestamp correction, and an exponential moving average (EMA) training strategy. For Task 2, we construct synthetic question-answer pairs through multimodal candidate generation, silent-audio filtering, and distribution-matched augmentation, and fine-tune Qwen3-Omni-30B-A3B-Instruct for tagged direct answering. On the Task 1 evaluation set, cropping reduces tcpMER from 18.30% to 17.27%, and EMA further reduces it to 16.73%. On the Task 2 evaluation set, jointly applying distribution-matched augmentation and tagged direct answering raises accuracy from 83.0% to 86.0%.

---


### 87. [Towards Efficient Multimodal and Multilingual Opinion Extraction for STI: A QLoRA-Based Fine-Tuning Approach](https://arxiv.org/abs/2608.14152)

**<font color=#1a73e8>作者：</font>** Sheng Hong, Xuanqi Wang, Jiacheng Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in large language models (LLMs) have reshaped semantic analysis. Opinion Extraction (OE) for Science and Technology Intelligence (STI) requires concise core opinions from large information streams. Off-the-shelf models struggle to filter noise from these streams and show limited structured-output reliability in zero-shot multilingual and multi-modal settings. To address information overload and extraction defocus, this study proposes a multimodal core-opinion extraction framework in which visual evidence serves as a contextual anchor for textual judgment. Using VideoLLaMA2 (VL2) and VideoLLaMA2.1 (VL2.1) as the base models, we apply Quantized Low-Rank Adaptation (QLoRA) fine-tuning on a curated dataset of 2,194 multilingual and multimodal samples. Under the selected Image-Augmented setting, fine-tuned VL2.1 generates structured JSON core-opinion outputs, achieving 64.98% Precision, 42.15% Recall, 51.14% F1-score, and 74.00% sample-level accuracy. Relative to the zero-shot VL2.1 setting, it raises the F1-scores of Spanish and Russian from 4.83% and 0.45% to 46.05% and 51.93%, respectively. The framework further incorporates a Fuzzy Cumulative Prospect Theory-based post-extraction triage module for case-level value assessment, providing a case-level value signal for downstream STI screening.

---


### 88. [BiasTrace: Linking Reasoning Behaviours to Biased Outputs in LLMs](https://arxiv.org/abs/2608.14161)

**<font color=#1a73e8>作者：</font>** Varsha Ramineni, Hossein A. Rahmani, Jerome Ramos 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLMs exhibit social biases that can produce inaccurate and discriminatory inferences, posing risks in high-stakes applications. While prior work has made progress in measuring and mitigating bias, it largely focuses on final outputs of models, with limited understanding of the mechanisms that produce biased outcomes. Recent advances in LLM reasoning offers a new lens for investigating bias, yet the link between reasoning and bias remains poorly understood. Existing approaches focus primarily on final answer correctness or explicitly biased language, overlooking different behaviours in reasoning that can drive biased outcomes. We introduce BiasTrace, an annotation scheme for labelling reasoning behaviours in model-generated traces and linking them to biased outcomes. BiasTrace captures bias-specific behaviours (e.g., unsupported demographic assumptions) as well as general reasoning patterns that may implicitly contribute to bias (e.g. overthinking). We apply BiasTrace to reasoning traces in bias-sensitive contexts, scaled using validated LLM-as-a-judge methods, producing a large annotated dataset. Our analysis shows that biased outputs often stem from subtle reasoning behaviours rather than explicitly biased language, and that reasoning-level annotations improve bias detection. We further show that BiasTrace behaviours can be exploited for inference-time mitigation. These findings underscore the importance of examining a broader range of reasoning patterns to better understand bias in LLMs.

---


### 89. [Can Language Models Understand mmWave Data? Benchmarking Large Language Models for mmWave Radar-Based Human Understanding](https://arxiv.org/abs/2608.14179)

**<font color=#1a73e8>作者：</font>** Jeongwan Shin, Jaehyeon Kim, Donguk Ko 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have shown remarkable reasoning and generative capabilities, motivating their use as universal reasoning engines for perception. While modern approaches such as vision-language models (VLMs) have attempted to incorporate reasoning capabilities into visual sensing, the integration of LLMs with the millimeter-wave (mmWave) modality-despite its unique advantages under low light and occlusion-remains largely unexplored. The principal bottlenecks stem from the scarcity of radar language pairs, severe cross-dataset heterogeneity, and the absence of a foundational mmWave encoder. We address this gap through a minimal textualization interface that serializes each mmWave point cloud into concise natural language, allowing off-the-shelf LLMs to operate in a question answering (QA) setting. Building on this, we present mmWave-QA, the first benchmark for language-conditioned mmWave human perception. mmWave-QA aggregates heterogeneous public mmWave datasets and harmonizes them via calibration-aware preprocessing and global taxonomy alignment, while providing natural language QA. Spanning six scenarios and five QA tasks, the benchmark enables standardized evaluation across diverse mmWave hardware and experimental conditions, establishing a foundation for scalable research on mmWave-LLM integration. We further evaluate and analyze LLMs on our mmWave-QA, highlighting their zero-shot reasoning potential for radar perception, as well as their robustness under visual degradation.

---


### 90. [KV Cache Compression Through the Lens of Transform Coding](https://arxiv.org/abs/2608.14191)

**<font color=#1a73e8>作者：</font>** Hannah Laus, Claudio Mayrink Verdun, Hao Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The key-value (KV) cache stores information from past tokens and is a major memory bottleneck in long-context inference. Existing quantization methods address this bottleneck by representing the KV cache uniformly with lower-precision data types and designing quantization schemes to minimize reconstruction error in the cache itself, without accounting for how that error propagates through attention mechanisms. We prove that, under a white-noise quantization model, the expected attention-aware distortion decomposes into additive key and value contributions that factor across tokens and channels. Building on transform coding and reverse water-filling, which are classical tools from signal processing and rate-distortion theory, we introduce Attention-Aware Transform Coding (AATC), which allocates bits over a calibration set to minimize attention-aware distortion. On Llama-3.1-8B-Instruct and Qwen-2.5-7B-Instruct, evaluated across LongBench, RULER, GSM8K, MMLU-Pro, and MATH-500, our method achieves near-lossless accuracy at approximately $5.8\times$ compression, whereas each baseline degrades in at least some settings.

---


### 91. [MINT: A Universal Zero-Shot Predictor for Transaction Data](https://arxiv.org/abs/2608.14198)

**<font color=#1a73e8>作者：</font>** Parameswaran Kamalaruban, Viktor Drobnyi, Maeve Madigan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Banks analyse sequential financial transaction data to perform many tasks, including fraud prevention, credit risk assessment and offer personalization. To improve the predictive accuracy of these tasks, Payments Foundation Models encode transaction sequence data as rich contextual embeddings, which can then be provided to task-specific models as features. However, these Foundation Models are not designed for flexible zero-shot reasoning across novel downstream prediction tasks, limiting their adaptability and utility. Existing LLM-based approaches to zero-shot prediction often fail to fully exploit the predictive signal within transaction data, while relying on costly text serialization or task-specific architectures that scale poorly. To address these limitations, we present the Multimodal Instruction Network for Transactions (MINT), a framework that connects a pretrained transaction sequence encoder to a decoder-only LLM through lightweight embedding injection, transaction-language alignment, and instruction tuning. We find that MINT achieves state-of-the-art predictive question-answering performance in both in-distribution and out-of-distribution questions, while substantially reducing input tokens, latency, and memory consumption compared to text-serialization baselines. Through comprehensive analyses of representations, alignment strategies, training data, and history length, we establish that compact transaction embeddings are a superior approach to transaction representation than text serialization for multimodal reasoning and zero-shot prediction tasks.

---


### 92. [FreeBalance: Pre-Routing Online Moe Load Balancing via Residual Workload Prediction](https://arxiv.org/abs/2608.14205)

**<font color=#1a73e8>作者：</font>** Pengfei Chen, Yize Wu, Shouxu Kuang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Load imbalance poses a major bottleneck to the efficiency of expert parallelism in distributed inference of Mixture-of-Experts (MoE) models. The most heavily loaded rank stalls global execution due to skewed routing distributions, directly increasing latency. While offline expert placement can alleviate persistent imbalance, practical multi-task serving workloads exhibit layer- and batch-dependent routing dynamics, making online load balancing indispensable. Existing approaches rely on routing statistics collected after each MoE router, requiring expert weight load or migration to begin only after routing decisions are available, consequently placing migration overhead on the inference critical path. In this work, we observe that online balancing can instead be largely overlapped with computation before target routing (e.g., attention), if routing distributions can be predicted accurately in advance. Therefore, we propose FreeBalance, a lossless online load-balancing framework that overlaps expert migration with preceding computation stages via residual workload prediction. FreeBalance leverages cross-layer similarities in hidden representations within the residual network to build a lightweight workload predictor. This enables proactive expert migration planning before routing decisions are available, creating substantial overlap between weight transfer and computation-heavy pre-routing stages. Furthermore, a cost model constrains the number of swaps to fully hide the synchronization overhead within the available window. Experiments across models and datasets show that FreeBalance reduces the max-to-mean rank load ratio by 32.8% and end-to-end prefill latency by 13.1%. Specifically, our method hides balancing overhead of an average of 5.1 experts per layer, which would otherwise account for about 8.5% of the critical-path latency.

---


### 93. [How Much Do Legal RAG Systems Still Hallucinate?](https://arxiv.org/abs/2608.14210)

**<font color=#1a73e8>作者：</font>** Souvick Das, Sallam Abualhaija, Domenico Bianculli  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Hallucination is a major challenge for retrieval-augmented generation (RAG) systems in the legal domain, where ungrounded answers can lead to serious consequences. To better understand this problem, we conduct a fine-grained analysis of hallucination behavior in eight legal RAG systems across two legal corpora, the GDPR (in English) and a national civil law (in French). Using claim-level and answer-level evaluation, we report on hallucination density and severity, analyze performance across question categories and user personas, and validate our findings on an independent set of 142 legal-expert-authored questions. Our results show that hallucinations remain pervasive, ranging from less than 10% of responses for the best-performing systems to nearly half in the worst case. We further find that false-premise questions, containing incorrect assumptions that must be rejected, produce high hallucination rates on the manually-drafted questions.

---


### 94. [APTER: Adaptive Post-Training with Expert-Grounded Rubrics](https://arxiv.org/abs/2608.14212)

**<font color=#1a73e8>作者：</font>** Xukai Wang, Liangqi Li, Zhiyue Xu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As large language models enter professional domains, they must satisfy domain constraints, include critical evidence, and provide complete reasoning rather than merely produce fluent responses. Existing post-training methods often rely on holistic preferences or outcome-level verification, while recent rubric-based methods usually generate rubrics independently for each query. In specialized domains, such unconstrained rubrics may omit critical requirements and vary across samples, hindering the diagnosis and targeted repair of persistent capability deficiencies. We propose APTER (Adaptive Post-Training with Expert-Grounded Rubrics), a framework that integrates structured domain knowledge into fine-grained evaluation, optimization, and diagnosis for specialized complex reasoning. First, expert-grounded rubric construction starts from an expert criteria framework built by domain experts, where each criterion represents a stable professional capability. For each query, APTER selects relevant criteria and instantiates them into query-level rubrics linked to their source criteria, turning reusable expert criteria into executable query-level supervision without reference answers. Second, adaptive post-training uses rubric verdicts as both optimization and criterion-level diagnostic signals. Aggregating low-scoring verdicts by criterion ID reveals persistent deficiencies and triggers targeted supervised fine-tuning updates during reinforcement learning. Experiments on mathematical reasoning and medical question answering show consistent gains across both domains. Across three model generations, APTER improves the mathematics and medical averages over the corresponding base models by up to 15.86 and 8.04 points, respectively. Code and rubric datasets are available at this https URL.

---


### 95. [MazeRunner: Nonlinear Task and Clue Orchestration for LLM-driven Black-Box Automated Penetration Testing](https://arxiv.org/abs/2608.14216)

**<font color=#1a73e8>作者：</font>** Zhenyuan Li, Yi Jiang, Junjie Cheng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Penetration testing is essential yet resource-intensive. Although large language models (LLMs) show promise for automating security auditing, existing agents mainly execute end-to-end workflows in simplified linear scenarios. Real-world black-box testing is fundamentally nonlinear: the attack graph is initially unknown and must be incrementally inferred from environmental feedback. Observations may reveal multiple attack branches, failures are often ambiguous, and critical clues may span long action horizons. Existing agents therefore tend to become trapped in depth-first exploration, misdiagnose failures, and forget prior evidence. We present MazeRunner, an autonomous penetration testing system built on a three-agent task-and-clue orchestration framework. It separates global orchestration, context-intensive execution, and failure-oriented review while persistently maintaining task states and environmental evidence. This design supports action revision, prerequisite recovery, branch switching, and long-range clue correlation. We evaluate MazeRunner on 10 recently released HTB targets, limiting each system-target run to 20 million LLM tokens and preventing target-specific solution leakage. With Claude Sonnet 4.5, MazeRunner completes 47.7% of annotated subtasks, compared with 36.2% for PentestGPT-V2 and 34.2% for Claude Code. It achieves user-level or higher access on six targets, including root access on two; each same-model baseline reaches user-level access on only two targets and never obtains root access. Execution-trace analysis further shows that MazeRunner explores more attack branches and acquires shells more efficiently.

---


### 96. [RankT2I: A Submodular Framework for Discovering Interpretable and Diverse Semantics in Text-to-Image Models](https://arxiv.org/abs/2608.14226)

**<font color=#1a73e8>作者：</font>** Ritika Allada, Pinar Yanardag  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in text-to-image (T2I) models have revolutionized the field of image generation and editing. However, identifying semantics that a T2I model can successfully edit in an image continues to be a challenging task. Most existing approaches require users to manually specify semantics to modify a particular image, a time-consuming process that often involves extensive trial and error. In this paper, we present RankT2I, a novel, training-free, and model-agnostic framework that automates the discovery of editable semantics in diffusion and FLUX-based models. Given a visual domain, we first utilize a multimodal vision-language model to gather a broad set of candidate semantics. We then frame semantic discovery as a set selection problem and use a submodular objective to identify semantics that are relevant, editable, and diverse. Our method helps users efficiently identify a wide range of semantics for text-to-image editing models across several domains while outperforming existing methods.

---


### 97. [AutoSchema: Live Schema Grounding for Agentic Text-to-Sparql over Heterogeneous Knowledge Graphs](https://arxiv.org/abs/2608.14228)

**<font color=#1a73e8>作者：</font>** Yiming Zhang, Koji Tsuda  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Life science knowledge graphs make large collections of structured data available through SPARQL, but each resource uses its own schema, identifiers, and links. TogoMCP helps language model agents query these resources by providing curated Metadata Interoperability Exchange files. Creating and maintaining these files still requires language model assisted drafting, validation, and manual review. We study \emph{live schema grounding}, where an agent obtains the schema evidence needed for a question directly from the current endpoints. We present \textsc{autoschema}, a general framework for live schema grounding that requires no training. It inspects live schemas, maps entity names in a question to graph identifiers, explores relation paths, and finds possible connections between resources during iterative query construction. We use TogoMCP as our main comparison framework. We evaluate \textsc{autoschema} on Resource Focused Biomedical KGQA, Multi Resource Biomedical KGQA, Longitudinal Biomedical Semantic QA over BioASQ Task B, and Chemistry Knowledge Graph Transfer to a previously undocumented RDF graph. \textsc{autoschema} improves mean factoid accuracy over TogoMCP in the biomedical KGQA tasks and gives consistent gains in the longitudinal BioASQ evaluation. It also reduces iteration budget exhaustion and uses fewer tool calls on average in the core evaluation. The transfer study gives preliminary evidence that live schema grounding can support irregular and previously unseen graphs without first creating a curated schema file.

---


### 98. [The More Popular, The Harder to Forget: Adaptive Popularity for LLM Unlearning](https://arxiv.org/abs/2608.14229)

**<font color=#1a73e8>作者：</font>** Anna Borisiuk, Andrey Savchenko, Alexander Panchenko 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Popular facts are memorised more deeply during pretraining and resist removal longer than rare ones, yet existing LLM unlearning methods apply uniform gradient pressure regardless of training-data frequency. We propose the AdaPop (Adaptive Popularity) method, which combines local token confidence with a per-fact popularity-dependent exponent derived from an external proxy (e.g., Wikidata sitelinks, LLM-as-Judge), and automates the forget-retain balance via a dual-ascent controller that adjusts the retain penalty each epoch. Across three model families and two benchmarks, AdaPop leaks ~5x less forgotten content than competing methods under paraphrased queries and ~1.6x less under adversarial reformulations. We support our analysis with internal metrics: under our method, forget-set hidden states move further from the pre-unlearning model's states than under other methods, while retain-set representations remain close.

---


### 99. [Grounding Without Corrective Control: Truth-Tracking Profiles for Large Language Models](https://arxiv.org/abs/2608.14252)

**<font color=#1a73e8>作者：</font>** Brett Reynolds  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent work suggests that some large language model representations have content or reference. Grounding can secure either without supplying live routes for correction. This paper asks what follows from that gap. An output is answerable when discrepancies can affect what a target- and task-specific arrangement produces, accepts, or withdraws. The arrangement has corrective control only when live, sufficiently independent routes can detect and repair fresh discrepancies. A route profile records which routes constrain the arrangement and how they are related. Those profiles support analysis of truth-tracking: patterned support for representational success.
Language models are the pressure case; text-only arrangements provide a task-relative limiting case. Text-trained models inherit patterns of testimony, coherence, and prior correction. Where target-sensitive correction survives training, these can supply derivative answerability (inherited constraint); live answerability is the relation supplied by a current route for fresh discrepancies. Fluent failures should follow when a task requires independently informative access to the facts. Self-consistency, retrieval, tools, code execution, multimodal input, and feedback should help selectively. Route-by-task interactions test the distinctions. The decomposition's empirical burden is to predict held-out route--task combinations or improve intervention choice without conceptual refitting. Surface improvement and truth-tracking improvement can come apart.

---


### 100. [On the Robustness of Temporal Vision-Language Models for Surgical Endoscopy Videos](https://arxiv.org/abs/2608.14262)

**<font color=#1a73e8>作者：</font>** Darakshan Rashid, Raza Imam, Ufaq Khan 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Temporal vision-language models (TVLMs) offer a reusable, prompt-based interface for surgical video understanding, yet, their robustness under clinically realistic acquisition artifacts in endoscopy remains insufficiently characterized. In practice, degradations such as defocus, haze, motion blur, noise, cautery smoke, and packet loss introduce structured distribution shifts which may compromise video-text alignment. We study the robustness of temporal VLMs under such shifts caused by corruptions in clip frames. We introduce Endo-C6, a compact corruption benchmark of six endoscopy-realistic perturbations evaluated at a fixed high severity, and apply it to public Gastrointestinal (GI) endoscopy and laparoscopic cholecystectomy videos. Under a standardized prompt protocol, we benchmark 3 recent surgical TVLM baselines and analyze robustness in both mean and worst-case settings, spanning 294 dataset-level evaluations. Finally, we present RobustEndoCLIP, obtained by few-shot parameter-efficient tuning with VeRA, outperforming existing TVLM baselines. Our findings show that off-the-shelf TVLMs can exhibit severe worst-case collapse under endoscopy-specific corruptions, whereas lightweight few-shot adaptation can substantially improve corrupted performance and robustness without changing the prompt-based interface. We expect Endo-C6 to support standardized robustness reporting and promote more reliable clinical vision-language systems.

---


> [!TIP]
> 当前位于：**51-100**（第 2/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-144](./part-03.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
