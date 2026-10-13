# 🧠 大模型相关研究 | 2026年10月14日

> 本类共 **230** 篇论文：已确认 **202** 篇，待复核 **28** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-230](./part-05.md)

---

### 151. [Proactive Agentic Orchestration](https://arxiv.org/abs/2610.13485)

**<font color=#1a73e8>作者：</font>** Xueyang Feng, Chaozhuo Li, Xiaohe Bo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agentic orchestration delegates tasks to sub-agents with independent contexts, providing a key path to extending the effective execution horizon of large language model agents. However, existing orchestration methods face two limitations: in execution, current methods fix sub-agents' goals and harnesses at creation time, limiting their adaptability to dynamic real-world environments; in optimization, sparse and delayed feedback constrains effective learning of the orchestration policy. To address these limitations, we introduce POrchestra, an on-the-fly proactive agentic orchestration framework. It allows sub-agents to proactively communicate with the orchestrator at any logical point to request harness adjustments while maintaining continuity of local execution. This mechanism not only enables sub-agents to adapt seamlessly to dynamic environments but also naturally inspires On-Policy Orchestration Distillation (OPOD) based on hindsight feedback. OPOD attributes sub-agents' proactive revision requests back to preceding orchestration decisions to derive targeted improvement signals, and leverages these signals as process supervision alongside the final reward to optimize the orchestration policy. We evaluate POrchestra on three long-horizon agent benchmarks spanning deep research, dynamic digital assistance, and software engineering. POrchestra improves task success by an average of 9.1% relative to the strongest baseline; combined with OPOD, it improves small-orchestrator success by an average of 10.0% relative to existing training baselines. POrchestra also achieves a more favorable cost-performance trade-off. Our code is publicly available at this https URL.

---


### 152. [EviRepair: Evidence-Driven Agents for Reliable Vulnerability Repair](https://arxiv.org/abs/2610.13491)

**<font color=#1a73e8>作者：</font>** Yilian Shi, Qingyu Liu, Tianyi Zhou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Recent advances in large language models (LLMs) have enabled agent-based approaches for repository-level automated vulnerability repair (AVR), showing promising repair capabilities. However, an important issue has received limited attention: how can we ensure that the evidence generated during the repair process is reliable enough to support accurate vulnerability understanding and patch generation? In this paper, we propose EviRepair, an evidence-driven multi-agent framework for repository-level AVR. EviRepair introduces evidence review into the repair process by enabling agents to collaboratively collect vulnerability evidence, verify evidence consistency, and construct a reviewed vulnerability model for patch synthesis and validation. Extensive experiments on PatchEval and SecBench benchmarks with multiple agent frameworks and LLMs demonstrate that EviRepair consistently outperforms existing agent-based baselines, achieving average improvements of 16.37% and 40.33% in resolved rates on PatchEval and SecBench, respectively. Codes are available at this https URL

---


### 153. [Humanize MLE Agents: Multi-Agent Session Alternation Beyond Single-Agent Limits](https://arxiv.org/abs/2610.13494)

**<font color=#1a73e8>作者：</font>** Changye Li, Zijian Zhang, Muheng Li 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing LLM-based agent approaches for long-horizon machine learning engineering (MLE) often use context engineering, implemented through custom harnesses that manage tools, skills, and accumulated experience. However, we find that as single-session execution lengthens, the agent's reasoning intensity declines alongside slowing progress, summarized as long-horizon deceleration, and the benefits of these custom harnesses vanish as the underlying model improves, summarized as harness staleness. These findings suggest that their benefits may not persist across versions, which motivates a workflow-level approach in which agents build on one another's work across sessions. We model these alternating agent sessions as a context-reset semi-Markov decision process (CR-SMDP) and establish sufficient conditions for alternation to exceed single-agent reference limits, derive an explicit experiment-budget bound, and characterize when session caps preserve this advantage. Guided by this analysis, we introduce Humanize MLE Agents (HMA), which alternates two agents on a shared workspace, limits each session to at most k experiments and resets the context between sessions, without additional task-specific harness or prior knowledge supplements. Across 75 Kaggle tasks in MLE-bench, HMA reaches a state-of-the-art any-medal rate of 78.2%, exceeding the strongest open-source baseline by 8.0 points with a quarter of its time budget. Moreover, among six configurations spanning five heterogeneous agent pairs, HMA improves any-medal rate over the constituent baselines by 6.4 points on average, demonstrating cross-pair generality. A supplementary case on kernel optimization reaches 878 cycles, within 1.6% of the community leaderboard leader, demonstrating applicability beyond MLE.

---


### 154. [Stride: Scale-Aware Multi-Agent Evolutionary Refinement for Infographic Generation](https://arxiv.org/abs/2610.13502)

**<font color=#1a73e8>作者：</font>** Yan Zhou, Yang Yang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Infographic generation challenges text-to-image models because a single image must satisfy numerous visual, textual, and semantic constraints. Iterative agentic refinement with a multimodal verifier is a natural remedy, but existing methods face a scale mismatch: local edits cannot correct global composition errors, while full regeneration may destroy already-correct regions. We introduce Stride, a constraint-grounded multi-agent framework that treats refinement over any frozen generator as a history-aware evolution strategy. Stride separates constraint evaluation - whether each requirement is satisfied - from visual grounding - where and how it is violated. It then routes global revisions to a composer subagent and local corrections to a retoucher subagent. Each subagent conducts internal planning and generates multiple candidates, while Stride accepts a candidate only when it improves the verifier score, reducing regression across iterations. Because stochastic generators and imperfect verifiers make any single step unreliable, it is this combination of scale-aware routing, per-step redundancy, and monotonic acceptance that yields stable improvement across iterations. With fully open-weight generator-verifier systems, Stride outperforms proprietary systems including Nano-Banana-2.0 and Seedream-5.0-Pro on BizGenEval, matches GPT-Image-2.0 and surpasses Seedream-5.0-Pro on IGenBench, and achieves a new state-of-the-art score on WISE, while substantially outperforming existing agentic methods across all evaluated benchmarks.

---


### 155. [Beyond Temporal Proximity: Explanatory World Models for Credit Assignment in Reinforcement Learning](https://arxiv.org/abs/2610.13504)

**<font color=#1a73e8>作者：</font>** Oriol Corcoll, Qiyao Wei, Ciarán Mark Gilligan-Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative Recommenders increasingly use Reinforcement Learning (RL) to optimize outcomes that may appear hundreds or thousands of interactions after a decision. Standard RL propagates reward according to temporal proximity rather than explicit relevance, attenuating the signal assigned to distant but important actions and creating a source of sample inefficiency. We introduce Explanatory World Models (EWM), an attribution framework that uses explanations to identify the earlier events that plausibly contributed to a realized outcome. We instantiate EWM with a frontier language model and use its explanations as learning signals using a conservative hierarchical operator that recursively redistributes reward while preserving the undiscounted episode return. To investigate what constitutes a useful explanation, we operationalize three complementary variants inspired by Halpern's actual causation, Lombrozo's explanatory simplicity, and Deutsch's hard-to-vary explanations. We evaluate EWM on two controlled long-horizon RL benchmarks, a public sequential-recommendation benchmark, and an industry-scale generative recommender. On Crafter and WordCraft, EWM substantially outperforms PPO and LaRe, with its largest gains when rewards are most delayed. On KuaiRand, EWM outperforms SFT and LaRe offline and A2C online. Finally, in an offline evaluation of an industry generative recommender, EWM considerably improves Recall and increases behavioral proxies. These results suggest that explanations can provide structured and reusable credit for learning from delayed outcomes.

---


### 156. [Retrieval-Augmented Multimodal Language Model with Heterogeneous Evidence Integration for Clinical Prognosis](https://arxiv.org/abs/2610.13510)

**<font color=#1a73e8>作者：</font>** Hamza Shafiq, Jialu Tang, Ting Dang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Clinical prognosis requires integrating structured measurements, physiological waveforms, longitudinal history, and population context. We introduce PRISM (Population-Retrieved Inference for Structured Multimodal Prognosis), a multimodal language model that combines per-feature numerical tokenization, recency-weighted aggregation of longitudinal ECGs, and a dual-modality population memory bank. Retrieval operates in representation space: the model receives mean-pooled embeddings of similar training-cohort encounters, while no individual retrieved record enters the prompt. On the 1,443-task MDS-ED benchmark, PRISM achieves AUROCs of 86.2% for diagnosis, 93.1% for deterioration, 91.8% for ICU admission, and 92.8% for mortality. These results use a 96-hour pre-arrival window unavailable to reported baselines. With benchmark-window inputs only, PRISM reaches 0.8895 AUROC, compared with 0.8937 for UniPACT and 0.8889 for MDS-ED. A matched-input compact fusion model using the same five evidence streams and frozen encoders reaches 0.7652 AUROC, versus 0.9092 for PRISM. Replacing numerical EHR encoding with text serialization reduces AUROC by 3.66 points; removing pre-arrival history reduces it by 1.97 points; and zeroing retrieval reduces it by 0.99 points. Genuine retrieval outperforms random-neighbor retrieval by 0.97 macro-average points, although a paired task-level sign test does not establish a uniform advantage (p=0.067). On the external MC-MED cohort, supervised fine-tuning reaches 0.8611 AUROC, compared with 0.8227 for locally trained gradient boosting and 0.7841 for source-only PRISM. These results support structure-aware multimodal integration and supervised external adaptation.

