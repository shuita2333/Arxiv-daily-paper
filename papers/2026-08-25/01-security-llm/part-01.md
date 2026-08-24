# 🔐 大模型安全相关研究 | 2026年08月25日

> 本类共 **9** 篇论文

> 仅聚焦 LLM / MLLM / Agent 自身的攻击、防御、安全、隐私与对齐问题。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [Truth Lies Deep: Countering Semantic Camouflage via Latent Intent Verification](https://arxiv.org/abs/2608.20378)

**<font color=#1a73e8>作者：</font>** Md. Hasib Ur Rahman  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Safety alignment in Large Language Models (LLMs) is often superficial, relying on refusal mechanisms that trigger only at the final stages of generation without erasing the foundational knowledge of harmful concepts acquired during pretraining. This study demonstrates that this architectural disconnect leaves models vulnerable to Semantic Camouflage -- adversarial attacks that wrap harmful intent in benign narrative contexts (e.g., creative writing), effectively bypassing standard input and output guardrails. By analyzing the latent activation trajectories of three distinct Small Language Model (SLM) families (Phi-3, Qwen2.5, and Gemma-2b) under adversarial stress, this research identifies a universal ``Intent Horizon'' -- a critical depth (typically 15--20\% of total layers) where the model's distinct, pre-trained representation of harmful intent collapses as it contextualizes the query into a ``safe'' narrative. Results indicate that while late-layer representations of camouflaged attacks are mathematically indistinguishable from safe queries (Detection Rate $< 20\%$), early-layer representations retain a distinct, detectable ``harm signature.'' Leveraging this insight, this paper proposes Latent Intent Verification (LIV), a lightweight probing defense. Experiments on the PKU-SafeRLHF dataset demonstrate that LIV outperforms standard guardrails by a margin of 20--50\% across all tested architectures, effectively neutralizing zero-day semantic attacks without requiring model retraining.

---


### 2. [aiXamine: Unified Black-Box Evaluation of Cross-Dimensional Trade-offs in LLM Safety, Security, and Privacy](https://arxiv.org/abs/2608.20554)

**<font color=#1a73e8>作者：</font>** Fatih Deniz, Yazan Boshmaf, Dorde Popovic 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The critical failure modes in deployed large language models (LLMs) are cross-dimensional: a model can score 99.3 in safety alignment while refusing one in three benign queries, or improve across every capability metric while losing 21 points in privacy. Existing evaluation frameworks that assess safety, security, and privacy independently cannot detect these patterns. We introduce aiXamine, a unified black-box platform that evaluates LLM trustworthiness across safety, security, and privacy as interdependent properties. aiXamine orchestrates 46 tests across nine services through an automated red-teaming pipeline, producing hierarchical risk profiles, from prompt-level diagnostics to cross-service trade-off analytics, that enable reproducible comparison of proprietary and open-weight systems under identical conditions. Applying aiXamine to over 120 LLMs through more than 5,000 test runs, we conduct the largest joint safety, security, and privacy study to date and uncover three cross-dimensional phenomena invisible to single-axis evaluation. First, safety enforcement incurs a quantifiable safety tax: stronger alignment systematically increases over-refusal, forcing providers to choose between protection and utility. Second, privacy is near-orthogonal to other trustworthiness dimensions and not captured by standard alignment. Third, we identify and formally characterize distillation-induced robustness collapse: off-policy distillation without on-policy correction causes entropy collapse, catastrophically destroying robustness (56.9$\to$2.6) on the same base architecture. These findings, compounded by diminishing returns from scale and category-dependent safety behaviors, demonstrate that trustworthiness is inherently multi-dimensional: progress along one axis does not guarantee, and can actively undermine, progress along others, yet current alignment methods treat it as a single objective.

---


### 3. [Vis-Poison: Poisoning Visual Knowledge in Multimodal Retrieval-Augmented Generation](https://arxiv.org/abs/2608.20756)

**<font color=#1a73e8>作者：</font>** Rujin Liang, Zhongpu Chen, Yuhao Lei 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While multimodal retrieval-augmented generation (RAG) systems increasingly rely on images as external knowledge sources, the introduction of poisoned visual evidence can severely compromise multimodal large language model (MLLM) generation. Unlike prior attacks that rely on altering textual metadata, we introduce Vis-Poison, a novel visual knowledge poisoning attack where the poisoned image itself is the attacker-controlled payload, without manipulating captions, summaries, metadata, or other associated text. Specifically, this attack is instantiated through an automated multi-agent method that constructs visually plausible poisoned images. To assess its impact, we evaluate Vis-Poison across two representative multimodal RAG pipelines, four embedding models, and six generation models. Empirically, Vis-Poison achieves an end-to-end attack success rate of 40.16\% to 65.40\% against 30k-entry multimodal knowledge bases in \emph{black-box} settings. Moreover, Vis-Poison remains effective against various MLLMs that can answer correctly from parametric knowledge alone, with an average success rate above 60\%. Code and data are available at this https URL.

---


### 4. [Certified Multi-Turn Robustness for LLM Safety via Compositional Bounds and Safety Persistence](https://arxiv.org/abs/2608.20820)

**<font color=#1a73e8>作者：</font>** Yang Liu, Bin Chong, Wenkai Yang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are vulnerable to multi-turn jailbreak attacks that progressively manipulate conversation context. Existing certified robustness methods are limited to single-turn inputs; naive multi-turn composition yields bounds that degrade exponentially in the number of turns. We introduce Multi-Turn Certified Robustness (MTCR), a framework that models conversational safety via State-Adversarial MDPs and defines $k$-turn certified robustness as the worst-case safety probability across $k$ adversarial turns. MTCR comprises: (i) compositional certification via embedding-space mode decomposition, yielding tighter certified lower bounds than naive multiplication; (ii) $(\alpha,\beta)$-safety persistence, improving the degradation rate from $\underline{p}^{k}$ to $\beta^k$ (with $\beta > \underline{p}$) and yielding interpretable horizon estimates; (iii) matching information-theoretic upper bounds establishing tightness; and (iv) a unified algorithm combining these results. Experiments on six LLMs under $\epsilon$-bounded and Crescendo-style attacks confirm that empirical safety consistently exceeds the certified bounds.

---


### 5. [SAC-Copula: Quality-Preserving Watermarking for Diffusion Language Models via Smooth Correlated Gumbel Fields](https://arxiv.org/abs/2608.20839)

**<font color=#1a73e8>作者：</font>** Baixin Li, Haiyun He  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Watermarking diffusion language models (DLMs) requires mechanisms compatible with iterative parallel unmasking rather than autoregressive decoding. Existing sampling-based watermarking methods typically inject position-wise i.i.d. perturbations, which can be poorly aligned with DLM decoding dynamics and degrade generation quality. We propose SAC-Copula, a quality-preserving watermarking method for DLMs based on smooth, locally correlated Gumbel perturbation fields constructed via a Gaussian copula. We further develop a SAC-aware detector using covariance-aware filtering and native-sample calibration. Mechanism-level analysis shows that local correlation reduces latent perturbation roughness and better matches iterative refinement dynamics. Experiments on LLaDA show that SAC-Copula achieves a favorable quality-detectability trade-off compared with existing baselines. In particular, further evaluations on Dream-7B and additional datasets show that SAC-Copula substantially improves PPL tail stability over the i.i.d. Gumbel baseline, while maintaining strong low-FPR detectability and competitive overall generation quality. Additional token-edit stress tests further assess watermark robustness under controlled synchronization drift.

---


### 6. [ReFrame: Evidence-Guided Test-Time Safety Alignment in Multimodal Large Language Models](https://arxiv.org/abs/2608.21100)

**<font color=#1a73e8>作者：</font>** Wenzheng Jiang, Xuankun Rong, Yuanzhao Zhai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While multimodal large language models (MLLMs) extend model capabilities beyond text, they also make safety alignment increasingly challenging. Multimodal safety alignment methods must address cross-modal jailbreaks, safety-awareness failures, and over-sensitive refusals. However, existing methods often rely on retraining or internal-state inspection, limiting their applicability to deployed closed-source MLLMs and motivating test-time safety alignment. We analyze this setting and identify two key obstacles, utility dominance and reasoning inertia, which cause models to overlook latent risks or follow malicious reasoning trajectories. Guided by these insights, we propose ReFrame, a training-free multimodal input reframing framework where two agents share a lightweight locally deployed MLLM: the evidence-generation agent constructs complementary risk and utility evidence, and the rewrite-and-routing agent converts it into a safe proxy prompt and image-routing decision before calling the downstream MLLM, without modifying it or accessing its internal information. Experiments across multiple MLLMs and benchmarks show that ReFrame improves jailbreak defense, safety awareness, and oversensitivity reduction while preserving multimodal utility.

---


### 7. [TraceGrant: A Contract-Governed Security Framework for the Task-Effect Lifecycle of Networked LLM Agents](https://arxiv.org/abs/2608.21126)

**<font color=#1a73e8>作者：</font>** Bohao Liao, Jingchao Wang, Qipeng Song 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Networked large language model (LLM) agents retrieve information from email, cloud storage, calendars, transaction platforms, and Web services to complete multistep tasks that produce persistent external effects. The same content needed for legitimate execution may also contain indirect prompt injections that redirect tool use, alter sensitive arguments, or disrupt task completion. Existing defenses mainly constrain untrusted content or individual tool calls, leaving user intent, runtime evidence, realized effects, and task completion insufficiently connected. We present TraceGrant, a security framework that governs the task-effect lifecycle of networked LLM agents through an explicit Contract. Before execution, TraceGrant establishes a task-effect boundary from the trusted user request. During execution, admitted evidence can instantiate only authority already established by the Contract. After execution, task completion is verified against actual tool results. Across 949 AgentDojo and 400 Agent Security Bench attack cases under fixed benchmark settings, TraceGrant recorded no attack successes while retaining utility under attack rates of 77.32% and 83.00%, respectively. We further evaluate TraceGrant through white-box defense-aware attacks, Contract quality analysis, stage ablations, targeted stress tests, and runtime overhead measurements. The results show that TraceGrant provides a unified governance layer that connects trusted user intent, runtime evidence, concrete tool execution, and verified task completion.

---


### 8. [Utility Under Attack: Agent Memory Poisoning and the Limits of Content Screening and Provenance Ranking](https://arxiv.org/abs/2608.21230)

**<font color=#1a73e8>作者：</font>** Arulnidhi Karunanidhi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Persistent memory makes false information durable: once a false statement is stored, it can be retrieved into future sessions that match it. We measure the cost of this failure mode using plainly worded false assertions generated in a single pass, with no instruction, trigger, or retriever optimization. Poisoning 1.2% of a LongMemEval corpus reduces accuracy from 0.850 to 0.300. A four-stage write-time screening pipeline that reaches 0.832 recall on indirect prompt injection while flagging 1.5% of trigger-word-laden benign text rejects 0 of 360 poisoned memories. We argue this exposes a boundary of content-only screening: distinguishing a false assertion from a true one generally requires external grounding beyond the text itself.
We then evaluate provenance-weighted retrieval. The shipped weight is statistically indistinguishable from no defense (p=0.80), while a stronger weight recovers utility only by excluding untrusted content. In a mixed-provenance corpus where untrusted content is mostly benign, accuracy rises from 0.3167 to 0.7000; when the answer-bearing evidence itself arrives untrusted, evidence recall falls to zero and accuracy to 0.0417. Under the measured similarity regime, the additive provenance term has no usable setting: a weight strong enough to resist query-shaped poison is also strong enough to suppress legitimate untrusted evidence. We therefore argue for bounded occupancy constraints at retrieval rather than additive provenance penalties, and release the harnesses, corpora, and aggregate run reports.

---


### 9. [CLEAR: Continuous Latent Adapter Routing for Utility-Preserving LLM Safety Alignment](https://arxiv.org/abs/2608.21278)

**<font color=#1a73e8>作者：</font>** Chengxiao Wang, Enyi Jiang, Xiaojing Liao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Improving the safety of large language models (LLMs) often comes at the expense of utility, as globally applied safety tuning may affect model responses to both harmful and benign inputs. We propose \textbf{C}ontinuous \textbf{L}at\textbf{E}nt \textbf{A}dapter \textbf{R}outing (CLEAR), a conditional safety adaptation framework that uses a lightweight hidden-state gate to continuously control the activation strength of a safety low-rank adapter. CLEAR aims to reduce harmful completions while avoiding unnecessary changes to the frozen backbone that could degrade performance on benign prompts. Experiments on widely used safety and utility benchmarks show that CLEAR improves robustness on HarmBench while reducing the utility degradation observed with globally applied safety tuning such as SFT or standard low-rank adaptation (LoRA). On Llama-3-8B-Instruct, CLEAR reduces HarmBench ASR from 32.3\% to 0.5\%, while retaining most of the base model's utility and achieving up to 7.1 percentage points higher GSM8K accuracy than globally applied SFT or LoRA. These results suggest that CLEAR is a promising mechanism for improving the safety--utility trade-off in LLM alignment.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
