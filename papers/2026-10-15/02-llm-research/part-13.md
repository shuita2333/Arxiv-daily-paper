# 🧠 大模型相关研究 | 2026年10月15日

> 本类共 **810** 篇论文：已确认 **758** 篇，待复核 **52** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**601-650**（第 13/17 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | **601-650** | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-810](./part-17.md)

---

### 601. [Agent-Reflex: Teaching Language Agents to Act Reflectively](https://arxiv.org/abs/2610.17953)

**<font color=#1a73e8>作者：</font>** Guanting Dong, Xinyu Yang, Jiajie Jin 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models have evolved from single-turn chatbots into interactive agents capable of long-horizon reasoning. In real deployments, MCP tool services can return noisy feedback and users may intervene to correct the agent, but existing methods provide limited supervision for reflection learning and failure recovery. To bridge this gap, we propose Agent-Reflex, a general training framework for incentivizing proactive reflection in agents. Specifically, Agent-Reflex comprises three stages. First, Environment Reflection Skill Discovery (RSD) injects grounded tool-feedback perturbations into environment scaling, samples a capability-diverse LLM pool, mines matched success-failure pairs, and summarizes reusable reflection meta-skills. Building on this skill library, we then apply Reflective Supervised Fine-Tuning (ReSFT) that converts each skill into supervision for self-reflection, skill recovery, and user-centric correction, strengthening complementary reflective behaviors. Finally, we propose On-Policy Reflective Policy Optimization (ORPO) to combine agentic reinforcement learning under noisy interactions with reflection-guided on-policy distillation to further elicit proactive reflection. Built on Qwen3-8B, Agent-Reflex reaches 58.6 overall on five long-horizon tool-use benchmarks and 29.1 on AgentNoiseBench, surpassing strong environment-scaling and reflection baselines. Experiments on six challenging agent benchmark suites demonstrate the effectiveness of Agent-Reflex. Further analyses show that Agent-Reflex improves agents' robustness to noise while maintaining stable training dynamics, supporting scalable agent training. Our code is available at this https URL.

---


### 602. [Virtual Head Attention](https://arxiv.org/abs/2610.17959)

**<font color=#1a73e8>作者：</font>** Xibo Ding, Guoxia Wang, Jinle Zeng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The design of attention mechanisms in long-context large language models faces an ``impossible triangle'' among KV cache size, training and prefill FLOPs, and model quality. GQA achieves strong quality but incurs high KV cache overhead; alternative approaches such as MLA and MFA can compress the cache, but MLA suffers from quality loss while MFA substantially increases training and prefill compute. We propose Virtual Head Attention (VHA), which simultaneously improves all three vertices through two lightweight linear operations: Q Premix applies a near-identity transformation to queries within each KV group to recover virtual head diversity from halved physical query heads, and Linear Postmix fuses inter-head features via a low-rank $I + AB^\top$ residual structure. Since VHA introduces no nonlinear operations, Premix can be folded into the query projection and Postmix into the output projection at inference time, reducing the model to a standard GQA-2 architecture that directly reuses all existing GQA inference optimizations. With only two KV heads, the group size in large models readily reaches 64, fully exploiting Tensor Core parallelism during decoding. Across four scales with 4K-context 50B-token pretraining, VHA consistently surpasses the standard GQA baseline at every scale ($+$0.05\% to $+$0.81\%), while reducing KV cache by $4\times$ vs.\ GQA-8 at dense scales and $2\times$ vs.\ GQA-4 at the MoE scale, and lowering training and prefill FLOPs by 7.9\% (1.7B, $S{=}4096$). On an industrial 30B-A3B MoE model trained on 500B tokens at 8K context, VHA outperforms both MLA and GQA-4 by $+$0.70\,/\,$+$2.60\,\% on a 12-benchmark base-model evaluation suite; in a separate matched 10B-A1B MoE comparison after long-context mid-training, VHA attains an average RULER score of 84.4 over 8K--128K versus 73.0 for GQA, while using two rather than four KV heads in the full-attention layers.

---


### 603. [BELT : BEhavior-Aligned Low-Rank KV Cache Compression with Learned Top-k Rank Allocation](https://arxiv.org/abs/2610.17966)

**<font color=#1a73e8>作者：</font>** Yaoyang Liu, Shuwei Shen, Jincheng Tang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-context inference makes the key-value (KV) cache a major memory bottleneck for large language models. We propose BELT, a low-rank KV cache compression framework. Its key-side objective targets attention distributions rather than raw keys or pre-softmax logits, yielding a quadratic surrogate with a closed-form low-rank solution. A learned global rank allocator uses differentiable soft selection during training and hard selection at deployment to meet a user-specified component budget. Experiments demonstrate improved model quality under aggressive compression and increased decoding throughput at comparable accuracy. Evaluated across three LLMs and multiple benchmarks, BELT achieves up to 70% low-rank KV cache compression while outperforming the strongest baseline by up to 23.3 points on LongBench, and up to 17.8x overall KV cache reduction when combined with quantization. With Triton-based GPU kernels and a quantized cache, BELT delivers up to 2.7x speedup for the attention module and 3.3x end-to-end decoding throughput.

---


### 604. [Neural Dimensional Analysis: Foundations of Dimensionless and Scale-Consistent Computation](https://arxiv.org/abs/2610.17969)

**<font color=#1a73e8>作者：</font>** Bum Jun Kim, Makoto Kawano, Yusuke Iwasawa 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern Transformers rely on many scale-control mechanisms, including normalization, residual scaling, attention temperatures, loss weighting, and adaptive updates. To explain how these mechanisms maintain scale consistency, we introduce Neural Dimensional Analysis (NDA), a unified framework based on dimensional consistency. We define neural units that specify how tensors rescale and which quantities can be added, just as physical units do in physics. Our rules match residual units, nondimensionalize attention and gate inputs, combine losses across units, and convert gradient units into parameter units. We implement NDA through dimensionless Unit Violation Indices (UVI) for diagnosing scale mismatches within Transformers, a unit-consistent multi-loss objective, and the Gauge-Canonical Transformer (GCT) with normalized coordinates and orthogonalized residual additions. In language-model experiments spanning 51M to 1B parameters, GCT remains stable during training across a broad sixteenfold learning-rate range, outperforming Pre-LN, LLaMA-style, and QK-Norm in 124M validation loss at tuned learning rates. GCT's normalized residual stream also shows improved robustness to quantization. At 1B parameters, calibrated per-tensor int8 quantization increases GCT's validation loss by only 0.009 nats, compared with up to 5.51 nats for the baselines. Vision and physics-informed neural network experiments further confirm NDA's benefits beyond language modeling. These results establish dimensional consistency as a neural network design principle.

---


### 605. [Seeing Depth but Choosing Cues in Vision-Language Models](https://arxiv.org/abs/2610.17976)

**<font color=#1a73e8>作者：</font>** Zhengtao Zou, Pekka Marttinen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Do vision-language models use depth information to judge which object is closer, or rely on image-plane cues? We investigate this question through controlled depth--cue conflicts, representation analysis, and interventions. Among the many image-plane cues relevant to depth perception, we focus on apparent size and vertical position. We compare depth judgments under cue-consistent and cue-conflict conditions in both rendered scenes and real-world photographs. Across model families and scales, depth judgments systematically shift toward misleading cues. Yet the correct depth order remains decodable from the queried objects' visual representations, including when the model answers incorrectly. Image and category controls support interpreting this signal as image-dependent depth information beyond the two target cues. Strengthening the model's own depth readout through object-level write-back can correct conflict decisions without updating model parameters or using ground-truth depth annotations. Interventions show that the effect of this correction depends on the direction and target tokens of the written signal, while its strength varies across architectures and domains. Together, these findings reveal a mismatch between a model's ability to represent depth and use this information when deciding the answer. VLMs can retain useful depth information while allowing competing image-plane cues to exert greater influence on their answers.

---


### 606. [Exact power indices for plurality-voting ensembles](https://arxiv.org/abs/2610.17980)

