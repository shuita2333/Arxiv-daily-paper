# 🧠 大模型相关研究 | 2026年10月07日

> 本类共 **505** 篇论文：已确认 **467** 篇，待复核 **38** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**301-350**（第 7/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-505](./part-11.md)

---

### 301. [More Than Words: Compositional Tokenization for Efficient Language Models](https://arxiv.org/abs/2610.05597)

**<font color=#1a73e8>作者：</font>** Yuval Reif, Guy Kaplan, Roy Schwartz  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models process and generate text sequentially in token units, and the tokenizer determines how much text each inference step covers. Under standard tokenization, a short English phrase such as "On the table." is usually produced as four separate predictions for the preposition (On), article (the), noun (table), and punctuation (.), where each consumes a sequence position and adds inference cost. We introduce CoBPE, a compositional tokenization approach that represents such phrases as a lexical base token (table) attached with a small set of reusable surface modifiers, composed in embedding space at input and predicted jointly at output. In controlled pretraining from scratch at 780M and 1.3B scales, CoBPE shortens sequences by 30% and improves average downstream performance by 1.2 points relative to standard BPE under matched training compute. Our results suggest that part of what is now expressed through token sequences can instead be modeled through structured representations, opening a broad design space for more token-efficient and capable language models.

---


### 302. [An LLM-in-the-loop RL Framework for Bioinformatics Feature Selection](https://arxiv.org/abs/2610.05600)

**<font color=#1a73e8>作者：</font>** Xinyuan Wang, Deepti Agrawal, Yanjie Fu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> High-dimensional bioinformatics data, characterized by a large number of features relative to the number of samples, pose major challenges such as the ``curse of dimensionality,'' leading to overfitting, high computational cost, and poor generalization. Traditional feature selection methods often suffer from limited scalability and adaptability in such domains. We propose an LLM-in-the-loop reinforcement learning (RL) framework for bioinformatics feature selection, where the RL agent formulates feature selection as a sequential decision-making task, while the large language model (LLM) enhances the process in two ways: (1) guiding exploration through domain-informed advice, and (2) providing hybrid rewards that integrate data-driven performance with knowledge-driven evaluation. The LLM also produces explanations to improve interpretability for human experts without altering the RL policy update. Experiments on diverse bioinformatics datasets show that the LLM-in-the-loop framework outperforms baselines, achieves stable performance across downstream models, and converges faster than pure RL.

---


### 303. [DREAM: Dynamic Resolution Assignment For Multimodal Multi-agent Debate](https://arxiv.org/abs/2610.05615)

**<font color=#1a73e8>作者：</font>** Khanh-Binh Nguyen, Van Dai Do, Tien Anh Nguyen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent debate (MAD) has emerged as an effective paradigm to improve the reasoning capabilities of large language models (LLMs) and is increasingly being extended to multimodal settings. However, existing multimodal MAD frameworks typically expose agents to the same fixed visual input, ignoring substantial variation in the visual scale needed across samples and agents. In addition, these frameworks frequently suffer from groupthink, a phenomenon where agents prematurely abandon correct deductions to conform with confident but hallucinated peer responses. To address these bottlenecks, we introduce DREAM (Dynamic Resolution Assignment For Multimodal Multi-Agent Debate), which operates via two core components: (1) Dynamic Resolution Assignment, a zero-shot probe round where agents test multiple resolutions, quantify uncertainty using Average Normalized Log-Likelihood (ANLL), and use an adaptive threshold to assign each agent to its empirically optimal resolution; (2) Uncertainty-Guided Rollback Aggregation counters groupthink by tracking each agent's uncertainty over rounds and restoring early low-uncertainty answers overridden by group pressure. On six multimodal datasets, DREAM improves the accuracy-token trade-off over multi-agent debate baselines by 1.5-3.2% accuracy without dataset-specific tuning.

---


### 304. [A Framework for Automated Multi-Source Satellite Data Analytics and LLM-Based Report Generation](https://arxiv.org/abs/2610.05625)

**<font color=#1a73e8>作者：</font>** Hind Yousif Alhammadi, Isam Mashhour Al Jawarneh  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper presents the workflow for building an automated ArcGIS Pro tool using ArcPy to extract the Land Surface Temperature (LST) from Landsat 7, 8 and 9 datasets. The tool eliminates the need for manual band selection and repetitive raster computations by automating the multi-step workflow of radiometric calibration, NDVI-based emissivity correction, and thermal conversion. In addition to supporting batch and single-scene processing, the tool has an optional Large Language Model (LLM) for statistical result interpretation and reporting. Depending on batch size, the tool reduced the processing time from around 11-58 minutes when done manually to around 4-11 minutes using the tool. We tested the tool with data from Ras Al Khaimah (RAK) in the UAE, and the LST obtained for Ras Al Khaimah ranged from approximately 25C to 50C, demonstrating an accurate LST mapping compatible with the weather conditions of RAK. In summary, our tool reduces human errors and improves processing accuracy and efficiency for thermal and environmental remote sensing applications, in addition to providing an interactive LLM-based interface for result interpretation.

---


### 305. [Atomic Visual Entailment: Enhancing Zero-Shot Vision-Language Reasoning through Atomic Fact Decomposition and Learned Selection](https://arxiv.org/abs/2610.05630)

**<font color=#1a73e8>作者：</font>** Nallathambi Vethiappan, Derya Soydaner, Gijs Wijnholds  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Visual entailment (VE) asks whether an image supports, contradicts, or leaves undecided a textual hypothesis. Strong results come from fine-tuning large vision-language models on labelled data, while zero-shot and hybrid approaches remain far behind. A VE hypothesis often bundles several visual claims, yet existing zero-shot methods reason over it as a single unit. We propose Atomic Visual Entailment (AVE), which decomposes the hypothesis into atomic facts, produces candidate predictions from both the full hypothesis and its facts using frozen vision-language models, and predicts the final label with a lightweight classifier trained only on how those candidates behave. We find that decomposition helps only when the hypothesis context is preserved: judging facts in isolation is worse than not decomposing at all. Full-hypothesis and atomic prediction make complementary errors, and learning which to trust recovers far more of that complementarity than majority voting, reaching 0.803 test accuracy on SNLI-VE without fine-tuning any vision-language model. AVE also localises the visual evidence behind its prediction without region-level supervision. These results suggest that learning which candidate prediction to trust can close much of the gap to fine-tuned systems, offering a practical alternative where fine-tuning a vision-language model directly would need more labelled data or compute than is available.

---


### 306. [The GenAI4IDN Benchmark 3.0 - a Public Tool to Assess Generative AI Tools for the Design of Interactive Digital Narratives](https://arxiv.org/abs/2610.05633)

**<font color=#1a73e8>作者：</font>** Hartmut Koenitz, Jonathan Barbara, Mirjam Palosaari Eladhari  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper presents GENAI4IDN Benchmark 3.0, the third iteration of an evaluation framework to assess Generative AI tools for creating Interactive Digital Narratives (IDNs). Moving beyond manual testing, this iteration introduces AI-assisted evaluation through a publicly accessible web application (this https URL), enabling the community to run benchmarks on demand, add new models, and propose new tasks. The revised evaluation framework is "blinded" to avoid model-bias, and can handle complex media such as music, videos, and full IDNs that previously required human raters. A significant addition - responding to concerns raised during ICIDS 2025 - is the addition of fact-checking and bias detection with dedicated tasks and rubrics, validated by human raters with lived experience in the depicted contexts. Findings from a diverse range of models report on maturing creative capabilities while observing runaway thinking and overzealous safety filters as limitations. Fact-checking reliably caught subtle historical inaccuracies, anachronisms, and fabricated claims while the bias rater consistently exposed structural assumptions, tropes, and marginalized group erasures.

---


### 307. [Visual Grounding Safety in Vision-Language Models](https://arxiv.org/abs/2610.05637)

**<font color=#1a73e8>作者：</font>** Erfan Shayegani, Kundan Krishna, Yue Dong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) are increasingly trained to generate structured outputs like points and bounding boxes that downstream interfaces, agents, and robots can act on, yet safety alignment of this output channel has not been systematically analyzed. We study visual grounding safety by repurposing three safety benchmarks spanning direct harm (VLSU), social bias (BBQ-V), and situational safety (Asimov-2.0) into 15,401 matched pairs of harmful requests that differ only in the requested output: a free-text answer (VQA) or a grounding (point or bounding box). Across five VLMs, models that refuse a harmful request posed as a question often comply when the same request asks for a grounding: averaged over models, grounding refusal trails VQA refusal by 31-59 percentage points, depending on the domain, and safety system prompts do not close this gap. We propose a fine-tuning approach that combines grounding-form refusals with capability grounding data and self-distilled benign data to counter over-refusal. For Qwen3-VL-8B and VisionReasoner-7B, it improves grounding refusal by 77-95 percentage points on VLSU and BBQ-V and by 64-85 points on the held-out Asimov-2.0 domain, while also improving VQA refusal, preserving grounding capability, and keeping over-refusal limited. Representation analysis shows that fine-tuning moves harmful requests toward each model's refusal direction, most strongly for grounding, while leaving benign requests near the harmless reference.