---


### 157. [Beyond Domain-Routed Supervision: Cross-Teacher Guarding for Multi-Teacher On-Policy Distillation](https://arxiv.org/abs/2610.13521)

**<font color=#1a73e8>作者：</font>** Shi-Yu Tian, Yong Liu, Ximan Liu 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-teacher on-policy distillation (MOPD) extends on-policy distillation (OPD) by routing domain-specific data to specialized teachers, integrating their capabilities through dense token-level supervision on student-generated trajectories. However, domain routing only distinguishes the supervision sources for different domains; updates from all domains still act on shared parameters. When teachers differ substantially in response style and domain expertise, supervision that is effective in isolation may still lead to persistent gradient conflicts and capability degradation during joint optimization. To address this challenge, we propose Cross-Teacher Guarding for MOPD (Road MOPD), which introduces non-routed teachers as auxiliary cross-domain critics on the same student trajectories and coordinates multi-teacher supervision through token-level credit assignment and gradient updates. Specifically, cross-teacher-guided credit assignment uses teacher agreement to strengthen token-level corrections jointly supported by the teachers and attenuate conflicting signals; preventive multi-teacher gradient projection uses auxiliary gradients from the same trajectories to constrain potentially conflicting updates and adaptively controls projection strength to retain target-domain learning signals. In experiments, Road MOPD mitigates degradation in the disadvantaged domain, gains over 5 percentage points under high conflict, and improves overall performance in low-conflict and three-domain settings.

---


### 158. [Simulating Training Spikes of Deep Neural Networks by Layer-wise Random Feature Models](https://arxiv.org/abs/2610.13524)

**<font color=#1a73e8>作者：</font>** Ran Tian, Courtney Paquette  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Intermittent ``spikes'' in loss, during the pre-training of Large Language Models (LLMs), remains a mysterious phenomenon both theoretically and empirically. In this paper, we show that simple quadratic models with heavy-tailed, power-law distributed inputs can replicate these spikes. We introduce a theoretical framework and simulation algorithm to model per-layer training dynamics of Deep Neural Networks (DNNs), using such quadratic models. In a case study on an Adam hyperparameter configuration (where $\beta_2$ is set close to $1$) known to induce spikes in Transformer LMs, our simulation successfully predicts bumps indicating spiky behavior from a given checkpoint. Furthermore, we derive an appropriate $\beta_2$ schedule from observed metrics, which empirically improves performance.

---


### 159. [S-Space: Exploring Spatial Workspace in Multimodal Language Models](https://arxiv.org/abs/2610.13527)

**<font color=#1a73e8>作者：</font>** Zhiyuan Shi, Xiang Li, Xingzhuo Guo 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal language models (MLLMs) exhibit promising spatial reasoning capabilities, yet the internal mechanisms supporting them remain poorly understood. We uncover S-Space, a linear representation subspace in which object-token representations encode continuous coordinates along horizontal, vertical, and distance axes. Although we identify these axes by differentiating spatial-answer scores with respect to object-token activations, S-Space is intrinsic rather than induced by specific data or prompts, remaining readable under non-spatial questions. We show that S-Space functions as an internal spatial workspace of MLLMs. Perception encodes object locations into it, forming spatial representations that can be directly read out to support accurate spatial judgments. Internal reasoning transforms it for changing viewpoints. Verbal responses selectively access it, evidenced by causal interventions that alter spatial judgments while largely preserving non-spatial responses. Case studies further show that S-Space assigns locations to unseen entities and the observer, and connects physical directions with abstract linguistic meanings, suggesting both the capabilities and limitations of large-scale language training. Finally, we use S-Space as a diagnostic tool for spatial reasoning failures. Direction-word readouts reveal systematic coupling between cardinal and image-relative reference frames. More importantly, a perception-computation decomposition exposes a key bottleneck: MLLMs can form capable spatial representations, yet fall short in the spatial transformations required to reason reliably across viewpoint changes.

---


### 160. [Auditing VLM Benchmarks from Existing Evaluation Runs](https://arxiv.org/abs/2610.13548)

**<font color=#1a73e8>作者：</font>** Denis Degtiarev, Anna Gromova, Sergey Katkov 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Every evaluation run of a vision-language model (VLM) already produces per-question artifacts (predictions, judged correctness, metadata) that leaderboards reduce to a single score and then discard. We reuse those artifacts to audit the benchmark itself, and add an audit layer to VLMEvalKit: six detectors that run as post-processing over saved outputs, plus one additional text-only rerun with visual inputs removed, emitting a per-question report. The layer reports per-question findings together with aggregate audit statistics; for the headline quantities, it attaches permutation-null excess where applicable, interval estimates for proportions, and sensitivity to the model pool. Auditing MMStar, a benchmark curated specifically so that the image is indispensable, with three models, we find zero aggregate accuracy gain from the image on 20.2% of its questions. An item-matched permutation null accounts for 17.0%, leaving a +3.2 pp excess (corrected permutation p = 0.001). This excess is concentrated in the mathematics and science categories and is absent from coarse perception, a localization consistent with knowledge substituting for visual evidence; confirming that mechanism would require item-level review. A second detector flags 134 questions on which every model that answered in parseable form picked the same non-gold option, and these candidates peak in the perception categories, whereas the zero-gain excess is largest in mathematics and science & technology. Replacing the LLM judge with exact string matching changes no conclusion, and every scoring discrepancy between the two traces to one model whose free-form answers a parser cannot read. On a binary yes/no benchmark the detectors measurably fall out of calibration, a scope boundary that we measure and report. The audit layer, the prediction artifacts and the generated reports accompany this submission.

---


### 161. [Personalization Without Stereotyping: Do Speech LLMs Know When to Turn a Deaf Ear?](https://arxiv.org/abs/2610.13550)

**<font color=#1a73e8>作者：</font>** Kshitij Ambilduke, Caroline Brun, Thibaut Thonet 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent speech LLMs can leverage rich paralinguistic cues, enabling more complex and personalized interactions. However, little work investigates how this sensitivity can lead to stereotyping, and existing evaluations largely measure demographic disparities without distinguishing beneficial personalization from stereotypical behavior. We introduce BASIS-Bench, a benchmark designed to disentangle these two aspects through three axes: (1) demographic robustness, measuring disparities in content-based tasks across speakers and demographic classification capabilities; (2) stereotypical bias, measuring whether perceived demographic cues trigger unprompted stereotypical behavior; and (3) personalization, measuring whether models can tailor responses to demographic characteristics when explicitly requested. We evaluate eight recent speech LLMs and find that, despite often recognizing demographic cues, most fail to translate them into appropriate personalization. Explicit demographic labels improve personalization but also amplify stereotypical associations already present in the textual backbones. These findings highlight the need to train speech LLMs not only to perceive demographic cues, but to learn when they should shape their responses.

---


### 162. [Rationally Linearized MLPs](https://arxiv.org/abs/2610.13568)

**<font color=#1a73e8>作者：</font>** Arijit Sehanobish, Byeongchan Kim, Avinava Dubey 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present Rationally Linearized Multilayer Perceptrons(RaLiMPs), a new approach to efficiently linearizing MLPs using low-degree rational approximations of standard activation functions. Inspired by polynomial-based MLP linearization, we show that rational approximations can provide accurate representations at substantially lower degree. RaLiMPs exploit these approximations to construct kernel representations with narrow bottlenecks, enabling efficient composition across MLP layers. We provide theoretical guarantees for the resulting approximation and evaluate RaLiMPs across applications ranging from implicit 3D models to large language models. Our experiments demonstrate favorable accuracy--efficiency tradeoffs, with RaLiMPs achieving competitive or improved accuracy while substantially reducing inference cost.

---


### 163. [Constructing Pareto Frontiers of Optimal Reasoning Termination Methods for Overthinking in Reasoning Models](https://arxiv.org/abs/2610.13570)