**<font color=#1a73e8>作者：</font>** Ilie Sarpe, Theofanis Georgakopoulos, Aristides Gionis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Plurality-voting ensembles aggregate the predictions of multiple base classifiers and output the most voted class, with ties typically broken at random. Despite the simple aggregation rule, attributing the impact of each base classifier to the ensemble's predictions is far from straightforward. That is, a single base classifier's impact depends on how it interacts with the votes of all other classifiers in the ensemble, for example, in resolving ties, and not only on its own predictions. We address the attribution problem using established tools from cooperative game theory, studying the Banzhaf and Shapley power indices for new games modeling plurality voting and random tie-breaking, for binary and multiclass classification settings. Computing power indices is, in general, intractable. Surprisingly, our methods, collectively named ENPOWER, enable the exact computation of Banzhaf and Shapley values in linear time for the binary classification setting and in low-degree polynomial time for the multiclass setting. The algorithms in ENPOWER rely on new combinatorial formulations of the Banzhaf and Shapley indices, yielding closed-form solutions for the binary case and ordinary generating function representations for the multiclass case. We validate empirically the methods in ENPOWER demonstrating their high applicability, providing attribution values not captured by existing methods. We apply the attribution of ENPOWER to: ensemble pruning and prompt-based ensembling of vision-language models.

---


### 607. [Seeing Through the Forgery Is Not Enough: Regressive Sycophancy under Fabricated Evidence in Medical Vision-Language Models](https://arxiv.org/abs/2610.17989)

**<font color=#1a73e8>作者：</font>** Sadif Ahmed, Soumya Swagata Biswas, Rifat Shahriyar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A medical vision-language model may analyze a given CT scan and correctly detect both kidneys in view. Continuing this conversation, if a user provides a prescription with an opposite direction, medical VLMs often sycophantically choose to realign their diagnosis. In this work, we study regressive sycophancy under fabricated evidence, where a model abandons a correct answer when pushback comes with a fake document. We test four open VLMs on 400 VQA-RAD yes/no questions in 19,200 multi-turn conversations, with and without a fabricated prescription. Without a disclosure that documents are synthetic, the models abandon 80.1% of 6,488 correct answers. Notably, under one script each, the same prescription raises the flip rate of Qwen2.5-VL-7B from 45.9% to 89.6% and lowers that of Qwen3-VL-8B from 77.7% to 50.9%. A model rejected the prescription while still preserving the correct answer in 915 of 3,232 conversations with the prescription (28.3%), and 40% of these flipped in later turns. System-prompt sentences that disclose the documents as synthetic lower one model's flip rate from 77.8% to 47.3%. Thus, we conclude that awareness about a forgery does not prevent a model from adopting its answer.

---


### 608. [Match the Canvas, Not Just the Answer: Predictability-Aware SFT for Diffusion Language Models](https://arxiv.org/abs/2610.18001)

**<font color=#1a73e8>作者：</font>** Miao Li, Hanyang Jiang, Hengyu Fu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion language models (DLMs) enable flexible parallel generation by resolving tokens according to the model's evolving predictability rather than a fixed left-to-right order. This flexibility, however, introduces training choices absent from standard autoregressive teacher forcing: which reference tokens are visible when a target is supervised and how much generation space is allocated. Standard supervised fine-tuning (SFT) typically makes these choices through random masking, independently of inference. Our analysis shows how this training-inference mismatch can misdirect supervision. Random masking can conceal prediction errors or penalize uncertainty that decoding would otherwise resolve, while the attention-visible input length can change which response formulations the model favors, even when the underlying solution is unchanged. Motivated by these findings, we propose Predictability-Aware Canvas Selection and Supervision (PACS), an SFT method. PACS uses the model's own predictability to select each example's attention-visible input length and supervises reference tokens immediately before their confidence-guided revelation. Across reasoning and code-generation benchmarks, PACS consistently achieves the highest mean accuracy among the compared SFT methods, with gains of up to 12.84 percentage points over vanilla SFT on individual benchmarks. Code will be released upon publication.

---


### 609. [Cost-Efficient Privacy Enforcement for Email-Generating LLM Agents under Strategic Information Requests](https://arxiv.org/abs/2610.18007)

**<font color=#1a73e8>作者：</font>** Qikun Cai, Tao Huang, Chen Hou  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM agents now act as delegated communication intermediaries: they read private context, draft messages, and send externally visible emails on behalf of a user. Existing checker-repair defenses can reduce inappropriate disclosure, but they rely on repeated calls to a remote action LLM (the model that drafts and repairs the email) and a remote checker LLM whenever a draft fails validation. This creates a cost problem as well as a privacy problem, especially when a requester strategically asks for exact values, raw records, source evidence, or other details that induce leakage-heavy drafts. We propose local contract-conditioned rewriting as a cost-efficient enforcement layer for email-generating agents. The mechanism intercepts an outgoing draft, constructs an information-release contract that specifies what to preserve, generalize, and forbid, rewrites the draft with a local Gemma rewriter, and selectively invokes a final PrivacyChecker. Across extensive email tasks under normal prompts and attack prompts that operationalize strategic information requests, Gemma + Checker reduces normal-prompt leakage from 11.41% to 4.03% while improving UsableRate (satisfied or partially satisfied outputs) from 85.2% to 92.6%. Under the strategic attack-prompt condition, it reduces leakage from 28.19% to 18.79% and reduces checker-only cost amplification from 1.32x to 1.02x. Offline replay ablation shows that the full contract reduces leakage relative to generic Gemma rewriting by 36.3% under normal prompts and 54.1% under attack prompts. These results support a local-first privacy enforcement design: move repair to a cheaper trusted local layer when possible, but retain the checker as the final semantic gate for high-risk sends.

---


### 610. [Correcting or Continuing? What On-Policy Distillation Learns from Student Errors](https://arxiv.org/abs/2610.18011)

**<font color=#1a73e8>作者：</font>** Shuo Yang, Zheyu Zhang, Mahito Sugiyama 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) trains a student on its own rollouts under a frozen teacher, mitigating the distribution mismatch of off-policy supervision. While prior work has primarily trained on problems a student can largely solve, we ask whether OPD can improve a student when training is restricted to problems it currently fails. We evaluate five representative OPD mechanisms with Qwen-3 and Phi-4 models under a unified competition-mathematics protocol. We find that OPD does not improve accuracy on this hard subset, with most mechanisms instead degrading performance despite continued decreases in training KL divergence. All eight configurations show a decline, and the two-sided sign test gives p=0.0078. In contrast, the same pipeline improves accuracy by 4.6 percentage points when training is not concentrated on failures, showing that the failure is conditional on the training regime rather than systematic. These findings suggest that OPD is effective when supervision is dominated by correct student prefixes, but can reinforce existing errors when training is concentrated on problems the student currently fails.

---


### 611. [LatentRemedy: Efficient Remedy For Non-Prefix KV Cache Reuse in Multi-Agent Systems](https://arxiv.org/abs/2610.18014)

**<font color=#1a73e8>作者：</font>** Zhiwei Chen, Zhongtao Rao, Waikit Xiu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Non-prefix KV cache reuse is a promising approach for improving inference efficiency in multi-agent systems as agents share the same context blocks. However, when agents have conflicting tasks, directly reusing non-prefix KV caches across agents can severely degrade model performance, causing up to a 90% drop. Existing remedies, including selective recomputation and offset-based calibration, recover a limited fraction of this loss. We argue that the problem lies not only in contaminated KV representations but also in the agent's difficulty interpreting reused context under its own instructions. To this end, we introduce LatentRemedy, which uses a few task-conditioned latent tokens to help the target agent leverage reused context without recomputing the shared block. Specifically, we use an MLP to map the last hidden state of the target prefix into a small number of latent tokens, which are placed after the reused KV block to interact with the shared context. To guide subsequent predictions toward the target task, we train the MLP through full-prefill distillation. Experiments show that LatentRemedy consistently outperforms existing reuse baselines on conflicting tasks while maintaining TTFT close to direct reuse as cache size grows. Code and data are available at this https URL.

---


### 612. [Machine--human agreement in marking undergraduate assignments is specific to model, prompt and institution](https://arxiv.org/abs/2610.18019)

**<font color=#1a73e8>作者：</font>** Giulio Corsi, Maryam Abo-Tabik, Yael Benn 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) promise to automate one of higher education's most resource-intensive activities: assessing student writing. Existing evaluations are typically limited to a single model, a single prompt and a single institution. Using 761 undergraduate psychology assignments from three UK universities, we evaluated three frontier LLMs, individually and in ensemble, on accuracy, prompt sensitivity, error independence, generalisability and evidential basis. Agreement between human and machine marks varied widely, with no model or prompt optimal across institutions. All models compressed marks towards a common central tendency, overvaluing the weakest assignments and undervaluing the strongest. Because this error was shared, ensembling failed to remove it. Machine marks also rewarded linguistic features more strongly than human marks. Since human-machine agreement was a joint product of model, prompt and institution, we conclude that current LLMs lack evaluative capacity transferable across contexts, and that single-context validation overstates readiness for deployment.