---


### 308. [StageVLN: Spatial and Trajectory Auxiliary Guidance for Efficient Vision-Language Navigation](https://arxiv.org/abs/2610.05664)

**<font color=#1a73e8>作者：</font>** Anh Dao, Quan-Dung Pham, Le Danh Vinh 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-and-Language Navigation (VLN) policies increasingly benefit from strong semantic priors provided by large vision-language models (VLMs). However, standard action supervision does not explicitly encourage intermediate representations to preserve scene geometry, relative orientation, or global episode progress. Incorporating depth estimators, explicit maps, point clouds, or geometry foundation models at inference can provide such structure but introduces additional computation, memory overhead, and architectural dependence during deployment. We introduce StageVLN, a training framework that shapes navigation representations through privileged spatial and trajectory guidance while preserving the original inference pathway. A frozen geometry foundation model provides multi-level spatial guidance to hierarchical navigator states, while relative-heading and expert-route progress objectives provide complementary trajectory-state supervision. All auxiliary components are used only during training and removed at deployment. On R2R-CE validation-unseen, StageVLN achieves 56.3\% SR and 51.4\% SPL with a 4B-parameter backbone, without an additional geometry encoder at inference. On RxR-CE, it achieves 54.3\% SR without additional navigation training data or a geometry encoder at inference.

---


### 309. [How Should a Prompt Optimizer Spend a Tight Budget? BudgetAPO with Noise-Adaptive Evaluation](https://arxiv.org/abs/2610.05671)

**<font color=#1a73e8>作者：</font>** Haoyue Liu, Zhichao Wang, Huanyu Yan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automatic prompt optimization (APO) has been widely employed to adapt large language models without updating their weights, yielding promising results. However, existing methods such as GEPA and OPRO assume hundreds to thousands of subject-model calls, far more than is practical behind paid, rate-limited APIs. Under tight budgets they fail in two ways: multi-stage pipelines can exhaust the budget and return the seed prompt unchanged, while single-stage methods compare candidates on fixed-size minibatches, regardless of each task's noise. As a remedy, we introduce BudgetAPO, a single-stage optimizer for the tight-budget regime. BudgetAPO incorporates (1) a noise-adaptive rule that sizes the evaluation slice to each task's noise, measured by a short probe; (2) a fixed slice that turns every accept/reject decision into a paired comparison; and (3) a reflective operator that rewrites reasoning strategy and output format jointly. Extensive results across seven benchmarks and five subject models demonstrate that BudgetAPO ranks first on every subject and beats every baseline under Holm-corrected paired tests, while returning the seed in 13% of runs at 250 calls against 86% for GEPA. On GPT-OSS-20B, GEPA needs 4.5 times as many calls to match BudgetAPO's 100-call score.

---


### 310. [Knowing the Rules, Applying the Rules: Evaluating Language Models on Traditional Chinese Bazi](https://arxiv.org/abs/2610.05682)

**<font color=#1a73e8>作者：</font>** Jiulin Li, Ping Huang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Knowing domain rules does not guarantee applying them to a case. We study this distinction in traditional Chinese Bazi through 3,000 Chinese multiple-choice questions spanning 14 Theory and 11 Case categories. Six endpoint systems are evaluated, with primary results reported on a 2,492-item model-informed refinement. Theory accuracy exceeds Case accuracy for every system, and gaps of 16.60-29.56 percentage points remain when invalid responses are excluded. The contrast is more specific than a general case-reasoning deficit. Across six systems, Twelve Stages and Nayin reach mean accuracies of 89.10% and 88.62%, while Shensha Basics reaches 75.96%. Within Case, Luck Pillars averages 84.62%, but Career and Family Relations average only 36.98% and 38.19%. Overall rankings also conceal different category strengths. On the original 3,000 items, paired DeepSeek native/disabled comparisons associate native configurations with Theory gains of 6.53 and 12.20 points for Flash and Pro, respectively; Case changes are -3.67 and +1.27 points. These are provider-configuration associations, not isolated causal effects of reasoning. The results motivate task-specific evaluation of cultural-domain applications rather than reliance on aggregate knowledge scores. The benchmark measures agreement with a model-generated, model-verified answer key, not real-world predictive validity. Final-set results are post-selection descriptions, and incomplete provenance and expert validation constrain their interpretation.

---


### 311. [Spend Bytes on Breadth: Precision-Count Trade-offs for Decode-Time KV Compression in Long Chain-of-Thought Reasoning](https://arxiv.org/abs/2610.05685)

**<font color=#1a73e8>作者：</font>** Runguo Li  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reasoning models write most of their KV cache while decoding long chains of thought (CoT), so the cache has to be compressed online under a fixed memory budget. Decode-time methods mostly decide which tokens to evict. We ask how a fixed byte budget should be split between the number of cached tokens and their precision. BreadthKV spends the bytes on more tokens at low precision, combining quantization with eviction, and picks the bit-width for each model and budget with a 60-problem end-to-end calibration, since offline attention error does not predict it reliably. On three reasoning models and four math and science benchmarks, it scores above eviction alone in 17 of 18 settings and produces shorter outputs. Much of what eviction loses comes from derailed runs, which keep reasoning until the length cap without reaching an answer. On Qwen3-8B at our tightest budget, eviction sends 91% of AIME samples to the cap and BreadthKV 40%. Under the same protocol, BreadthKV is statistically indistinguishable from a joint rate-distortion allocator (RDKV) that uses 27% more KV memory-time, and it outperforms our re-implementation of ThinKV.

---


### 312. [From Token-Max to Outcome-Max: How You Use AI Determines Its Productivity](https://arxiv.org/abs/2610.05697)

**<font color=#1a73e8>作者：</font>** Chen Xu, Mengqiao Liu, Beibei Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative artificial intelligence (AI) models can perform increasingly complex tasks, yet greater AI usage does not necessarily translate into proportional productivity gains. We identify token-max as one source of this inefficiency: when token consumption is treated as productive effort, agents are encouraged to over-exert and expend computation beyond what is necessary. We instead propose outcome-max, which rewards independently verified task completion per unit cost and induces a principled stopping rule. Then, to study these objectives, we develop a three-level simulation framework spanning immediate interaction, long-run behavioral adaptation, and organizational collaboration. Across all three levels, outcome-max improves the efficiency of AI-assisted production while largely preserving verified task performance. To further align these incentives with outcome-max, we introduce OutcomeShare, an incentive mechanism. Theory and simulation show that OutcomeShare can induce participation while generating shared gains for employees, firms, and LLM providers. Together, our results suggest that AI productivity not only depends on model capability, but also on how to construct the objectives governing AI use.

---


### 313. [Voltic: Distinguishing Volatility from Stochasticity in Recurrent Memory](https://arxiv.org/abs/2610.05700)

**<font color=#1a73e8>作者：</font>** Parsa Hejabi, Morteza Dehghani, Payam Piray  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recurrent sequence models must decide how strongly to overwrite their memory at each token. Read as Bayesian filtering, this write is the gain of a Kalman update, set by uncertainty from two sources that pull it in opposite directions: volatility, how quickly the underlying associations change, and stochasticity, how noisy each observation of them is. First, we show that the update of gated delta-rule memories is the form this filter takes under isotropic uncertainty. Next, we introduce Voltic, a recurrent memory that keeps the covariance anisotropic and makes both noise variances input-dependent, so the write is vector-valued and carries uncertainty accumulated over the sequence. A dense covariance would have to be propagated token by token, ruling out the parallel training these models depend on. We therefore give two assumed-density approximations, diagonal and quasi-diagonal, both of which leave the memory update in delta-rule form and reuse its chunked kernels. On controlled recall tasks in which associations change and observations are corrupted, Voltic leads all baselines. On the task combining volatility and stochasticity, its margin over the strongest baseline is larger at both extrapolation sizes than at the training sizes. In 45M-parameter language models it leads an eight-task reasoning average and achieves higher retrieval accuracy beyond the training context length than gated baselines, at throughput close to those baselines. Deriving the write from an uncertainty recursion therefore makes memory more responsive to change.

