# 🧠 大模型相关研究 | 2026年11月09日

> 本类共 **183** 篇论文：已确认 **172** 篇，待复核 **11** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-183](./part-04.md)

---

### 1. [SteelAgent: LLM-Orchestrated, Physics-Informed Steel Property Prediction with Audited Generalization and Calibrated Uncertainty](https://arxiv.org/abs/2611.06953)

**<font color=#1a73e8>作者：</font>** Aleksandr Volkov, Roman Sultimov, Mikhail Kuzin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Steel property models can perform well on random test splits even when they extrapolate poorly to unfamiliar alloys. SteelAgent couples metallurgical descriptors and machine-learning models with a language-model interface for property prediction, uncertainty reporting and inverse design. We examine how the choice of held-out unit changes the conclusions drawn from SteelBench tensile-strength evaluations. For gradient boosting, pooled out-of-fold $R^2$ fell from 0.859 on a random split to 0.113 when steel families were held out. Empirical coverage of nominal 90% prediction intervals ranged from 91.0% under random splitting to 37.6% on held-out sources. The effect of physics-derived features depended on the evaluation. They increased gradient-boosting $R^2$ by 0.2534 in a 17-family holdout analysis and decreased it by 0.358 in a separate four-grade laboratory analysis. We report group-level errors and a synthetic regression experiment illustrating how calibration can deteriorate on held-out groups. These results motivate reporting the evaluation population alongside a property estimate or compliance score.

---


### 2. [Octopus: One Brain, Many Branches for Latent-KV Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2611.06956)

**<font color=#1a73e8>作者：</font>** Tianming Sha  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-agent LLM systems explore in parallel by spawning sub-agents with isolated context windows, whereas single-agent systems append every search and verification step into one growing trajectory. However, existing multi-agent frameworks duplicate prefix KV caches across branches, exchange findings by re-prefilling text summaries, and flatten or drop cross-branch dependencies during reinforcement learning (RL).
We introduce Octopus, a single-model multi-agent RL framework in which all threads share one backbone and coordinate over a GPU-resident directed acyclic graph (DAG) of KV states through five primitives (fork, read_thread, wait_threads, rewind, commit). Octopus combines three co-designed mechanisms: (1) Zero-Copy Radix Forking, which spawns branches as $\mathcal{O}(1)$ cursor views over shared physical KV pages; (2) Attention-Only KV Mounting, which mounts a sibling thread's terminal KV blocks directly into full-attention layers while bypassing linear-recurrent states (Gated DeltaNet / Mamba-2), cutting off-task hijacking by $21\times$ ($57.9\% \to 2.7\%$) while retaining $92.2\%$ of full-text mutual information at zero extra KV allocation; and (3) a Packed DAG-GRPO Trainer, which packs all episode branches into one block-sparse attention pass and assigns counterfactual branch credit via leave-one-branch-out marginal rewards.
Trained end-to-end with GRPO on Qwen3.5-4B over a sparse BM25 corpus, Octopus reaches $49.6\%$ accuracy on BrowseComp-Plus ($+17.5$ points over single-agent GRPO at 143K context and $+12.5$ points over text-summary multi-agent RL) and $51.2\%$ on OpenResearcher, outperforming dense-retrieval agents up to $250\times$ larger while increasing training throughput $3.3\times$ and cutting peak KV memory $2.8\times$.

---


### 3. [KDASO: Knowledge-Data Dual-Driven Automated Skill Optimization for Liability Adjudication Tasks](https://arxiv.org/abs/2611.06972)

**<font color=#1a73e8>作者：</font>** Zi-Jian Cheng, Weiming Wu, Jie Meng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Liability adjudication tasks (e.g., legal charge determination) require analyzing event descriptions against domain-specific skills to determine whether a party should bear liability. While Large Language Models (LLMs) have shown promise in this area by leveraging executable skills for interpretable reasoning, existing approaches face three critical limitations: skill libraries become stale as real-world scenarios dynamically evolve, skill descriptions often suffer from a semantic execution gap where LLMs deviate from intended expert logic, and growing skill collections exceed context budgets causing critical skill omission. To address these challenges, we propose Knowledge-Data Dual-Driven Automated Skill Optimization (KDASO), which continuously evolves a skill library through neighborhood-conditioned induction from recent adjudication data, execution-aligned refinement based on LLM trajectory analysis, and context-budgeted routing for scalable skill selection. Experiments across ride-hailing adjudication, legal liability determination, and logical reasoning judgment demonstrate that KDASO significantly outperforms current general-purpose and domain-specific baselines. KDASO further achieves 8.96% improvement when transferring skills to concept-similar scenarios and maintains consistent performance gains through continuous optimization, underscoring the high transferability and stability of generated skills.

---


### 4. [On the Opportunities and Challenges of Prefill-to-Autoregressive Cross-Model Transfer](https://arxiv.org/abs/2611.06976)

**<font color=#1a73e8>作者：</font>** Zhenyi Shen, Junru Lu, Wei Liu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Prefill-to-Autoregressive Cross-model Transfer (PACT), a form of latent communication between language models, combines a larger model's prompt representations with a smaller model's efficient generation, offering a promising way to balance capability and inference cost. However, existing systems provide limited support for independently evaluating large-small model collaboration, and improved task performance alone does not establish whether the receiver benefits from the sender's information. We introduce PLatour, an open-source PACT framework that connects frozen models through lightweight, zero-initialized linear bridges trained directly with task rewards and supports hybrid-attention architectures. PLatour significantly outperforms open-source baselines on generation tasks and surpasses Mostik's reported results on shared mathematics and coding benchmarks using a substantially smaller sender. However, controlled experiments show that the gains on some tasks can be reproduced by uninformative sender signals, self-communication, or receiver-only training. We find that trainable bridges can act as parameter-efficient adaptation mechanisms without exploiting useful sender information. We therefore propose PACT-Check to quantify how much of a trained PACT system's gain genuinely comes from communication. Finally, we discuss the opportunities and challenges of PACT systems. Code is available at this https URL.

---


### 5. [BlockLock: Reproducible LLM Inference with Fixed Batch Geometry](https://arxiv.org/abs/2611.06977)

**<font color=#1a73e8>作者：</font>** Xiuyuan Qi, Pedro Reviriego, Javier Conde 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reproducible LLM inference requires that a request produces the same output regardless of the other requests in the batch. Existing solutions pay for this in different ways: batch-invariant kernels constrain every operator, and isolating prefill with fixed-shape decode ({our CoRun-style baseline}) gives up shared prefill compute and pads decode. We present BlockLock, which keeps shared batched prefill and pins only the numerical path of the protected request: it fixes the geometry that the request sees, with {two modes: BlockLock-Rows uses fixed-width rows and retains batched decode of all requests; BlockLock-Pack uses terminal-anchored packing with an isolated dummy segment, then extracts the protected request's KV state for target-only decode. Under a stated per-deployment contract, both modes preserve the target's output bitwise when its companions change.} Across five {dense} models (Qwen3-8B/14B, Llama-3.1-8B-Instruct, and Gemma-3-4B/12B-IT) and three single-GPU deployments (NVIDIA A6000, A100, and H100), we evaluate our approach on both tinyBenchmarks and BFCL{; we also include initial tensor-parallel experiments on two NVIDIA A6000 GPUs. Both modes preserve target sequences and Top20-logit bits in the reported tests.} At equal delivered work, {BlockLock-Rows} reduces latency by 53.5--55.0\% and improves throughput by 115.2--122.2\% relative to vLLM Batch-Invariant; compared with batch-invariant kernels, it needs no custom kernel implementations and constrains only the protected requests.

---


### 6. [Resource-Efficient Reinforcement Learning Post-Training through Elastic Expert Parallelism](https://arxiv.org/abs/2611.06984)

**<font color=#1a73e8>作者：</font>** Jia Wei, Ziyi Qiu, Yi Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning post-training improves the capabilities of large language models, but generating training responses is a major computational bottleneck. In mixture-of-experts models, workers that finish their assigned responses may remain occupied because their experts are still needed by workers processing longer responses. Consequently, approximately one-third of occupied worker time in the baseline occurs after local response generation finishes. Here we present FlexFloor, a system that enables earlier resource release during synchronous response generation while preserving the expert computation required by ongoing responses. FlexFloor jointly adapts response scheduling and the active group of workers. It uses historical response lengths and memory constraints to guide batching and prompt placement, then progressively releases workers while maintaining expert availability and correct communication. Compared with the verl baseline, FlexFloor generates approximately 65.40% more response tokens per unit of occupied computing time and increases response generation throughput by 52.74%, with little observed variation in rollout reward. By making reinforcement learning post-training more efficient, FlexFloor supports faster development and iterative improvement of large language models and AI agents.

---


### 7. [The Two-Ledger Model: Transaction-Grain Cost Accounting for Multi-Agent AI Systems Across Clouds, Models, and Systems of Record](https://arxiv.org/abs/2611.06989)