---


### 613. [FRACTION: Fraud Explanation Generation via Agentic Graph Context Navigation](https://arxiv.org/abs/2610.18023)

**<font color=#1a73e8>作者：</font>** Cecelia Soh, Jun Hu, Yuan Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph fraud explanation generation emerges as an important task, which requires jointly leveraging graph structure and content information to produce human-readable explanations for a given risk label. An intuitive approach is to adapt existing graph-enhanced large language models (LLMs), which inject graph structure into LLMs via graph-conditioned instruction tuning or structure-aware embeddings. However, existing methods face two key challenges in graph fraud explanation generation: a lack of evaluation protocols tailored to explanation quality, and a mismatch between the granularity of graph information they provide and what explanation generation requires. In this paper, we propose FRaud Explanation Generation via Agentic Graph Context NavigaTION (FRACTION), a framework for graph fraud explanation generation. To evaluate explanation quality, we introduce a task-specific rubric that assesses faithfulness, graph grounding, helpfulness, consistency, and conciseness, and validate it against human judgments. To focus on fine-grained details of relevant neighbors without reading the entire neighborhood, we equip a language model with graph tools that progressively disclose neighbor records. To train our graph agent, we propose a rubric-guided trajectory distillation strategy through which the agent learns both tool-use behavior and structured explanation generation. Experimental results on three fraud datasets demonstrate consistent improvements over state-of-the-art baselines under a human-aligned rubric.

---


### 614. [SHELDON: Reasoning through Dual Search over Hypothesis and Observation Spaces](https://arxiv.org/abs/2610.18025)

**<font color=#1a73e8>作者：</font>** Harshit Joshi, Priyank Shethia, Monica S. Lam  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Test-time scaling has enabled LLMs to solve increasingly complex reasoning, discovery, and optimization tasks. However, existing approaches often gather observations while seeking evidence for current hypotheses, then generate new hypotheses conditioned on those hypotheses and their associated evidence. This couples observation discovery to existing hypotheses, favoring local refinements over exploration of unknown hypotheses regions. Inspired by the hypothetico-deductive method (Hempel, 1945) and dual-space models of scientific discovery (Klahr & Dunbar, 1988), we introduce SHELDON, a scientific reasoning harness that separately represents and jointly explores hypothesis and observation spaces. By actively seeking new observations along with new hypotheses, SHELDON can discover observations that its current hypotheses do not explain. These unexplained observations expose gaps in its understanding, motivate new investigations, and guide the generation of hypotheses beyond refinements of existing ones. Across diagnosis, abstract reasoning, and optimization benchmarks, SHELDON outperforms evaluated baselines by up to 26.7 points. Additional analysis shows that SHELDON generates up to 4.5x more novel solutions.

---


### 615. [ChampionKV: Head-Wise Adaptive Budget Allocation for KV Cache Compression](https://arxiv.org/abs/2610.18026)

**<font color=#1a73e8>作者：</font>** Yuechuan Chen, Yanda Guo, Xiaoxi Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Some observation-window-based KV cache compressors use prompt attention to identify important tokens but allocate uniform or predefined budgets across heads, overlooking input-dependent differences in budget demand. We propose ChampionKV, an input-adaptive head-wise budget allocator for long-context KV cache compression. It uses the maximum aggregated observation-window attention score as a lightweight empirical proxy for attention concentration, assigning larger budgets to heads with dispersed attention and smaller budgets to concentrated heads. An abnormal-head mask and a floor-budget mechanism improve robustness under weak attention responses. ChampionKV plugs into compressors such as SnapKV and PyramidKV without changing their token-selection procedures. On LongBench and RULER, both Champion variants consistently improve over their SnapKV and PyramidKV base compressors; the improvements are largest and statistically significant on Llama3.1-70B-Instruct, especially under tight budgets, whereas results on the tested 7B/8B models remain competitive but mixed. ChampionKV does not uniformly outperform Ada-KV, whose global cross-head Top-K selection retains an advantage in several settings. Controlled analysis further shows improved retained attention mass over the corresponding base compressors at negligible overhead.

---


### 616. [inLoRA-MINT: Internal Representations for Auditing Training Data in Domain-adapted LLMs](https://arxiv.org/abs/2610.18051)

**<font color=#1a73e8>作者：</font>** Gonzalo Mancera, Julian Fierrez, Aythami Morales 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This work investigates the application of the Membership Inference Test (MINT) to large language models (LLMs) fine-tuned with LoRA, aiming to determine whether specific samples were used during training and address concerns about data privacy, leakage, and transparency. Building on our previous LoRA-MINT framework, which relies exclusively on perplexity under a strict black-box setting, we propose an approach based on intermediate model representations, including activations and parameter-dependent signals. These representations enable a MINT classifier to distinguish training from non-training samples without requiring full access to model parameters.
We evaluated the method on four LLMs (Qwen, Phi-4, DeepSeek-V3, and LLaMA 3.2-3B) fine-tuned on three datasets covering medical, mathematical, and academic reasoning tasks. Results show consistent performance across architectures and domains, achieving scores between 95% and 98%, with robustness to variations in model configurations and data distributions. The proposed approach enables efficient auditing of sensitive training data and supports data provenance and compliance with emerging privacy and AI governance regulations. Although our experiments focus on LoRA-based fine-tuning, the methodology can be extended to other LLM adaptation techniques and, more broadly, to other AI models.

---


### 617. [Can Agents Forget When Asked? A Benchmark for Memory Unlearning in LLM Agents](https://arxiv.org/abs/2610.18052)

**<font color=#1a73e8>作者：</font>** Bofan Xie, Chaokun Wang, Guanchen Ge 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-term memory has become a core component of large language model (LLM) agents. As agents accumulate personal information over long-term use, users increasingly ask them to delete sensitive or outdated facts. A memory system should honor such requests. It should remove exactly what was requested and keep the rest of its memory intact. However, existing memory benchmarks evaluate only memory writing, retrieval, and organization, so whether agents can forget at the user's explicit request remains under-evaluated. To address this gap, we propose Bemula, the first benchmark dedicated to memory unlearning. It comprises 50 multi-session dialogue instances, 135 forget requests of six types, and 1,742 test questions. Each dialogue has a control version without the requests, so that only systems that have stored the target can earn credit for forgetting. Across the paired versions, five test suites measure storage, removal of the requested information, preservation of unrelated memories, relearning of similar facts, and resistance to extraction attacks. On Bemula, we evaluate six mainstream memory systems under three backbone LLMs, together with the Full Context LLM on two of them. The results are negative. Across all evaluated systems and backbones, no system passes more than 1.5% of forget requests end to end, and most pass none at all. These systems either leave the requested information extractable under simple attacks or delete far more than requested. Memory unlearning therefore remains an open challenge for agent memory design. We release our data and code at this https URL.

---


### 618. [WorkRover: Scaling Long-Horizon Cowork Agent Training Via Recursive Environment Evolution](https://arxiv.org/abs/2610.18067)

**<font color=#1a73e8>作者：</font>** Hang He, Linting Wang, Guanming Liu 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scaling interactive environments is important for training long-horizon agents through reinforcement learning. These environments often require further testing and refinement after initial generation, and correcting defects in a task may also require updating its work context and verifier. However, existing construction pipelines offer limited support for such iterative refinement while keeping these components aligned. We introduce WorkRover, a framework for training long-horizon cowork agents through recursive environment evolution. Its harness-driven synthesis enables construction agents to jointly build and validate semantically aligned work contexts, executable tasks, and evidence-grounded verifiers, adapting their actions to workspace state and execution feedback rather than following a fixed construction workflow. To support environment evolution, we introduce Factorial Compatibility Replay (FCR), which uses rollout feedback to evaluate combinations of component revisions through dependency-closed replay and selects the smallest validated repair among tested candidates while preserving task requirements and evaluation constraints. To provide finer-grained training signals, we propose Verifier-to-Turn Credit Assignment (VTCA), which augments trajectory-level GRPO advantages with signals from deterministic workspace-progress checks and assigns a bounded share of positive-progress credit to prerequisite turns using recorded tool-output and artifact dependencies. Using WorkRover, we post-train Qwen3.5-35B-A3B to obtain WorkRover-35B-A3B and evaluate it on several cowork-agent benchmarks. Its reported scores exceed those of Qwen3.5-35B-A3B by 26.27 percentage points on JobBench, 29.32 percentage points on OfficeQA Pro, and 413.25 Elo points on GDPval v2. These results suggest that WorkRover offers a promising foundation for scalable training of long-horizon cowork agents.