---


### 314. [Rotated, but How Far? Diagnosing and Improving Object-Rotation Reasoning in VLMs](https://arxiv.org/abs/2610.05715)

**<font color=#1a73e8>作者：</font>** Zhaochen Wang, Yujun Cai, Huangbo Zou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) can detect that an object has rotated across views, but cannot reliably tell by how much. We introduce OR-Bench, a fine-grained benchmark for object-rotation reasoning with eight tasks covering rotation detection, rotation magnitude estimation, and multi-view rotation reasoning. Across 12 VLMs, the gap is stark: the strongest models approach 100% accuracy on detection, yet even coarse magnitude estimation is near chance. When asked for exact angles, models place 91.8--100% of their predictions on just $0^\circ$, $90^\circ$, and $180^\circ$, a failure we term canonical-angle collapse. This collapse persists even without visual input. Representation probing shows that missing information is only part of the explanation. Although rotation information becomes less recoverable at finer granularity, substantial coarse-grained information remains, and a simple linear probe outperforms the models' generated answers. This suggests that VLMs underuse rotation information they already encode. We therefore propose RotationCue, a lightweight decoder that recovers coarse rotation information from the VLM's own frozen representations and feeds it back to the model as intermediate textual context. Across three VLMs, RotationCue improves every model--task combination on OR-Bench, raising macro-average accuracy by 7.9--12.6 points while preserving general capabilities.

---


### 315. [FreSia: Frequency-Semantic Instantiation and Alignment for Multivariate Time Series Analysis](https://arxiv.org/abs/2610.05726)

**<font color=#1a73e8>作者：</font>** Yubo Wang, Hui He, Hezhe Qiao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have shown strong potential in multivariate time series forecasting and anomaly detection. Existing studies predominantly inject temporal information into LLMs via direct numerical tokenization or heuristic textual descriptions. However, LLMs still face difficulty in perceiving the underlying structural patterns of numerical time series, particularly the seasonal and trend components obscured by discrete numerical tokens. To bridge this gap, we propose FreSia, a frequency-aware framework that establishes an effective alignment between the semantic space of LLMs and the frequency space of time series. Specifically, FGPrompt, a Frequency-Guided Prompt mechanism within FreSia, distills the frequency-domain structures of time series and projects them into prompts tailored to the semantic space of LLMs. Furthermore, we introduce a Global-driven Context Learning (GCL) component, which uses a global CLS-driven probe to generate global context to bridge the time-frequency domain gap and fuse the multi-modal information. Experiments on eight forecasting benchmarks show that FreSia achieves average improvements of 13.48% and 8.06% in MSE and MAE, respectively.

---


### 316. [PACMI: Provenance-Aware Cascading Memory Invalidation for Long-Term LLM Agents](https://arxiv.org/abs/2610.05732)

**<font color=#1a73e8>作者：</font>** Yiqi Wang, Jiaqi Liu, Jiaqi Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM agents rely on long-term memory to retain and reuse information when performing tasks over long horizons. Existing methods provide limited support for handling memories that become outdated as new observations or domain evidence arrive. Such outdated memories may remain semantically relevant, continue to affect dependent records, and retain value as historical evidence. This calls for two capabilities: dependency tracking to identify downstream effects and historical preservation to retain useful past records. We propose Provenance-Aware Cascading Memory Invalidation (PACMI), a framework that represents memories and new evidence in a provenance graph with typed dependency edges. PACMI assigns records to a four-state validity lattice, propagates validity changes to dependent memories, and uses the resulting states for retrieval and stale-premise detection. We also introduce a diagnostic benchmark with 100 cases and 300 queries across five domains. The evaluation separates node, context-, and answer-level performance. PACMI achieves the highest final-answer accuracy on this benchmark, and its paired difference from the strongest baseline is significant under an exact McNemar test. The premise checker achieves perfect precision, recall, and F 1 on the controlled query distribution. Cascading propagation primarily improves memorystate correctness: removing it increases final-answer errors from 3 to 11, but the paired difference does not reach the 0.05 significance threshold. Code and data will be made publicly available.

---


### 317. [HLA-WM: Hybrid Linear Attention for Long-Horizon Video World Models](https://arxiv.org/abs/2610.05739)

**<font color=#1a73e8>作者：</font>** Zhuokun Chen, Feng Chen, Xi Lin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-horizon video world models require persistent memory to preserve scene consistency over extended rollouts. Softmax attention retains the full generation history through a growing KV cache, whereas recurrent linear attention compresses history into fixed-size states with substantially lower memory cost. However, we identify severe long-range forgetting in Gated DeltaNet (GDN), where information from distant but relevant scenes is progressively attenuated by subsequent state updates. To address this limitation, we propose HLA-WM, a training-free hybrid linear-attention framework that combines coarse-grained geometry-guided retrieval with fine-grained recurrent linear-state computation. HLA-WM exploits the affine structure of GDN to cache compact chunk-wise transition summaries, retrieve scene-relevant historical chunks using camera geometry, and recompose them into query-specific recurrent states. On the $60$-second SANA-WM-Bench, HLA-WM improves all six aggregate revisit-consistency and camera-control metrics of the base autoregressive generator without additional training, including a $0.74$ dB PSNR gain and a $28.5\%$ reduction in rotation error. The improvements persist after downstream refinement and generalize to MBench-A, where HLA-WM consistently improves all three revisit-consistency metrics across all four subsets and all evaluated inference modes over $547$ samples. At a $60$-second context, HLA-WM reduces historical-state memory by $12\times$ relative to full KV caching while incurring at most a $1.6\%$ reduction in inference throughput. These results demonstrate that selectively addressable recurrent memory can improve long-range scene recall while preserving the efficiency advantages of GDN. Project page: this https URL

---


### 318. [CIPHER-MoE: Balancing Efficiency and Routing Fidelity in Trillion-Scale MoE Training](https://arxiv.org/abs/2610.05744)

**<font color=#1a73e8>作者：</font>** Jing Li, Jian Meng, Yingmeng Gao 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) has been widely adopted in recent large language model (LLM) architectures. However, scaling up MoE in LLM training introduces system-level challenges on training, where non-uniform token routing can lead to highly imbalanced workloads across experts and devices, further destabilizing the training process. With trillion-scale LLMs, imbalanced expert workloads further amplify the resource cost of MoE training, resulting in degraded training efficiency and hardware utilization for underloaded experts, while hot experts require additional resources to accommodate excessive workloads. Recent studies address imbalanced MoE training through intricate parallelism strategies or resource reallocation. However, these system-level approaches often introduce additional resource requirements and considerable orchestration complexity, which become increasingly difficult to afford when training trillion-parameter LLMs under constrained computational resources. This work introduces CIPHER-MoE, which mitigates MoE workload imbalance while keeping the router's token-side Top-K selection unchanged. CIPHER-MoE applies affinity-aware Expert-to-Token filtering with explicit capacity control to reduce hotspot expert workloads without additional hardware resources or complex runtime design. The proposed method has been evaluated on large-scale MoE models, including DeepSeek-V4-Pro, showing up to 64.9 percentage points Top-1 expert workload reduction and 1.10$\times$-1.94$\times$ training acceleration, while preserving the training quality. The source code will be released soon.

---


### 319. [Beyond In-Distribution Preservation: Recovering Generalization in Quantized VLAs via Vulnerability-Oriented Tuning](https://arxiv.org/abs/2610.05745)

**<font color=#1a73e8>作者：</font>** Shen Ruan, Wenchang Gao, Jin Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-training quantization has been shown to preserve VLA performance under standard evaluation conditions, but whether it preserves the full-precision model's robustness and generalization remains underexplored. In this study, we systematically study the robustness and generalization of post-quantized VLA policies under environmental disturbances. Empirical results show that quantized policies can become fragile to subtle environmental variations despite retaining comparable in-distribution performance. We further observe that action discrepancies are concentrated in a small subset of rollout states, while teacher guidance has opposite effects depending on discrepancy: it improves generalization at high-discrepancy states but can degrade it at low-discrepancy states. These findings reveal that effective post-quantization recovery requires selectively intervening on vulnerable states rather than globally distilling the student. We therefore propose Policy-Induced Vulnerability-Oriented Tuning (PIVOT-Q), a vulnerability-aware On-Policy Distillation (OPD) framework that selectively corrects vulnerable states encountered during quantized-student rollouts using the frozen full-precision policy as a teacher. PIVOT-Q identifies vulnerable states using discounted accumulated discrepancies over a short horizon, applies phase-balanced sparse supervision, and uses a Behavioral Anchor to prevent unnecessary changes. Experiments under seven LIBERO-Plus environmental variations demonstrate consistent recovery across multiple VLA backbones and quantization methods. Notably, PIVOT-Q consistently outperforms full-state distillation across all settings while using only 7.4% of its state-level distillation budget. Our code is available at this https URL.