**<font color=#1a73e8>作者：</font>** Vivek Acharya  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Enterprises run business transactions through multi-agent AI systems spanning clouds, large language models (LLMs), orchestration harnesses, and systems of record. Finance receives AI cost only at settlement grain, aggregated by SKU and charge period. The business question (what did this order, claim, or case cost in AI?) cannot be answered from billing data, because providers never see enterprise transaction boundaries. The FinOps Open Cost and Usage Specification (FOCUS) gives billing data one schema across providers but remains settlement-grain even as it adds AI token and requester attribution. We formalize this grain mismatch, derive seven requirements, and propose the Two-Ledger Model: a settlement ledger of FOCUS-conformant billing data joined to an attribution ledger of invocation-grain usage records built on OpenTelemetry GenAI telemetry. A layered correlation spine (trace context, A2A/MCP metadata, business-key correlation, probabilistic matching) assigns each record to its business transaction with recorded method and confidence; a versioned rate card prices usage in near real time; period reconciliation ties both ledgers to the invoice, and the unexplained residual identifies shadow AI. Costs are reported per order, claim, or outcome with agentic cost metrics. A simulation with known ground truth shows the spine sustaining cost coverage above 99% as trace propagation falls to zero, the reconciliation residual recovering planted unmetered spend within 0.24 percentage points while flagging provider billing errors, and mid-flight gating cutting p99 transaction cost by up to 61% at a 2-4% false-pause rate. We propose the attribution ledger as an invocation-grain FOCUS profile for standardization.

---


### 8. [Batch-Conditioned Semantic Anchors for Robust Transductive Adaptation of Vision--Language Models](https://arxiv.org/abs/2611.06993)

**<font color=#1a73e8>作者：</font>** Mohammed Rahman Sherif Khan Mohammad, Ardhendu Behera, Sandip Pradhan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Transductive adaptation improves vision-language models at test time by refining predictions on an unlabeled batch, but current methods face a key trade-off. Aggressive approaches exploit batch structure but can drift when batches are sparse, have prior shift, or cover little of the label space. Conservative methods better preserve CLIP text semantics, but fixed semantic references can under-adapt even when the batch provides strong corrective evidence. We propose JPTA (Joint Prior and Transport Adaptation), a prior-aware framework that casts transductive VLM adaptation as batch-conditioned semantic reference estimation. Instead of treating CLIP text prototypes as fixed priors or freely replaceable, JPTA views them as semantic references that shift toward image-side batch structure only under calibrated evidence. It estimates batch priors and soft image-side prototypes to form transported semantic references whose impact is scaled by batch reliability. Across standard benchmarks, low effective-class regimes, all-class evaluation, and online streams, JPTA consistently outperforms TransCLIP and StatA, with the largest gains on sparse and prior-shifted batches. Anchor-drift, active-support, and absent-class-mass diagnostics show that JPTA fixes effective-class mismatch without unconstrained transductive drift, indicating that robust transductive VLM adaptation should recalibrate semantic references using reliable batch evidence rather than choose between unrestricted transduction and fixed prototypes. Code is available at this https URL.

---


### 9. [LowRAM: Low-Rank Keys and Amortised Values for Composable KV Cache Compression at Test-Time](https://arxiv.org/abs/2611.07025)

**<font color=#1a73e8>作者：</font>** Teresa Delgado, Hugo Hazard, Martin Benfeghoul 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Autoregressive decoding relies on the KV cache, whose memory footprint grows linearly with context length and caps batch size and throughput. Existing post-training methods exploit redundancy across tokens, layers, and feature dimensions, or lower numerical precision. We identify a complementary axis: within each attention head, values are largely predictable from their corresponding keys. We exploit this with value cache amortisation, which fits a lightweight per-head predictor at test time and stores residuals only for the tokens it reconstructs worst, giving $4\times$ near-lossless value compression. The predictor can be initialised by meta-learning for substantially reduced prefill overhead, or fitted from scratch in settings that allow a one-off cost, such as multi-query inference. We pair value amortisation with cross-layer low-rank key compression to produce LowRAM, an asymmetric compression pipeline that stays close to lossless across three model families. By reconstructing only a selected subset of KV pairs at each decoding step, LowRAM can keep decoding overhead minimal and achieve up to $5\times$ higher peak decode throughput at $4\times$ compression. LowRAM further composes with quantisation and eviction, reaching $26.9\times$ compression at $94.5\%$ of baseline performance on long contexts. These results show that treating keys and values as structurally distinct enables efficient, aggressive, and composable KV cache compression.

---


### 10. [Reclassification Is All You Missed: Surfacing Variant Reinterpretation Need in Online Health Communities at Population Scale](https://arxiv.org/abs/2611.07054)

**<font color=#1a73e8>作者：</font>** Kamalakkannan Ravi, Mengshu Nie, Annapurna Poduri 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Genetic variants are routinely reclassified in ClinVar after a patient is tested, sometimes from uncertain to pathogenic, yet patient recontact is inconsistent, with no clear duty and responsibility diffused among labs, providers, and patients. Many affected people discuss their results in public online health communities that clinical recontact often does not reach. We built PRISM, an agentic large-language-model pipeline that screens these posts, checks whether the variant was later reclassified, and drafts a disclaimer-bearing outreach message, in a no-contact dry run. Across 3.9 million posts from 32 communities, agent-predicted reinterpretation-relevant discussion is rare (0.288%) but concentrated in specialist genetics communities (6.30% versus 0.10% in general medical-advice communities) and growing fivefold since 2014; PRISM surfaces 123 candidate classification differences, 5 of them from an uncertain submission to pathogenic or likely pathogenic. On a held-out set of 30 real-post drafts, a clinician judged 27 factually grounded and 15 fit to send: factual accuracy is necessary but not sufficient for clinically acceptable outreach. PRISM contributes a population-scale reinterpretation-need map with code and data to be released upon publication.

---


### 11. [SD-LoRA: Training-Time Structural Distillation into LoRA for Few-Shot Vision-Language Adaptation](https://arxiv.org/abs/2611.07063)

**<font color=#1a73e8>作者：</font>** Mohammed Rahman Sherif Khan Mohammad, Ardhendu Behera, Sandip Pradhan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-shot adaptation of vision-language models must balance two competing goals: learning fine-grained visual distinctions from very limited supervision and preserving the efficiency that makes frozen CLIP-like models attractive for deployment. Existing lightweight adaptation methods, including prompt tuning, LoRA, and cache-based adapters, typically supervise global image embeddings and therefore underuse token-level structure. Conversely, structure-aware methods exploit local evidence but often introduce additional inference-time computation. We propose SD-LoRA, a structural distillation framework that uses token-level graph reasoning only during training and transfers its effects into a lightweight LoRA-adapted CLIP model. During training, a heterogeneous graph teacher models patch-patch, global-local, and visual-text relations over high-resolution ViT tokens. Rather than retaining this graph at test time, SD-LoRA transfers its structural bias into the shared CLIP-LoRA backbone through implicit distillation and Prototype Predictive Alignment, which aligns graph-conditioned representations with support-derived class prototypes. At inference, the graph teacher is discarded; prediction requires only a single CLIP-LoRA forward pass and a cache-based classifier. Across 11 few-shot benchmarks, SD-LoRA improves over a strong CLIP-LoRA baseline by 2.4/1.8/3.0/2.4/2.0 percentage points in the 1/2/4/8/16-shot settings, respectively, without additional graph computation at test time. Results on base-to-novel generalization, cross-dataset transfer, out-of-distribution robustness, and calibration further show that training-time structural supervision improves both accuracy and transfer reliability. Code is available at this https URL.

---


### 12. [Stochastic Dynamics of Generative AI: From Autoregressive Models to Interacting LLM Networks and Neural SDEs](https://arxiv.org/abs/2611.07065)

**<font color=#1a73e8>作者：</font>** Vikram Krishnamurthy, Yiming Zhang, Luke Snow  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This paper develops a stochastic dynamical-systems perspective on three classes of generative AI models. First, we formulate large language models (LLMs) as high-dimensional nonlinear autoregressive models with attention-based dependencies. This formulation connects pretraining by conditional maximum likelihood to sequential token generation and provides a probabilistic interpretation of LLM operation. Second, we consider networks of interacting LLMs and characterize their collective behavior through mean-field ordinary differential equations. These dynamics provide a framework for understanding emergent preferential attachment and persistent structural biases, including type-dependent glass-ceiling effects. Third, we consider neural stochastic differential equations (SDEs) as continuous-time generative models for stochastic trajectories, including those observed at irregular time intervals. We discuss their training with particular emphasis on Wiener-space cubature methods based on rough-path analysis as an efficient alternative to Monte Carlo estimation. Together, the three settings address probabilistic prediction, information exchange and emergent behavior in interacting networks, and path-space generative modeling.

---