**<font color=#1a73e8>作者：</font>** Weixin Guan, Liang Li, Shiyu Xie 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reasoning models can benefit from test-time scaling, but continued reasoning may become ineffective or harmful, a phenomenon termed overthinking. Evaluations against full thinking compare accuracy and token usage but lack references for overthinking severity and strategies' theoretical mitigation potential. To characterize overthinking at the model-task level, we first introduce Step-wise Truncation Probing (STP), repeatedly generating answers from multiple retained prefixes along each fixed sampled reasoning trajectory. Using each trajectory's earliest measured position attaining maximum empirical accuracy as a reference, we define Overthinking Ratio and Accuracy Degradation as the fraction of thinking tokens generated afterward and the accuracy decrease from this reference to full thinking, respectively. Secondly, we then formulate dynamic routing, fixed budgets, and dynamic early exit within a unified framework to quantify the theoretical mitigation potential of different termination strategies. Based on this unified framework, we use the complete STP measurements to construct a token-accuracy Pareto frontier for each strategy under a common normalized thinking-token budget. We further develop OTBench, a reusable benchmark built from the STP process, which produced 70.5B reasoning tokens and the corresponding probing measurements across six models and four benchmark groups.

---


### 164. [MENTOR: Learning from Failure with On-Policy Pedagogical Intervention](https://arxiv.org/abs/2610.13594)

**<font color=#1a73e8>作者：</font>** Guanlan Yue, Hang Yu, Xiaoyong Huang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning from Verifiable Rewards (RLVR) is a key driver for Large Reasoning Models, but it is vulnerable to "zero-reward collapse", a training failure where a sudden increase in task difficulty causes the learning signal to vanish. We argue that the conventional approach of discarding these failed trajectories is wasteful, as they contain valuable diagnostic information about the model's cognitive gaps, a bright side that can be leveraged for recovery. Existing solutions, however, often regress to static, "off-policy-style" interventions like pre-defined hint libraries or perform post-hoc refinement, failing to provide the adaptive, forward-looking guidance needed to escape the collapse. To address this, we propose a paradigm shift towards on-policy pedagogical intervention and introduce MENTOR, a multi-agent framework that acts as a live mentor. MENTOR diagnoses the root cause of failure in real-time and dynamically generates targeted, instructional prompts to guide the learning agent's next attempt. As a plug-and-play module, MENTOR integrates seamlessly into existing policy optimization pipelines like GRPO without modifying the training infrastructure. Extensive experiments on math and code generation show that MENTOR effectively mitigates zero-reward collapse, outperforming state-of-the-art baselines. Notably, it achieves massive average relative gains of up to 78.3% on Llama-3.2-3B-Instruct over its base model.

---


### 165. [zip2zip++: Towards Inference-Time Token Compression with Minimal Quality Loss](https://arxiv.org/abs/2610.13605)

**<font color=#1a73e8>作者：</font>** Saibo Geng, Andrea Gentilini, Xinxian Ma 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Dynamic vocabularies built on-the-fly via Lempel-Ziv-Welch (LZW) compression let a language model represent the same text in fewer tokens, but prior work shows that this efficiency comes at a cost to reasoning and perplexity. We show that this quality gap is not a fundamental price of compression but can be substantially closed through targeted improvements to the compression layer and LZW codec, without modifying the underlying pretrained language model. Our analysis reveals four key issues: (1) LZW's compression algorithm creates an implicit conflict between the input embedding and the output embedding, a tension that a single shared embedding cannot resolve; (2) naively applying RoPE to LZW-compressed sequences ignores that merged tokens can span multiple tokens; (3) merging certain tokens (notably digits) disproportionately hurts downstream accuracy; and (4) dynamic vocabularies introduce an inherent segmentation ambiguity that confounds standard evaluation. We address these through decoupled input/output dynamic embedding layer, size-aware RoPE positioning, and a modified LZW codec supporting selective merges and multi-view segmentations. Across four models, our recipe improves perplexity on every corpus we evaluated as well as mathematical reasoning accuracy, closing roughly half the quality gap between zip2zip and the uncompressed baseline at a similar compression ratio on general text. This represents a significant step toward lossless adaptive-vocabulary compression for language models.

---


### 166. [BLiMPPI: Benchmark of Linguistic Minimal Pairs for Polarity Items](https://arxiv.org/abs/2610.13607)

**<font color=#1a73e8>作者：</font>** Arzu Burcu Güven, Anna Rogers, Leonie Weissweiler 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Negative polarity items (NPIs), such as "anymore" and "ever", are grammatical only in select environments, predominantly in the context of negation. Because their grammaticality depends on both syntax and semantics, they have a rich, multilingual literature in theoretical linguistics, yet work on NPIs in language models is almost entirely confined to English. We introduce BLiMPPI, a multilingual evaluation suite of over 12,000 NPI minimal pairs in 33 languages, built by a pipeline that discovers NPIs in Universal Dependencies (UD) treebanks, labels their licensing environments, and perturbs these into minimal pairs. Evaluating 12 multilingual and 2 monolingual models alongside n-gram baselines, we find that multilingual models struggle most with lower-resource languages and with pairs that are not n-gram solvable. We further examine the effects of NPI typology, language family, licensing variability, and NPI-licenser distance. Data: this https URL

---


### 167. [Training User Simulators with Latent Intrinsic Feedback](https://arxiv.org/abs/2610.13617)

**<font color=#1a73e8>作者：</font>** Tarek Naous, Craig Boutilier, Wei Xu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> User simulators are gaining attention as environments to train LLM assistants that can better cope with the nuances of multi-turn conversations with real users. Prior work on user simulation has emphasized generating realistic user utterances, leaving unexplored their potential as a source of direct feedback on the assistant's responses. Such evaluation signals may not be explicitly communicated in language, but can instead reside in the latent reasoning of users. In this work, we introduce user simulators with intrinsic feedback, namely, models equipped with latent evaluation states: internal thoughts, reactions, and scalar ratings that evaluate the assistant from a first-person user perspective at each conversation turn. We train LLM-based simulators using interaction logs between real users and assistants and demonstrate that intrinsic feedback improves simulation realism and critiquing behaviors versus prompted simulator baselines, while also providing turn-level evaluations that existing fine-tuned simulators lack. Further, evaluations generated by our trained simulators correlate better with human judgments than those of prompted simulators of the same size. Lastly, our experiments reveal that simulators with intrinsic feedback provide effective reward signals for multi-turn RL training, matching setups that rely on external judge LLMs for rewards while cutting RL compute by more than half.

---


### 168. [APEX-Harm: Evaluating Agent Safety in Shared Professional Workspaces](https://arxiv.org/abs/2610.13623)

**<font color=#1a73e8>作者：</font>** Ziyi Yang, Adel Bibi, Guohao Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Professional agents increasingly work through command-line interfaces and multiple tools over shared workspaces containing files, messages, and business applications. These environments create safety risks that are difficult to capture with attacks placed at a single, known read location. We introduce APEX-Harm, a benchmark for evaluating prompt and script injection against long-horizon agents performing finance, consulting, and legal tasks in large workspaces. Each task contains 115 to 328 files, together with email, calendar, chat, document, spreadsheet, PDF, and code-execution tools exposed through MCP servers. The benchmark includes six attack categories covering static and dynamic injections, task-specific script replacement, and attacker-provided generic scripts, and evaluates attack success, exposure, and task performance. We evaluate 12 frontier models on 180 task instances per model. Opus 5 and Sonnet 5 have the lowest overall attack success rates (8% and 20%), while task-specific script replacement and attacker-provided generic script attacks remain substantially more effective, averaging 81-84% and 73% attack success, respectively. Gemini 3.8 Flash achieves the highest mean task score (0.877) while still exhibiting a 33% attack success rate. These results show that completing the requested task is not sufficient evidence of safe behavior: an agent can produce a correct deliverable while also performing an unauthorized action in the workspace.

---


### 169. [AMLworld-Compact: Importance-Weighted Downsampling for Cost-Effective LLM Evaluation and Error Diagnosis](https://arxiv.org/abs/2610.13627)