---


### 320. [InteractionBench: A Real-Time Interaction Benchmark for Streaming Video Systems](https://arxiv.org/abs/2610.05775)

**<font color=#1a73e8>作者：</font>** Enxin Song, Suhao Yu, Yifei Xu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A video assistant must speak when its instruction warrants a response and stay silent otherwise. We introduce a benchmark that evaluates this decision for the complete system of model, memory, and response controller. InteractionBench covers query responses, event triggers, and ongoing updates in 1,060 interactions over 812 videos, with 69 negative streams and 53 suites that pair counted events with look-alike near misses. It scores content accuracy, timing accuracy, and silence compliance on the video clock. Timely speech costs silence across systems. Polled Qwen3-VL-8B reaches 77.8 timing accuracy but 10.9 silence compliance. A native real-time interaction system reaches 29.2 silence compliance at 66.8 timing accuracy, yet emits on 89.9% of negative streams. No open-weight system clears a third of the near-miss suites. Fewer replies help only when chosen, as random deletion merely trades timing for silence. Offline scores miss these failures and mispredict online behavior. Adding restraint is costly, as the native system's controller adds little by itself and agentic systems add it only at about 30 s per this http URL page: this https URL Code: this https URL Data: this https URL

---


### 321. [Mining Agent Skills from Production Traces](https://arxiv.org/abs/2610.05777)

**<font color=#1a73e8>作者：</font>** Yue Ran Kang, Colton Mikolajczyk, Chhaya Methani 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent skills that record procedural instructions are increasingly mined from execution traces rather than curated by hand. Skill-mining pipelines often use known task outcomes or feedback to guide skill construction. In production, reliable information on whether a run has succeeded may be unavailable. We study how the sampling of execution traces, access to success or failure information, and the form of the mined skills affect downstream task performance. Holding the mining pipeline fixed, we compare six combinations of mining evidence and skill forms. Mining evidence has three levels: successful trajectories only, successes and failures with their outcome labels, or the same mix with labels withheld. Skill form has two types: an ordered workflow plan, or a declarative ontology of entities, states, and policies. We evaluate the mined skills on two enterprise benchmarks, ThinkingBox-Bench and APEX-Agents. Analysis of task-level paired differences shows that the benefits of different configurations of mining evidence and skill forms depend on the enterprise domain. On ThinkingBox-Bench, paired differences show that workflows score better than ontology by 1.7 pp, Goldilocks beats success-only evidence type by 2.4 pp and Goldilocks blind simulating skills learnt without outcomes is worse by 3.1 pp. APEX-Agents shows a moderate preference for ontologies and no clear preference between evidence regimes. Within each domain, task structure related constraints drive uneven performance with mined skills. These findings motivate tailoring meta-skills to the demands of the target tasks rather than adopting a one-size-fits-all approach.

---


### 322. [MedicalHarness: A Controlled Evaluation of LLMs and Agent Harnesses on Medical Tasks](https://arxiv.org/abs/2610.05778)

**<font color=#1a73e8>作者：</font>** Ziqing Wang, Lili Zhao, Kaize Ding  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM agents are increasingly built for medical work and scored on clinical benchmarks. Each such score, however, comes from a model running inside an agent harness, the system that controls the loop between the model and its environment. An agent's score is therefore a property of a model--harness pair. For medical agents, how much outcomes change with the harness has rarely been measured. Measuring this change, and explaining it, raises two challenges. First, a harness comparison must change nothing but the harness and be repeated across models and kinds of task. Second, comparing whole harnesses leaves their mechanisms bundled together, so it cannot show when an individual mechanism helps. To address these challenges, we present MedicalHarness, a controlled study of models and agent harnesses on medical tasks. We first build MedicalHarnessBench to evaluate agents on $107$ tasks across four domains that each test a different harness capability. Using this benchmark, we run five open-weight models under five agent harnesses, changing only the harness within a comparison, and analyze both outcomes and execution traces. To study individual mechanisms, we build MH-Lab, a controlled harness that switches off context management, planning or tool exposure one at a time within a shared execution loop. We find that the harness and its interaction with the model account for about a quarter of the outcome variance, and that no single harness is best across models and tasks. Code and data are available at this https URL.

---


### 323. [Agentic-ZTA: A Multi-Agent Architecture for Autonomous Zero Trust Enforcement](https://arxiv.org/abs/2610.05782)

**<font color=#1a73e8>作者：</font>** Shovan Roy, Lopamudra Praharaj, Maanak Gupta 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic AI is emerging as a promising paradigm for automating complex cybersecurity decisions, yet its use in enforcing zero trust introduces significant challenges in safety, reliability, and policy compliance. This paper presents Agentic AI based zero trust architecture (Agentic-ZTA) that operationalizes the NIST SP 800-207 ZTA architecture control loop through coordinated multi- agent decision pipeline. In the proposed framework, policy knowledge is embedded into a retrieval-augmented generation pipeline and retrieved at inference time as top-k relevant policies. Access requests are intercepted by the Policy Enforcement Point (PEP), enriched with contextual metadata. The request context is routed to a policy engine agent which invokes domain-specialized core agents first followed by supporting agents, if further evaluation needed. AI agents reason over access context, policy constraints and determine trust. The retrieved policies are embedded into agent prompt during inference time and agentic trust scores are aggregated and evaluated by a trust-algorithm, producing the final access decision for enforcement under continuous verification. We implement Agentic-ZTA in a testbed and evaluate it on representative access-control use cases scenarios. Our Agentic-ZTA framework achieves 95.0% accuracy, 93.9% precision, and 96.3% recall, and demonstrate the feasibility of enforcing zero trust using AI agents.

---


### 324. [A Testable Theory of Atomic Features](https://arxiv.org/abs/2610.05794)

**<font color=#1a73e8>作者：</font>** Kenny Peng, Jon Kleinberg, Nikhil Garg  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We develop and test a theory of language model representations in which there exist atomic features. Our main theoretical insight is that in such a model, sparse dictionaries (e.g., SAEs) of increasing size recover an increasing prefix of the most prevalent atoms in the training data. This "recovery principle" yields three testable predictions: many features in small SAEs are shared by all larger SAEs, SAEs trained on different data share features prevalent in both, and sufficiently large SAEs recover both parent and child features. In contrast to conventional wisdom that SAE features are unstable and "split" as size increases, we find that these predictions hold on SAEs of sizes ranging from 512 to 131,072 trained on two large embedding models. From a theoretical perspective, our results suggest the promise of a scientific theory of representations based on atomic features. Practically, our results suggest the promise of scaling SAEs.

---


### 325. [Nash Equilibrium Text: A Game-Theoretic Decoding Framework for Text Generation](https://arxiv.org/abs/2610.05817)

**<font color=#1a73e8>作者：</font>** Alireza Jafari, Arman Adibi, Mohammad Ghavamzadeh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Text revision has become an integral component of large language models. This paper formulates revision such that it admits a Nash equilibrium: Token positions are players, vocabulary items are actions, and each player's utility is the language model's log conditional probability. We motivate the revision by showing that Nash equilibria can have exponentially higher likelihood than autoregressive outputs as the sequence length grows. We further propose Nash decoding, an algorithm that reaches an $\varepsilon$-Nash equilibrium in $O(1/\varepsilon)$ time given access to the joint probability of tokens conditioned on a prompt. In practice, we run Nash decoding using conditional probability estimates from large language models and evaluate the resulting equilibria on question-answering benchmarks. On CLAPNQ, PubMedQA, and CoQA, Nash equilibria obtained from masked language models achieve higher F1 and ROUGE scores than autoregressive models up to $18\times$ larger, without any fine-tuning or retraining, at the cost of additional test-time computation.

---


### 326. [Supporting Couples' Social Well-being in Daily Life: A Needs Assessment and Co-design with Co-located Couples](https://arxiv.org/abs/2610.05822)