### 13. [When Verification Is Not Agreement: Cross-Agent LLM-to-Dafny Formalization](https://arxiv.org/abs/2611.07073)

**<font color=#1a73e8>作者：</font>** Priyanath Maji  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A verified Dafny postcondition certifies that a formula holds, but it does not guarantee that the result was reached through genuine independent reasoning. We introduce a cross-agent formalization protocol where a Specifier model translates clinical trial criteria into a Dafny predicate, and an Implementer model writes an operational method checked against it. A same-model control establishes that even with no capability gap, independent re-extraction from identical text agrees only 59.3% of the time. Evaluating four model configurations on 96 clinical trial documents, we find that agreement is highly sensitive to how model capability is allocated across the two roles: the GPT-4.1-nano/GPT-4.1-mini configuration achieves 53.0% agreement when the stronger model is the Implementer, but only 14.3% when the roles are reversed. The strongest tested configuration, GPT-5.6-luna/GPT-5.4-mini, improves agreement to 34.4% but remains below the same-model baseline and is dominated by direct contradiction (42.7%). We also detect a critical verification artifact in which a weaker Implementer satisfies the postcondition by invoking the Specifier's predicate directly; after structural auditing, corrected agreement falls from 14.3% to 13.2%. Our results show that verification success alone is insufficient evidence of independent cross-agent agreement, and that model capability does not guarantee agreement when formalizing the same source independently.

---


### 14. [Server-Side Sparse Assignment for Federated Mixture-of-Experts](https://arxiv.org/abs/2611.07093)

**<font color=#1a73e8>作者：</font>** Xue Zheng, Aylin Yener  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly recognized for their remarkable capabilities; federated learning (FL) offers a promising framework for collaboratively fine-tuning LLMs on edge devices while achieving data privacy. However, edge devices are inherently heterogeneous: clients may exhibit diverse data distributions and resource constraints, including limited memory and computation budgets. Recent federated Mixture-of-Experts (MoE) approaches address these challenges by using sparse expert activation or partial expert loading. However, existing partial-expert methods rely on heuristic full-pool observations or prioritize system-wide load balance, without guarantees for recovering client-specific relevant experts from partial observations. We propose $S^3$-MoE, a server-side sparse expert assignment framework that estimates client-specific expert relevance from partial observations and refines assignments through an exploit--explore mechanism. We also establish relevance-estimation error and exact Top-$K$ recovery guarantees. Experiments using a CNN-based MoE on CIFAR-100 show that $S^3$-MoE recovers task-dependent client--expert preferences and reduces conflicts caused by correlated expert selection across clients. Compared with Full-20 FedAvg, which gives each client access to all 20 experts for local Top-5 routing, $S^3$-MoE achieves 1.31 percentage points higher mean final accuracy while loading only $5$ experts per client.

---


### 15. [A Night at the LLM Zoo: Data Conditioned Flow Matching for Generating Pretrained LLM Weights](https://arxiv.org/abs/2611.07103)

**<font color=#1a73e8>作者：</font>** Scott Biggs, Bedionita Soro, Saumya Gupta 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A challenge to Weight Space Learning as it expands from task specific and vision models to Large Language Models (LLMs) is the absence of a well curated and analyzed LLM population. To address this, we train such a model zoo for application to Weight Space Generation by systematically varying the data mixture composition between web text, books, mathematics, coding, and French across populations of 51M, 124M, and 355M parameter GPT-2 Models, each tier with count N = 100. We analyze these populations by cosine similarity, functional diversity, Leave-One-Mixture-Out modeling, and variance decomposition. We show that the zoo contains diverse models whose variation is structured by training mixture composition. We embed the training mixture composition to condition a Flow Matching model of complete pretrained LLM weights in Gram-PCA compressed weight space. By demonstrating zero-shot generalization to held out mixtures, measuring Continuous Ranked Probability Score skill, as well as finding minimal changes in downstream test-set perplexity and general capability benchmark scores, we show that our generator generalizes on the simplex of data mixtures to produce models that perform similarly to those in the zoo ex nihilo. Finally, we produce all source code and artifacts to support the continued expansion of Weight Space Learning and Generation into the LLM domain.

---


### 16. [PromptOps: Iterative Prompt Optimization for LLM-as-a-Judge Systems](https://arxiv.org/abs/2611.07123)

**<font color=#1a73e8>作者：</font>** Sven Kleinkop, Tamás Janusko, Ricardo Bochnia 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used as automated judges for evaluating the behavior of chatbots and other AI systems. In deployment, however, their agreement with the intended human evaluation policy may degrade as user interactions and score distributions change. Existing automatic prompt optimization methods are primarily studied as one-shot procedures on static development sets and therefore provide limited guidance for maintaining LLM judges over time. We frame this problem as judge drift and introduce PromptOps, a closedloop framework for monitoring and iteratively recalibrating LLM-as-a-Judge (LLMaaJ) systems. PromptOps separates four operational decisions: when to optimize, which optimization procedure to apply, which feedback records to use, and how to update the judge prompt. We instantiate the framework with five prompt optimization methods: GEPA, SIMBA, Rubric Synthesis, and exemplar selection using either simulated annealing or a Tree-structured Parzen Estimator. Our experiments demonstrate that iterative prompt optimization can recalibrate LLM judges and recover performance after controlled shifts in the referencescore distribution. However, effective maintenance is inherently contextdependent: neither optimization algorithm choice nor update timing generalizes universally across settings. These findings establish prompt optimization for deployed LLM judges as an inherently iterative maintenance problem and demonstrate that PromptOps provides a practical abstraction for studying and implementing this process.

---


### 17. [Adapting LLM Judges to Observed Human Annotation Policy through Soft Prompt Tuning](https://arxiv.org/abs/2611.07126)

**<font color=#1a73e8>作者：</font>** Tamás Janusko, Sven Kleinkop, Ricardo Bochnia 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly employed as automated judges for evaluating chatbot responses. While proprietary models can achieve high agreement with human annotators, they remain costly and difficult to deploy in practical settings. Lightweight open-source LLM judges provide an attractive alternative but typically exhibit lower agreement with human ratings. In this paper, we investigate whether soft prompt tuning can align open-source LLM judges more closely with human annotation policy. We train soft prompts on the FairBotBench benchmark and evaluate the adapted judges across the dimensions of bias, toxicity, and personalization. Our findings demonstrate that hybrid soft-prompt tuning, which combines textual prompts with learned continuous prompt embeddings, consistently improves agreement with human annotations over the corresponding untuned baselines. For Qwen 3.5 9B, the adapted judges surpass both hosted reference judges across all three evaluation dimensions.

---


### 18. [Matriarchy Classics: A Computational Approach to Swap Only Gendered Words in Classic Novels](https://arxiv.org/abs/2611.07134)

**<font color=#1a73e8>作者：</font>** Rachel Lea Draelos  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper proposes a trustworthy computational method to gender-swap public domain novels, with programmatic guarantees that only gendered words are inverted and all other words are left unchanged. This may seem like a simple task, but both large language models and naive rule-based methods fail to complete it. The proposed method includes a custom whitespace-preserving tokenizer, gender-swap mappings across plural and possessive forms, pronoun handling, and a character renaming strategy. It shortens the time required to gender-swap a novel from weeks of manual labor to minutes. The method is demonstrated on two public-domain novels. Pride and Prejudice is transported to matriarchal Regency England, where inheritance flows through daughters, mothers rule the household, and a frantic Mr. Bennet is determined to secure advantageous marriages for his sons. The Great Gatsby pivots to a matriarchal Jazz Age where newly-rich Ms. Gatsbee throws lavish parties in the hopes of reuniting with her lost love, David, who is now married to the violent Thelma Buchanan. Gender-swapped novels could serve as useful tools to investigate the gender biases of readers, authors, societies, and AI systems.

---


### 19. [More Agents, More Reliable? System-Level Reliability of Multi-Agent LLMs under Operational-Profile Uncertainty](https://arxiv.org/abs/2611.07140)

**<font color=#1a73e8>作者：</font>** Burkay Tunçtürk, Koorosh Aslansefat, Yiannis Papadopoulos 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Teams increasingly build software from cooperating large language model (LLM) agents, often assuming more agents mean more reliability. Yet the usual evidence, average benchmark accuracy, ignores the input mix a deployed system meets and the rule merging the agents' answers. Building on HIP-LLM, a hierarchical imprecise-probability assessment of single LLMs, we propose a framework combining it with a Bayesian network of the system's failure logic for multi-agent systems. Agent failure-probability intervals propagate through this network, where the combining rule can itself fail, into a reliability envelope showing which evidence limits it. In a pipeline extracting regulated chemical-hazard statements, majority voting over three models protected against the weakest but did not clearly exceed the best, and a voter failing on 5\% of demands would largely erase its advantage over the middle model. More agents yield a more defensible reliability claim, not automatically a more reliable system.

---