---


### 619. [From Agents to Edges: Paired Optimization for Multi-Agent Collaboration](https://arxiv.org/abs/2610.18069)

**<font color=#1a73e8>作者：</font>** Feng Lin, Xiaotian Yu, Yifan Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Strong individual agents do not guarantee effective collaboration. Communication must align what one agent conveys with how another interprets and uses it. This dependency makes the communication edge a natural unit of optimization. We introduce Paired Automated Communication Optimization (PACO), which jointly optimizes the instructions at both ends of each edge and their shared communication convention in systems built on black-box language models. PACO keeps model weights, agent roles, and workflow topology fixed. A state-aware discounted bandit selects edges for refinement, while execution feedback guides paired revisions evaluated through staged end-to-end execution. The optimized instructions integrate into existing agent prompts without additional model calls at deployment. On a four-agent workflow evaluated across diverse multi-agent benchmarks, PACO consistently outperforms leading prompt-optimization and communication baselines. Configurations learned on HotpotQA retain their advantage in cross-dataset transfer without target-specific optimization. These results demonstrate that optimizing how agents communicate can substantially improve collaboration within an otherwise fixed system.

---


### 620. [LensErase: A Foundation Model for Erase Anything](https://arxiv.org/abs/2610.18072)

**<font color=#1a73e8>作者：</font>** Yunuo Chen, Xiuyu Wu, Qinhong Yang 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce LensErase, a general-purpose mask-based Erase Anything foundation model designed to cover a broad spectrum of real-world erase scenarios. LensErase supports diverse objects, visual text, watermarks, associated visual effects, multiple-object removal, and a wide range of object scales, aspect ratios, and image resolutions. First, to enable such broad coverage, we construct LensErase-100M, a large-scale dataset containing 101.07 million paired source-mask-target examples spanning diverse erase scenarios. Second, we pretrain LensErase from the text-to-image model Lens, adapting its strong generative prior to mask-based erasing. To efficiently incorporate the source image and erase mask, we propose Mask-Aware RoPE, a 3D rotary positional encoding that directly injects mask information into the source-image tokens without introducing a separate mask token sequence. Finally, we refine the model through supervised fine-tuning and reinforcement learning with contract-guided, region-aware rewards, and apply TraceFusion at inference to preserve high-fidelity content outside the effective edit region. Across six public benchmarks and the proposed LensErase-Bench, LensErase achieves substantial improvements under both reference-based objective metrics and reference-free VLM evaluation. We hope LensErase can serve as a foundational model for erase-related applications and systems.

---


### 621. [AReaL-RSI: Adaptive Scaling and Coordination of Recursive Self-Improvement](https://arxiv.org/abs/2610.18083)

**<font color=#1a73e8>作者：</font>** Wenhao Zhou, Jiajun Song, Haitao Wang 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scaling recursive self-improvement requires additional computation to produce useful research progress in reaching persistent objectives. Intuitively, more researcher agents can explore more hypotheses, but early evaluation scores might misrepresent their promise, shared findings could lose their applicability conditions, and useful procedures could remain confined to completed investigations. In this paper, we present AReaL-RSI, a framework for organizing a persistent research team of agents without updating backbone LLM weights. We formulate the scaling problem in terms of evaluated outcomes and whole-system resource expenditure. Concretely, a leader agent selects task-appropriate research orientations and guides ongoing investigations; conditional memory sharing distinguishes unresolved problems from supported findings and enables recipient adaptation. During recursive evolution, after each campaign, evidence-based review revises researcher orientation, knowledge, and skills for later campaigns. Experiments compare AReaL-RSI with Codex-Goal on downstream harness optimization, GPU kernel optimization, and AI research tasks using two backbones. Under the reported resource allocations, AReaL-RSI improves Terminal Bench performance by 2.2 percentage points for each backbone and increases mean KernelBench speedup by 32.2-36.8%; further scalability comparisons favor the design of AReaL-RSI over native scaling: combining experience sharing with specialized researcher roles yields 1.9-27.5% lower kernel latency than independent exploration and 1.3-33.9% lower latency than sharing alone across all seven comparable task-backbone pairs.

---


### 622. [ResearchFlow-Eval: Tracing the Execution Gap in End-to-End Multi-Claim Autoresearch](https://arxiv.org/abs/2610.18088)

**<font color=#1a73e8>作者：</font>** Peng Jiang, Dongyang Li, Quanying Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autoresearch systems increasingly undertake entire research projects. In practice, scientific research requires systems to pursue multiple interdependent claims through a continuous, multi-stage workflow and revise experiments as evidence accumulates. Existing evaluations of autoresearch systems, however, typically score isolated tasks or final artifacts, leaving these process-level capabilities largely unmeasured. We therefore introduce ResearchFlow-Eval, a fine-grained framework for assessing continuous scientific execution and iteration at both the stage and claim levels. Each evaluation is grounded in a published anchor paper, from which we derive stage-specific rubrics that decompose each research stage into dimensions and separately scored rubric items. Using these rubrics, we score each research stage and examine experimental execution in detail, focusing on multi-claim completion and revisions across attempts. We apply the evaluation framework to general-purpose agent harnesses, skill-augmented harnesses, and systems with research-specific orchestration. Across all evaluated systems, experimental execution consistently lags behind design and planning. Within execution, systems struggle to produce high-quality results and meet claim requirements, and repeated attempts rarely yield measurable improvements. Moreover, neither skill augmentation nor research-specific orchestration reliably yields higher scores. ResearchFlow-Eval thus extends autoresearch evaluation beyond isolated, single-objective runs to continuous workflows in which systems pursue multiple claims and refine their work across iterations.

---


### 623. [AM-Bench: Understanding Agents under Task Underspecification across Models and Harnesses](https://arxiv.org/abs/2610.18090)

**<font color=#1a73e8>作者：</font>** Kaiyu Huang, Yiting Li, Angyang Gu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Ambiguous or incomplete task specifications complicate both execution and clarification for language-model agents. Yet agents' responses to these information gaps remain poorly characterized across models and execution harnesses. We present AM-Bench, a benchmark built from 48 tasks adapted from Terminal-Bench 2.0 and Harness-Bench. Each task includes a fully specified reference and six variants spanning ambiguous or missing goals, context, and constraints. We evaluate every pairing of five models and four harnesses over 20,160 runs. Our results reveal distinct execution deficits: goal gaps hinder completion, context gaps increase token use, and constraint gaps weaken compliance without necessarily preventing completion. Missingness lowers success more than ambiguity in all three domains. These effects also reshape system comparisons: advantages under complete information need not persist, and rankings depend on model $\times$ harness pairings and the evaluation criterion -- completion, success, or repeat consistency. Estimates based on observed clarification requests and matched fully specified runs further suggest that clarification could recover unfinished work while leaving most constraint violations unresolved. Together, these findings motivate joint model-harness evaluation across information conditions and targeted clarification of unresolved requirements before dependent actions. To support future research on agents under task underspecification, we provide the AM-Bench project repository at this https URL.

---


### 624. [LifeSearch: Benchmarking Deep Research Agents for Real-World Life and Productivity](https://arxiv.org/abs/2610.18092)

**<font color=#1a73e8>作者：</font>** Yibo Wang, Senjie Jin, Yansong Ning 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deep research (DR) agents address open-ended information needs through multi-step reasoning, long-horizon web search, and evidence synthesis. However, existing benchmarks primarily focus on academic research or synthetic tasks, leaving DR agents' capabilities in real-world life and professional productivity settings insufficiently evaluated. To bridge this gap, we introduce LifeSearch, a challenging benchmark comprising 203 Chinese and English tasks derived from real-user query seeds across 7 concrete life and productivity domains. With more than 4,500 hours of human annotation, we construct over 4,000 expert-written, fine-grained rubrics, covering both report-content criteria for coverage and accuracy and concrete criteria specifying values, units, dates, and URLs. We conduct extensive experiments on 12 advanced DR agents under a unified evaluation harness, systematically analyzing their performance patterns and failure modes. We find that even the best-performing frontier agent, GPT-5.6 Sol, achieves a score of only 63.4%, leaving substantial room for improvement on realistic life and professional DR tasks. We select the grading configuration by comparing candidate LLM judges against human rubric labels, and a human ranking study shows strong alignment between aggregate benchmark scores and human judgments (Spearman's $\rho = 0.89$, Kendall's $\tau = 0.81$). LifeSearch provides a rigorous evaluation framework and foundation for advancing DR agents toward real-world life and productivity.