**<font color=#1a73e8>作者：</font>** Yuna Naito, Timothy Bickmore, Varun Mishra 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Romantic relationships shape physical, mental, and social well-being, and relationship quality is built through everyday interactions. Addressing minor issues early and reinforcing positive interactions help maintain relationship quality, and ubiquitous computing creates new opportunities to sense and support couples' relationships in daily life. However, existing systems remain largely developed with limited involvement from couples, raising questions about which types of sensing and support couples may accept in their private lives. To address this gap, we conducted exploratory needs-assessment interviews and co-design sessions with five co-located couples (10 participants) to identify their needs and preferences for relationship-attunement-enhancing technologies, including the use of LLMs. Couples' own designs converged on systems that detect meaningful moments---such as conflict onset---and offer subtle mediation rather than AI-generated advice, highlighting dyadic concerns around partners' agency, authenticity, and control over shared interaction data. We offer preliminary design implications for ubiquitous sensing and intervention systems that center the couple as a unit rather than the individual.

---


### 327. [Who Keeps the Gains from Personal AI Assistants? Seller Adaptation and the Unassisted in a Language-Model Market Simulation](https://arxiv.org/abs/2610.05823)

**<font color=#1a73e8>作者：</font>** Haonan Huang, Joey Xiao  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Personal AI assistants are beginning to transact for consumers, and early adopters capture real savings. Whether those savings survive, and what happens to consumers who have no assistant, depends on how sellers respond -- a question single-user evidence cannot answer. We build an agent-based rental market in which language models play consumers, assistants, and six adaptive sellers guided by an algorithmic pricing tool. Half the population receives an assistant under an advisory or an executing mandate; the contract pairs a fee only the renter's physical action avoids with a pre-selected add-on an authorised assistant can cancel online. An analytical benchmark and a behaviourally calibrated rule market supply ex-ante predictions, and paired branches with frozen versus adaptive sellers separate adoption effects from market feedback. Across thirty simulated markets, executing assistants cut adopters' spending by 13.7 USD per renter-day when sellers are frozen; adaptation claws back about a third, leaving 8.7, with the gains arriving both as lower bills and as rentals completed at all. Sellers raise headline rates while cutting fees, and the calibrated forecast of the burden on unassisted consumers (+3.6) does not transfer: their mean spending change is +0.4, confidence interval -0.6 to +1.3. Seller-model swaps and a within-market transfer of fee-setting to the pricing tool show that fee conduct, and with it the division of the gains, is decided on the seller side. Assistants, we conclude, should be evaluated at market level -- completion, total spending, and non-users included -- and the comparison layers locate exactly where a calibrated behavioural forecast fails in a language-model market.

---


### 328. [Measurement-First Auditing of Agentic Leaderboards: Contamination Susceptibility, Matched-Control Re-evaluation, and Scorer Validation](https://arxiv.org/abs/2610.05830)

**<font color=#1a73e8>作者：</font>** Dishu Yang, Qi Su, Hongbo Qin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic leaderboards increasingly evaluate systems on public benchmarks whose task statements and solution-bearing artifacts can remain accessible. We propose a measurement-first audit framework that distinguishes contamination claims according to the evidence required to support them. It separates three channels that require different evidence: training-time exposure, evaluation-time retrieval, and pipeline/scaffold leakage. Each channel is coded as open, partial, closed, or unknown under a fail-closed rule. Across nine Holistic Agent Leaderboard (HAL) configurations, none of the 27 channel assessments was coded closed, but incidents were confirmed in four configurations. We then apply the behavioral component of the framework to a reported file-localization gap on SWE-bench Verified, using an outcome-blind, same-repository matched-control design with symmetric prompt-leakage screening, paired and repository-aware uncertainty analyses, and scorer validation, evaluated on GPT-4.1 and DeepSeek-V4-Flash. Among the 100 pairs retained after symmetric screening and the pair-integrity exclusion, GPT-4.1 showed a $+10.0$-point pair-weighted Top-3 benchmark-associated gap, but the 95\% intervals from both the prespecified paired-bootstrap procedure and the post-hoc repository-balanced analysis included zero, leaving the benchmark-associated gap inconclusive. The reproduction scorer did not pass its validation gate: against consensus human labels, sufficient scorer sensitivity could not be established for either model, and both DeepSeek-V4-Flash firings on correct-gold comparisons were false positives. Without provenance evidence, appropriate controls, symmetric leakage screening, and validated scorers, stronger contamination claims are not warranted. The results do not establish training-data membership, contamination prevalence, or benchmark-induced score inflation.

---


### 329. [Request Order Matters: Cache-History Sensitivity in Selective KV-Cache Reuse for Rolling Agents](https://arxiv.org/abs/2610.05833)

**<font color=#1a73e8>作者：</font>** Tiffany Gu, Annie Guan, Manshu Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-running agents repeatedly call an LLM while retaining most of their document window, evicting old documents, and appending new ones. These rolling updates break exact prefix caching and motivate non-prefix KV-cache reuse with selective recomputation. We show that persistent KV-cache reuse with selective recomputation can be history-dependent: in our rolling-agent workload, an unchanged prompt can produce different answers depending on the requests processed before it. At a matched 5% recomputation budget, document-aligned recomputation reduces answer variation across request orders from 69.0% with CacheBlend's token top-$k$ policy to 26.1%. When each prompt is evaluated after a different sequence of preceding requests, document-aligned recomputation improves fidelity to full prefill by 34.5-52.5 percentage points over token top-$k$, while both policies achieve approximately 5.7$\times$ median TTFT speedup. Our ablation study shows that, in our rolling-agent workload, contiguity is the main factor associated with robust selective recomputation.

---


### 330. [Compromise Is Not Consequence: Evaluating Task-Scoped Authorization in LLM Agents with Paired Replay](https://arxiv.org/abs/2610.05840)

**<font color=#1a73e8>作者：</font>** Tural Hagverdiyev  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> A tool-using model can follow a malicious instruction even when its credentials are valid. We study whether task-scoped authorization contains the resulting tool execution. Our paired-replay testbed samples a model request once and submits the same action, resource, and arguments to broad bearer, scoped JWT, sender-constrained, and Open Policy Agent conditions. The frozen main experiment uses 128 scenarios across four tool domains and five local model configurations. Among valid attacked post-exposure decisions, broad-bearer harmful execution ranges from 8.9% to 37.8% across models; all three scoped conditions record zero. The policy changes execution, not the frozen model decision. These results support containment of the tested cross-action and cross-resource consequences under researcher-supplied task authority, not prevention of prompt injection. A bounded six-task AgentDojo extension preserves native scoring and records 11/24 injected broad-policy attack flags versus 0/24 scoped flags, with utility of 5/24 and 6/24. Low exposure, invalid decisions, and purposive task selection limit that comparison. The primary experiment measures safe continuation rather than final-answer correctness. An empirical-bank fresh-sampling comparison finds no estimation advantage from pairing when scoped outcomes are constant zero. The contribution is a controlled measurement of compromise, enforcement, and continuation, with explicit limits on what each observation establishes.

---


### 331. [HLA: Expressive Hybrid Linear Attention via Chunk-Wise Dynamic Mixing](https://arxiv.org/abs/2610.05842)

**<font color=#1a73e8>作者：</font>** Zhuokun Chen, Xi Lin, Xiyu Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Linear attention enables efficient long-context autoregressive decoding by compressing history into recurrent states, but this compression can make selective access to sparse and distant information difficult. Existing chunk-based extensions increase memory capacity, yet learned chunk-mixing coefficients may remain fixed with respect to input content and therefore cannot adapt historical access to each query. We introduce \emph{Hybrid Linear Attention} (HLA), a query-dependent chunk-level attention mechanism for Gated DeltaNet (GDN). HLA represents each completed chunk as an exact affine state transition and computes content-dependent routing gates from compact, self-attentively pooled representatives. Each gate interpolates the corresponding historical transition with the identity map, controlling both the chunk's additive memory and its transformation of earlier states. Effective-support regularization further encourages concentrated routing for sparse inference. We evaluate HLA under both pretrained adaptation and from-scratch training. Across Qwen3.5 models from 0.8B to 9B, HLA consistently improves over native GDN and fixed chunk mixing, with gains of up to 5.57 percentage points on LongBench-V2 and 3.97 points on RULER. In a controlled from-scratch 1.3B setting trained for 100B tokens with a 4K context, HLA also improves RULER performance from 4K to 32K, with gains increasing from 0.83 points at 4K to 4.22 points at 32K. These results demonstrate that query-dependent composition of recurrent memory improves long-context modeling and remains effective beyond the training context while using compact per-chunk affine summaries. Project page: this https URL

---


### 332. [Imagine to Act: High-Fidelity Data Synthesis via Image Editing World Model for Scalable GUI Agent Training](https://arxiv.org/abs/2610.05861)