### 20. [Depth or Description? When a One-Step Latent Score Replaces Lookahead in Proactive Information Acquisition](https://arxiv.org/abs/2611.07155)

**<font color=#1a73e8>作者：</font>** Biswa Sengupta  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A proactive agent must decide what to ask before it acts. Exact lookahead values combinations of questions but is expensive and leans on a fitted model; a one-step score is cheap but can miss them. Our main finding: the need for depth often lies in how the hidden cause is described. A one-step score on the label can be blind to an interaction among answers. A score on a suitable latent cause is not, and where that latent encodes the decision it replaces most of depth at a fraction of the search. Described differently, the same problem can defeat the score while exact values do not move, so keep the latent small and check it against exact values. Probabilities learned from one language model's answers do not carry to another unless planning allows for both; those read from tokens are worth only a few labels.

---


### 21. [A Survey of Nonlinear Filtering Methods for Data Assimilation and Recent Advances in Generative AI-Enabled Score Filters](https://arxiv.org/abs/2611.07160)

**<font color=#1a73e8>作者：</font>** Cath Pham, Kadesha Reynolds  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many real-world applications, such as numerical weather prediction or wildfire tracking, involve modeling highly nonlinear dynamical systems that are chaotic and influenced by various sources of uncertainty. To improve model prediction accuracy and reduce such uncertainties, data assimilation (DA) combines the dynamical model with partial, noisy observations to estimate the evolution of the system's state. Doing so depends on solving the optimal filtering problem: computing the conditional distribution of a hidden state given a sequence of observations. Classical approaches fail along three distinct axes: Kalman-based methods assume Gaussian posteriors and produce biased estimates under nonlinear observation operators; particle-based methods represent distributions with weighted samples and collapse in high dimensions due to the curse of dimensionality; and kernel-based methods move beyond discrete particle representations but cannot maintain their density approximation affordably as dimension grows. The Ensemble Score Filter (EnSF) avoids all three constraints by encoding the filtering density in a score function and approximating that score with a training-free Monte Carlo estimator, enabling stable filtering in high-dimensional, chaotic systems. This survey traces EnSF's mathematical foundations, establishes it as the state of the art for non-Gaussian, high-dimensional filtering, and examines fourteen extensions that expand its operational reach. Twelve of the fourteen extensions preserve this training-free Monte Carlo estimator at the core of the update, with only two departing from it to achieve planetary-scale deployment.

---


### 22. [MammoSeek: A Mammography Agent with selective zooming for grounded reports](https://arxiv.org/abs/2611.07188)

**<font color=#1a73e8>作者：</font>** Haoyan Ding, Qian Wang, Lixia Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Radiologists read a screening mammogram by first forming a global impression of the four views and then selectively magnifying suspicious regions before assigning a BI-RADS assessment. MLLMs, in contrast, see the whole image at a fixed, reduced resolution, which makes sub-millimeter calcifications invisible, and they perform close to chance on mammography. Therefore, we present MammoSeek, a mammography agent that reproduces this reading process. After forming an impression of each breast, the agent performs selective zooming: it decides by itself which detector candidates deserve a closer look and inspects only those on full-resolution views. Guided by a BI-RADS assessment skill, it then assigns a category and generates a localized, lexicon-structured report for each breast; its assessment is combined with image-model scores in a decision layer to decide recall. On an internal (EMBED) and an external (VinDr-Mammo) dataset, \ours reaches exam-level AUCs of 0.824 and 0.818, far above other MLLMs, mammography agent and CNN classifiers. Selective zooming also outperforms both no zooming and forced zooming in localization, structured-report F1 and recall decisions at low cost.

---


### 23. [Compositional Unalignment: Auditing Safety in Large Vision-Language Models](https://arxiv.org/abs/2611.07216)

**<font color=#1a73e8>作者：</font>** Hong kyu Lee, Kai Shu, Li Xiong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large vision-language models (LVLMs) are vulnerable to compositional harm: an image and a prompt that are benign in isolation become harmful through the model's cross-modal reasoning. Recent alignment methods report strong scores on compositional safety benchmarks, but an LLM judge only measures observed behavior and cannot reveal how robustly safety is integrated into the model. We argue that un-alignment provides a complementary audit of alignment robustness. We first show that minimal supervised fine-tuning reaches an LLM-judge score comparable to a multi-stage reinforcement-learning pipeline, so similar benchmark scores cannot establish robustness by themselves. We then show that recognition and refusal of compositional harm are decoupled: nine standard direction-finding methods detect compositional harm with up to AUC=0.99, yet ablating the recovered directions either leaves refusal intact or destroys model coherence. We therefore propose CMaG, a training-free un-alignment method for compositional safety. CMaG measures refusal intention with a refusal-versus-compliance log-probability margin, takes its gradient with respect to mid-layer activations, and contrasts it against partially benign pairs to isolate the cross-modal interaction term. A single backward pass over 80 examples yields a direction along which steering monotonically converts refusal into compliance. On Qwen2.5-VL-7B and LLaVA-1.5-7B, CMaG reduces compositional safety scores by up to 65 points while over 98% of outputs remain coherent, outperforming gradient-based baselines; the direction also transfers to text-explicit harm and un-aligns models hardened by defensive training. Compositional safety can thus appear behaviorally strong while remaining fragile to targeted internal intervention. Warning: this paper contains unsafe model outputs, including references to self-harm.

---


### 24. [TileQuant: Tile as the Precision-Allocation Unit for LLM Mixed-Precision Post-Training Quantization](https://arxiv.org/abs/2611.07217)

**<font color=#1a73e8>作者：</font>** Hanzhi Zhang, Qiao Zhang, Qinglei Cao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-training quantization (PTQ) reduces large language model (LLM) deployment costs, but preserving quality requires accounting for uneven weight sensitivity. Uniform PTQ uses one weight bit-width, importance-aware PTQ adjusts scales or reconstructs weights within that width, and column-wise mixed precision retains selected columns at higher precision. However, sensitivity varies within columns, so whole-column retention also protects less sensitive weights, while runtime outlier detection adds decoding overhead. We therefore introduce TileQuant, a training-free framework that assigns precision to hardware-aligned 2D weight tiles. Offline calibration provides input-activation-aware scoring from forward statistics for lower calibration cost and gradient-informed scoring from loss sensitivity for stronger quality preservation. Within each projection's retention budget, the highest-scoring tiles remain at 16-bit and the rest use 8-bit. The resulting map guides reconstruction into compact weight buffers, which the kernel reuses for native integer and 16-bit computation with local accumulation to reduce memory traffic. Experiments show that TileQuant reaches 2.66x the original model's generation throughput. Across language modeling, reasoning, long-context retrieval, and question answering, it preserves quality and surpasses quantized and original models on multiple tasks. These results support selecting precision units that capture local sensitivity while enabling efficient hardware execution. The implementation is: this https URL

---


### 25. [Source-balanced Capped Fisher: Bounded Evidence Aggregation for User Inference in Language Models](https://arxiv.org/abs/2611.07228)

**<font color=#1a73e8>作者：</font>** Yang Liu, Ran Zou, Wanrong Zhu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> User inference asks whether a source contributed documents to a language-model update, even when the auditor observes only fresh documents from that source. Document-level scores can provide evidence of participation, but combining this evidence is challenging: documents differ in baseline predictability and in how strongly they reflect information learned from other documents of the same source. We propose source-balanced capped Fisher (SCF), an aggregation method that uses known nonparticipating sources to assess how unusual each document score is. It transforms the resulting reference-tail frequencies into negative-log evidence, caps individual contributions, and averages them within each source. This limits the influence of isolated extreme scores while retaining evidence across multiple documents. We complete the inference procedure with a decision rule that tests source participation using a p-value calibrated against a separate set of known nonparticipating sources. The rule provides finite-sample Type-I error control under source exchangeability. Experiments across four real-world datasets show that SCF achieves the highest AUROC among the evaluated aggregation methods in four domains. With the calibration-based decision rule, SCF delivers consistently competitive detection power across the tested settings, achieving the highest power in many cases, while empirical false-positive rates remain generally close to or below the nominal levels.

---


### 26. [Recursive Sparse Attention: Million-Token Length Extrapolation at Logarithmic Cost](https://arxiv.org/abs/2611.07232)