**<font color=#1a73e8>作者：</font>** Natapong Nitarach, Phume Ngampornsukswadi, Pittawat Taveekitworachai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Evaluating large language models (LLMs) on AMLworld's smallest test splits is costly because each of over a million targets requires a separate graph prompt. Sampling reduces this cost, but small balanced subsets change unweighted precision and F1. We introduce AMLworld-Compact, an evaluation set that retains every illicit test transaction and samples benign transactions from supervised-score strata. Its HT-Coreset protocol reduces evaluation targets by 271x and 611x on HI-Small and LI-Small. Horvitz-Thompson weights give unbiased full-test confusion-count estimates for fixed predictions; recall is exact, while precision and F1 are ratio estimates. In a held-out study using Graph Feature Preprocessor (GFP) features, one boosted-tree family defines strata for evaluating the other over 500 draws per configuration. At the released sizes, F1 RMSE is 0.00-2.58 percentage points versus 4.44-7.41 for uniform sampling with HT weights; conservative intervals remain broad. Under the evaluated graph prompts, seven open-weight LLMs have weighted precision near the predict-all-illicit baseline. In an outcome-stratified audit of 1,000 HI-Small few-shot outputs from one run per model, lexical checks pass for 84.5% of correct and 56.2% of incorrect binary verdicts, so these markers do not establish correctness. We release the evaluation sets, construction code, and audit tools at this https URL and this https URL.

---


### 170. [Humanize Olympiad Agents: A Multi-Session Workflow for Olympiad Problem Solving with Solve, Review, Wiki, Verify](https://arxiv.org/abs/2610.13632)

**<font color=#1a73e8>作者：</font>** Zhengyang Zhang, Jing Xiong, Hongzhou Lin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents are rapidly improving on long-horizon scientific and olympiad tasks. Recent systems have produced a Lean-formalized resolution of the Navier--Stokes problem and autonomous solutions to four open questions in the Erdős Conjectures database. Yet neither system releases both its underlying model and complete inference stack. More broadly, a single agent session remains brittle on difficult problems: early errors can propagate, missing domain knowledge can stall progress, and apparent success can mask a misinterpretation or weakening of the original task. We introduce HOA (Humanize Olympiads Agent), an open, flow-level framework that coordinates multiple agent sessions through three complementary feedback channels. First, an independent reviewer evaluates each candidate and provides actionable feedback. Second, a structured wiki supplies task-specific knowledge that may be missing or unreliable in model pretraining. Third, a verifier checks generated Lean proofs against trusted challenge statements. With GPT-5.6 Sol, HOA achieves perfect scores on the IMO, IPhO, and IOI 2026, near-full marks on the IChO 2026 problem set, and solves all 672 problems (100%) on PutnamBench. On the Lean-Eval leaderboard, HOA ranks first, solving 251 of 304 problems (82.6%). We further evaluate HOA with open models. Using Kimi-K3, HOA achieves full scores on the IMO, IPhO, and IOI, and a gold-level score of 97.1% on the IChO. These results closely match the closed-source GPT-5.6 Sol + /Goal baseline on the IMO and IPhO, while exceeding it on the IChO and IOI, demonstrating that systematic feedback can help bridge substantial differences in base-model capability.

---


### 171. [Benchmarking Answer-Grounding Consistency in Remote Sensing Visual Question Answering](https://arxiv.org/abs/2610.13636)

**<font color=#1a73e8>作者：</font>** Ping Guo, Zhiqi Huang, Xinran Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In grounded remote sensing visual question answering, a model produces a textual answer and identifies relevant objects in the image as grounding evidence. Existing evaluations measure answer correctness and localization quality, but do not directly assess answer-grounding consistency. We propose the Answer-Evidence Support Protocol (AESP) to assess this consistency through evidence support: whether the grounding evidence supports the model's own answer. AESP applies task-specific rules to existence, counting, and comparison questions. We further construct the Grounded Remote Sensing Visual Question Answering (G-RSVQA) benchmark, containing 15,027 samples with questions, reference answers, and all related object-level annotations. Experiments on seven grounded vision--language models reveal failures of evidence support across all three question types. Up to 50.82% of correct answers in the evidence evaluation subset are not supported by the provided grounding evidence.

---


### 172. [ToFu: Exploiting and Fuzzing the LLM-Orchestrator-Tool Trust Boundary](https://arxiv.org/abs/2610.13651)

**<font color=#1a73e8>作者：</font>** Md Nazmul Islam Ananto, Pierre Prevost-Avenel, Colin Smith 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed as agents that interact with external software through tools, with an orchestration layer translating model outputs into structured tool invocations. This architecture creates an LLM-orchestrator-tool trust boundary where tool semantics may go unenforced and LLM-generated arguments may be incorrectly treated as trusted. We present ToFu, a tool-aware framework that automatically derives semantic security checks for LLM tools from their existing metadata and a CWE-guided sanitizer corpus. ToFu specializes these checks to individual tools and automatically generates fuzzing harnesses and semantic oracles using runtime introspection and outcome sanitization. We evaluated ToFu across 273 MCP servers containing 3405 tools and identified verified bugs corresponding to CWE weakness classes in 343 tools across 118 of the servers. Our findings show that real-world tools frequently fail to enforce their documented input semantics, making it unsafe to treat LLM-generated arguments as trusted.

---


### 173. [A Multi-Agent LLM System for Automated Tuning of Specialized Neural Network Models](https://arxiv.org/abs/2610.13663)

**<font color=#1a73e8>作者：</font>** Ivan Moloshnikov, Dmitry Kunitsyn, Alexander Sboev 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Many machine learning approaches are two-level: an expert selects a class of methods, within this class the choice of key components is critical and usually manual. This paper addresses the automatic tuning of these components and proposes a framework transferable across models of different nature. The multi-agent large language model (LLM) framework has three roles---analyst, coder, and recorder~---with an experiment log and a sandboxed execution environment. Unlike systems that optimize the entire ML script or search architectures in a discrete space, the framework operates over an open but semantically narrow space: the agent generates code only for the specified components, leaving the overall network structure unchanged. The approach is validated in two directions: tuning a classification spiking neural network with correlation learning, and solving high-order differential equations with Physics-Informed Neural Networks (PINN). Across five tasks---spiking classification on MNIST and Digits, and boundary-value problems for the generalized nonlinear Schrödinger equation (GNLSE) and Kuramoto--Sivashinsky (KS) equations---the agent outperforms the baselines: classification accuracy is 13 percentage points (MNIST) and 6 percentage points (Digits) higher; the error against the analytical single-soliton solution is reduced approximately 2491-fold; the invariant-preservation error drops approximately 325-fold in the selected GNLSE run with a Gaussian perturbation and by more than 100-fold on average over repeated initializations; and the mass drift drops 14-fold for the KS problem with a Gaussian perturbation. The framework thus tunes key components on tasks of different nature without changing its internal structure.

---


### 174. [A Step Harder, Not a Step Too Far: The Benefits and Limits of Curriculum Difficulty Progression in GRPO](https://arxiv.org/abs/2610.13669)

**<font color=#1a73e8>作者：</font>** Ronghan Li, Fei Chen, Mingyu Lu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Curriculum learning typically organizes training samples from easy to hard. In GRPO, medium-difficulty samples are attractive for online selection because they are more likely to yield informative group-relative learning signals, and prioritizing them can improve training efficiency. However, it remains unclear whether persistently selecting such samples also leads to the strongest final model performance, or whether training can benefit from progressing toward harder samples. Meanwhile, sample difficulty changes as the policy evolves, so fixed difficulty estimates can become misaligned with the current policy. We therefore re-estimate sample difficulty under the current policy and, inspired by the easy-to-hard principle of curriculum learning, design and evaluate a staged curriculum that progressively shifts the active difficulty band toward harder samples. Experiments on GSM8K show that persistent medium-difficulty selection does not achieve the strongest observed performance. Across three random seeds, progressing to a moderately harder difficulty band improves test accuracy to $0.6591 \pm 0.0077$, compared with $0.6449 \pm 0.0024$ for the fixed-medium curriculum. However, further progression to a harder difficulty band reduces accuracy to $0.6405 \pm 0.0053$. These results show that staged difficulty progression can outperform persistent medium-difficulty selection, but its benefit is non-monotonic. Effective GRPO curricula can therefore benefit from progressing beyond medium difficulty, while avoiding excessive progression toward overly difficult samples.}

---


### 175. [Inject a Turn, Not a Token: Learning Where to Redirect LLM Reasoning for Self-Correction](https://arxiv.org/abs/2610.13672)

**<font color=#1a73e8>作者：</font>** Jiwon Jeon, Myungsik Cho, Jeonghye Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models struggle to reliably identify and correct errors in their own reasoning. Unlike prior training-based approaches that fine-tune an LLM to generate revisions or feedback, we learn where to intervene in failed rollouts and determine how to redirect them. To choose where to intervene, we train a 130K-parameter MLP head on a frozen encoder using only final-answer correctness. For redirection, we find that under a fixed generation budget, the tested inline injections fail to reliably redirect reasoning, whereas presenting the same instruction in a new user turn changes the model's course. The resulting correction framework, UPTURN (User-Prompt TURN injection at a learned position), requires no LLM fine-tuning: it retains a selected prefix, injects an instruction as a new user turn, and regenerates the suffix. Across four reasoners and six math benchmarks, UPTURN improves average accuracy in every setting over a 32-rollout baseline. It outperforms self-correction and reflection-token injection baselines under matched correction budgets, transfers across reasoners and to GPQA-Diamond without retraining, and complements GRPO and self-correction methods.