**<font color=#1a73e8>作者：</font>** Yongxin Ning, Runliang Niu, Qianli Xing 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Graphical User Interface (GUI) agents have emerged as a promising paradigm for automating complex digital workflows across diverse applications. However, training highly capable and generalizable agents fundamentally relies on massive, high-fidelity visual-action trajectories, which are notoriously difficult to acquire. While human demonstrations are unscalable, existing GUI world models rely on text descriptions or HTML rendering, discarding crucial pixel-level visual details like icons and layout styles. To address this issue, we introduce Infinite-Dreamer, a simulation-free data synthesis method powered by a pixel-level Image Editing World Model. By conceptualizing GUI transitions as image editing tasks, we leverage Vision-Language Models (VLMs) to describe action-induced UI changes as structured delta-text. We then fine-tune an image editing backbone to controllably synthesize realistic screenshot transitions. We utilize this model to generate both single-frame visual robustness data and multi-step imaginary trajectories. To validate the effectiveness of our approach, we fine-tune the Qwen3-VL baseline solely on the synthesized data to obtain Infinite-Actor, and evaluate it on AndroidWorld, MobileWorld, and AndroidControl-Curated benchmarks. Infinite-Actor consistently outperforms the Qwen3-VL baselines across scales: Infinite-Actor-8B improves AndroidWorld Pass@1 by +4.45 and nearly doubles the MobileWorld Pass@3 success rate, while Infinite-Actor-2B improves Pass@1 by +9.05. Code is available at this https URL.

---


### 333. [CCQ: A Multi-State Child Care Quality Dataset to Support AI for Children's Health Research](https://arxiv.org/abs/2610.05863)

**<font color=#1a73e8>作者：</font>** Victor Li, Yuzhang Xie, Ziwei Dong 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> High-quality child care in early life is a critical determinant of children's growth and development. Research on child care quality has been constrained by fragmented, non-research-friendly, and privacy-bound datasets. We present CCQ (Child Care Quality), a large-scale, de-identified dataset for applied data science research at the intersection of AI and early childhood health. CCQ integrates 59,372 child care provider records across 12 U.S. states, covering diverse provider types as well as data schemas. To ensure research utility while protecting privacy, we implement an automated, LLM-based curation pipeline that anonymizes, cleans, and standardizes raw state records into two complementary releases: a cleaned textual release and a fully preprocessed tabular release. We also benchmark traditional machine learning models, tabular foundation models, and language models on quality rating prediction and important features analytics. Within a state, tabular classifiers on the preprocessed tables perform best. Across states, zero-shot transfer is near chance, but modest target-state supervision recovers most of the within-state performance, and pretraining on other states benefits finetuned language models. We release both datasets with all code to accelerate AI-driven research on child care quality and ultimately improve children's health and development.

---


### 334. [Global Communication or Graph-Specific Memory?](https://arxiv.org/abs/2610.05874)

**<font color=#1a73e8>作者：</font>** Hamed Shirzad, Danica J. Sutherland  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scalable Graph Transformers are commonly trained and evaluated on static large graphs in a transductive setup. Many scalable Graph Transformer components can be formulated as a constant-size shared memory, similar to virtual nodes, providing compressed information about the whole graph. The counterpart of these models in language models and other domains is justified as the input changes, and this mechanism learns to compress some useful information about the input. In transductive learning on a single fixed graph, however, any shared memory can be seen as a constant at test time. This raises the question of what exactly this shared memory does in this static setup. We give preliminary evidence that optimizing a shared memory directly performs similarly to global communication methods, and so normal local message-passing models can embed similar information in their weights. Thus, these settings may be a poor fit for evaluating global communication in graph neural networks.

---


### 335. [OGAM: Connecting Systematic Testing to Runtime Assurance through Object-Grounded Attention Monitoring for VLA Policies](https://arxiv.org/abs/2610.05878)

**<font color=#1a73e8>作者：</font>** Haki Darwish, Xiangyu Yin, Changwen Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Benchmarks expose vision-language-action (VLA) policies to few canonical instructions, while exhaustive deployment testing is impossible. We introduce Object-Grounded Attention Monitoring (OGAM), connecting systematic testing to runtime assurance: testing reveals attention divergence between successful and failed executions, and OGAM uses this signal to stop failures beyond the finite suite. We generate scene-grounded instructions through pairwise combinations of action templates and objects, and separately test meaning-preserving paraphrases. All 87 out-of-benchmark cases reveal problematic behavior across OpenVLA, OpenVLA-OFT, UniVLA, and $\pi_{0.5}$: none completes any of the 24 feasible instructions, while infeasible or hazardous requests also trigger behavior substitution. At each action query, we project gradient-weighted visual attention through object masks and group it by instruction role for comparison across tasks and policies. Dynamic time warping aligns this course with a successful reference despite speed differences; conformal calibration on successful episodes sets the early-stopping threshold for sustained deviations, with a nominal false-stop target of $\alpha=0.05$. Across four policies, OGAM stops 87-100% of failed episodes at median times of 5-12s within a 20s budget, with observed false-stop rates of 3-5%, without failure-labeled training. Finite testing thus identifies attention patterns that support online intervention before failure fully unfolds.

---


### 336. [Learning to Learn a Language](https://arxiv.org/abs/2610.05879)

**<font color=#1a73e8>作者：</font>** Lennart Carstens-Behrens, Holger Fröhlich  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present the Prior-Fitted Language Model (PFLM), a 300M-parameter byte-level transformer pretrained only on samples from a synthetic non-linguistic prior. Given a prefix of real text, it learns to predict the language in context with frozen weights, having never seen a word of any real language. Every training sequence is generated by a recurrent structural causal model drawn fresh from a distribution over such models. The model never sees the same language twice during training, so the only way to predict the continuation is to infer the language from the prefix. Samples from this prior share the statistical signatures of natural text: Zipfian frequencies, slow entropy-rate convergence, and long-range dependence. On Wikipedia in six languages, bits per byte fall from the uniform eight to between 0.9 and 2.4 at one million bytes of context. Given numerals instead of text, PFLM learns to count, to compare magnitudes, and to add approximately. It predicts deterministic sequences like Rudin-Shapiro or the prime indicator, and it compresses six non-text domains, from source code to speech, below gzip and PPMd. The model has not learned a language. It has learned to learn one.

---


### 337. [Noise Out, Bias In: Targeted Bias Injection in Diffusion Language Models via Closed-Loop Activation Steering](https://arxiv.org/abs/2610.05894)

**<font color=#1a73e8>作者：</font>** Sarim Hashmi, Mukul Ranjan, Abdelrahman Elsayed 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Masked diffusion language models (dLLMs) generate text by iteratively denoising masked positions, re-predicting each token multiple times before it is committed. An autoregressive decoder exposes an answer's distribution once, at the step that commits it; a dLLM exposes it at every denoising step before commitment, and we show that an adversary can exploit this. Since an answer remains open to revision over many denoising steps, an adversary with access to internal activations can watch how likely the model is to produce a chosen answer and adjust the intervention accordingly. Building on this observation, we study targeted bias injection, an attack that steers a frozen dLLM toward a demographic answer selected by the adversary. The attack uses a simple proportional-integral (PI) controller that tracks the target-answer probability during denoising and adapts the strength of a steering vector on the fly. On ambiguous BBQ questions where the correct answer is abstention, our attack raises LLaDA-8B-Instruct's preference for the targeted group from 1.8 to 16.7 percentage points, more than three times the strongest fixed-strength steering baseline, and on SocialStigmaQA it raises the selection of stigmatizing answers from 17.6% to 58.1%. Fitted to other demographic targets, the same attack shifts answers by up to 37 percentage points, and each attack takes about 40 minutes on one GPU. On the primary target, feedback is what makes the attack work: constant steering at the same average strength over the token-committing steps produces a far smaller shift while corrupting nearly three times as many outputs, and a constant strength set separately for each example still falls well short. Our findings identify the denoising trajectory as a new control channel in dLLMs and call for bias audits that examine the serving stack rather than the frozen model alone.

---


### 338. [Fitting Vision Adapters at Frontier Scales](https://arxiv.org/abs/2610.05897)

**<font color=#1a73e8>作者：</font>** Jaehoon Lee, Harry Partridge, Mudith Jayasekara 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Training a small projector between a frozen vision encoder and language model is an established approach to multimodal learning. As the parameter count of language models scales dramatically, we revisit which vision capabilities this approach can add while keeping their pretrained weights fixed. Here we train a 50M parameter projector from the vision encoder of Kimi K2.6 to GLM 5.2 and 5.3, both models without native vision capabilities, and further present a reproducible recipe for training these adapters at scale. We study the following: (a) how vision capabilities of multimodal models scale as purely the language model side scales, and (b) what specific vision capabilities are able to be imbued into a pure language model at scale, and which ones remain limited. We evaluate on MMMU-Pro and BLINK, examining both overall performance and results on individual visual tasks.