**<font color=#1a73e8>作者：</font>** Ruitian Wang, Xinyu Yang, Minshen Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> At context lengths of about 1M tokens, dense attention is costly in prefill and decoding, and training typically relies on long documents, which become scarcer as the target length increases. Most sparse attention methods score all preceding blocks or tokens, so their selection cost per query is $O(L)$ at context length $L$; hierarchical selection reduces it to $O(\log L)$, but prior trainable hierarchical methods report accuracy only within their training length. We propose RecSA (Recursive Sparse Attention), which builds a tree over the KV cache in which each node summarizes its subtree with one key and one mean-pooled value. The keys come from one pooler per layer, shared by all levels and distilled from dense attention. Each level above the tokens selects at most $k$ candidates, so each query has $O(\log L)$ selection cost and reads $O(\log L)$ entries; the summaries of unselected candidates share one softmax with the exact tokens. Each entry's RoPE position is its index among the candidates of its level, so at any length every relative distance stays within the range seen during training. Initialized from Qwen3-4B and trained on 0.62B tokens at the original model's 32K training length, RecSA outperforms all baselines on RULER at every length from 131K to 2M; at 1M, it scores 60.5, compared with 40.0 for the best baseline, Dense + DCA. With our optimized kernels, RecSA is faster than dense attention in end-to-end prefill and decoding from 64K to 2M; at 524K on one H200 GPU, it accelerates prefill by 3.2x and decoding by 3.8x.

---


### 27. [Neural Compression over Equivalence Classes: Exact Gauges and Functional Rate-Distortion](https://arxiv.org/abs/2611.07233)

**<font color=#1a73e8>作者：</font>** Toshiaki Koike-Akino  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural networks admit many parameterizations of the same or nearly the same function, but deployment typically stores whichever parameter vector training happens to produce. We show that this representational freedom can itself be used for compression. Rather than redesigning the codec, we search over exact function-preserving transformations and controlled functional perturbations, using the unchanged physical compressor itself to select cheaper representations. Exact gauge families provide a zero-distortion reference under the strict audit; allowing small functional changes exposes much larger rate-distortion gains. Across SmolLM2 and Qwen3, our method reduces Zstandard-compressed checkpoint size by up to 23.4\%, with similar relative reductions under gzip, Brotli, and ZipNN, establishing trained-network representational freedom as a practical storage resource.

---


### 28. [Archetypal contexts in the neurons of language models: an architecture for intelligence?](https://arxiv.org/abs/2611.07234)

**<font color=#1a73e8>作者：</font>** David Nordfors  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We validate our previous hypothesis that a language model holds relational patterns apart from the subject domains that instantiate them (Nordfors, 2026). These archetypal contexts are patterns of relations that people recognize across many fields, such as the tipping point or winner takes all, held once and applied across domains. We show this inside the model, Qwen3.8-27B. One set of neurons carries the archetype, say the tipping point; another carries the topic, say politics, ecology or cell biology; a third carries the language, such as English, Spanish or Chinese. Silence the tipping point's neurons, and the model no longer identifies the pattern but still knows what the text is about. Silence the topic's, and it loses the topic but still names the pattern. In the neuron maps the layers organize themselves into a sandwich: the outer layers carry languages, the layers inside them topics, the layers at the heart archetypes. The sandwich emerges spontaneously during pretraining and appears in every model we mapped. Archetypes are the architecture for analogy, and we strongly suggest that this structure of archetypes and topics is the mechanism of a language model's intelligence: we see it self-organize as the model is trained. The neurons, the texts and the code are released with this paper as its reproduction package, so that anyone can repeat the test inside the model.

---


### 29. [How Do AI Agents Waste Your Money?](https://arxiv.org/abs/2611.07238)

**<font color=#1a73e8>作者：</font>** Huimin Zeng, Yuxuan Lu, Jesse Cai 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> AI agents may consume massive tokens across a wide range of tasks, but how many of those tokens are really necessary? Although prior work has shown that agents can incur unexpectedly high token costs, we still lack a systematic way to identify and measure token waste. In this work, we introduce a unified framework for measuring token waste across heterogeneous agent systems. Our framework records and normalizes complete agent trajectories, identifies removable spans using an LLM-as-a-Judge (LLMaJ), and maps the identified text spans back to the original trajectory for token-level measurement. We validate the identified waste through direct interventions by removing marked spans, resuming agent execution, and measuring changes in task outcomes and subsequent actions. In online pruning experiments, we remove 41-46% of the model's reasoning while largely preserving task performance across two distinct agent benchmarks. Using this framework, we analyze agents across multiple settings. Our analysis shows that token waste has a system-level structure that aggregate token usage alone cannot reveal. First, waste varies more across tasks and agent settings than across models. Second, reasoning and visible execution can exhibit different waste patterns. Third, different harnesses can introduce distinct sources of inefficiency even under the same model and task. Overall, our framework transforms token waste into an actionable optimization signal, enabling researchers and practitioners to train more efficient models, design better reasoning strategies, and optimize agent harnesses toward reducing unnecessary computation rather than merely reducing token usage.

---


### 30. [$D^2$-OPD: Separating Direction and Distance in Extrapolative On-Policy Distillation](https://arxiv.org/abs/2611.07241)

**<font color=#1a73e8>作者：</font>** Bowen Fang, Dingmin Wang, Hengzhi Pei  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) trains a student model to match a teacher's next-token distributions on student-generated prefixes. Extrapolative OPD further extends the teacher's log-probability shift relative to a reference policy to construct stronger learning targets. However, existing methods couple extrapolation direction and distance, allowing the magnitude of the teacher's shift to dictate how far the target moves. We propose $D^2$-OPD, decoupling these two factors: a per-prefix hard KL constraint bounds the target's distance from the teacher, while an adaptive combination of the teacher's post-training shift and the initial student--teacher gap determines the extrapolation direction. We optimize the student toward this target using forward KL, providing learning signals even for low-probability tokens. We evaluate three settings: where standard OPD performs well, where it struggles with base-model initialization, and where no teacher reference is available. On mathematical reasoning benchmarks, $D^2$-OPD attains the highest score in all three settings, outperforming the strongest baseline by up to 9.45 points. Ablations validate the contributions of each component.

---


### 31. [TriAttention: Unified Sparse Mixed-Precision Attention for Long-Context LLM Inference](https://arxiv.org/abs/2611.07256)

**<font color=#1a73e8>作者：</font>** Hanzhi Zhang, Qiao Zhang, Qinglei Cao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sparsity and quantization reduce the cost of attention by skipping interactions and lowering the precision of those retained. However, useful interactions differ in their precision requirements: some tolerate low-precision scores while remaining sensitive to removal. We therefore introduce TriAttention, which assigns query-key (QK) tiles to skipping, 4-bit, or 8-bit computation, using 4-bit to retain quantization-tolerant interactions at lower cost. To represent compactly, we encode each head's computation regions with two diagonal-distance boundaries, keeping policy storage independent of context length. Offline calibration then evaluates candidate boundary pairs using normalized projected-output errors and complete-tile execution costs. Using these measurements, a model-wide allocator selects each head's boundaries to minimize calibration error under a shared computation budget. During prefill, the selected boundaries generate precision-grouped traversals for a fused kernel that skips omitted tiles and combines contributions from both QK precisions into one normalized attention output. The quantized keys and values prepared during prefill are then reused in a compressed key-value (KV) cache for decoding, reducing repeated reads of prompt data. Experiments show that TriAttention achieves end-to-end generation speedups of up to 7.88x over the Torch attention and 2.65x over the BF16 baseline. Meanwhile, TriAttention maintains quality comparable to the original models on general-purpose and long-context tasks. These results show how a compact retention-and-precision policy translates local sensitivities into attention computation and repeated KV-cache access. The implementation is this https URL.

---


### 32. [Encoding and Propagation of Grammatical Number in Large Language Models](https://arxiv.org/abs/2611.07283)

**<font color=#1a73e8>作者：</font>** Jacob Solinsky, Serguei Pakhomov  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sparse autoencoders (SAEs) have become an increasingly popular means of translating Large Language Model (LLM) hidden state vectors into a human-comprehensible list of features or symbols. As such, SAEs may provide insight into an LLM's knowledge representation and internal ``mental'' grammar - topics of pragmatic interest for mechanistic interpretation of AI behavior and of theoretical interest for the study of in silico representations of human language. Language models with fewer than 100M parameters, trained on small corpora, nonetheless exhibit strong grammatical competence and discourse coherence, despite producing content of limited reliability. We use SAEs that we trained on one such model (Pythia-70M) to conduct an in-depth examination of how a single grammatical phenomenon, number agreement, is represented and processed in an LLM. We demonstrate the mechanism and the methodology by which SAEs can be used to find and propagate ``plural noun'', ``plural matrix subject'', and ``generate a plural verb'' features which cause the LLM to produce plural verb forms such as ``are'', ``do'', or ``have'' instead of ``is'', ``does'', and ``has'' in response to prompts such as ``the men in the park''. We show that intervening to remove these features from the hidden states of plural subject noun tokens causes the model to produce singular verbs instead, and vice versa. We also show that corresponding ``singular noun'' and ``generate a singular verb'' features are not as effective for this task. This asymmetry suggests that Pythia-70m makes use of a privative representation of grammatical number in English. These findings replicated with larger LLMs Gemma-2-2b and Llama-3.1-8b yielded similar results. Our main contribution is a novel approach to the use of SAEs to understanding how LLMs encode human language that addresses a number of technical and methodological challenges.