---


### 176. [Verifiable Retrieval for Legal Reasoning through Structure-driven Knowledge Graph](https://arxiv.org/abs/2610.13695)

**<font color=#1a73e8>作者：</font>** Ibrahim Siddig, Sviatoslav Tugeev, Munir Georges  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Any automation within reliability-critical contexts such as medicine or law has to be transparent and verifiable. Despite their advantages, current LLM-based systems do not meet these requirements due to their inherent black-box nature. Retrieval Augmented Generation (RAG) attempts to ground the generative process in the relevant interpretable documents, thereby reducing the risk of AI 'hallucinations' and potentially enabling verification of the initial generation context. However, as the number and size of potential sources increases, naive retrieval approaches tend to perform worse, ignoring critical context elements. In this paper we aim to tackle this problem in the context of German Legal Code. Using structure-driven parsing to create a Knowledge Graph (KG) for the source document navigation and retrieval, we compare several KG-informed chunking and retrieval strategies and evaluate their effect on the accuracy of retrieved citations.

---


### 177. [Improving Semantic Coverage in AI Test & Evaluation through Generative Augmentation](https://arxiv.org/abs/2610.13697)

**<font color=#1a73e8>作者：</font>** Connor Hashemi, Bharadwaj Ravichandran, Connor Anderson 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In test and evaluation (T&E) of AI models, evaluators typically have access only to a held-out test dataset and no knowledge of the training data or its semantic composition. If critical input conditions---such as time-of-day, weather, or scene location---are underrepresented in this test dataset, T&E results can be misleadingly due to this semantic coverage gap. We propose a three-stage generative AI pipeline to detect and fill such semantic gaps without requiring ground-truth labels of these semantics. First, vision-language models (VLMs) perform zero-shot binary labeling of semantic factors, and an embedding-space clustering step identifies which semantics most affect downstream model behavior. Second, diffusion-based image-to-image models transform existing covered images into the underrepresented semantic domain, preserving scene content while augmenting high-level appearance. Third, statistical analysis of the augmented image embeddings verifies that the synthetic imagery improves dataset coverage before it is incorporated. Crucially, the synthetic data is used only to enrich the test set and no model retraining is performed for T&E. We validate the full pipeline on both image classification and object detection under day/night semantic gaps, showing that the augmented test datasets better distinguish models with and without exposure to the missing semantic, thereby yielding T&E conclusions that more closely match those of an ideal, fully covered dataset. Code available at this https URL

---


### 178. [A Baseline Assessment for the Agentic Web Technology Stack](https://arxiv.org/abs/2610.13703)

**<font color=#1a73e8>作者：</font>** Vagner Figueredo de Santana, Diogo Cortiz  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The fast pace in which protocols, frameworks, and technologies are being proposed for LLM-based agents results in a complex scenario for anyone aiming to create state-of-the-art AI solutions. Without an assessment on how different protocols, frameworks, and libraries work together to compose an Agentic Web solution, developers and organizations face different challenges (e.g., skilling, governance, infrastructure) even before becoming part of the Agentic Web ecosystem. In this context, we propose a system for performing Agentic Web evaluations called MASTIF (Multi-Agent System TestIng Framework) and present a baseline assessment of Agentic Web technologies, including 3 LLMs, 3 protocols, and 4 agent implementation frameworks, against 300 Mind2Web benchmark tasks. Results suggest that selecting a task-specific technology stack may result in gains of task completion rate, efficiency score, and social value stability scores; and reductions in verbosity and time to complete tasks. With the presented results, we expect to present a baseline in terms of metrics and results for this complex and fast evolving scenario for those aiming at designing, assessing, and developing multi-agent systems.

---


### 179. [Adaptive DHiSparse: Speculative Decoding over a Load-Adaptive KV Hierarchy](https://arxiv.org/abs/2610.13708)

**<font color=#1a73e8>作者：</font>** Naji Alazhar, Wassel Alazhar  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-context serving runs out of KV memory before the hardware reaches its useful throughput. HiSparse stores history in host memory and fetches only the selected entries, but it uses one cache budget at every load and does not handle draft-model speculative decoding such as DSpark and DFlash2. We present Adaptive DHiSparse, which supports speculative decoding over hierarchical sparse KV and adapts residency to load. It protects the required working set, retains additional history while GPU memory is spare, and recovers the rest through exact fused retrieval. DSpark and DFlash2 keep their proposal and acceptance rules: queries share missing-row retrieval, draft KV uses a window-bounded ring, and verification staging is reused across layer groups. At 100K context and concurrency 128, GLM-5.3 with DFlash2 delivers 793 output tokens/s per decode GPU, 1.45$\times$ HiSparse and 1.27$\times$ non-speculative adaptive serving. Held to the same latency bounds as HiSparse, it sustains up to 4$\times$ the concurrency and 2.3 to 3.7$\times$ the output, depending on the per-token bound. On DeepSeek-V4.1-Flash at 500K context and concurrency 512, Adaptive DHiSparse with DSpark delivers 1.85$\times$ the output of resident serving with DSpark. In a load step, optional residency reduces host fetches from 14.2% to 1.4% of selected rows at low load and releases memory under pressure.

---


### 180. [OpenSocialJax: Evaluating Social Adaptation in Sequential Social Dilemmas with Open-Ended Environmental Dynamics](https://arxiv.org/abs/2610.13710)

**<font color=#1a73e8>作者：</font>** Zihao Guo, Meng Fang, Joel Z. Leibo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Sequential social dilemma benchmarks capture diverse social interactions, but rarely test whether agents can infer hidden environmental rules through repeated interaction while adapting to other agents. We introduce \textbf{OpenSocialJax}, which extends Clean Up and Commons Harvest across an open-ended distribution of latent environment configurations, systematically varying spatial layouts and hidden rules governing tool crafting, payoffs, and resource dynamics. Each episode samples one configuration from tens of millions of possibilities and holds it fixed across five trials. We evaluate eight large language models, including three closed source models and five open source models. Our evaluation tests whether models can discover hidden rules and adapt to other agents in homogeneous and mixed teams. We find that rule discovery often improves performance but does not reliably sustain cooperation, as the cleaning burden becomes concentrated among fewer agents in OpenCleanup and every team eventually exhausts the shared resource in OpenHarvest. In our mixed arena, one cooperative agent was able to sustain the public good in OpenCleanup at a cost to its own return, but could not prevent resource depletion in OpenHarvest. Together, these results highlight the difficulty of adapting jointly to unfamiliar environmental dynamics and the changing behavior of other agents.

---


### 181. [Enhancing Legal Reasoning in Pre-trained Language Models via Knowledge Graph-Guided Multi-Task Pre-training](https://arxiv.org/abs/2610.13722)

**<font color=#1a73e8>作者：</font>** Ibrahim Siddig, Munir Georges  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Legal language understanding requires reasoning over semi-structured regulatory documents, yet standard pre-training objectives do not explicitly target this structural capability. Because current legal language models rely solely on masked language modeling, they treat statutory text as flat token sequences and ignore the underlying hierarchical constraints. To bridge this gap, we present a multi-task pre-training approach for German traffic law (StVO). Our approach combines three complementary objectives: Next Sentence Prediction (NSP), Knowledge Graph (KG) Guided Clustering (CLU), and Knowledge Graph (KG) Aware Paragraph Classification (CLS). This approach explicitly encodes structured legal knowledge directly into the model weights. This encoding enables zero-shot legal reasoning at inference time and removes the need for discrete graph traversal. We evaluate our approach across nine Transformer-based encoders and 324 experimental runs. On synthetic StVO question answering, our models demonstrate consistent relative improvements between 10.3% and 155.0% over baselines. Furthermore, relative to the established LexGLUE baselines (Chalkidis et al., 2022), our models improve over prior results on four of seven legal benchmarks. It also achieves consistent zero-shot transfer gains between 3.4% and 15.8% on Austrian driving regulations. These experimental results indicate that our training approach generalizes successfully beyond the initial training legal domain.

---


### 182. [LAPT-Scale: Scaling Embodied Policies with Latent Action Pre-Training on Human Videos](https://arxiv.org/abs/2610.13732)