---


### 339. [Collaborative Personalized Preference Alignment for LLMs under Data Deficiency](https://arxiv.org/abs/2610.05898)

**<font color=#1a73e8>作者：</font>** Liyan Yang, Yige Yuan, Zhiqin Yang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Real-world users often exhibit highly heterogeneous preferences over multiple objectives for LLM responses. A lightweight aligner can tailor these responses to individual preferences, but scarce user-specific feedback makes personalized training difficult. Learning shared initializations across users can support few-shot adaptation. However, heterogeneous preferences and competing objectives cause gradient conflicts across users and within each user, hindering effective initialization learning. This raises a central question: \textbf{how can we collaboratively learn aligner initializations that support few-shot adaptation to diverse user preferences?} To answer this question, we propose \textbf{A}pproximate \textbf{P}areto \textbf{O}ptimality (APO). We first group users whose updates are compatible, so that their information can be combined with less interference. Within each group, we combine gradient descent with controlled ascent to coordinate competing objectives and move towards preference-specific points on the Pareto front. This produces an initialization that is close to the optima of the users in the group. We then iteratively refine it using updates from few-shot local adaptation, making it more effective for personalization. Furthermore, we establish conditional suboptimality bounds for a one-local-step collaborative update and characterize how initialization error affects subsequent stochastic adaptation. Experiments on Fed-ChatbotPA and UltraFeedback show consistent improvements over existing methods using only 20 local examples.

---


### 340. [AstraSR: Real-World Thermal Super-Resolution with GPT-6 Astra](https://arxiv.org/abs/2610.05910)

**<font color=#1a73e8>作者：</font>** Mengyuan Li, Changhong Fu, Jun Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-world thermal super-resolution (SR) is constrained by limited sensor resolution and the difficulty of obtaining corresponding high-resolution (HR) observations for direct model supervision. Conventional SR methods typically construct training pairs by treating captured thermal images with real-world degradations as HR references and applying predefined degradation to generate synthetic low-resolution (LR) inputs. Such a construction not only introduces a domain gap between synthetic and captured LR observations but also retains acquisition degradations in the supervision. To address this issue, we propose AstraSR, a real-world thermal SR method guided by GPT-6 Astra, a frontier multimodal generative model endowed with emergent and transformative visual capabilities. Specifically, we construct a dataset of image pairs by using captured LR thermal images to condition GPT-based HR reference. We develop a direct generative supervision strategy that learns from captured thermal inputs paired with GPT-generated HR references. Pixel, gradient, and perceptual losses jointly supervise the transfer of intensity patterns, structural boundaries, and visual details from the generated references. Qualitative comparisons with seven existing state-of-the-art real-world SR methods show continuous object contours, distinct structural boundaries, and smooth intensity transitions in the thermal scenes. These results demonstrate that AstraSR outperforms existing real-world SR methods in both thermal clarity and structural coherence.

---


### 341. [ThunderSyncRL: Lossless Acceleration of Agentic Reinforcement Learning](https://arxiv.org/abs/2610.05935)

**<font color=#1a73e8>作者：</font>** Seil Kang, Hangoo Kang, Tarun Suresh 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language models are moving beyond generating answers to pursuing long-horizon goals in interactive environments. Post-training these agents requires long, heterogeneous trajectories, and synchronous systems leave learner engines idle until rollout and verification finish. To squeeze out these pipeline bubbles, asynchronous training overlaps rollout and learning across updates, but comes at the cost of policy staleness. We introduce ThunderSyncRL, which starts gradient computation as soon as all required inputs are fixed, without policy staleness. For group relative policy optimization (GRPO), ThunderSyncRL computes each trajectory's score gradient as soon as the reward for that trajectory arrives, without waiting for the group. For on-policy distillation (OPD), it computes gradients for each completed agentic turn's teacher-scored actions while tool calls run in the sandbox. We prove that gradient streaming produces the same GRPO and OPD updates as batch-synchronous training, without changing either objective. On SWE-bench Verified and Terminal Bench 4.0, we train models to the same performance up to $1.9 \times$ faster than synchronous training. With zero policy staleness, ThunderSyncRL also outperforms asynchronous training at a fixed budget by up to $2.47$ percentage points.

---


### 342. [ReMem: Streaming Video Understanding With Long Context Retention](https://arxiv.org/abs/2610.05940)

**<font color=#1a73e8>作者：</font>** Li Yiheng, He Xu, Wang Shaobo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite their impressive performance on a wide range of video understanding tasks, current Vision Language Models (VLMs) are predominantly designed for offline scenarios and struggle to handle online streaming videos that demand low latency response. Several studies have explored memory and token compression strategies in an attempt to adapt offline VLMs for streaming video understanding tasks. However, through our probing experiment, we identify that most existing works tend to progressively lose long context information as length of input stream increases. To address this, we propose ReMem, a novel training-free adaptation technique that enables VLMs to process streaming videos of arbitrary lengths while improving their long context information retention capability. ReMem exploits memory from two perspectives, implemented as two core components. The Streaming Context Memory (SCM) continuously compresses historical context with query-independent attention. The Retrieved Vision Memory (RVM) then retrieves the most salient, query-relevant context from memory to augment the VLM's input. Comprehensive experiments demonstrate that the proposed ReMem achieves state-of-the-art (SOTA) performance across a variety of widely used benchmarks, spanning both streaming video and general long video understanding tasks.

---


### 343. [Discovered, Not Designed: Population Evolution for Collaborative and Compute-Intensive Model Discovery](https://arxiv.org/abs/2610.05950)

**<font color=#1a73e8>作者：</font>** Bo Peng, Lizhu Zhang, Yuhang Zhou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM-driven evolution enables iterative model development, but two practical goals remain underexplored: finding model designs that transfer across related tasks and sustaining improvement when training is expensive. We introduce Population Evolution (PE), a collaborative, hierarchical framework that connects ongoing local searches through shared experimental evidence. PE evaluates code changes across related training instances and shares the results to guide subsequent proposals and promotion to larger training scales. For expensive targets, PE searches small training subsets and screens candidates through peer and intermediate evaluations before full-target training. We introduce RMD-Bench to evaluate both settings across ranking, watch-time prediction, RL algorithm discovery, and LLM/VLM pretraining. Compared with standalone evolution at matched source iterations, PE raises mean best local gains from 7.01% to 8.97% in ranking and from 2.84% to 3.85% in watch-time, while improving the best larger-scale outcome in all three joint-discovery families. In watch-time discovery, PE improves best larger-scale gains with four of five harnesses and all four proposers. On new recommendation datasets under shared target-side calibration, every evaluated PE design improves over the reference in mean performance. Under matched total GPU compute, completed LLM discovery runs yield a best relative accuracy gain of 2.48% and 13 successful candidates for PE, versus 0.92% and none for direct evolution. VLM loss reduction reaches 8.78% versus 5.05% under matched total GPU compute.

---


### 344. [HuatuoGPT-3: RL-Only Domain Adaptation from Base Models](https://arxiv.org/abs/2610.05966)

**<font color=#1a73e8>作者：</font>** Junying Chen, Xinyuan Xie, Ziniu Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Domain adaptation aims to turn a general-purpose large language model (LLM) into an expert for a target domain. While the dominant SFT+RL pipeline offers a convenient cold start, it may reduce exploration diversity and introduces additional complexity through multi-stage optimization. These limitations motivate RL-only adaptation. However, pure on-policy RL suffers from a cold-start problem, while mixed-policy RL still falls short: informative tokens in teacher outputs are learned too slowly in early training, and stale teacher outputs can hinder later improvement. We identify these two failure modes as Gradient Starvation and Teacher-Distribution Anchoring. To address them, we propose One-stage Policy Optimization (OnePO), which treats teacher outputs as transient guidance for policy improvement. OnePO combines Adaptive Objective Evolution to strengthen learning on informative low-probability teacher tokens and Teacher Retirement to discard teacher outputs once the current policy can surpass them. On medical adaptation, OnePO achieves 67.2 on HealthBench (Total) with only 20K training samples, outperforming SFT+RL and pure RL by 2.7 and 7.4 points, respectively. We further scale OnePO to produce HuatuoGPT-3, an open-source medical LLM series whose 27B variant reaches 70.1 on HealthBench (Total) and 71.4 on HealthBench Professional, surpassing frontier models such as GPT-6 Astra. Models and code are available at this https URL.

---


### 345. [Transfer-Stratified On-Policy Distillation for RL-Improved Reasoning Teachers](https://arxiv.org/abs/2610.05974)