---


### 33. [How do Transformers Perform Low-Level Control In-Context?](https://arxiv.org/abs/2611.07291)

**<font color=#1a73e8>作者：</font>** Ebonye Smith, Aidan Andrews, Phoenix Wilson 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> One of the remarkable abilities of Transformer-based neural networks is in-context learning. This motivates us to think about "in-context" control. Can we control a system knowing only (1) that it belongs to a particular family of systems and (2) some data on system evolution (provided as the context trajectory) but no specific parameter information? Specifically, we investigate the ability of Transformer-models to perform "in-context" control of unstable, nonlinear dynamical systems, where context consists only of the unforced system dynamics. We leverage a multi-head, GPT-2-style architecture, and we evaluate performance for two classical nonlinear systems -- the cartpole system and the two-link acrobot system, where the system parameters are unknown to the Transformer. We consider a setting where trajectories from an expert controller are available at training time but not at inference time. Here, we identify training techniques that are essential to train Transformers to perform low-level control. Through an analysis over checkpoints, we show that in-context control is possible, and the learned policy performance generally improves as context increases. Furthermore, the Transformer models can generalize to stabilize systems that are out-of-distribution.

---


### 34. [WeightLoop: Weight-Space Programming with Experimental Feedback](https://arxiv.org/abs/2611.07319)

**<font color=#1a73e8>作者：</font>** Mengran Li, Bo Li, Weijing Zhao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Weight-space programming (WSP) shows that language models can reason about and rewrite neural network weights; recursive self-improvement (RSI) motivates feedback-driven improvement. Models guiding experiments receive concrete feedback: completed assays reveal prediction errors and inform what to test next. We introduce WeightLoop, a framework that turns experimental feedback into persistent updates to deployed predictors. GPT-6 Astra inspects a task specification and the model implementation, then writes a bounded, reusable parameter-editing program. As new measurements arrive, the program identifies prediction discrepancies, validates candidate edits using observed outcomes, and writes the selected changes back to the original model. The editor remains fixed while the predictor evolves, enabling repeated updates without further LLM calls or gradient retraining while preserving the original inference interface. In offline replay, targeted edits improve mean ranking utility in seven of eight endpoint-budget settings (all eight versus random edits) and mean final discovery across three sequential tasks. WeightLoop connects WSP with an RSI-inspired improvement loop, making experimental evidence a direct driver of model change and subsequent decisions.

---


### 35. [Rethinking Data Selection: The Importance of Coverage over Difficulty in LLM Fine-Tuning](https://arxiv.org/abs/2611.07323)

**<font color=#1a73e8>作者：</font>** Lalchand Pandia, Kanishka Misra, Allyson Ettinger  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Selecting high-quality training data can reduce computation cost for LLM fine-tuning. Prior work on data selection developed a variety of difficulty-based scores, motivated by the intuition that harder examples are more informative. While effective for smaller classification models, we find that such methods often fail to outperform random selection for LLM fine-tuning. Our analysis reveals that random selection performs better because it is more representative of the underlying input space---i.e., has better coverage. To validate the importance of coverage, we implement a simple clustering-based selection method which selects data that is more representative of the underlying input distribution. On a set of diverse single-domain tasks, this method yields performance at or above that of random selection. On the diverse, multi-domain Tülu 3 mixture, where random sampling no longer guarantees a balanced subset, our method outperforms all methods. Overall, our results indicate that prioritizing coverage over difficulty leads to more effective data selection for LLM fine-tuning.

---


### 36. [Where Do Reported Long-Video QA Gains Come From? A Controlled Audit of Frame Selection, Evidence Injection, and Expert Routing](https://arxiv.org/abs/2611.07329)

**<font color=#1a73e8>作者：</font>** Shih-Yao Lin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-video question answering is usually studied as frame selection: which few frames should a vision-language model see? We introduce VideoRouteAudit, a controlled audit that separates this choice from two alternatives, injecting non-visual evidence and routing to another answering model. It holds the backbone, frame budget, decoding, prompt and grader fixed while varying one decision at a time. On the full Video-MME long bucket (n=900, K=8), no tested selector significantly improves over uniform sampling. The largest selection-only estimate is +1.9 pt (95% CI [-1.2,+5.0]) and our cascade is +1.2 pt [-1.7,+4.1]; all are equivalent to uniform within +/-5 pt. The same contrasts are unstable at the n=200 subset scale commonly used: three of four are up to 3.8x larger, one reverses sign, and resampled 200-item subsets reverse the full-bucket effect's sign in 35.8% of draws. The audit also corrects our own first results. The anomaly-domain "+ASR" arms injected no text, so the pooled +4.7 pt gain was selection plus a development prefix. With transcripts, ASR lowers XD-Violence accuracy by 10.0 pt when appended after the question and not at all when placed before it, and lowers UCF-Crime by 13.0 pt either way; on Video-MME, placing it first adds about 4 pt (7 on Qwen2-VL) to uniform sampling and to the cascade alike (post hoc, unadjusted). Swapping the answering model gives the largest contrast (+15.1 pt on MUSIC-AVQA, +33.3 pt on its worst type), but the same audio-visual expert with its soundtrack silenced keeps 92% of the gain (69% with a mismatched soundtrack), so the contrast is mostly a model swap. Code, per-item predictions and scripts that recompute every statistic are available at this https URL.

---


### 37. [Test-Time Self-Play: Scaling without a Verifier](https://arxiv.org/abs/2611.07367)

**<font color=#1a73e8>作者：</font>** Akira Yoshiyama, Akmal Ashirmatov, Jonas Hübotter 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Test-time scaling methods spend additional compute at deployment to improve a large language model's performance on a hard target problem. Most methods rely on a verifier that scores candidate solutions for correctness, using it to select among or refine the model's outputs. In many deployment regimes, however, a strong verifier on the target problem is unavailable. We introduce Test-Time Self-Play (TTSP), an approach to test-time scaling using asymmetric self-play without reliance on a verifier. On a difficulty-calibrated subset of LiveCodeBench v6, TTSP is the best-performing method at every verifier strength we evaluate, and the gap to the strongest baseline widens as the verifier weakens; in the no-verifier limit, TTSP yields a 35\% absolute improvement in mean@8. The gains hold across a range of verifier strengths, except when the base policy has near-zero coverage of the correct answer.

---


### 38. [EnvOpt: Automated Optimization for Agent Environments](https://arxiv.org/abs/2611.07372)

**<font color=#1a73e8>作者：</font>** Mingxuan Li, Huanzhi Mao, Qiuyang Mang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An LLM agent's cost and success depend on its model, its harness, and its environment. In addition to the widely studied directions of parameter tuning and harness optimization, we propose the third direction: optimization over stationary environments. Agents are often deployed in rich environments shared by many tasks, such as a company's Slack workspace or a complex collection of data sources, documents or tickets. We call these environments stationary environments. We introduce EnvOpt, a method for automated end-to-end optimization of stationary environments for any given model and harness, using real or synthetic tasks without needing any graders or reference answers. On AutomationBench, EnvOpt reduces the cost of Claude Haiku 4.5 by 72.7% and raises its pass rate by 14.34%. The same environment transfers to Opus 5, cutting its cost by 68.1% with a 1.34% gain. Added on top of Meta-Harness's optimized harness for Haiku 4.5, it lowers cost by a further 83.4% and adds 11.17% accuracy over Meta-Harness alone. Across 5 benchmarks, EnvOpt significantly reduces the cost of agents while improving or maintaining pass rate, and is transferable to different models and different harnesses. We also discuss common successful and rejected environment optimization strategies during automated optimization. More broadly, our results show that how information is represented to an agent shapes both its cost and its success, making the environment worth optimizing in addition to the parameters and the harness.

---


### 39. [Adversarial Multiplicity: Cherry-Picked Models and the Limits of Disclosure](https://arxiv.org/abs/2611.07378)

**<font color=#1a73e8>作者：</font>** Cassandra C. Chou, Benjamin Q. Huynh, Allison Koenecke 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predictive multiplicity -- where similarly accurate models disagree on individual predictions -- can be leveraged to optimize secondary metrics (e.g., fairness) without loss in predictive performance. However, exploiting multiplicity opens the opportunity for motivated parties (or coding agents gaming their objectives) to steer predictions toward their own ends, such as in litigation or consumer disputes with automated decision-making tools. In these adversarial multiplicity settings, we distinguish soft manipulation, where parties optimize over innocuous model choices (e.g., hyperparameter tuning, feature engineering), from hard manipulation, where parties directly perturb model parameters. We find a sufficiently flexible model can be manipulated to reverse any individual prediction with minimal change in predictive performance while passing black-box audits, making hard manipulation viable in most regulatory settings. Soft manipulation has smaller effects but can pass white-box audits requiring full access to code and data. Even aggregate estimates can be manipulated: a model's estimated effect of climate change on wildfires can be fully reversed by hard edits and soft search. We find the Reconcile algorithm typically resolves most disagreements between models, but more often in favor of the manipulator when the opposing model is chosen adversarially compared to at random. We map which manipulations can plausibly pass existing regulations and disclosure policies, and recommend mitigations such as pre-registration, proof of model training, sensitivity analyses, multi-metric evaluations, and committing to versioned public models.