---


### 625. [From Spectral Saliency to Finite Deletion: Evaluating Selective Language Model Edits](https://arxiv.org/abs/2610.18098)

**<font color=#1a73e8>作者：</font>** Ibne Farabi Shihab, Joyanta Jyoti Mondal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deleting singular components offers a precise way to remove a capability from a language model, yet the first-order spectral saliency used to rank components predicts only a local loss change, whereas deletion is a finite intervention. In this paper, we study how prediction error affects selective editing, where selective editing requires degradation of a target task while preserving others. We decompose the error into derivative transfer across item splits and nonlinear response along the deletion path. We establish that outer interval screening retains every feasible candidate when every candidate's intervals contain its finite validation loss changes on every task. We evaluate these effects using one answer-only negative log-likelihood objective for search, validation, and test, with disjoint calibration and evaluation masks. The primary configuration targets arithmetic in Mistral-7B-Instruct-v0.3 while preserving code and question answering; extensions cover Llama-3.1-8B-Instruct and reversed target roles. In the primary study, which deletes 1024 coordinates from a support of 7168, calibrated intervals cover 968 of 1024 evaluation masks. Outer screening reaches the direct-selected edit after 25 verification checks, whereas direct verification abstains at a 32-check cap, but it rejects 4 of 74 feasible masks. All three selected edits pass validation, yet only one meets every test constraint. Interval coverage, feasible-candidate retention, and independent test preservation are therefore distinct properties and require separate assessment.

---


### 626. [Chain of Thought Monitoring Can Fail Even When CoT Is Necessary](https://arxiv.org/abs/2610.18105)

**<font color=#1a73e8>作者：</font>** Lennart Bürger, Piotr Komorowski, Moritz Weckbecker 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Chain of Thought (CoT) monitoring is used by frontier labs to detect misbehaviour of AI systems. Yet, its reliability remains poorly understood. We attribute this to the lack of a successful organizing principle that leads to generalizable conclusions about monitoring reliability in different regimes. Recent work attributes monitoring failures to the CoT not being necessary for the answer, and argues that CoT becomes monitorable when it is necessary. We show that this binary necessary/not-necessary organizing principle is too coarse by demonstrating that monitoring failures persist even if the CoT is necessary for the answer. In response, we introduce a more fine-grained organizing principle based on a hierarchy of four CoT necessity levels. Building on this hierarchy, we develop a framework for measuring CoT monitorability at the three lowest levels via intervention experiments. We demonstrate monitoring failures at all three of these levels on realistic, hard prediction tasks. On a difficult medical-diagnosis task, patient sex and a clinical attribute influence the answer in at least 19% and 24% of correct responses with a necessary CoT, respectively, yet their influence is almost never articulated. These results show that even when CoT is necessary, it is not guaranteed to be monitorable.

---


### 627. [A CaLLM Judge is a Better Judge: Mitigating Bias in LLM-as-a-judge](https://arxiv.org/abs/2610.18108)

**<font color=#1a73e8>作者：</font>** Cesare Barbera, Luca Stradiotti, Lorenzo Cascioli 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used as judges to predict which of two candidate answers a human evaluator would prefer, providing a scalable alternative when human evaluation is too costly. Unfortunately, LLM judgments can exhibit systematic biases. Prior work has documented position, verbosity or model family of the candidate answers influencing the judge decision rather than their quality, while additional biases may remain undocumented. $\textit{Multicalibration}$ provides a natural framework to address this problem: each bias corresponds to miscalibration on an identifiable group, $\textit{e.g.}$, family bias manifests as overconfidence in answers generated by models belonging to the same family of the judge. The challenge is to fix miscalibration simultaneously across many, potentially unknown groups. To this end, we introduce $\mathrm{CaLLM}$, a post hoc framework that multicalibrates an LLM judge, thereby bounding all such biases simultaneously. We prove that $\mathrm{CaLLM}$ bounds the bias of every group whose error structure is captured by an available representation, and that augmenting it with explicit bias groups further reduces the residual bias. We then derive theoretical conditions under which $\mathrm{CaLLM}$ improves the judge's accuracy, rather than trading it for calibration. Finally, we evaluate $\mathrm{CaLLM}$ across pairwise preference benchmarks, showing that it reduces the multicalibration error on both specified and unspecified bias groups, while improving predictive performance of the judge.

---


### 628. [Narrative Lookahead in LLMs: Event-Level Decodability, Predictive Advantage, and Steering](https://arxiv.org/abs/2610.18121)

**<font color=#1a73e8>作者：</font>** Donghoon Jung, Min Kim, Seojin Choi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Do language models carry information about narrative events before writing them, and how far ahead? We examine narrative lookahead through salient, state-changing events rather than tokens or response-level attributes. We extract 23,355 LLM-annotated events from 2,000 stories generated by four open-weight LLMs, labeling them along three nonexclusive dimensions of change: within agents, between agents, and in the story world, with human validation on a subset. Event segmentation and plot-independent labels enable comparisons across stories at horizons measured in events rather than in tokens. At event ends, we probe hidden states for upcoming event types and compare predictions with text-only predictors using matched prefixes. Across four models, future event types are decodable above prevalence baselines for at least four subsequent events, but probes significantly outperform both primary text-only predictors only for the next event. In exploratory steering with OLMo-3.1-32B, a probe-derived direction shifts the proportion of the target event type in both intended directions at higher strengths. Our event-level approach links the prediction of future narrative developments to interventions that reshape subsequent event composition.

---


### 629. [Cheap, Consistent, Calibrated, but Biased? Typed Decision Models as Judges](https://arxiv.org/abs/2610.18122)

**<font color=#1a73e8>作者：</font>** Fabian Lukassen, Christoph Weisser, Alexander Silbersdorff  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Typed decision models (TDMs) return a probability for each allowed answer instead of generating text, which makes them candidates for cheaply replacing LLM judges that compare two answers. Whether they share the biases of LLM judges is untested. We run the CALM benchmark's bias tests on eight TDMs and seven LLM judges of 2024 and 2026. Every TDM is biased, in three to eight of twelve tests. Emotional tone affects them most, and rewriting the better answer in such a tone lowers the accuracy of a typical TDM from 99% to 42%. TDMs are more biased than 2026 LLM judges. All eight change verdicts when the answers swap places, which the 2026 LLM judges hardly do, and several side with an answer that most people allegedly prefer or that a famous model allegedly wrote. Yet both kinds of judge are tripped up by the same prompts. The TDMs' probabilities show that most tests mainly flip verdicts the TDM was unsure of, and that good calibration does not protect against bias. As TDMs are more consistent and 37 times cheaper than 2026 LLM judges, our results suggest they can be attractive judges if their biases are tested for the task.

---


### 630. [Fresh at Decision, Stale at Action: Routing New Information to LLM Decisions Already Made](https://arxiv.org/abs/2610.18126)

**<font color=#1a73e8>作者：</font>** Ayoub Merimi, Souhail Bakkali, Abdeljalil Sakat  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Freshness shapes an LLM decision at the moment it is made; the action it commits to is latent, carried out later, in a changing world. We therefore introduce a timestamp theory of decision validity and a decision ledger that realises it. Six timestamps define a decision; a freshness ceiling bounds what up-to-date evidence guarantees at action time, placing the remaining risk in information published afterwards. Accuracy then factorises into two capabilities: routing, which delivers that information to affected decisions before their revision deadlines, and temporal judgment, which reads it for the time of action. The ledger is persistent state holding each decision's times, evidence and background knowledge, indexed by watch conditions written at decision time. Controlled decision streams with exact labels confirm four predictions across five LLMs, from 8B to frontier scale: freshness alone yields exactly the accuracy the ceiling predicts; models act on decisive news once it arrives, so accuracy follows routing; the ledger's index sets what routing reaches, and watch conditions reach indirect dependencies at low exposure; and the remaining errors concern when a change takes effect. Freshness makes a decision right when it is made; routing and temporal judgment keep it right when it is carried out.

---