**<font color=#1a73e8>作者：</font>** Xiaoyu Chen, Bo Shao, Tiangang Zhu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning can substantially improve a reasoning teacher, but it is unclear which of those improvements survive when the teacher supervises a smaller on-policy student. We study this question in mathematical reasoning by comparing teacher lineages before and after GRPO, multiple student scales, direct GRPO, and several on-policy distillation objectives. The central finding is that transfer is structured rather than scalar: teacher strength alone does not make dense distillation competitive, while an RL-improved teacher creates useful but metric-dependent student gains. This motivates Transfer-Stratified On-Policy Distillation (TS-OPD), which screens training problems by the joint sampled success of the student and teacher, routes acquisition problems to gated forward KL, routes consolidation problems to gated reverse KL, and adds an entropy brake to protect sampled coverage. Across the main comparison, TS-OPD is the strongest student objective for macro average correctness with the GRPO-improved teacher, while pass@K remains more mixed. Ablations show that the gains come from routing and token gating rather than skipping problems. These results support a transfer-aware view of OPD: stronger teachers help when the supervision direction and token budget match the student's observed ability, not merely because the teacher endpoint is stronger.

---


### 346. [Can Language Models Learn to Reject Their Own Bad Reasoning Steps?](https://arxiv.org/abs/2610.05976)

**<font color=#1a73e8>作者：</font>** Siheng Xiong, Xiaoze Liu, Yiqiao Jin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Verifier-guided decoding can prevent harmful reasoning steps from contaminating subsequent generation, but typically relies on an external learned verifier. We ask whether a language model can instead reject its own bad reasoning steps. We define a prefix's recoverability as the probability that the frozen generator can complete it correctly. Diagnostics show that adjacent recoverability changes are often difficult to resolve with practical Monte Carlo budgets, while same-prefix candidates exhibit a sparse low-recoverability tail. We introduce Self-Step Rejection (SSR), which trains a lightweight LoRA acceptance gate on the generator backbone while keeping the base model frozen. SSR uses confidence-qualified first-passage supervision: steps before the first resolved crossing of a root-relative recoverability barrier are accepted, the crossing step is rejected, and unresolved steps and suffixes are excluded. Training combines pointwise classification, same-prefix pairwise learning, and group-relative policy refinement using final-answer correctness. At inference, SSR accepts candidates or resamples from the unchanged prefix under rejection budgets, without an external learned verifier. Across three reasoning models and five mathematical reasoning benchmarks, SSR improves macro-average accuracy over single-pass decoding by 5.4--10.1 points using 1.21--1.40x as many generated tokens, and achieves the highest macro-average accuracy among evaluated step-level methods. Full-solution scaling methods require 4.47--8.27x the single-pass token cost for comparable performance.

---


### 347. [StagQ: Constraint-Driven Multi-Precision Weight Quantization for LLMs](https://arxiv.org/abs/2610.05977)

**<font color=#1a73e8>作者：</font>** Zhe Wei, Mengqi Guo, Yuan Yuan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Serving a large language model (LLM) across a fleet of deployments requires several weight-precision operating points. Multi-precision formats serve them all from one stream whose prefixes are valid lower-precision codes, instead of storing multiple copies. We present StagQ, a multi-precision weight format whose main stream is a 2-bit group-wise affine base followed by a configurable number of 1-bit refinement planes on a dyadic step schedule. Every supported precision is a readable prefix, decoded by an affine map derived from metadata shared across all precisions, with no per-weight lookup. A sparse side record, filled both before and after the grid is fitted, holds out the few weights the grid serves worst. We report two configurations of the encoder. At two bits the cheaper one leads the strongest multi-precision baseline on Llama-3.1-8B, Phi-4, and OLMo-2-7B by 3.1 to 7.0 MMLU points, at a slightly lower logical rate. At three bits it leads on Llama-3.1-8B, leads on Phi-4 at a higher rate, and ties on OLMo-2-7B. At four bits it ties on all three, at a higher rate. In a batch-one matrix-vector product on an NVIDIA A100 GPU, timed on synthetic weights, our kernel is faster than the two baseline kernels in most shape-precision cases.

---


### 348. [Byte Language Models: Scaling, Emergent Abstractions, and Information Allocation](https://arxiv.org/abs/2610.05978)

**<font color=#1a73e8>作者：</font>** Jie Wang, Shiwei Luo, Qi Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Tokenizer-free language models remove the inductive bias of fixed tokenizers by modeling text directly as bytes, but the resulting longer sequences substantially increase computation and eliminate explicit text abstractions. We ask whether this additional computation can be useful, and whether standard Transformers can learn the abstractions that tokenization provides. We study these questions on Transformers without specialized tokenization-related architectures. With token-superposition training and hash embeddings, byte Transformers consistently outperform subword Transformers as model size scales. We further find that byte Transformers build local text abstractions as external tokenizers: a set of segmentation-like positions are used to collect local context representations, and restricting up to $25\%$ of intermediate layers to these local representations preserves downstream performance. Finally, these learned structures induce highly non-uniform generation difficulty, with uncertainty concentrated near local structure boundaries; exploiting them for speculative decoding yields $3.4\times$ more accepted tokens than in subword Transformers.

---


### 349. [Breaking the Tie: A Cluster-Aware Routing Framework for Large Language Models](https://arxiv.org/abs/2610.05982)

**<font color=#1a73e8>作者：</font>** Yao Lu, Zhaiyuan Ji, Yaxin Gao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> With the rapid development of artificial intelligence, the emergence of various Large Language Models (LLMs) has created a rich model ecosystem. However, this also brings a key challenge: how to select the optimal model for a specific user query. LLM routing addresses this need by dynamically assigning queries to the most suitable expert in the pool of candidate models. However, existing routing frameworks often simplify this process to a standard classification task; thus, a critical vulnerability is exposed when multiple candidate models correctly answer the same query. We formalize this capability overlap as routing noise, which misleads the router with arbitrarily correct candidate models, ultimately leading to routing collapse (a severe decline in generalization ability on unseen tasks). To address this problem, we propose a novel Cluster-Aware Soft-Labeling Routing (CASLR) framework. CASLR shifts the evaluation paradigm from the success of a single query to macro-domain consensus by replacing traditional one-hot vectors with a masked softmax mechanism. Specifically, for experts who answer incorrectly, we penalize their target probability to zero; for the remaining candidates, we directly compute continuous fine-grained soft labels based on their global clustering utility scores. We then use these refined soft labels to supervise a lightweight router. Specifically, the framework not only demonstrates superior accuracy on multiple benchmarks, but also outperforms Llama-3.3-70B-Instruct by 7.80% in overall average performance. Furthermore, the extremely low routing inference latency of only 1.13s further confirms that CASLR can achieve efficient system scheduling with almost zero additional overhead, while ensuring high response quality.

---


### 350. [H-CRSPV: Preventing Semantic Omission in Late-Bound Large Language Model Releases](https://arxiv.org/abs/2610.05989)

**<font color=#1a73e8>作者：</font>** Weijie Miao, Henry Hong-Ning Dai, Ming Li  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large-language-model release pipelines increasingly combine commitments, signatures, provenance records, and heterogeneous verification backends. Yet validating every submitted object does not establish that a release realizes every requirement of its registered transformation. An untrusted realization proposer may omit a required relation, propose an unauthorized evidence-sharing assignment, or bind valid evidence to the wrong object. This verification-boundary failure is termed Semantic Omission under Valid Evidence (SOVE). Hybrid Cryptographic Relation-based Semantic Plan Verification (H-CRSPV) is a replicated admission layer that enforces required-set completeness before release consumption. Before evidence selection, an authorized registration entity commits an authenticated authority record. Validators independently derive the required-obligation multiset, check exact entry-occurrence coverage, validate proposal-induced evidence sharing, and bind admissible groups one-to-one to keeper-resolved objects. Evidence remains provisional until the challenge window closes and an atomic finalizer activates the release. The analysis establishes structural exactness and conditional semantic guarantees under explicit assumptions. Across 36 omission artifacts, submitted-object validation accepts all 36 because every submitted object passes its backend-specific verifier. H-CRSPV rejects all 36 while accepting all six honest releases. The prototype also validates six restricted source-to-RelationIR bindings and rejects all 60 tested mutations. In a continuous four-validator Qwen2.5-1.5B workflow, the same authority record remains fixed across three legal releases with different post-registration availability states. These results show that per-object validity does not establish complete, correctly bound, and finalized release evidence.

---


> [!TIP]
> 当前位于：**301-350**（第 7/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-505](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