**<font color=#1a73e8>作者：</font>** Zhiyuan Xiang, Peidong Liu, Mingyang Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scaling generalist robotic policies is limited by the high cost of collecting embodied interaction data. Large-scale egocentric human videos offer a rich alternative, but they lack robot action labels, and existing action annotation methods are often noisy under real-world visual complexity and diverse manipulation dynamics. We introduce LAPT-Scale, a scalable latent action pre-training paradigm with two components: LAPT-Scale-LAM learns continuous latent actions by explaining frame-to-frame visual transitions in human videos and uses them as human-derived supervision, while LAPT-Scale-Policy trains a VLA policy through human-video latent-action pre-training, target-robot embodiment alignment, and task-specific post-training. Unlike prior vector-quantized LAMs, LAPT-Scale-LAM uses a continuous latent space to preserve fine-grained motion and interaction dynamics. We further combine perceptual, semantic, and optical-flow alignment signals to improve transition-level supervision beyond pixel reconstruction. Trained on 23.3K hours of egocentric video, LAPT-Scale-LAM provides implicit action supervision for policy pre-training, yielding consistent scaling gains and improving real-robot success from 63.3% to 85.0% as annotated human video scales from 1K to 5K hours. The learned policy also generalizes to unseen visual conditions.

---


### 183. [Studying the Effects of Task Diversity Using Small Mathematical Worlds](https://arxiv.org/abs/2610.13750)

**<font color=#1a73e8>作者：</font>** Emily Xia Meng, Xuanyu Yang, Junaid Hasan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Basic mathematical tasks like modular addition have been a valuable tool for illuminating aspects of neural network behavior that are challenging to see in noisy, unverifiable, large-scale, real-world settings. These studies have typically focused on a single task. However, modern language models are exposed to a vast number of tasks despite being trained with a next-token prediction objective. In this work, we introduce two mathematical task ecosystems, IntWorld and PermWorld, built from distinct but related tasks on integers and permutations. Both are designed to simulate task diversity within a cohesive mathematical 'world' where tasks are distinct but related. Because the datasets are procedurally generated, we can precisely vary the number of tasks, allowing us to begin to disentangle the role of task variety from other factors in training. After describing the datasets, we provide some initial results obtained from these datasets which support the idea that increasing task diversity increases the richness of a model's internal representations.

---


### 184. [Matched-Context Group Policy Optimization for LLM Agent Training](https://arxiv.org/abs/2610.13755)

**<font color=#1a73e8>作者：</font>** Chenxu Zhang, Yaorui Shi, Wenlong Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training long-horizon language model agents requires assigning credit to intermediate decisions from sparse terminal feedback. Within a finite group of sibling rollouts, useful action comparisons depend on their context, evidence for both alternatives, and how that evidence enters learning. We propose Matched-Context Group Policy Optimization (MCGPO), a procedure for constructing weighted action preferences from already collected trajectories. MCGPO defines comparison contexts with pre-action state summaries and observed rubric progress, annotated by task rules. Two-action support selects among ordered exact and coarse matching rules. Fixed folds separate candidate decisions from the terminal outcomes used to orient their preferences, and support-dependent evidence weights scale an auxiliary pairwise objective alongside shared GraphGPO task learning. MCGPO reuses rollout data and each response's original history, preserving critic-free training. Across six environment-backbone settings with three training seeds each, MCGPO improves mean success over matched GraphGPO: by 0.47-1.46 percentage points on ALFWorld and WebShop with Qwen2.5-1.5B and 7B, and by 3.96 and 5.16 points on WebShop with Qwen3-4B and 8B. The ALFWorld gains build on baseline success above 92%, where remaining headroom is limited. Integrated success improves in three of four Qwen2.5 settings. Three-seed factorial controls support opposite-fold evidence and evidence weighting; joint state-rubric matching achieves the highest mean in all four representation-control settings.

---


### 185. [DualQuant: Dual-scale Calibration-free Weight-and-Activation Quantization for LLMs](https://arxiv.org/abs/2610.13767)

**<font color=#1a73e8>作者：</font>** Mahsa Salmani, Sayeh Sharify, Hesham Mostafa  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-bit inference on accelerators with native 4-bit support requires quantizing both weights and activations to realize the full throughput gains these formats provide. While post-training weight quantization has been extensively studied, activation quantization remains considerably more challenging and typically requires calibration data. In this work, we introduce DUALQUANT, a dual-scale, calibration-free post-training quantization framework that directly minimizes the weight-reconstruction Mean Squared Error (MSE) and, as an immediate by-product, yields per-channel activation rescalings prior to activation quantization. Our key observation is that the scaling factors obtained by minimizing weight-reconstruction error provide effective activation rescalings, enabling competitive activation quantization without calibration data. We formulate DUALQUANT as a non-differentiable weight-reconstruction problem and develop an efficient solver based on variable splitting and block coordinate descent, where each subproblem admits a closed-form update. DUALQUANT provides a unified algorithm supporting a wide range of formats, including the full MX family and NVFP4. To our knowledge, DUALQUANT is the first dual-scaling method to formally support MX and NV block formats. Across Llama and Qwen models evaluated on WikiText-2, C4, and zero-shot downstream tasks, DUALQUANT matches or exceeds the accuracy of calibration-based SmoothQuant across most models and formats, and substantially outperforms calibration-free baselines, with large gains for MX and NV block formats. We validate these gains with a real packed W4A4 inference path for Llama-3.1-8B on an RTX 4090. The resulting implementation closely matches the accuracy of fake quantization while delivering up to 2.61x memory reduction and up to 2.46x throughput speedup over BF16.

---


### 186. [ReplaySSM: Cache SSM Inputs, Not State](https://arxiv.org/abs/2610.13778)

**<font color=#1a73e8>作者：</font>** Ze-Wei Liou, Harris Nover, Amey Naik 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> State-space models (SSMs) maintain a fixed-size recurrent state, but reading and writing it at every decoding step can bottleneck hybrid models. This eager state management causes large state I/O with low arithmetic intensity, leaves speculative decoding no cheap rollback, and feeds state quantization error into subsequent recurrent updates. We introduce ReplaySSM, which unrolls the recurrence to represent the state as a checkpoint and a buffer of recent SSM inputs. This separates output computation from checkpoint updates. By updating the checkpoint periodically, ReplaySSM avoids state writes on most steps and roughly halves the dominant state memory traffic. Keeping recent inputs also makes speculative rollback a buffer-pointer operation and enables output-only verification without materializing intermediate states. The same separation allows a low-precision checkpoint to serve output computation on most steps while a higher-precision checkpoint serves recurrent updates, so rounding error in the low-precision copy never enters later updates. We implement ReplaySSM in vLLM for Mamba-2 and Gated DeltaNet. At serving batch size 256, it accelerates standard decoding by $1.20$--$1.47\times$ over a tuned vLLM baseline across four hybrid models, and delivers about $1.8\times$ the throughput of vLLM's speculative decoding on the two 120B-class models. Separate state precisions also reduce output KL divergence and downstream accuracy losses compared with a shared low-precision checkpoint.

---


### 187. [UkrMeme: Multimodal Explainable Persuasion Detection in Ukrainian Memes](https://arxiv.org/abs/2610.13783)

**<font color=#1a73e8>作者：</font>** Nazar Andrushko, Vera Schmitt, Veronika Solopova  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Memes play a central role in modern online communication, especially in contexts of political conflict where visual and textual cues combine to convey persuasive messages. We study persuasive technique detection in Ukrainian memes using vision-language models (VLMs). We introduce UkrMeme, a dataset of 200 organically produced Ukrainian wartime memes annotated for persuasion techniques, and PTM-UA, a Ukrainian translation of a subset of the Propaganda 950 benchmark that preserves original visual content while translating meme text. We evaluate VLMs in a zero-shot prompting setup across image, text, and multimodal inputs using hierarchical F1 metrics. Finally, we compare Layer-wise Relevance Propagation (LRP) and model-generated token attributions and analyze the semantic categories of evidence emphasized by each explanation method.

---


### 188. [OccludeBench: Can VLMs Find What's Missing?](https://arxiv.org/abs/2610.13790)