### 631. [Monitoring latent reasoning in looped language models](https://arxiv.org/abs/2610.18127)

**<font color=#1a73e8>作者：</font>** Pawel Olszowiec, Paulina Tomaszewska, Maciej Żelaszczyk 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Looped language models (LMs) reuse one block of layers several times per token generation, promising more latent computation at no additional storage cost. Despite their rising popularity, the analysis of looped LMs is still in its infancy: little is known about whether the iterative transformations actually improve their capabilities, or whether these models remain stable under prompt perturbation. We construct an inspection protocol rooted in Mechanistic Interpretability comprising five diverse lenses. We apply it to examine eight looped LMs from four families. Models differ in many aspects but the key one is whether the prompt is transmitted only within the looped state (carry loops: Ouro, LoopUS) or re-supplied at every iteration (re-read loops: Parcae, and Rec-OLMo & Huginn from the Raven family). The results of our study provide valuable insights concerning safety and efficient use of looped language models.

---


### 632. [Revisiting Error Feedback for Model Quantization](https://arxiv.org/abs/2610.18139)

**<font color=#1a73e8>作者：</font>** Wai-Yiu Keung, Chi Cui, Wing-Kin Ma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study causal error-feedback coefficients as design variables for model quantization. Modeling instantaneous quantization errors as independent, zero-mean variables with a common fixed variance, we formulated a metric-dependent trace problem for designing feedback coefficients. The formulation resembles fixed-order GPTQ/LDLQ feedback and supports Jacobian-aware designs that account for downstream error propagation. For a positive-definite metric $\boldsymbol{H}$, we prove that the joint rotation-feedback trace minimum is $n\det(\boldsymbol{H})^{1/n}$ and present an attaining pair using the geometric mean decomposition. Experiments on synthetic networks, trained MLPs, and language models show benefits from downstream-sensitive feedback, but also reveal that trace optimality need not improve finite-level performance. Small QAT experiments further illustrate direct loss-driven feedback tuning with fixed or trainable network weights.

---


### 633. [SparPR: Runtime KV-Cache Recovery for Resource-Constrained LLM Inference on Consumer Hardware](https://arxiv.org/abs/2610.18140)

**<font color=#1a73e8>作者：</font>** Jieyun Deng, Keming Hu, Yanghe Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Running large language models (LLMs) on consumer hardware is bottlenecked by the key-value (KV) cache, which grows with every decoded token and quickly exhausts the memory and bandwidth of a single consumer GPU. We present SparPR (Sparse Partial Recomputation), a runtime KV-cache recovery mechanism that does not modify model weights and requires no offline training. SparPR couples three online decisions: Query-Aware key-block selection scores historical blocks against the current query; dynamic budget control estimates per-block copy and recompute costs to decide how many blocks to retain; and on-demand local recomputation with cost-aware fallback merges retained blocks into continuous spans and switches between sparse recomputation and full recovery according to a runtime cost comparison. Implemented on FlexGen/FlexLLMGen, SparPR is evaluated on a single consumer laptop (RTX 3070 Ti 8GB, Ryzen 9 6900HX, 16GB RAM). It cuts end-to-end latency by 31%, 52%, and 63% at 1k, 2k, and 4k prompt tokens respectively, with 1.4x-2.7x higher throughput, and completes an 8k-token workload in 44 minutes where the FlexGen baseline times out. Under a fixed cache budget, SparPR retains a Needle Accuracy that stays well above StreamingLLM and H2O at every keep ratio, and ablation studies confirm that the three mechanisms act jointly.

---


### 634. [Mitigating Cross-Modal Hallucinations by Correcting Modality Misrouting in Omnimodal LLMs](https://arxiv.org/abs/2610.18141)

**<font color=#1a73e8>作者：</font>** Yu Mi, Licheng Pan, Jiayi Zhu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Omnimodal large language models (OLLMs) are susceptible to cross-modal hallucinations under audio-visual interference. We find that, for a substantial fraction of incorrect joint predictions, the question-relevant unimodal branch can still recover the correct answer, suggesting that task-relevant evidence can remain recoverable from the relevant modality even when it is not reflected in the joint prediction. We refer to this recoverable failure pattern as \emph{modality misrouting}. We propose CaRe (Conflict-aware Residual Intervention), a training-free inference-time method for identifying and correcting modality misrouting. CaRe uses a text-only modality probe to identify a candidate modality-specific counterfactual branch, and flags potential misrouting when its prediction conflicts with the original joint prediction. For such cases, CaRe computes a residual direction from the discrepancy between the counterfactual and fused representations and uses it to steer the original multimodal state toward the relevant modality evidence, while retaining both modalities in the original audio-visual inference path. The intervention strength is adapted based on the confidence of the counterfactual branch. Experiments on CMM and AVHBench across two OLLMs show that CaRe consistently outperforms the evaluated inference-time hallucination-mitigation baselines.

---


### 635. [RadixFlow: Filling Execution Bubbles in Prefix-Cached Hybrid LLM Serving](https://arxiv.org/abs/2610.18143)

**<font color=#1a73e8>作者：</font>** Huihao Jing, Wenbin Hu, Shaojin Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Prefix reuse improves LLM inference by sharing the KV cache of common prompt prefixes. This helps only if the scheduler can execute a matched branch in the current worker round. Schedulers assume that a matched prefix is ready, which holds for full attention but fails for hybrid LLMs. There, a branch (the consumer) may need recurrent state that another branch (the producer) is still computing in the same round. The native scheduler stops its waiting-queue scan at this blocked consumer, and the resulting head-of-line blocking creates \emph{execution bubbles}: idle batch slots that independent work could fill. We introduce RadixFlow, which decouples prefix matching from state readiness. Its state-ready traversal turns a global scan barrier into a local wait: only the consumer is blocked until the next round, while feasible independent branches keep filling the batch under the native state check. On five hybrid models, RadixFlow lowers mean latency by 3\% to 24\% and worker rounds by 11\% to 44\% at almost unchanged reuse. On the larger Qwen3.5 models, ablations show that most of the gain comes from traversal, which adds little on a full-attention control. Heavier rounds limit how much of this saving reaches latency.

---


### 636. [Fan Out or Relay? Ownership-Aware Routing for LLM Agents Querying Siloed Tables](https://arxiv.org/abs/2610.18157)

**<font color=#1a73e8>作者：</font>** Zhexi Feng  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Inside organizations, a question's data often sit with several owners, who query their own tables but never hand them over. An LLM coordinator can fan out, sending the question to every owner at once, or relay, querying owners in turn and reusing earlier rows. We show that neither is safe in advance, because data ownership decides which one is right. Across thirteen settings on PeopleJoin and BIRD with three model families, fan-out is more accurate in twelve on questions one owner can answer, yet answers at most 4.3% of those joining two owners' tables. The flip follows ownership, not query shape: on BIRD two-table joins, fan-out answers 32-44% when one owner holds both and 1-4% otherwise. Relay wins by conditioning on returned rows, and hiding them from an otherwise identical planner cuts two-owner accuracy from 23.2% to 5.1%. Since ownership is public, we propose Ownership-Aware Routing (OAR), which drafts a schema-only SQL query, counts the owners whose tables it joins, and routes the question before any private row is read. In ten settings OAR is never significantly less accurate than the best fixed protocol, and beats every fixed protocol on PeopleJoin, by up to 9.3 points on held-out organizations.

---


### 637. [Claim Framing as a Driver of LLM Sycophancy](https://arxiv.org/abs/2610.18159)

**<font color=#1a73e8>作者：</font>** Jean Seo, Pepa Atanasova, Isabelle Augenstein  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sycophancy in Large Language Models, the tendency to align responses with user preferences over ground truth, has largely been studied using questions without a clear ground truth and with a single, plainly stated user opinion. We present a systematic study of which framings of a user's claim trigger sycophancy in factual question answering, where every answer is objectively verifiable without extra context. Evaluating 14 models on 42K questions, we express correct and incorrect user opinions through various claim framings over 8 dimensions and 21 types, and measure a broad set of opinion-driven behaviors. We find that all models are susceptible to user opinions regardless of size. Models are most influenced by how confidently an opinion is stated, whom it is attributed to, and whether it is presented as shared between the user and the model. In contrast to prior work, framings based on the user's expertise, authority over the model, or social pressure matter little in our factual setting. Larger models resist incorrect opinions better but are no better at recovering from their own errors. Our results call for sycophancy evaluations that probe how an opinion is framed, not merely whether one is present, and that measure multiple behaviors beyond a single flip rate.