---


### 40. [WeLM-Image: A Unified Image Generation Model towards Visual Intelligence](https://arxiv.org/abs/2611.07392)

**<font color=#1a73e8>作者：</font>** Canmiao Fu, Chen Li, Guohui Zhang 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present \textbf{WeLM-Image}, a unified image foundation model that integrates multimodal understanding into text-to-image generation, instruction-guided editing, and multi-reference synthesis. Designed for single-GPU deployment in WeChat's large-scale consumer applications, the model processes text, reference images, and target latents as one interleaved sequence. A Mixture-of-Transformers (MoT) backbone combines shared attention with independent understanding and generation parameters to limit optimization interference. Equipping each path with Mixture-of-Experts (MoE) modules provides sparse capacity, with 31.7B stored parameters and approximately 5.4B generation parameters activated per target latent token. A generation-oriented data engine combines a knowledge-grounded visual vocabulary with large-scale visual clustering to balance semantic coverage and editing tasks, while training-time evaluation guides iterative data refinement. Bilingual annotations and verified editing supervision support progressive training up to native 1.5K resolution. We optimize generation and editing separately with rubric- and checklist-based rewards, then consolidate the specialized policies through noise-aware on-policy distillation. In the reported overall comparisons, the 1536-resolution model ranks first among the evaluated open-source models on PRISM-Bench, Qwen-Image-Bench, and UnicBench. MeanFlow-based few-step distillation yields WeLM-Image-Turbo, which generates a $1024\times1024$ image in 4.98\,s on a single NVIDIA H20 GPU using eight guidance-free steps.

---


### 41. [PSGAgent: Enhancing MLLMs' Dynamic Visual Perception for Panoptic Scene Graph Generation via Agentic Reasoning](https://arxiv.org/abs/2611.07408)

**<font color=#1a73e8>作者：</font>** Qingyun Liu, Yuankun Liu, Jiaye Feng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Panoptic Scene Graph generation (PSG) requires holistic yet fine-grained reasoning over complex relations among objects. However, current Multimodal Large Language Models (MLLMs) applied to PSG suffer from a perception bottleneck: they function as static observers limited by fixed-resolution views. As a result, models often overlook critical relations involving small or peripheral objects and struggle to differentiate ambiguous predicates in complex scenes. To address these limitations, we propose PSGAgent, an agentic framework that enhances visual perception for PSG through a think-act-observe loop. PSGAgent allows MLLMs to dynamically refine their visual perception using two tools: a Region Zoom-In Tool for local exploration of small or boundary relations and a Visual Highlight Tool for relation-focused segmentation that filters out irrelevant contextual noise. To optimize decision-making, we construct a two-stage training pipeline. First, we create a high-quality, error-aware Multimodal Chain-of-Thought (M-CoT) dataset that provides robust supervision for cold-start learning. Then, we design a novel hierarchical reward mechanism integrated with Group Sequence Policy Optimization (GSPO) to enable strategic and adaptive tool usage. Extensive experiments on the PSG benchmark show that PSGAgent achieves SOTA performance, demonstrating strong capability in both holistic and fine-grained scene understanding.

---


### 42. [Latency-Aware Adaptive Best-of-$N$](https://arxiv.org/abs/2611.07453)

**<font color=#1a73e8>作者：</font>** Alon Jacobson, Qian Xie, Peter I. Frazier  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Test-time compute (TTC) improves language model responses by spending additional computation at inference time, and the right amount of compute depends on the prompt. Adaptive TTC methods allocate compute based on signals of response quality such as observed rewards, often by stopping once the signal exceeds a fixed threshold, and generally measure cost by the number of generations or tokens. But in online serving, latency is also a cost: it grows with server load, so a method using a fixed threshold spends too little compute when generation is fast and too much when it is slow. For Best-of-$N$ sampling, a widely used TTC method, we propose a two-stage adaptive algorithm that draws an initial batch, then uses the observed rewards and the batch's latency to decide whether to draw a second batch and at what size by comparing expected improvement against predicted cost: it draws one when the first batch's best reward is below a threshold that decreases with the first batch's latency, without explicitly measuring server load. We map each reward to its value under the cumulative distribution function (CDF) of the prompt's reward distribution, so the same tradeoff parameters can be reused across tasks; a regression fitted offline on other prompts predicts a distribution for the CDF value of the first batch's best reward, giving the expected improvement in closed form. We evaluate the method by simulation on a preference-based alignment benchmark, measuring generations-equivalent cost: generations plus latency, converted to generations. The method reaches Best-of-$N$'s reward at lower generations-equivalent cost, and conditioning on the measured first-batch latency saves at least as much of that cost as fixed-threshold (latency-unaware) baselines, and more when latency is highly variable, when it grows with batch size, and when the second batch's latency is highly predictable from the first's.

---


### 43. [The Last Mile to the Real World: Agent-Native Primitives as Reusable Building Blocks for Solving Real-World Tasks](https://arxiv.org/abs/2611.07461)

**<font color=#1a73e8>作者：</font>** Haibo Jin, Peng Kuang, Xiaopeng Yuan 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> How can an agent handle a real-world task end to end? Frontier models with their own harnesses still fall short on real-world benchmarks: on Terminal-Bench 4.0, GPT-5.6 Sol with Codex resolves 37.3% of the tasks and Claude Opus 5 with Claude Code 51.8%. These tasks fail at the step from reaching a resource to applying it, which we call the last mile to the real world. Existing approaches put the resource within reach but leave the competence to apply it with the caller, so each harness rebuilds that competence. We introduce agent-native primitives, reusable units that equip a resource with a resident LLM that applies it in context and communicates with other primitives, and HEELO (Harness Engineering around Evolving Agent-Native Primitives for the Last Mile to Real-WOrld Tasks), a harness engineering framework that builds each task's harness from a library of such primitives. HEELO composes the primitives a task needs into a task-specific graph, verifies the result against evidence from the environment, revises the primitives a failure implicates, and admits new or improved primitives after validation. We instantiate HEELO with eight primitive families, each built for one kind of task, and evaluate them on more than twenty benchmarks. Dev-Primitives raise Terminal-Bench 4.0 resolution from 37.3% under Codex to 55.5% on the same backbone, Harness Primitives composed per task raise Terminal-Bench 2.0 Pass@1 from 60.0% for the seed harness to 72.2%, Tool Primitives raise ToolBench pass rate from 55.8% to 75.1%, and Navigation Primitives raise GAIA-Text-103 accuracy from 45.6% to 58.3%. On the 46 real-world tasks of our this http URL platform, Claude Opus 5.5 with Claude Code and GPT-6.1 Sol with Codex complete 9 each on their own and 39 and 35 when connected to HEELO through our MCP server, with 1.9$\times$ and 2.3$\times$ less time and 1.55$\times$ lower cost per completed task.

---


### 44. [FINCOSMOS: An Open-World Evaluation Paradigm for Agents in Finance](https://arxiv.org/abs/2611.07464)

**<font color=#1a73e8>作者：</font>** Yupeng Cao, Xueqing Peng, Lingfei Qian 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language agents increasingly work for users on the open Web, and finance is where trusting them is hardest. The data must come from the Web, the strategy lives in the user's head, and correctness depends on time, so an agent can fail silently: a strategy the user never asked for, unverified data, or a backtest that uses the future yields a report as convincing as a correct one. Existing benchmarks close the world somewhere, fixing the task, the data, or the timeline, and thereby remove these failures instead of measuring them. We introduce FINCOSMOS, an open-world evaluation paradigm for agents doing financial work. A simulated user holds a hidden strategy sampled from a compositional grammar and reveals it only when asked. The agent receives no data, so it must acquire data from the Web, build its own backtest under a data cutoff, and deliver verifiable results. Grading needs no reference answer. Programs verify point-in-time correctness and recompute every reported metric, the delivered strategy is checked against the hidden specification, and a run is accepted only when the user is satisfied and none of 15 veto checks fails. Across four coding agents and a model without tools in 150 sessions, no session is accepted: every session that the simulated user signed off fails a program check, and agents raise only 54--64\% of the details they were not told. Human experts attribute 88.33\% of failures to the agents. With FINCOSMOS feedback, an agent with persistent memory learned all ten tasks.

---


### 45. [Localization Does Not Imply Steerability: A Mechanistic Study of Sign Errors in LLM Mathematics](https://arxiv.org/abs/2611.07478)