**<font color=#1a73e8>作者：</font>** Jasin Cekinmez, Addison J. Wu, Ryo Mitsuhashi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> How well can vision-language models (VLMs) reason about what is missing from an image? We study this question with OccludeBench, a manually curated benchmark for recovering fully occluded objects from the visual evidence that remains. OccludeBench distinguishes direct cases, where the hidden object must be recovered from a specific physical cue such as a shadow or reflection, from inferential cases, where it can be inferred from broader scene context. Across five VLMs, accuracy averages 42.7% on direct cases versus 62.7% on inferential cases, exhibiting a 20.0-point gap. Humans attain higher accuracies of 63.4% versus 68.5% for direct and inferential images, respectively, with no significant gap. To locate this failure, we introduce OccludeTrace, a four-stage diagnostic that isolates where the visual reasoning process breaks down. The bottleneck emerges when models must recover the relevant object from the projection within the full image: they succeed on only 50% of failed examples, compared with 91% of examples they answer correctly. Extended reasoning, tool use, and few-shot prompting yield inconsistent improvements and do not reliably eliminate the gap. In contrast, an inpaint-then-confront intervention, which prompts models to first generate a candidate hidden object and then evaluate that hypothesis against the visible physical cue, reduces the gap to a statistically non-significant difference for both models with image-generation capabilities. Together, our results establish a tractable, controlled diagnostic for isolating how VLMs reason about visual content that is missing from an image.

---


### 189. [Not Just an Evaluation: A Case Study of Discourse Particle Sensitivity in Language Models](https://arxiv.org/abs/2610.13794)

**<font color=#1a73e8>作者：</font>** William Sheffield, Jiahui Chen, Amy Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Discourse particles subtly shape the flow of discourse by reflecting conversational context and interlocutor attitudes, often leaving the truth-conditional meaning untouched. They are also often polyfunctional, with distinct senses which partially overlap with other particles; for example, the exclusive use of English "just" and "only" ("John only/just drinks water"). Despite the frequency of these words in natural language, they have gone largely unstudied due to the subtle nature of their effects. We investigate LLM sensitivity to "just" and "only" in natural conversations using behavioral and mechanistic analyses. First, we find that LLMs and humans similarly prefer the presence of these particles in context, and both are more sensitive to "just" compared to "only". Second, when sampling from LLMs with and without these particles, we find LLMs consistently rate generations as more likely, given their source context, demonstrating their particle sensitivity. In both experiments, instruction tuning increases sensitivity. Finally, we localize particle-sensitive units within LLMs and find the overlap between "just" and "only" is asymmetric: "only" units transfer selectively to exclusive "just", while all "just" units transfer to "only" equally well regardless of sense, suggesting LLM lexical-level particle representations are partially organized by sense. We release our code, sense-labeled dialogue stimuli, and human preference annotations at this https URL.

---


### 190. [QTestBench: A Test Framework for Evaluating LLM-Generated Quantum Code](https://arxiv.org/abs/2610.13811)

**<font color=#1a73e8>作者：</font>** Meriem Terki, Nouhaila Innan, Minghao Shao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have shown strong results in classical code generation and are increasingly used to write the unit tests that safeguard that code. Whether they can do the same for quantum software is less clear, because quantum programs are probabilistic, depend on numerical tolerances, and are judged by domain-specific checkers, so a well-formed test can still disagree with the benchmark's verdict. Existing quantum benchmarks measure whether a model produces a correct solution, but not whether its tests can distinguish correct implementations from faulty ones. We introduce QTestBench, a framework that evaluates LLM-generated quantum test suites against independent benchmark checkers, never treating the tests themselves as ground truth. For each task, QTestBench prompts models to produce syntactic, semantic, and behavioral tests, injects candidate solutions at runtime, and compares each test verdict with the checker's label under three validation cohorts, each answering a distinct diagnostic question. We benchmark five LLMs on eight PennyLane QHack challenges and ten Qiskit HumanEval tasks. Generated suites almost always execute, but discrimination lags behind: the best generator reaches a test quality of 0.71 on QHack and 0.34 on Qiskit HumanEval, so executability alone overstates test quality. Oracle-verified synthetic mutants stabilize bug-detection estimates when natural faulty solutions are scarce, as on three of ten Qiskit tasks that yield none. QTestBench offers a reproducible, cross-framework benchmark for the trustworthiness of LLM-generated quantum tests.

---


### 191. [Can Language Models Learn When to Abstain? Policy Learning and Calibrated Answer Selection](https://arxiv.org/abs/2610.13821)

**<font color=#1a73e8>作者：</font>** Juan Terven, Diana-Margarita Córdova-Esparza, Ruben Gomez 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A useful language model should know when to answer and when to say "I don't know." Can we improve that decision by training the model itself or by training a separate component to check its answers? We study both approaches on Qwen3-14B for factual questions, using a score that rewards correct answers, penalizes mistakes, and allows abstention. Across three training seeds and two held-out confidence thresholds, a learned answer selector improves threshold-averaged utility over the original model's calibrated confidence filter. On TriviaQA, mean coverage increases from 20.2% to 30.9%, while the pooled error rate among scored answers decreases from 23.0% to 14.5% under exact-match grading. The tested reinforcement-learning changes do not establish consistent gains. On NQ-Open, the selector improves threshold-averaged utility over the filter but still performs worse than always abstaining. A partial human-reviewed audit preserves the TriviaQA finding. Our results support learning to select answers in this setting while showing that reliable abstention across datasets remains unresolved.

---


### 192. [SpatialASM: Internalizing Active Mentalization for Spatial Reasoning](https://arxiv.org/abs/2610.13832)

**<font color=#1a73e8>作者：</font>** Yuhong Liu, Shenxi Wu, Junyi Chi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> When solving complex spatial reasoning tasks, ordinary humans naturally revisit the scenes from task-relevant viewpoints and mentally reconstruct the spatial layouts from those viewpoints. But can Large Vision-Language Models (LVLMs) proactively think in the same way? We term this ability Active Spatial Mentalization (ASM), an intrinsic component of visual intelligence that remains substantially underdeveloped in current LVLMs. To bridge this gap, we introduce SpatialASM, a scalable framework to internalize ASM into LVLMs through training-time spatial simulation. SpatialASM employs an allocentric novel-view generator to ground hypothetical viewpoints in visual evidence and produces two complementary forms of supervision: i) explicit ASM trajectories that teach LVLMs when and how to adaptively invoke view planning and imagination during spatial reasoning, and ii) automatically-constructed perspective-taking tasks that further strengthens viewpoint-conditioned scene imagination. On seven benchmarks spanning relatively perception-oriented spatial understanding to more challenging tasks requiring multi-image, cross-view and viewpoint-transformation reasoning, SpatialASM yields performance gain on LVLMs of four LVLM backbones in spatial reasoning while retaining their original general vision capabilities. The experimental results demonstrate that our approach improves average accuracy across the seven spatial benchmarks. And the synthesis of ASM trajectories provides a scalable pathway to alleviate the scarcity of spatial Chain-of-Thought (CoT) supervision for eliciting active viewpoint exploration and mental scene simulation.

---


### 193. [On the Design Space of Continuous Diffusion Language Models](https://arxiv.org/abs/2610.13834)

**<font color=#1a73e8>作者：</font>** Oscar Davis, Daan Roos, Alice Bizeul 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continuous diffusion language models (CDLMs) promise to bring the benefits of continuous flow modelling to language, including accelerated sampling and controllable generation. The field has grown rapidly, and the capabilities of CDLMs have begun to rival those of discrete diffusion. Yet, unlike for continuous modalities such as images or videos, our grasp of the levers that matter when training CDLMs remains limited. In this work, we focus on two of these levers, namely self-conditioning and embedding geometry, and shed light on some of the mechanisms behind them, which in turn suggest cheaper and more effective designs. We begin by showing that self-conditioning corrects a train/inference mismatch by exposing the model to inference-like states that are otherwise rare during training. These gains can be recovered without an extra forward pass by a two-level interpolant, coined $\mathrm{DoubleCat}$, which improves TinyGSM accuracy more than threefold. Self-conditioning also aids in recognising tokens dominated by large-norm Gaussians$\unicode{x2013}$an issue known as token identifiability. To address it directly, we introduce discrete reveals to $\mathrm{DoubleCat}$, yielding $\mathrm{SemiCat}$, which achieves discrete diffusion-level performance on TinyGSM, reaching $49.94\%$ with standard training hyperparameters and a tuned sampler. At the $1.7$B scale, $\mathrm{SemiCat}$ outperforms discrete diffusion on four of six likelihood-based evaluations, and surpasses one-hot flows on unconditional generation. On embedded spaces, we find that cross-entropy drives embeddings towards a geometry whose decoding error rate closely matches the one-hot one. We briefly explore a range of further options, such as hybrid corruption processes and noise schedules, including asynchronous ones. We believe this exploration can help the community better understand and advance the design space of CDLMs.

---


### 194. [Studying Comics at Scale with Artificial Intelligence: The PAGE Framework and Three Studies of American Comics and Japanese Manga](https://arxiv.org/abs/2610.13840)