---


### 638. [Benchmarking Multimodal Large Language Models for Zero-Shot Human-Object Interaction](https://arxiv.org/abs/2610.18161)

**<font color=#1a73e8>作者：</font>** Oriol Rabasseda, Zenjie Li, Kamal Nasrollahi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) have demonstrated strong zero-shot reasoning across diverse domains, but their potential for Human-Object Interaction (HOI) remains unexplored. Unlike traditional HOI approaches that rely on extensive labeled datasets and fixed interaction taxonomies, MLLMs offer flexible reasoning, making them well-suited for dynamic, real-world scenarios. In this work, we present the first systematic study of MLLMs for HOI recognition and detection within a pipeline that combines an external object detector for entity localization with zero-shot multimodal reasoning for interaction understanding. We introduce a benchmark framework for principled zero-shot evaluation, consisting of (i) a unified taxonomy of zero-shot prompting strategies, and (ii) a methodology that transforms token-level logits into interaction scores, enabling fair comparison with specialized HOI models under standard metrics. To support prompt-based evaluation, we additionally construct new question-answer annotations for standard HOI datasets, transforming them into a format suitable for MLLMs. Building on this, we propose two visual prompting strategies, namely Objects as Context and Black Other Objects, that guide MLLMs to target objects while preserving scene context. Experiments on HICO, HICO-DET, and V-COCO demonstrate state-of-the-art zero-shot performance, achieving 53.50 mAP on HICO and 23.69 mAP on HICO-DET. Overall, our work provides a principled benchmarking framework for MLLMs in HOI, opening the door to new models and datasets and enabling flexible open-world interaction understanding.

---


### 639. [LoOPSD: On-Policy Self-Distillation with Looped Teachers](https://arxiv.org/abs/2610.18162)

**<font color=#1a73e8>作者：</font>** Wei Fan, Qingyue Yang, Chao-Hong Tan 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy self-distillation improves a model using guidance from the model itself, but it still requires a teacher that provides more useful predictions than the student. Existing approaches obtain such guidance by giving the teacher additional context or instructions. We ask whether it can instead come from changing how the same model uses its own layers. To address this, we introduce LoOPSD, which searches over a model's layer execution order to construct a stronger teacher and distills its advantage into the student. Specifically, we keep the model weights unchanged while searching for layers to repeat, and use the resulting teacher's predictions on student-generated prefixes to guide learning. We then alternate search and distillation, rebuilding the teacher from the updated student in each round so that the student progressively absorbs the gains from alternative layer execution. Experiments on mathematical and logical reasoning tasks show improvements across models. On GSM8K with a 400-token thinking budget, LoOPSD raises Qwen3-1.7B accuracy from 42.30% to 79.61%; subsequent distillation rounds yield further gains beyond the first round. Together, these findings show that by searching layer execution to construct teachers, we can turn a model's additional computation into improved student capabilities, opening a new avenue for self-distillation to derive supervision from the model's own computation.

---


### 640. [TRACESTEER: Trace Driven Activation Steering for Hallucination Mitigation in Diffusion Language Models](https://arxiv.org/abs/2610.18173)

**<font color=#1a73e8>作者：</font>** Xin Zhang, Yili Wang, Yue Tan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion large language models (dLLMs) have emerged as a promising alternative to autoregressive LLMs, yet remain susceptible to hallucination. Activation steering offers a promising mitigation approach by guiding parallel token predictions through internal representations. However, existing steering methods largely overlook two characteristics of dLLMs: dynamic denoising states and temporal hallucination risks, which challenge predefined steering vectors and uniform intervention strengths. We propose TRACESTEER, a trace-driven activation steering framework that uses preceding denoising predictions as feedback to jointly adapt steering direction and strength. Specifically, Denoising Feedback Steering (DF-Steering) constructs step-specific steering vectors from preceding predictions and current hidden states. Trajectory-Guided Steering Gate (TS-Gate) regulates their strength using prediction uncertainty and the denoising timestep. With the backbone frozen, factual supervision and magnitude regularization jointly guide the learning of adaptive steering interventions, promoting factual reliability and stability throughout denoising. Experiments on two dLLMs show improved factual reliability on TruthfulQA and generalization across five downstream benchmarks.

---


### 641. [A Few More Tokens Ahead: Reinforcing Parallelism in Diffusion LLMs](https://arxiv.org/abs/2610.18200)

**<font color=#1a73e8>作者：</font>** Jiahao Kuang, Yangfan Gao, Tao Gui 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Parallel generation is widely regarded as an inherent advantage of diffusion large language models. Yet our fixed-quota evaluation of four representative models reveals severe degradation across mathematics and code, with all scores below 15% at 16 tokens per step. Token-level probes identify local predictive potential near the observed prefix, especially in mathematical text. We propose RePara, which reinforces short consecutive token blocks through group-relative policy optimization and reduces rollout and log-probability recomputation costs. On LLaDA and SDAR, \ours improves GSM8K and MATH-500 accuracy over JustGRPO under reduced denoising budgets, with a 1.96x training-step speedup in our LLaDA/MATH setup.

---


### 642. [TextualRL: Textual Reinforcement Learning for Context Management](https://arxiv.org/abs/2610.18216)

**<font color=#1a73e8>作者：</font>** Tianyu Huai, Jie Zhou, Bo Mao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM agents can adapt to task feedback by revising the textual context that guides their behavior, without changing their model parameters. However, turning execution rewards into reusable context updates is challenging: individual trajectories offer limited comparative evidence about what to change, while task-specific fixes may overgeneralize when incorporated into a shared context. We introduce TextualRL, a gradient-free reinforcement learning framework that treats a group of rollouts from the same task under the same context, rather than an isolated trajectory, as the unit of policy critique. Groupwise Policy Critique contrasts successful and failed rollouts within a task; when outcomes are uniform, it draws on cross-task evidence to identify behaviors worth preserving or formulate repair hypotheses. Cross-Group Policy Update reviews the resulting proposals against evidence pooled across groups, including observations that yield no proposed edit, to refine their content and applicability. Reviewed proposals form a bounded textual patch, with adoption of the candidate context determined by held-out validation rewards. Together, these components establish a reward-driven policy optimization loop in which multiple attempts jointly inform reusable context updates. We evaluate TextualRL with five target agents on six benchmarks. Averaged over the six benchmarks, TextualRL improves test accuracy over the base model by 24.4 and 15.3 percentage points for GPT-5.5 and Qwen3.8-27B, respectively.

---


### 643. [Holding Agents Accountable with Verifiable Agent Insurance](https://arxiv.org/abs/2610.18230)

**<font color=#1a73e8>作者：</font>** Cheng Hua, Taro Tsuchiya, Nicolas Christin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> While AI agents are useful for many tasks, they regularly misbehave in destructive ways, such as deleting important data. While prior work has focused on preventing such misbehavior, we consider how to recover after an agent misbehaves. We propose verifiable agent insurance (VAI), a framework for agent providers to commit financially to promises, a list of programmatically-specified policies that an agent is meant to follow. These promises are embedded in a smart contract on an immutable ledger (e.g., a blockchain) to prevent tampering, along with a monetary escrow. A user who detects a violation of committed promises can prompt a verifier to review agent execution traces, which are logged through the agent harness's shared tool-execution path, without instrumenting each tool separately. Upon verification of the violation, the agent provider's escrow funds are paid to the reporting user. We instantiate VAI as an end-to-end implementation on an Ethereum layer-2 network, and evaluate its coverage on three prominent agent benchmarks, two of which we re-annotated to obtain task-level policy-compliance labels. Currently, many agents do not emit user authorizations and security-relevant information as explicit, structured data objects -- rather, they embed the data needed to verify policy violations in natural language exchanges. Even so, VAI manages to detect violations in 42.2% of runs containing violations across three benchmarks. By augmenting agents to explicitly emit such objects, violation detection rises to 83.0% of traces. Our findings suggest that for improved auditability, agents should be co-designed with their security policies to emit explicit, structured records of user authorization and security-relevant actions.

---


### 644. [Heading Hierarchy Reconstruction for Complex and Long Documents with Level-Wise Multimodal Memory](https://arxiv.org/abs/2610.18238)