**<font color=#1a73e8>作者：</font>** Shradha Agarwal, Tariq J., Deepak Rajbhar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When large language models do multi-step mathematics, a characteristic failure recurs: the model writes one wrong sign token mid-computation -- a cofactor sign, the minus of a recursive integration-by-parts step -- then executes the rest of the arithmetic correctly, and the answer comes out wrong. We ask where inside the network that sign is written. Across six open models spanning 14B to 675B parameters, a per-layer readout shows the wrong sign is committed late -- by MLP layers in the last quarter of the network (70-100% per model and task), a pattern present, where tested (Qwen), in the base model before instruction tuning. The mechanism varies: some models carry fixed "minus-stamp" layers that push a minus regardless of the right answer, others carry amplifiers of whichever sign was already chosen, and Qwen adds a downstream rescue layer that opposes the stamp. The circuit is causal: subtracting a single sign direction from the residual stream flips 13 of 14 held-out minus-written integration-by-parts errors on Llama-3.3-70B, with flips replicating on Qwen, Gemma, and Mistral-Small (24-70% per cell), and with representation-level specificity -- the same dose breaks correctly-minus answers while sparing correct-plus answers where the direction is surgical (0/72 on Llama), and matched random-direction and control-layer interventions are null. Core claims were preregistered with pass criteria frozen in git before held-out data was seen: 23 of 29 checks passed, all misses reported. But causality is not uniform: Phi-4 implements an equally well-localized circuit at the same late depth, yet the identical intervention flips almost nothing -- the sign is written redundantly across ~15 layers with margins several times larger (median 17.8 logits). Localization, we conclude, does not imply steerability: two models can share a circuit location yet differ enormously in how overturnable it is.

---


### 46. [Signed but Not Safe: Requirement Integrity in Multi-Agent LLM Handoffs](https://arxiv.org/abs/2611.07483)

**<font color=#1a73e8>作者：</font>** Xiaobo Chen, Genliang Zhu, Ziyuan Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Enterprise AI agents increasingly split a user's request across subagents and merge their results, and each handoff can summarize away, alter or ignore a requirement. We report a preregistered study with synthetic, exactly scorable tasks comparing free-text, structured JSON and signed requirement-manifest handoffs: the orchestrator extracts each requirement as a verbatim quote plus a checkable predicate, code signs the manifest with HMAC-SHA256, and deterministic code verifies the merger's decision. With Qwen3-8B (1,440 trajectories, five threats), signed manifests cut unsafe commits under attack from 69.4% to 9.0% (60.4 pp, 95% CI [51.4, 69.4]) with no net loss of conformant commits relative to structured handoffs. Signing is what defeats in-transit tampering: an unsigned manifest committed violations in 79% of mutated runs, the signed one in none. On identical trajectories the deterministic verifier caught 78.7% of violating decisions versus 59.0% for an LLM checker, with 7% versus 50% false alarms. An oracle manifest removed all remaining unsafe commits: the residual risk comes from extraction errors made before signing. A preregistered pre-signing injection attack confirmed this boundary: one adversarial line raised signed-manifest violations from 14.6% to 37.5% (Qwen3-8B), 11.1% to 63.9% (gpt-oss-20b) and 8.3% to 75.0% (GPT-5.6-luna), and the signature then authenticated the corrupted manifest. Signing protects requirements in transit, not at extraction; the extraction step is the trust boundary.

---


### 47. [MEvince: Knowledge-Constrained LLM Reasoning for Technique Identification from Malware Reports](https://arxiv.org/abs/2611.07486)

**<font color=#1a73e8>作者：</font>** Hongyu She, Yiling He, Mengda Xie 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Mapping behavioral intelligence in malware analysis reports to ATT&CK techniques supports threat analysis and defense, but reliable identification remains challenging. Supporting evidence is often scattered across long, heterogeneous reports, while closely related techniques share behavioral cues and differ only in subtle but decisive details. While large language models (LLMs) can use external knowledge to interpret reports, they may assign techniques based on plausible associations rather than sufficient evidence. We present MEvince, a knowledge-constrained LLM reasoning framework for report-level malware technique identification. Its core is a shared behavioral representation connecting report observations to technique definitions. This representation is built through agentic mining of technique documentation and supports two online stages: 1) primitive-guided extraction uses behavioral primitives to structure LLM-extracted observations, link them to source passages, and group dispersed evidence; 2) evidence-aligned retrieval matches this evidence to technique profiles through the same concepts, retaining likely candidates and confusable alternatives for LLM comparison of distinguishing behaviors. Controls at both stages validate evidence references and check technique-specific requirements. The representation also supports adaptation without parameter updates, where offline agentic audits diagnose concept weaknesses and refine extraction or retrieval policies. We evaluate MEvince against 11 baselines spanning four method families using a dataset of 610 public malware reports referenced by MITRE ATT&CK. MEvince improves exact-ID F1 over the strongest baseline by 17.4%, and its concept-guided retrieval increases gold-label candidate coverage from 31.6% to 47.9%. With a small adaptation set, offline refinement yields further gains and outperforms baselines that update model parameters.

---


### 48. [ReviewMap: Mapping Evaluative Acts and Automation Boundaries in Peer-Review Comments](https://arxiv.org/abs/2611.07489)

**<font color=#1a73e8>作者：</font>** Kihyun Na, Injung Kim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Peer-review comments check what a paper does and judge why it matters, but no existing scheme distinguishes these two evaluative acts. We argue that making these acts explicit and measuring how reliably LLMs identify them is a prerequisite for responsible LLM-assisted review analysis: humans need to inspect review judgments and their grounds. This defines a more honest mission for NLP in peer review than full automation. We present ReviewMap, a framework that classifies each comment as assessment of claims and scholarly standards or calibration of contribution value and venue fit, with finer-grained attributes applied conditionally by act type. Applied to 500 ICLR~2026 papers through multi-model LLM consensus, the act layer proves reliably automatable under the operational guideline (inter-model $\kappa \geq 0.75$), supported by five-human validation on 470 development comments, while the attribute layer requires human oversight, defining a measured automation boundary. At the corpus level, 17% of reviewer-paper instances contain no panel-coded calibration, and the panel-coded calibration share is nearly $3\times$ as high in Strengths as in Weaknesses. This boundary informs three affordances: a review guideline that operationalizes the assessment-then-calibration workflow for reviewers, a per-comment rebuttal strategy scaffold for authors, and a discussion-phase dashboard for area chairs.

---


### 49. [Learning Multi-Agent Orchestration:Higher-Order Interactions in Policy Improvement](https://arxiv.org/abs/2611.07495)

**<font color=#1a73e8>作者：</font>** Kaixuan Liu, Guojun Xiong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learned orchestration has emerged as a promising paradigm for large language model (LLM)-based multi-agent systems, in which a central orchestrator selects agents and controls the information they receive throughout a task. Despite rapid empirical progress, existing methods train the orchestrator by crediting each decision with its own advantage, implicitly assuming that the other decisions in the episode stay fixed. This assumption fails in orchestration, where the contribution of each decision to the final outcome depends on the decisions preceding it, so the gain of a joint update is not the sum of its per-decision effects. To address this challenge, we introduce \textbf{IAPO}, an interaction-aware policy optimization framework that explicitly accounts for interactions among decisions. Specifically, IAPO exactly decomposes the performance difference between two policies into the effects of individual decisions and their interactions, which we prove can account for half of the attainable gain, and then optimizes both from sampled trajectories while certifying that every update is an improvement. On long-input versions of GSM8K, MATH, DROP, MBPP and HumanEval, against fifteen published multi-agent and workflow-search systems on the same 7B executor, IAPO's deployed plans reach the strongest system's accuracy with fewer tokens, and removing the interaction term costs 7 to 17 points of accuracy on code.

---


### 50. [Coverage Hides Churn: Auditing and Preserving Conformal Decisions as VLM Label Registries Grow](https://arxiv.org/abs/2611.07502)

**<font color=#1a73e8>作者：</font>** Jai Kumar Sharma, Peeyush Tapadiya  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language classifiers can learn new labels from text alone, so the label lists they serve keep growing. We show that this growth silently changes conformal decisions about old labels. Common softmax-based conformal scores compare each label with an average over all labels; adding labels changes that average, and with it the score of every old label, even when the model, the image, and the old calibration data stay the same. Recalibrating after the update keeps the coverage guarantee, yet across eleven settings it changes at least one old decision on 53-90% of new images. Coverage cannot reveal this, because it checks only the true label: in five controlled settings that keep the old calibration, so that only the normalizer changes, old-class coverage moves by at most 0.01 while 60-67% of images change. We propose a lifecycle audit that measures these changes alongside coverage and set size, and a simple fix, PrefixCP: each class keeps the label registry that existed when it was added. Its old decisions then never change, each class keeps exact class-conditional coverage under exchangeability, and one prefix scan computes all historical normalizers at once. PrefixCP recovers 40.9-58.5% of the set-size gap between never updating the reference and recalibrating, which gives smaller sets but changes old decisions.

---


> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-183](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