**<font color=#1a73e8>作者：</font>** Emilio Ferrara  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Comics are one of the great visual records of the twentieth century: hundreds of thousands of pages in which a mass readership saw its leaders, its wars and its heroes. Most of this record has never been studied as a whole; comics scholarship proceeds one book at a time. We argue that artificial intelligence, including generative models, can change this to the benefit of the medium itself. We propose PAGE, a framework that makes artificial intelligence an instrument for comics research. It parses every scan into panels, text and a bibliographic record; annotates each page with a vision-language model that follows a written codebook, as a human coder would; grounds samples of these readings in human annotation; and explains change across an archive, with estimates controlled for publisher and genre. We demonstrate the framework on 3,929 American comic books (1938--1956) and 87 volumes of Japanese manga, in three studies, each resting on a different capability. The first pairs text search with visual reading to recover how a mass medium portrayed political power. The second measures the page's visual form across an industry and recovers the hand of individual artists. The third follows who speaks across two comics traditions, checked against human annotation. Beyond research, the same instruments can make archives searchable by what is drawn, open comics to blind and low-vision readers, and help preserve fragile collections and credit uncredited artists. We outline a research agenda in which artificial intelligence strengthens the study, preservation and reach of the medium.

---


### 195. [Returning to Development States: When Full Sandbox Snapshots Help Coding Agents](https://arxiv.org/abs/2610.13841)

**<font color=#1a73e8>作者：</font>** Daniel Thi Graviet, Tanmay Shah  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Coding agents often make useful progress before they fail, but retry-from-scratch discards the machine state created along the way. This makes failure recovery an interesting search problem: if intermediate environment states preserve meaningful progress, restoring and branching from them could outperform repeatedly restarting from the initial state. We implement Go-Explore-style search over full Daytona snapshots and find that higher and more efficient solve rates depend mainly on progress that sits outside the repository, such as databases, services, and other runtime state. Our results suggest that full-snapshot search is most effective when long-horizon coding work spans multiple services whose state cannot be reconstructed from a single diff.

---


### 196. [LapMerge: Differentiable Exact-Budget Token Merging in Linear Time](https://arxiv.org/abs/2610.13858)

**<font color=#1a73e8>作者：</font>** Magdalena Trędowicz, Aleksandra Nowak, Tomasz Steifer 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern vision and language models process ever longer token sequences, and reducing them is the main lever on downstream cost. Token compression, however, faces a fundamental trade-off: selecting tokens discards information, while existing merging methods preserve it only through pairwise token-to-token matching or $MN$ token-to-output interactions. We introduce LapMerge, a differentiable merging operator that resolves this trade-off for ordered sequences: a learned mass distribution partitions the sequence into exactly $N$ equal-mass segments under a Laplace-kernel density, and prefix/suffix scans aggregate each segment, so both the forward and the backward pass run in $\mathcal{O}(M+N)$ time. This combination - an exact output budget, end-to-end differentiability, and linear cost - is precisely what previous reducers trade off against one another. The budget can be changed without changing operator parameters, and the learned mass doubles as a token-level map of where the budget is allocated. Across vision and vision-language tasks, LapMerge matches or improves on strong token reducers while being up to two orders of magnitude faster at large sequence lengths; it is particularly effective when token order reflects spatial or temporal locality, and works both as a drop-in reduction module and as a trainable architectural component.

---


### 197. [Ask Your Advisor: Learning When to Consult Stronger Models in Agentic Systems](https://arxiv.org/abs/2610.13870)

**<font color=#1a73e8>作者：</font>** Pascal Sowietzki, Steffen Holter, Yannick Metz 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> To balance task performance and computational cost, agentic workflows can use a lower-cost model for execution and selectively consult a stronger model. In such executor-advisor systems, the executor decides when to seek advice, making escalation depend on self-assessment, although current language models struggle to detect where their own reasoning fails. The need for stronger reasoning emerges during execution and varies across workflow phases. We introduce ARIA, a meta-controller that learns when to consult by balancing task success against consultation cost. Our approach formulates consultation as a sequential resource-allocation problem. At workflow contact points, ARIA maps execution evidence to a compact state abstraction and selects SILENT or CONSULT, with action values learned by Monte Carlo control from cost-penalized outcomes. Across evaluated tasks of SWE-bench Verified, Terminal-Bench 2.1, and $\tau^2$-bench, ARIA recovers 44-81% of the executor-advisor success gap at less than half the advisor model's cost. ARIA achieves the best observed success-cost trade-off among ten other evaluated conditions, including routing and cascading methods, fixed and prompted consultation, and random placement at matched advice volume. The policies are compact and inspectable, with a single consultation-price parameter governing the success-cost trade-off without retraining either underlying model.

---


### 198. [Task Context Shapes Component Roles in Language Models](https://arxiv.org/abs/2610.13895)

**<font color=#1a73e8>作者：</font>** Sovesh Mohapatra, Dani S Bassett  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models reuse the same attention heads across tasks, but identifying these shared heads does not explain what they do differently in each task. A natural source of inspiration is task-dependent interactions among shared brain regions, which motivate a network view of language-model computation. Here, we compare fixed model components across tasks using identical graph facts, statements specifying which directed connections are present. We measure how interventions affect attention heads and the activation state in later layers (influence), as well as the answer (importance). Task changes redistribute the influence in five open-weight models spanning four families and 1.5-14 billion parameters. In Gemma-2-9B and Qwen3-14B, an activation edit changes an early internal activation vector and switches which fact the model reads while the written instruction stays fixed. The same heads then respond to different graph facts and influence later components differently. For each prompt, we construct two linear response maps, one before the edit and one after it. Each map predicts a later head's response from a measured change in an earlier head. For a separate factual intervention, the map for the corresponding condition reduces mean squared prediction error by 53.6% in Gemma and 5.0% in Qwen compared with the average of the two maps. These findings show that task context changes both which graph facts the shared components respond to and how their outputs affect later computation. A network account may help explain how models use shared parameters to perform different computations. Measurements of task-dependent influence could also guide interventions intended to alter one behavior while preserving others.

---


### 199. [When VLMs Destroy What They Know: Spatial Representations Fall Below Lexical Priors](https://arxiv.org/abs/2610.13910)

**<font color=#1a73e8>作者：</font>** Shubh Garg, Chen Shani  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) increasingly analyze and reason about images, yet it remains unclear whether their internal representations faithfully encode the structured relations required for such reasoning. We introduce EICS (Evaluation-Invariant Concept Stability), a metric for testing whether representations consistently encode concepts under controlled one-concept interventions, and CASP-VL (Causally controlled Spatial Perturbations for Vision-Language models), a benchmark of causally controlled spatial perturbations derived from Visual Genome scene graphs. Across multiple VLM architectures, we find that spatial relations are represented substantially less faithfully than lexical information, even when the same models score well above chance on compositional benchmarks. Further analysis shows that the relation is identifiable at the predicate's own tokens but is lost when the sentence is aggregated into a global representation, whether through the (EOS) token or by mean pooling. These findings reveal a systematic failure invisible to output-based evaluation: VLMs do not preserve, in the representation used downstream, relational information that is present in their own input.

---


### 200. [Can machines reason non-verbally?](https://arxiv.org/abs/2610.13925)

**<font color=#1a73e8>作者：</font>** Shaheer U. Saeed, Zion Tse, Gregory Slabaugh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern machines can solve equations, follow logic and reason through language, yet they still struggle with problems that require visual non-verbal reasoning. This is evident even in advanced systems such as DeepSeek, ChatGPT and Gemini, which remain limited on visual tasks such as completing abstract patterns or delineating ambiguous regions-of-interest. Unlike explicit intermediate steps in verbal reasoning which can be verified through logic or automated tests, visual reasoning involves implicit intermediate steps with no clear methods for verification. Non-verbal reasoning is therefore challenging to model and, as a result, remains a fundamental limitation of current machine intelligence. Here we introduce GenVerOpt, a general framework that unifies generation, verification and optimisation into a reasoning pipeline for machines. By generating candidate solutions, verifying their correctness, and iteratively refining them, GenVerOpt enables per-sample optimisation rather than relying solely on dataset-level trends captured during model training. This process mirrors human problem-solving where multiple possibilities are imagined, evaluated, and refined until a correct solution emerges. Across diverse domains, GenVerOpt demonstrates capabilities beyond existing systems: it surpasses humans on abstract IQ puzzles, matches clinicians in prostate cancer segmentation, exceeds experts in liver vessel reconstruction and outperforms state-of-the-art approaches in tumour boundary alignment. These results show that machine reasoning can extend beyond language, establishing visual non-verbal reasoning as a foundation for more flexible and generalisable intelligence.

---


> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-230](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