**<font color=#1a73e8>作者：</font>** Qian Chen, Xianyin Zhang, Lifan Guo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) have been widely adopted for document parsing and optical character recognition (OCR), as they can accurately extract page-level elements. However, downstream applications such as retrieval-augmented generation (RAG) also require coherent document-level structure. Although these models indicate heading levels using different numbers of preceding ``\#'' symbols, page-by-page prediction often lacks document-level consistency. In practice, input-resolution and context-length constraints make it infeasible for a VLM to jointly process all page images in documents containing tens or hundreds of pages. To address this limitation, we propose a VLM-based framework that incrementally reconstructs heading hierarchies with a \emph{level-wise multimodal memory}. The memory retains a compact subset of all previously processed pages, selected by anchors. Our framework supports flexible anchor selection, and in this work we select the most recent node at each level, allowing the VLM to observe the visual, textual, and layout patterns of headings at every level. For comprehensive evaluation, we also introduce the Complex and Long Document Heading Hierarchy Reconstruction Benchmark (CLDoc-HHRBench), comprising 250 documents and 11,212 pages with expert-verified annotations. Experiments on CLDoc-HHRBench and three existing benchmarks demonstrate the effectiveness of our method.

---


### 645. [Beyond Answer Sharing: TrueMAD for Targeted Peer Engagement in Multi-Agent Debate](https://arxiv.org/abs/2610.18240)

**<font color=#1a73e8>作者：</font>** Dezheng Bao, Sihang Du, Renhong Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent debate (MAD) aims to improve large language model reasoning by exposing agents to alternative solutions and enabling iterative revision. However, standard broadcast-style MAD makes peer answers visible without requiring agents to engage with a particular peer claim. As a result, reliable reasoning may be suppressed by conflicting or majority responses, limiting achievable performance, while erroneous reasoning may persist and degrade final predictions without actionable feedback. We propose TrueMAD, a backbone-agnostic test-time plug-in that introduces one-to-one, free-form peer advice between answer broadcasting and self-revision. Each source agent responds to a target's current reasoning through support, rebuttal, refinement, or further questions, while the target retains control over how to revise. The same mechanism can augment standard MAD and its improved variants without parameter updates. Across AIME, GPQA-Diamond, and TruthfulQA with Qwen3-30B-A3B, TrueMAD improves agent-level and strict-majority accuracy over MAD by 3.62 and 3.52 percentage points on average, while TrueDMAD improves DMAD by 4.72 and 4.06 points, respectively. Analyses at the utterance, agent-transition, and group levels further show more peer-specific deliberation, more correction-oriented revisions, and more favorable consensus dynamics.

---


### 646. [PACT: A Pragmatic Prompting Framework for Expressive and Voice-Preserving Speech-to-Speech Translation](https://arxiv.org/abs/2610.18247)

**<font color=#1a73e8>作者：</font>** Yuchen Song, Satoshi Nakamura  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speech-to-speech translation should preserve not only what is said, but also who says it and how it is said. Existing end-to-end S2ST, speech MLLM, and cascade systems can preserve content or timbre, but often struggle to realize emotion, tone, rhythm, pauses, and pragmatic attitude in the target language. We propose PACT, a target-space pragmatic prompting framework for expressive and voice-preserving S2ST. PACT extracts source pragmatic cues, projects them into the target-language expression space, calibrates the projected representation to a realizable target subspace, and converts it into continuous prompts for a frozen speech generator. On bidirectional Spanish-English TOPI evaluation, PACT achieves the best overall performance among evaluated systems across content fidelity, voice preservation, and expression preservation metrics.

---


### 647. [Are We Testing Too Much? A Survey of Benchmark Compression for Efficient Evaluation of Large Language Models](https://arxiv.org/abs/2610.18248)

**<font color=#1a73e8>作者：</font>** Guoming Ling, Yupei Lin, Zhongzhan Huang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Benchmarks are essential for evaluating and improving large language models (LLMs). Yet many widely used benchmarks are redundant, making evaluation unnecessarily expensive. Benchmark compression lowers this cost by estimating full-benchmark scores and rankings from a partial evaluation. Research in this area has grown rapidly since 2024, but to our knowledge no survey has systematically organized its methods and findings. We review 119 papers to explain how methods choose what to evaluate, recover full-benchmark results, and verify their reliability. From this analysis, we develop a taxonomy covering compression within individual benchmarks, across benchmark suites, and during adaptive evaluation, together with work on redundancy and reliability. We compare their information needs, total costs, reliability checks, and limitations. Methods reduce evaluation costs by selecting representative subsets, using cheaper or reusable information, and testing adaptively, but risk poor coverage, inaccurate estimates, and sequential delays. The resulting taxonomy and practical guide help researchers choose, validate, and deploy methods for more efficient and reliable LLM evaluation.

---


### 648. [Teach Me After You Learn It: Lookahead Self-Distillation for RLVR](https://arxiv.org/abs/2610.18256)

**<font color=#1a73e8>作者：</font>** Zepeng Zhai, Meilin Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy self-distillation (OPSD) has emerged as a popular training paradigm for LLMs, providing dense, token-level supervision by aligning a model's own distribution with the distribution induced by privileged information. However, existing OPSD methods derive supervision solely from privileged information of the same instance, leaving inter-instance supervision largely unexplored. We propose Lookahead Self-Distillation (LEAD), which introduces inter-instance distillation by allowing the teacher to first learn from other on-policy rollouts before teaching the student. LEAD constructs lookahead teachers through virtual RL updates on disjoint subsets of on-policy rollouts, and uses each teacher to provide cross-group token-level supervision for the other subset. To reconcile the complementary yet potentially conflicting signals from OPSD and RLVR, we introduce harmonious modulation, which adaptively modulates the GRPO advantage based on the agreement between the two signals. Extensive experiments on scientific reasoning and interactive-agent benchmarks show that LEAD achieves the best in-domain average performance across model scales while maintaining out-of-domain generalization comparable to GRPO.

---


### 649. [Encrypted Skills Can Become New Security Exploits If AI Agents Know How to Decipher](https://arxiv.org/abs/2610.18262)

**<font color=#1a73e8>作者：</font>** Yan-Lun Chen, Pin-Yu Chen, Chia-Mu Yu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Third-party skills can expose LLM agents to malicious instructions hidden by encoding. We introduce Ciphered Skill Injection (CSI), which embeds such instructions in skill files for agents to decode and follow. We evaluate Caesar and layered variants across eight models and 139 injection-task pairs, separating instruction recovery from attack success. In the primary setting with shortened skills, the variants achieve attack success rates of up to 47.5% and 40.3%, respectively. Successful decoding does not guarantee attack success, and layering has model-dependent effects. The tested skill scanners rarely flag injected skills. These findings highlight the risk of promoting decoded, untrusted content into actionable instructions.

---


### 650. [PAINT: A Framework for Multilingual Pain Representation from Medical Licensing Exams to Real-World Clinical Texts](https://arxiv.org/abs/2610.18269)

**<font color=#1a73e8>作者：</font>** Boya Zhang, Yuanchao Ma, Jiageng Wu 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Pain is one of the most common and clinically important symptoms, reflecting disease onset, progression, and treatment response. However, pain is difficult to accurately capture and interpret from medical text, as its expression varies across languages, documentation types, and patient demographics, and is often embedded in terminology, negation, temporality, and contextual descriptions. Existing pain-related studies remain largely monolingual or limited to narrow clinical settings. In this study, we introduce PAINT, a multilingual framework for studying pain representation across medical exams and real-world clinical texts. PAINT includes nine pain-focused dataset partitions spanning English, Spanish, Portuguese, and Japanese, with clinician annotations in all four languages. We curated a structured schema covering pain relevance, pain presence, anatomical location, pain descriptors, and demographic information. To capture multilingual pain representations, we leverage large language models (LLMs) and adopt an ensemble strategy to improve performance. Ten clinicians across four languages validate the labels: the ensemble reaches macro-F1 of 0.91-1.00 on pain relevance and pain presence and 92-100% accuracy on demographics, with inter-annotator $\kappa$ of 0.82-1.00. We release the WorldMedQA-Pain ensemble labels, the extraction pipeline, validation scripts, and clinician annotation sheets for publicly licensed corpora, providing a foundation for pain-centered clinical NLP and for studying pain documentation across languages and healthcare contexts.

---


> [!TIP]
> 当前位于：**601-650**（第 13/17 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-600](./part-12.md) | **601-650** | [651-700](./part-14.md) | [701-750](./part-15.md) | [751-800](./part-16.md) | [801-810](./part-17.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
