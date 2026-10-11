# 🧠 大模型相关研究 | 2026年10月12日

> 本类共 **288** 篇论文：已确认 **273** 篇，待复核 **15** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**1-50**（第 1/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-288](./part-06.md)

---

### 1. [Synthesis Through Simulation: Generating Coherent Enterprise Data via Scalable Agent-System Interaction](https://arxiv.org/abs/2610.10549)

**<font color=#1a73e8>作者：</font>** Yipeng Li, Ashutosh Hathidara, Jane Lo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool-calling agents have become central to enterprise AI, yet training and evaluating them at scale remains severely constrained due to business and legal restrictions on enterprise systems, data, and database schemas. Tabular data synthesis offers a natural alternative, but its effectiveness is fundamentally limited by structural validity and schema availability, while procedure-based approaches yield the opposite weakness, typically lacking distributional fidelity without per-domain authoring. We introduce **Synthesis Through Simulation** (STS), a **schema--free** data synthesis paradigm in which an LLM agent generates data by executing operations against policy-enforcing APIs within simulated enterprise environments. Because data is generated through the same environment that defines what is valid, STS guarantees structural validity by construction while decoupling validity enforcement from distribution modeling, allowing each to be addressed independently. The **Generalist Populator** (GP), STS's domain-agnostic agent, addresses the remaining challenges of distributional fidelity and synthesis scalability: GP achieves **0.88** average marginal fidelity and **100\% constraint satisfaction** across all ten environments *without access to DB schemas*, while statistical synthesizers are inapplicable to seven due to necessary seed data requirements, and schema-privileged agents fail 82\% of trajectories on airline environment's tightly coupled workflows due to brittle task composition. We open-source the full framework, all ten environments, and generated datasets at this https URL.

---


### 2. [Freeze the Decoder, Heal the Encoder: Parameter-Efficient Adaptation for SVD-Based KV-Cache Compression](https://arxiv.org/abs/2610.10552)

**<font color=#1a73e8>作者：</font>** Yufeng Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Comparing parameter-efficient fine-tuning recipes under a single, shared learning rate is a common but flawed practice: when the arms being compared have very different trainable-parameter counts, a shared rate can simultaneously depress the larger arms' means and inflate their variance, manufacturing a large, seemingly multi-seed-significant advantage for the smallest arm that is not a real effect. We document this confound in a concrete setting: post-hoc SVD-based KV-cache compression, where an already-pretrained model is converted to a low-rank (multi-head-latent-attention-style) cache by factorizing its key/value weights into a down-projection ("encoder") and an up-projection ("decoder"), after which a short fine-tune ("healing") recovers the accuracy lost to truncation. Under a shared learning rate, freezing the decoder and healing only the encoder looks like a clear win over healing the decoder or both factors; once every arm is given its own tuned learning rate, that apparent advantage disappears, and encoder-only healing instead reaches parity with the alternatives, at a real, measured saving of 3x fewer trainable parameters and 3x less optimizer-state memory. We verify this parity with per-arm learning-rate tuning and three seeds per configuration on a vision-language model (Qwen2.5-VL-3B-Instruct), at the one compression ratio this protocol covers, and replicate it on a text-only testbed across two backbones. Encoder-only healing is therefore a lower-memory drop-in recipe for retrofitting low-rank KV-cache compression at training time, and the shared-learning-rate pitfall we document and correct is a cautionary result for comparing any fine-tuning recipes whose arms differ in trainable-parameter count.

---


### 3. [SLVR: Structured Latent Visual Reasoning via Human-like Reasoning Flows](https://arxiv.org/abs/2610.10563)

**<font color=#1a73e8>作者：</font>** Albert Gao, Bing Xue, Andrea Zanette  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) often answer visual reasoning questions by relying on linguistic priors rather than task-relevant visual evidence. Textual chain-of-thought reasoning can partially mitigate this issue by encouraging models to decompose visual questions into intermediate evidence-seeking steps, but generating these steps autoregressively increases inference cost. Latent reasoning avoids explicit rationale generation, but existing approaches provide limited control over what intermediate states encode, making it difficult to impose separate supervision for planning, grounding, and evidence selection. We propose Structured Latent Visual Reasoning (SLVR), a training framework that bridges explicit chain-of-thought and latent reasoning by organizing multimodal reasoning into typed latent stages for planning, grounding, evidence selection, and reasoning integration.
SLVR first trains the model to rely on the image by masking answer-revealing text and contrasting the correct answer with visually plausible distractors. It then organizes reasoning into latent stages for planning, grounding, evidence selection, and integration, supervising each stage with the corresponding signal: plans, boxes, visual evidence, and final rationales. This gives latent reasoning an explicit functional structure while avoiding generated textual chains at inference time.
Built on Qwen2.5-VL-7B, SLVR improves consistently across multimodal reasoning benchmarks, with absolute gains of +9.4 on MMVP and +14.2 on BLINK Relation, as well as improvements on V*, MathVista, and ChartQA. These results suggest that structured latent supervision can improve fine-grained visual reasoning without the decoding overhead of textual CoT. Project page is available \href{this https URL}{here}.

---


### 4. [Agent-Controlled Forgetting for Tool-Using Agents: Reversible Context Curation in Practice](https://arxiv.org/abs/2610.10590)

**<font color=#1a73e8>作者：</font>** Jan-Peter Franke  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool-using agents repeatedly carry observations whose useful content can be much smaller than their original payload. We study agent-controlled forgetting: the acting model selects previously observed tool results, replaces each with a short note at its original position, and retains the exact original in a recoverable archive. A Python harness exposes batch archival and explicit recovery without task-specific model training, while protecting user instructions and assistant messages from these operations. In an exploratory OpenTelemetry debugging case followed by an unrelated implementation task, the method ended with 231,951 provider-reported prompt tokens versus 912,492 under retained history, used 50% fewer cumulative input tokens, and had an estimated API cost of USD 1.28-1.44 versus approximately USD 4.38. Both arms passed the two-case primary behavioral oracle; neither fully satisfied the follow-up evaluation. The method made more requests and took 17% longer. A contrasting application-development pair produced no context or cost saving, and an earlier continuation exhibited lower manually assessed quality despite reduced context. These observations demonstrate substantial resource savings in noisy tool-use trajectories and identify workload dependence as a central consideration for reversible context management.

---


### 5. [Wieszcz-XIX: A 3.1-Billion-Word Corpus of Pre-1918 Polish and Temporally Bounded Language Models Trained From Scratch](https://arxiv.org/abs/2610.10592)

**<font color=#1a73e8>作者：</font>** Szymon Kocur  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Historical Polish is well documented as a language but annotated in machine-readable form only to about a million words for the period this paper covers; the rest sits behind optical character recognition of variable quality. We present Wieszcz-XIX, a corpus of 6.75 billion tokens (about 3.1 billion words) in 294,369 documents, most of them periodical issues, of Polish published from 1800 to 1918, assembled from Wolne Lektury and the Internet Archive by a pipeline that filters, deduplicates, audits for post-1918 leakage and splits at the document level. It is over three orders of magnitude larger than the annotated corpus of the same period, and we quantify its defects: recognition corruption against a false-positive floor, near-identical duplication, which is removed, and post-1918 leakage, which is excluded from the training corpus itself down to a known residue of 0.04 to 0.38% of its bytes, found in the transcribed source, so the published corpus is the trained one document for document. On a hand-corrected sample the character error rate is 0.68% where the text is legible, and 45% of the sampled passages cannot be corrected. On it we train a ladder of decoder-only models from 47M to 349M parameters from scratch, and measure their temporal boundedness. Against two modern Polish base models, one far larger, the 349M shows a crossover, as does the 107M against the comparator of its size: post-1918 vocabulary costs them about 3.1 bits per byte more than period vocabulary, a gap the comparators do not show, and period vocabulary costs them fewer bits than it costs the comparators. Shown period text, the models keep its spelling and the comparators only partly. Adding parameters gains about twice as much as a second pass over the data. We release the corpus, code and weights. Content warning: the models reproduce period prejudice, including antisemitic statements.

---


### 6. [Coverage, Not Difficulty, Sets How Much Synthetic Data an Activation Probe Needs](https://arxiv.org/abs/2610.10594)

**<font color=#1a73e8>作者：</font>** Ankush Checkervarty  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Activation probes that monitor deployed language models are trained on synthetic conversations, and how many a probe needs is open. We trace learning curves over 10-590 synthetic samples for three monitoring concepts, high-stakes situations, replies harmful to a person, and replies that do not follow the user's instruction, on fourteen held-out evaluation distributions and four probe models, varying the generator LLM and the prompt's detail. The need is set by what is monitored: probes for high-stakes and harmful are within a few hundredths of their plateau from 80 samples on Gemma-3-27B-IT, instruction probes need several times as many, and the ordering holds on three smaller probe models and on real samples (from dev set). Prior work advises spending a generation budget on breadth, more kinds of data, over depth, more of each kind. We read the depth a concept needs as the half-gain size of a fitted curve, the number of samples at which half the gain is in hand. Concept and distribution account for 42-45% of its variance, the generator, probe model, and prompt detail for under 10%. What sets the value of the half-gain size is coverage, not per-kind difficulty: the number of samples of its own kind a distribution needs to saturate. Every kind, one per evaluation distribution, has a median half-gain size of 7-11 own-kind synthetic samples under all three concepts alike. What differs is how far samples of one kind transfer to the concept's other kinds, almost fully under high-stakes, less under harmful, and least under instruction, which accounts for most of the gap between concepts on generated and real samples. Breadth therefore pays differently by concept: many kinds are necessary under instruction, where no kind covers another, and nearly redundant under high-stakes, where one kind covers the rest. We release the evaluation suites, dev sets, and generated sets.

---


### 7. [From Investigation Failures to Reliable SOC Agents: Understanding and Improving LLM-Based Alert Triage](https://arxiv.org/abs/2610.10608)

**<font color=#1a73e8>作者：</font>** Saimon Amanuel Tsegai, Alex Kantchelian, Danfeng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Security operations centers (SOCs) must triage large volumes of alerts, most of which are benign, while missed attacks can remain uninvestigated. Tool-using large language model (LLM) agents can retrieve evidence during triage, but it remains unclear how reasoning strategies determine what to gather and when an investigation is sufficient to close an alert. We study five representative approaches spanning single-pass tool use, iterative retrieval, sampled investigations, self-review, and explicit verification. To support this study, we build ALERT-BENCH, an interactive benchmark that replays enterprise telemetry through a live SIEM and requires each system to retrieve evidence. Across 1,247 alerts from a multi-stage attack scenario, every approach missed at least 40.4% of attack-related alerts. Trace analysis shows that attack alerts are more likely to be dismissed when searches return no records, same-context review has negative net correction, and dismissal receives no consistently stronger investigation than escalation. Based on these findings, we further design AIDA (Adversarial Investigation and Dialectical Analysis), a multi-agent framework that requires an explicit proposed decision before independent challenge and stronger evidentiary requirements before dismissal. AIDA preserves investigation history in an append-only Investigation Ledger and keeps the challenge in a separate reasoning context. A separate Judge adjudicates the proposed decision and challenge against evidence, resolving the alert or requesting another round when evidence is missing. On the same alerts, AIDA achieves an F1 score of 0.958, compared with 0.371-0.744 for the studied approaches, and reduces the false-negative rate from 40.4% to 3.1% while escalating 18.4% of alerts to analysts. These results show that structuring evidence retrieval and decision review can substantially improve agentic SOC triage.

---


### 8. [PyCache Trap: The Inspection-Execution Gap in Agent Skill Scanners](https://arxiv.org/abs/2610.10612)

**<font color=#1a73e8>作者：</font>** Jie Liao, Simeng Qin, Wenqi Ren 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Agent skills combine instructions with executable resources, giving third-party packages access to an agent's runtime. Existing skill scanners inspect documentation and visible source, but Python may execute a bundled bytecode cache with different behavior. We study this gap between inspection and execution through PyCache Trap, which pairs benign source with a substituted cache accepted by the loader and connects it to a task-relevant invocation. Scanner-guided rewriting changes the invocation wording while preserving the cache body, separating package admission from recognition of the concealed behavior. Across 100 skills and seven scanners, PyCache Trap achieves 94-100% attack success, with no semantic recognition of the cache-resident behavior. We propose execution-aware validation (EAV) to connect inspected instructions, scripts, imports, and runtime artifacts in a typed execution graph. EAV combines grounded behavioral analysis with trusted reproduction of compiled artifacts. It detects all 100 evaluated source-present cache substitutions and reaches 92.8% Recall at 10.0% FPR across five attack families and 200 benign skills. The results support checking the executable artifacts a runtime can select as part of skill admission, within the supported loaders and code-object normalization. The code is released at this https URL.

---


### 9. [Recurrent Self-Improvement: Dynamic Cross-Loop On-Policy Distillation for Looped Language Models](https://arxiv.org/abs/2610.10623)

**<font color=#1a73e8>作者：</font>** Yi Wang, Rui Qian, Yu Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Looped Language Models (LoopLMs) offer a parameter efficient approach to scaling reasoning by reusing shared parameters across recurrent computation steps. Despite their promise, effective post-training of LoopLMs remains challenging. Existing approaches either provide reward based supervision that is sparse or costly to extend across loops, or rely on external teachers or privileged information, leading to limited teacher availability or teacher-student context mismatch. To address these limitations, we introduce LoopOPD, a cross-loop on-policy distillation framework that uses additional recurrent computation within a LoopLM as its own source of supervision. LoopOPD uses a frozen terminal loop policy as a compute privileged teacher for an intermediate loop student on student generated rollouts, providing dense supervision without an external teacher or privileged information. We further propose Dynamic LoopOPD (D-LoopOPD), which continually refreshes the terminal loop teacher as the shared model parameters are updated, enabling recurrent self-improvement. We characterize how distillation updates propagate across loop depths and derive sufficient conditions under which a single update yields simultaneous local improvement at both loop depths. Experiments on Ouro-Thinking models show that LoopOPD improves mathematical reasoning, while D-LoopOPD yields further gains through dynamic teacher updates. Despite being trained only on mathematical data, the resulting models also improve on general reasoning and code generation benchmarks, demonstrating that recurrent computation can serve as an effective source of supervision for LoopLMs. Our code and model checkpoints will be released upon acceptance.

---


### 10. [The Harness as the Only Mutable Surface: Compliance-Bounded Self-Evolution of LLM Agents in Credit Pipelines, with a Measured Admission Gate](https://arxiv.org/abs/2610.10629)

**<font color=#1a73e8>作者：</font>** Ravil Akhtyamov  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-improving LLM agents can adapt a credit pipeline to a changed rule, but an agent that rewrites itself destroys the artefact a supervisor reviews: a named change, a recorded test, an approval. We argue that self-evolution is reviewable only if it is confined to the runtime harness (instruction text, tool-call logic and primitive composition) while model weights stay fixed, so that every adaptation is a diff with a cause and a test attached. We give a dual-loop engine built on that bound, with one admission gate that writes a hash-chained record before deployment, and we measure the gate in simulation, with a simulated agent and a seeded-search proposer rather than language models. Across three families of supervisory re-interpretation at three severities, 10 seeds each, the gated loop admitted 144 of 7,449 candidate changes, none of which worsened error on held-out history, and restored the false-positive rate to the oracle level without raising missed flags in every low- and mid-severity cell. With the gate replaced by the check an unbounded system applies (fewer errors visible in recent traces), the same loops admitted 309 harmful changes and left missed flags above 10% in 49 of 90 runs: false positives fell because the screen was loosened. Evaluated on pre-shift labels, the gate rejected every candidate, so a re-interpretation must be encoded as a rule that relabels history. Parametric and scope shifts were repaired locally, a structural one only by primitive replacement; at the highest structural severity the gate's fixed tolerance blocked the correct replacement in half the seeds. We map the mechanisms to the EU AI Act's provisions for high-risk credit scoring and note that the April 2026 US model-risk guidance excludes agentic AI from its scope.

---


### 11. [Speaking the Navigator's Language: Trajectory-Grounded Instruction Translation for Frozen Aerial VLN Agents](https://arxiv.org/abs/2610.10635)

**<font color=#1a73e8>作者：</font>** Xi Chen, Zhe Liu, Xiaogang Xu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Aerial vision-and-language navigation (VLN) agents are typically trained on detail-rich, trajectory-aligned commands, whereas users issue short, intent-driven instructions; on a frozen OpenFly navigator, this \emph{instruction gap} drops success rate (SR) from $31.03\%$ to $11.33\%$. To scale translator training, we prompt a language model with human-written style examples to convert original commands into paired, intent-centered Weak commands, which yield $15.27\%$ SR. We introduce the \textbf{Trajectory-Grounded Instruction Translator (TGIT)}, a front-end that keeps the navigator frozen and translates Weak inputs into agent-executable commands by learning from its trajectory outcomes. The resulting Weak-trained translator raises Weak-input SR to $37.93\%$ and transfers zero-shot to real human instructions ($11.33\%{\rightarrow}32.51\%$); it also improves held-out OpenFly ($4.95\%{\rightarrow}20.79\%$) and yields recovery on CityNav and AirVLN.

---


### 12. [D-SLR: The Disjoint Row-Sparse plus Low-Rank Decomposition](https://arxiv.org/abs/2610.10636)

**<font color=#1a73e8>作者：</font>** Vincent Szolnoky  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Compressing a matrix for reconstruction still defaults to the truncated SVD, approximating the data with a single low-rank structure. It is common to reduce the residual further by adding an overlapping row-sparse component, but methods that solve this joint problem often require iterative solvers and tuning of regularization parameters. We propose the Disjoint Row-Sparse plus Low-Rank (D-SLR) decomposition, a closed-form drop-in for the truncated SVD that improves or exactly matches it. D-SLR restricts rows to either being stored verbatim or approximated by the low-rank fit, never both. Under squared error this restriction costs nothing: the joint optimum is attainable disjointly with fewer parameters at every non-trivial rank and stored row count (shape). With zero stored rows D-SLR reduces to the truncated SVD, so it never does worse at equal cost. The algorithm scores the entire error-versus-parameters tradeoff, and the solution is chosen afterwards by a supplied error target or parameter count, or by a selection rule. The grid and solution together cost three SVDs, with no tuning or regularization. We derive an assumption-free, a-posteriori lower bound on the error at every shape, giving each solution a computable certificate on the potential gain of any other choice of rank and stored rows. Experiments on synthetic and real data (LLM embedding tables, network traffic, hyperspectral images) confirm the gains and quantify the certificate.

---


### 13. [Coverage-Aware Reasoning with Medical Tokens for Diagnosis Prediction](https://arxiv.org/abs/2610.10641)

**<font color=#1a73e8>作者：</font>** Kaisong Zhang, Haotian Fang, Junmeng Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) offer promising potential for next-visit diagnosis prediction, owing to their ability to integrate longitudinal clinical evidence and reason over it in natural language. However, reinforcement learning for LLM reasoning commonly rewards each trajectory according to the correctness of its final answer. In next-visit diagnosis prediction, multiple diagnoses can be simultaneously valid, but independently rewarding one diagnosis per trajectory does not distinguish repeated hits from coverage of different diagnoses. The policy can therefore concentrate on a few correct diagnoses, leaving others uncovered. Meanwhile, LLM tokenizers can split ICD codes into several generic tokens with limited clinical meaning, requiring multiple decoding steps to predict each diagnosis and hindering reasoning over a large disease vocabulary. To address both challenges, we propose CARing, a framework that represents diagnoses with compositional Semantic IDs (SIDs) and optimizes reasoning trajectories for multi-label coverage. Concretely, we first encode ontology-enriched disease semantics into compact SIDs through residual quantization, and ground the resulting SID tokens in natural language and longitudinal EHR contexts through multi-task alignment and reasoning-enriched training to unlock transferable LLM reasoning. CARing further improves unordered multi-label prediction through a coverage reward for reinforcement learning and multi-positive supervision. At inference time, the model supports both efficient direct constrained decoding and multi-chain reasoning with rank fusion. On MIMIC-III and MIMIC-IV, CARing exceeds all EHR-trained baselines in weighted F1 and attains the highest top-k recall at every reported cutoff, including R@30 of 46.04% and 46.52% in reasoning mode. Our codes and logs are available at this https URL.

---


### 14. [Large Language Model-Assisted Preparation of Transportation Management Plans: A Case Study with WisDOT WisTMP System](https://arxiv.org/abs/2610.10650)

**<font color=#1a73e8>作者：</font>** Zihao Sheng, Pei Li, Zilin Huang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Work zones are critical yet hazardous components of transportation infrastructure, requiring carefully designed Transportation Management Plans (TMPs) to ensure safety and mobility. However, TMP preparation remains labor-intensive and heavily dependent on practitioner expertise. This paper proposes a Large Language Model (LLM)-assisted framework to automate TMP content generation, leveraging the WisDOT WisTMP system as the application context. The framework fine-tunes multiple open-source LLMs across different model scales and deploys them locally to ensure data security. To support model training, we construct a domain-specific dataset from historical WisTMP documents by converting PDF files into structured question-answer pairs in JSON format. Experimental results show that fine-tuning significantly improves performance across standard text generation metrics. Further section-wise and strategy-level analyses reveal that, while LLMs achieve strong overall performance, they tend to over-generate strategies and struggle to produce project-specific justifications and accurate cost estimates. In addition, scaling from 7B/8B to 14B yields limited gains. These findings demonstrate the potential of LLMs to improve TMP preparation efficiency while highlighting remaining challenges in LLM-assisted TMP development. The source code and demo videos will be publicly available at this https URL.

---


### 15. [Nullify: Null-Space Activation Steering for Training-Free LLM Unlearning](https://arxiv.org/abs/2610.10655)

**<font color=#1a73e8>作者：</font>** Wei Zhai, Xiang Liu, Qiang Huang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) inevitably internalize substantial amounts of sensitive or private information during pre-training, while LLM unlearning aims to selectively erase specific knowledge to prevent privacy leakage with minimal loss of model utility. However, existing methods struggle to balance forget quality with utility, and typically incur substantial computational costs due to parameter fine-tuning. To address this, we propose Nullify, a training-free, non-destructive activation steering method for LLM unlearning. Nullify employs steering vectors during inference to redirect privacy-related activations away from their memorized answers, while satisfying a null-space constraint that leaves retained-query activations essentially unaffected to maintain utility. Evaluations on TOFU and MUSE show that Nullify matches or surpasses established baselines in forget quality while achieving near-lossless preservation of model utility. By avoiding weight updates entirely, Nullify serves as an efficient, plug-and-play inference-time intervention framework.

---


### 16. [Lossy Compressive Text Autoencoders](https://arxiv.org/abs/2610.10738)

**<font color=#1a73e8>作者：</font>** Vinko Sabolčec, Angelos Katharopoulos, David Grangier  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Our work explores learning a compressed latent representation of text, at the intersection of data compression and representation learning. We propose an autoencoder architecture that performs residual downscaling and upscaling of hidden representations along the time axis, with a residual low-dimension discrete bottleneck. We analyze our approach for different quantization methods, training objectives, and datasets. For different levels of compression, we evaluate the similarity between the original and reconstructed text both at the surface-level (BLEU) and at the semantic-level (LLM-based judge). Additionally, we evaluate our models on downstream question-answering and semantic text similarity benchmarks. Our approach results in compressed representations which are on par with lossless text compression algorithms at 2.24 bits per byte on web text data, while having good reconstruction and downstream task performance.

---


### 17. [VICO: Visual Environments Co-Evolving for Vision-Language Model Reasoning](https://arxiv.org/abs/2610.10782)

**<font color=#1a73e8>作者：</font>** Meng Lu, Ligeng Zhu, Olivia Xiao 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) has become a standard recipe for post-training vision-language models (VLMs),
but it typically assumes a static training environment. As the actor improves, fixed tasks drift out of its learning frontier: many
become trivial, others remain unsolvable; and the learning signal collapses. We argue that VLM post-training should evolve the
visual environment alongside the actor, not just the actor itself. We propose VICO, a co-evolutionary framework in which an actor
and an Environment-as-Rewriter (EnvRewriter) are trained jointly: the EnvRewriter edits verifiable image-side structures, such as
scene graphs, chart tables, or protected region masks, and re-renders them to produce label-valid training samples whose difficulty
is calibrated to the actor's current ability through a pass-rate-based reward. This loop continuously realigns task difficulty with
actor capability without any additional human annotation. Across nine multimodal benchmarks spanning mathematical reasoning and
visually grounded understanding, VICO-8B improves over its base model by up to +5.0% on out-of-domain tasks, surpasses the strongest
self-evolution and text-editing co-evolution baselines by +4.3% and +8.4% respectively, and stays comparable to chart-specialized
RLVR methods using 16-160 times fewer labeled samples. By shifting from human-labeled supervision to image-editing co-evolution,
VICO offers a scalable path beyond static-corpus RLVR for visual reasoning.

---


### 18. [Plan-and-Patch: Diffusion Language Models for Agentic Planning](https://arxiv.org/abs/2610.10786)

**<font color=#1a73e8>作者：</font>** Syamantak Kumar, Jiang Guo, Hassan Hamad 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Planning is increasingly important for long-horizon agents, where successful execution requires coordinating subgoals, tool use, and intermediate outcomes over many steps. Yet assumptions made during planning may be invalidated by the environment, tools may return unexpected results, or actions may fail. Effective agents must therefore not only generate plans, but also revise them. Such revisions often affect only part of a plan, leaving the preceding and subsequent structure intact. Rather than regenerate the entire plan and risk unnecessary changes, repair can regenerate the affected region conditioned on the preserved prefix and suffix. We introduce Plan-and-Patch, a plan-and-act framework in which a diffusion language model (dLLM) generates a structured, program-like plan through parallel unmasking and repairs it by filling in selected regions while keeping the surrounding steps fixed. We compare DreamReasoner-8B and Qwen3-8B as diffusion and autoregressive (AR) planners. On Natural Plan without task-specific training, diffusion (53.7%) achieves nearly twice the plan repair success rate of AR (27.0%). After task-specific training on agentic benchmarks, ALFWorld and TextCraft, the planners achieve similar observed success in plan generation, while diffusion reduces mean plan-generation latency by 39-46% relative to AR. Our results show that Plan-and-Patch provides a framework for faster plan generation and effective plan repair in long-horizon agents.

---


### 19. [Evaluating Rubric Generation with Interventional Transfer](https://arxiv.org/abs/2610.10809)

**<font color=#1a73e8>作者：</font>** Erik Skalnes, Layne C. Price, Raviteja Anantha 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Instance-specific rubrics are common in AI benchmarks where reliable evaluation requires specific expert knowledge. This approach is difficult to scale, prompting research into the generation of rubrics with large language models (LLMs). However, even when expert rubrics are available as references, it is unclear how to productively evaluate the quality of generated rubrics at scale. In this paper, we introduce a method for the evaluation of rubric generation, which we call Interventional Transfer (IT), based on the idea that two rubrics are similar if they move together when a response is perturbed to pass/fail one of them. In contrast to existing approaches for evaluation of rubric generation, we argue that different forms of interventional transfer can be used to evaluate the utility of generated rubrics for different tasks. For instance, we apply this approach in a case study on HealthBench, where we demonstrate an asymmetry in rubrics generated by Qwen3.8-27B, Deepseek-V4-Flash, and Opus-5, used to evaluate responses from GPT-5.6-Terra. Perturbations that degrade responses according to the generated/expert rubric transfer into lower scores on the corresponding expert/generated rubric, but perturbations that improve on one rubric do not reliably transfer into higher scores on the other. We argue that this finding has implications for the usage of LLM-generated rubrics for performance monitoring and hill-climbing. We contrast our approach with existing approaches for rubric evaluation, which do not surface the same asymmetry that we observe.

---


### 20. [Guided Reflection for Personal Sleep Insight in Everyday Sleep Tracking](https://arxiv.org/abs/2610.10822)

**<font color=#1a73e8>作者：</font>** Bokyung Kim, Amama Mahmood, Honghao Zhao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Digital sleep technologies make tracking accessible, yet users often struggle to interpret what changes in their sleep mean. Behavioral sleep medicine addresses this through guided discovery, helping patients develop personal interpretations rather than simply receiving explanations. To bring this to everyday tracking, we present DREAM, an LLM-powered voice assistant that monitors conversational sleep diaries, selectively invites users to interpret meaningful changes, and uses their interpretation to tailor subsequent education. We co-designed DREAM with sleep specialists iteratively and evaluated it in a six-week field study (N=14) against a generic-education control. DREAM participants reported greater personal sleep insight, motivation, and willingness to use the system, and described a clearer rationale for trying strategies. Our findings suggest that guided reflection made participants more active interpreters of their own sleep. Furthermore, we argue that expert involvement is not a single transfer of knowledge but an ongoing process of making tacit judgment explicit and testable.

---


### 21. [Grammar Concept Annotation at Scale: Deployed Fine-Tuned Small Language Models Outperform Prompted Frontier Models](https://arxiv.org/abs/2610.10827)

**<font color=#1a73e8>作者：</font>** Marjan Celikik, Ana Peleteiro Ramallo, Javier Morales  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Corrective feedback is among the best-evidenced drivers of second-language acquisition, yet corrections delivered during lessons rarely accumulate into an actionable view of grammar mastery. Prompted frontier models can provide such a view from learner--tutor lesson transcripts, but they are costly at scale. We close this gap by fine-tuning Qwen3.5 small language models (SLMs) on filtered and rebalanced teacher-generated supervision, then deploying an efficient 0.8B model in an end-to-end grammar mastery tracker for all English learners on our platform. Internalizing the annotation contract into adapter weights enables pairing the 0.8B model with a compact matched prompt rather than verbose instructions. On two human-curated benchmarks, both the deployed 0.8B model and a 4B reference comparator outperform prompted GPT-5.4 and GPT-5.6 Sol in precision and recall under nested matching criteria of increasing strictness: concept, evidence span, and correctness. The deployed 0.8B SLM reduces serving cost by approximately 16$\times$. A feature-level online experiment shows significant gains in learner engagement ($+15.8\%$) and key business metrics, including scheduled hours ($+2.1\%$) and GMV from new lessons ($+13.2\%$).

---


### 22. [On the Clock: Towards Punctual and Productive Time-Budgeted AI Agents](https://arxiv.org/abs/2610.10833)

**<font color=#1a73e8>作者：</font>** Aaron Wang, Neelabh Madan, Vlad Sobal 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We study whether small LLM agents can operate effectively under explicit wall-clock time budgets by both respecting the allocated runtime and using available time productively. We evaluate Qwen3.6-27B on five competitions from MLE-Bench Lite and Qwen3-4B on Zork I (Jericho), two agentic benchmarks where additional computational time can meaningfully improve performance. In the simplest setting, where the budget is stated only in the prompt, agents fail to translate the stated budget into controlled use of time. These failures arise from gaps in time awareness, since the harness provides no timing feedback, but also because they cannot reliably anticipate the duration of actions, and do not have a learned mapping from available time to an appropriate strategy. We investigate two complementary classes of interventions: harness-based mechanisms that expose timing information and enforce deadlines, and reinforcement learning with budget-aware rewards. Injecting timing information through the harness substantially improves budget adherence for Qwen3.6-27B without measurable loss in performance, while enforcement hooks tighten adherence further. RL with GRPO achieves near-perfect budget adherence on Zork I and generalizes to held-out budgets not seen during training, but does not improve task performance over the untrained harness on MLE-Bench. Once agents are made to respect the budget, they still fail to use additional time to improve task performance. RL-trained policies learn when to stop but often fill extra time with repeated actions, and GRPO training on multiple budgets tends to collapse toward the strategy learned for the shortest budget. Our results reveal a gap between time adherence and productive time allocation, which remains a central challenge for budget-conditioned agents.

---


### 23. [Real Long-Term Memory for AI: A 50-Million-Token Window That Is Faster and Cheaper Than Recompute](https://arxiv.org/abs/2610.10845)

**<font color=#1a73e8>作者：</font>** Sietse Schelpe  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A large language model can only use the text that fits in its context window, and it recomputes its internal key-value (KV) state for a prompt every time the prompt is sent. We test a memory layer, the public package galahad-kv, that saves the KV state of each block of about 16,000 tokens to encrypted local NVMe disk and loads it back later, byte-exact, without recomputing it. We ran it on 50,000,000 tokens of real public text, served through vLLM on one NVIDIA H100, with Gemma 4 12B and Gemma 4 31B. Every block we probed was loaded back from the encrypted store with no recompute (100 of 100, at depths from 0 to 50M tokens) on both models. Loading a block was 2.8x to 4.3x faster than recomputing it and used 8.8x to 12.3x less GPU energy, and GPU memory stayed flat over the whole 50M-token stream. Asked about facts planted millions of tokens earlier, the 12B model gave the right answer 82 times out of 100 and the 31B model 98 times out of 100. Neither model made up an answer. The limits are as follows. This is reuse of stored state, not a wider attention window: one block is loaded at a time, and how well a question is answered depends on the model. Writing the memory is a one-time cost, and the store takes terabytes of local NVMe disk. We describe the test protocol, which is built to resist common ways of gaming long-context benchmarks, and give a single-GPU reproduction that uses public software and a free licence for the package.

---


### 24. [Amortized Off-Policy Evaluation for LLMs](https://arxiv.org/abs/2610.10848)

**<font color=#1a73e8>作者：</font>** Younwoo Choi, Leo Feng, Vincent Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate evaluation is central to selecting which LLM to deploy, yet testing a candidate on live traffic exposes real users to an unvetted model. Teams therefore evaluate candidates offline, on data produced by already-deployed models. This is off-policy evaluation (OPE), and it faces two distribution shifts: as a model is updated in post-training, its responses diverge from the logged ones (policy shift), and the reward definition under which it is judged changes with business requirements (reward shift). Classical OPE methods are ill-suited to this continual-deployment setting because they are defined per task and require fitting from scratch on every new logged dataset or reward definition. To address this, we propose PFN-OPE, a prior-data fitted network that amortizes OPE across a distribution of contextual-bandit tasks. We pretrain it once on tasks constructed from a pool of LLM responses scored by several reward functions, in which both shifts occur. At test-time it maps a logged dataset and one sampled target response per prompt to a value estimate in a single forward pass, with no per-task fitting. On HelpSteer2 and UltraFeedback with Qwen, Llama, and Gemma policies, PFN-OPE achieves 2.0 to 9.3 times lower error than the best baselines across all tested configurations in the reward-shifted settings.

---


### 25. [KDFP: A first-principles approach to knowledge distillation in large language models](https://arxiv.org/abs/2610.10854)

**<font color=#1a73e8>作者：</font>** Ryan Swift, Konstantinos Psounis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Knowledge distillation is an established technique for improving the capabilities of small, efficient student models by training them with the representations of larger, more capable teacher models. Much of the recent work in the distillation of large language models (LLMs) has focused on distilling abilities learned during post-training, such as instruction following, chain-of-thought reasoning, and tool usage. This has left a large research gap in general knowledge distillation for LLMs, which is essential for developing efficient and private systems suitable for deployment on edge devices. We take a first-principles approach, evaluating previous lessons from prior works and conducting new explorations to develop a distillation methodology suitable for modern LLMs. We present KDFP, a novel methodology for white-box general knowledge distillation in LLMs. We demonstrate that KDFP outperforms existing methods by 1.6% $-$ 4.9% across 9 benchmarks while increasing training efficiency by up to 99.1% through ephemeral parameter reduction.

---


### 26. [Sparse Attention Is Matrix Approximation, Not Choosing from a Bag of Values](https://arxiv.org/abs/2610.10871)

**<font color=#1a73e8>作者：</font>** Fang Wan, Xufeng Liu, Fan Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) achieve strong performance across many domains, but their efficiency is limited by the quadratic cost of attention with respect to prompt length. Sparse attention reduces this cost by retaining only a small fraction of query-key interactions to approximate the full attention matrix. However, existing methods are trapped in a mathematically wrong view: they simply keep large scalar entries or high-mass regions of the attention matrix. This treats the attention matrix as a bag of values, ignoring that it is used as a structured matrix whose entries jointly determine the attention output through multiplication with value vectors. We argue that this is the core conceptual issue: sparse attention should be formulated as matrix approximation, not as blindly choosing the largest values from a bag of entries. Based on this view, we propose Matrix Approximation Sparse Attention (MASA). MASA replaces raw attention-mass ranking with a closed-form score that measures how much each sparse unit reduces matrix-product approximation error. As a theory-grounded plug-in correction, MASA can be added to existing sparse attention frameworks without changing their sparse kernels or budgets. Extensive experiments across multiple sparse attention methods, benchmarks, and LLM backbones show consistent accuracy gains, supporting both MASA and the matrix-approximation view of sparse attention.

---


### 27. [Stochastic Teacher Intervention for Agentic On-Policy Distillation](https://arxiv.org/abs/2610.10878)

**<font color=#1a73e8>作者：</font>** Junnan Liu, Linhao Luo, Zhijun Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) efficiently transfers capabilities from a stronger teacher to a student language model through dense token-level supervision on student-generated rollouts and has shown promise on complex tasks such as mathematical reasoning. However, in multi-turn agentic tasks, student decisions shape subsequent observations, causing early errors to accumulate across turns. The resulting trajectories can drift away from the teacher's rollout distribution, making the teacher's token-level supervision less reliable or even counterproductive for OPD training. To address this issue, we introduce STI-OPD, a stochastic teacher intervention framework for multi-turn agentic OPD. During multi-turn interaction, STI-OPD uses teacher intervention guided by teacher-student policy discrepancy to replace the student's proposed action with a teacher-generated one to maximize the acquisition of reliable supervision. We further develop a stochastic intervention strategy, addressing the limitations of previous threshold-based or fixed-schedule approaches, that estimates policy discrepancy using KL divergence and maps it to an intervention probability. By sampling whether to intervene from this probability, STI-OPD adaptively balances teacher control with student exploration. To learn from the resulting mixed-policy trajectories, we introduce an Importance-Weighted Reverse KL objective that corrects the token sampling mismatch between teacher-generated responses and the student policy to preserve the original OPD objective. Across tool-integrated reasoning and long-horizon interaction, STI-OPD outperforms the strongest prior OPD baseline on every evaluated benchmark and student size. Ablations further show that both discrepancy-guided intervention and importance weighting contribute to these gains.

---


### 28. [SPLIT-RL: Staged Perception-Language Reasoning Training with Claim-Level Advantages](https://arxiv.org/abs/2610.10889)

**<font color=#1a73e8>作者：</font>** Raja Kumar, Rajat Koner, Ritwick Chaudhry 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language (VL) reasoning requires a model to both extract relevant and accurate information from an image (visual reasoning, VR), and to infer the answer from it (language reasoning, LR). Reinforcement learning with verifiable rewards typically trains both through a single chain-of-thought with a final-answer reward. This gives every CoT token the same sequence-level advantage, failing to distinguish capability specific errors. We propose SPLIT-RL, a staged post-training approach that trains VR and LR in disjoint phases. Because a group's rollouts differ along one capability at a time, the group-relative advantage isolates it, and each phase is optimized using phase-specific reward. We further introduce Claim-Level Advantage (CLA-GRPO), which decomposes VR-phase rollouts into atomic visual claims and provides a fine-grained advantage at claim level based on visual-type group formation. Although trained in two phases, trained policy is evaluated like GRPO model, with a single CoT call at inference time. Under this protocol, SPLIT-RL improves average accuracy over GRPO by 1.4-6.1 points across Qwen3-VL models from 2B to 30B-A3B and InternVL3.5-8B. Evaluating each capability using an oracle based diagnostic shows that answer-only GRPO leaves perception unchanged, whereas SPLIT-RL improves both VR and LR.

---


### 29. [Less from More: Reinforcing Sparse Video Reasoning from Dense References](https://arxiv.org/abs/2610.10893)

**<font color=#1a73e8>作者：</font>** Wenfang Sun, Yingjun Du, Cees G. M. Snoek  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video-language models commonly assume that more temporal observations lead to more reliable reasoning. We question this assumption and argue that the key challenge is not merely processing more video frames efficiently, but learning to reason reliably under limited temporal evidence. We propose SAVER, a dense-to-sparse post-training framework that uses dense video views as training-time references for sparse-frame inference. During reinforcement post-training, paired dense and sparse views are optimized with grounding rewards and a reliability-gated reference reward, encouraging sparse view predictions to preserve task-relevant temporal evidence. Notably, SAVER is trained only on 1,250 randomly sampled temporal grounding examples, without using any video question answering annotations. Across three temporal grounding benchmarks and six video question-answering benchmarks, SAVER consistently improves performance across frame budgets. In particular, SAVER can match or surpass dense-frame Qwen3.5 baselines while using substantially fewer frames. These results show that temporal grounding can serve as an effective evidence-localization proxy for learning sparse video reasoning that transfers to broader video understanding tasks.

---


### 30. [Reading the Room: Foundations, Design, and Challenges of Normative Competence in LLMs](https://arxiv.org/abs/2610.10906)

**<font color=#1a73e8>作者：</font>** Andrea Wynn, Harsh Satija, Seokhyun 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Human communities are governed by normative systems: shared standards that produce \textit{norms} dictating acceptable behavior, enforced through community sanctioning. Aligning increasingly autonomous AI systems with these norms is a central alignment challenge, complicated by the fact that norms are vast in number, change quickly, and are often arbitrary (e.g., dress or language conventions). Thus, alignment requires \textit{normative competence}: the ability to discern from interaction alone what norms a community enforces without relying on static pretrained knowledge. We introduce a multi-agent community debate setting, where access to debate is governed by synthetic norms, to study normative competence in isolation from pretraining exposure. We show that baseline LLM agents fail to learn norms even when doing so would improve their accuracy. We then experiment with various \textit{normative modules} -- architectural components for norm inference -- finding that norm-following is highly sensitive to both the style of norm and the model powering the normative module, suggesting a lack of generalizability. Furthermore, when idiosyncratic, non-normative behaviors accompany the true norm, LLM agents exhibit an unselective attribution failure: they indiscriminately copy idiosyncratic noise alongside enforced rules, a pattern that persists even when imitating unnecessary behaviors is explicitly penalized. To the best of our knowledge, our work is the first to operationalize and evaluate normative competence in LLMs, demonstrating that current AI systems excel at behavioral mimicry but lack the capacity to discern socially enforced order.

---


### 31. [Large Language Models for Machine Translation Quality Annotation: Humans and Models Are Both Challenged](https://arxiv.org/abs/2610.10918)

**<font color=#1a73e8>作者：</font>** Hala Almaghout, Christian Federmann, Qin Gao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are considered to be a more efficient and cost-effective alternative to human judgment for Machine Translation (MT) evaluation. With MT evaluation spanning a large number of language pairs, domains and levels of annotation granularity, LLMs must be thoroughly evaluated across these dimensions before being reliably used as alternatives to human evaluation. In this paper, we evaluate the performance of LLMs for two prominent MT quality evaluation schemes: Multidimensional Quality Metrics (MQM) and Error Span Annotation (ESA) by comparing their agreement with human annotators. We present results on a long-context test set of 70 language pairs and the publicly available WMT23 and WMT25 data, investigating both score and error span annotation agreement across a variety of language pairs and domains. Our results show that while LLM agreement with human annotators exceeds agreement between human annotators for some evaluation tasks, both vary substantially across annotation schemes, language pairs and domains and remain unreliable for most settings. Furthermore, we identify challenges facing both human and LLM annotators: humans are particularly challenged by fine-grained MQM annotations and low-resource language pairs, while LLMs struggle with minor errors, wrong language variants and error span annotation. Our results highlight the potential for improvement for both human and LLM annotation performance, possibly through human-LLM collaborative annotation pipelines that address the reliability issues identified in this work.

---


### 32. [Language Models for Page-Level Layout Decisions in E-commerce Search](https://arxiv.org/abs/2610.10920)

**<font color=#1a73e8>作者：</font>** Varun Joshi, Eva C. Song, ChengXiang Zhai  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> E-commerce search pages are critical touchpoints for millions of online shoppers. While traditional search engines return a ranked list of results, modern E-commerce search pages increasingly incorporate recommender system modules -- for example, secondary stacks that surface alternative product groupings at specific positions. When introduced appropriately, secondary stacks can improve user engagement; however, suboptimal placement may disrupt browsing flow and degrade the primary results. Unlike traditional search ranking, where evaluation techniques such as interleaving are well established, evaluating page-level layout changes e.g., when and where to insert a secondary stack remains challenging without costly online A/B testing. To address this, we study offline methods for evaluating whether a given layout decision -- specifically, the inclusion of a secondary stack at a particular position -- is beneficial to users. We investigate language models as scalable evaluators by comparing direct prompt-based, prompt-derived feature, and representation-based methods. Our results show that representation-based approaches consistently outperform prompt-based judging in predicting user engagement, suggesting they provide a reliable foundation for offline layout evaluation in E-commerce search.

---


### 33. [Speedbumps: Rejection Attacks on Speculative Decoding](https://arxiv.org/abs/2610.10929)

**<font color=#1a73e8>作者：</font>** Adam Y. J. Jones, Yu Yuan, Sergio Maffeis  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Speculative decoding is a popular technique for increasing the speed and reducing the costs of large language model (LLM) inference by verifying multiple draft tokens in a single target-model forward pass. The resulting benefit depends on the ability of the drafter to approximate the target model's distribution. In this work, we study Speculative Rejection Attacks (SRAs), a novel class of attacks that cause draft and target models to disagree more often, resulting in fewer draft tokens being accepted per draft cycle. This leads to more target model forward passes needed per generated token, slowing down inference and increasing costs for the victim. We introduce two attacks which append an adversarial suffix to attacker-controlled content to degrade speculative decoding on a victim's prompts. Both attacks optimise the expected length of the accepted speculative prefix, estimating per-depth acceptance from the target's probability of the drafted proposals (Speedbump-P) or from the overlap between the draft and target distributions (Speedbump-D). In some cases, attacks degrade speculative decoding to the point of being slower than autoregressive decoding. The degradation reduces the output quality - regularisation restores output quality but gives up most of the degradation, trading effectiveness for stealthiness. Additionally, the suffixes remain effective under sampling, and transfer across drafters (Speedbump-P) or across target models sharing a drafter (Speedbump-D). These findings identify the draft-target interaction of speculative decoding as a realistic attack surface through which adversarial inputs can inflate inference costs.

---


### 34. [Rethinking the Tradeoff Between Temporal Encoding and Nonlinear Computation in Spiking Language Models](https://arxiv.org/abs/2610.10933)

**<font color=#1a73e8>作者：</font>** Hanfei Liu, Shuchang Feng, Yanxia Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spiking language models face a tradeoff between representing continuous semantic features over short temporal windows and retaining costly nonlinear attention operations. We introduce Spora, which jointly designs spike encodings and attention operators. Binary temporal weights let $T$ spikes represent compositional values with up to $T$ bits of capacity, compared with $O(\log_2 T)$ bits for spike-count readout. Unipolar Binary Spiking (UBS) uses thresholds and spike-triggered residual decay to produce non-negative integer codes; Bipolar Binary Spiking (BBS) separates sign and magnitude and learns a scale for signed activations. These representations support accumulation-and-shift dot products and integer-exponent mappings in attention. With four time steps, Spora achieves 76.6 average GLUE score and 44.1 CoLA MCC, improving over SpikeLM by 1.2 and 6.2 points, respectively. Extending BBS to six steps raises these scores to 78.2 and 47.4. Conditional-decay analysis, matched-budget activation-quantization comparisons, event-workload statistics, and fixed-point evaluation further characterize the connection between encoding fidelity and computational cost.

---


### 35. [StoreBench: A Live-Commerce Environment for Evaluating and Training Autonomous Operator Agents](https://arxiv.org/abs/2610.10942)

**<font color=#1a73e8>作者：</font>** Daksh Raghuvanshi, Ved Vedere, Yifan Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning environments are now a primary lever for improving large language model (LLM) capabilities in post-training, yet most agentic benchmarks remain static: the world moves only when the agent acts, the reward is a terminal verdict, and the pass bar is set arbitrarily. We introduce StoreBench, a live-commerce environment in which an agent runs a mid-size online apparel store on a production-grade commerce backend, testing long-horizon planning and economic judgment under uncertainty. Customers order around the clock, suppliers reprice and fail, and market shocks arrive with partial or no warning. The agent acts through the same 29 merchant tools a human operator would use, under a windowed operation budget that makes simulated time a function of actions taken, so model latency cannot influence simulated time. Pass thresholds are calibrated against scripted anchor policies, the reward is hardened against a catalogue of reward hacks, and every episode replays identically given a sequence of actions. We evaluate seven frontier LLMs on 11 scenarios of 30 to 45 days and a full simulated year, over three world seeds at matched reasoning effort. No model matches the scripted smart-triage policy on average: the best, DeepSeek-V4-Pro, passes 49% of task-seed cells against the heuristic's 97%. Human experts working through the same tools and budgets outscore every model (mean composite 0.708 vs. 0.700). Over a full simulated year under the Claude Code harness, most models show dramatic performance improvement. In a GRPO post-training run, Qwen3.5-27B trained on only five disjoint tasks raises its mean composite on the held-out evaluation tasks from 0.136 to 0.373. We release five example training-split tasks, ten sample trajectories, and the scoring and verification tooling; the full environment and evaluation suite are withheld to keep the benchmark uncontaminated.

---


### 36. [AI4Fire: Evaluating Large Language Models on Wildfire Tasks](https://arxiv.org/abs/2610.10946)

**<font color=#1a73e8>作者：</font>** Yue Zhao, Xiyang Hu, Zuobin Xiong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are entering wildfire management, where overstated evaluations can cost property and lives. How do they perform on wildfire tasks, with and without grounding? Bare means a model receives the task input alone. Grounded means it also receives one task-specific addition: for smoke detection, a smoke-free reference frame from the same camera. AI4Fire runs six core models bare and grounded on five wildfire tasks, zero-shot; a sweep adds 29 more. Our literature search on fire tasks found 138 works; none combines this roster, task coverage, and paired bare and grounded runs. We report three findings. (1) Grounding helped most where the addition carried the answer: a read-only SQL tool lifted every core model's database accuracy from at most 16 to at least 88 percent. (2) Simple rules were hard to beat: no core model outperformed repeating today's staffing count, and two open-weight models mostly copied the median of similar earlier fire-days, a worse forecast. (3) Public releases carry hazards: a fire-danger column separates the holdout perfectly, and 67 aerial fire frames carry smoldering or fire-free labels read from a clipped thermal maximum. We release prompts, responses, scores, code, and the survey record.

---


### 37. [RH-Detect: A Unified Benchmark for Reward Hacking Detection](https://arxiv.org/abs/2610.10947)

**<font color=#1a73e8>作者：</font>** Junwei Quan, Evgenii Opryshko, Rohan Subramani 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reward hacking, where a model exploits an evaluation signal without completing the intended task, threatens the reliability of deployed language model systems. Existing datasets use different labels, response formats, and metadata conventions, making detector results difficult to compare. We present RH-Detect, a benchmark that combines reward-hacking-relevant subsets from eleven public datasets, comprising 92,761 rows and six behavior categories, into a common schema. On 5,021 open-ended evaluation units, each comprising a task prompt and a free-form model continuation, including multi-turn tool-use trajectories, we evaluate six off-the-shelf language models from five families as reward hacking detectors without additional training. The best model achieves a pooled AUROC of 0.962, with accuracy above 93%. For the four strongest models, however, accuracy on the two multi-turn tool-use datasets, MALT and TRACE, is 10.7-15.9 percentage points lower than on the other sources at a common decision threshold, highlighting a key gap for deployment-time monitoring. We find that different input formats have different effects across models. Removing thinking raises Qwen3.5-4B AUROC from 0.779 to 0.849, but lowers Qwen Flash from 0.977 to 0.950. We also evaluate the benchmark as a training dataset for detectors. Holding out each source in turn, single-token SFT improves average AUROC on five of six held-out sources. A GRPO follow-up on that failure case yields a slight improvement in detection performance. Our results show that a single pooled score can conceal variation across data sources, detector inputs, and training procedures.

---


### 38. [Learning How to Search for Plans with Exponentially Less Space](https://arxiv.org/abs/2610.10954)

**<font color=#1a73e8>作者：</font>** Dominik Drexler, Simon Ståhlberg, Markus Fritzsche 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Heuristic search for a plan can store exponentially many states, even when its heuristic is almost perfect. We instead learn search control, one specification per domain, written as an indexical policy: a generalized policy with registers that hold objects and modes that sequence its rules. We add the choose rule, which loads an object into a register and marks a backtracking point, where one candidate suffices; every other rule must work for all of its outcomes and needs no search. Our main result is that structural termination, which rules out infinite executions, also bounds every execution by a polynomial in the number of objects. A depth-first procedure then finds a plan in polynomial space, however large the state space, with no list of visited states. The cost is time, exponential only in the choice depth, the number of real choices along an execution. Any class that such a policy solves therefore lies in NP, and in P at constant choice depth. We learn these policies with a language model in a counterexample-guided loop that certifies termination, verifies the training tasks, and keeps the choice depth small. With the learned policies, the procedure solves 1,709 of 1,890 test tasks of the IPC 2023 Learning Track and the Autoscale Agile suite, more than LAMA, BFWS, and Levitron, and most of them within one second and 100 MiB.

---


### 39. [Spectrally Targeted Muon](https://arxiv.org/abs/2610.10965)

**<font color=#1a73e8>作者：</font>** Vishrut Goyal, Rohan Ramkumar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Muon optimizer orthogonalizes each update matrix, setting all of its singular values to one, and has proven highly effective for training large language models. It remains unclear, however, whether this success comes from amplifying small singular directions that gradient descent neglects or from suppressing large, degenerate directions that disrupt training. We introduce Spectrally Targeted Muon, which orthogonalizes only the singular values above or below a threshold $\tau$, so that varying $\tau$ interpolates between normalized SGD and Muon. It isolates the relevant singular subspaces with projections computed by Newton-Schulz iteration on a shifted Gram matrix, so no SVD is needed. We evaluate these variants on the CIFAR-10 and NanoGPT speedruns, tracking the effective rank of gradient, update, and weight matrices and a new metric, the alignment of updates with the tangent space of the weight matrix's isospectral manifold. We find three things. First, the small singular values of the momentum are not noise. Orthogonalizing everything except the few largest singular values of each matrix nearly matches Muon while touching only a small fraction of the momentum, whereas orthogonalizing only the top falls well short even though it holds almost all of it. On language models every momentum singular value is far below one, so targeted orthogonalization can only amplify, and Muon wins by making directions that are too small to train on at their raw scale trainable. Second, shrinking the largest singular values is what keeps the parameter spectrum flat; this is cheap, and it is not what drives the loss. Third, AdamW differs from Muon mainly in how slowly it builds structure, which explains its slower start and why warmup helps AdamW but only hurts Muon.

---


### 40. [When Citations Mislead? A Claim-Level Benchmark for Legal Hallucination Detection](https://arxiv.org/abs/2610.10971)

**<font color=#1a73e8>作者：</font>** M. Mikail Demir, M. Abdullah Canbaz  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used in legal research and drafting, but they can still produce claims that sound convincing without being supported by the cited source. We introduce PARCEL, a benchmark for checking whether a legal claim is supported by the underlying authority. Using recent New York State Court of Appeals decisions, we build a dataset of 3,396 parenthetical-style claims labeled as Supported, Refuted, or Not Found. We cast this task as a three-way natural language inference problem and evaluate several state-of-the-art LLMs in a zero-shot setting. Although the strongest models reach up to 0.97 accuracy, the results also show an important weakness: models still incorrectly mark unsupported claims as supported, even when the full opinion text is provided. Across models, missing support is harder to detect than direct contradiction, and fabricated but plausible citations cause the largest drop in performance. Overall, PARCEL provides a practical benchmark for testing claim-level groundedness in legal RAG systems.

---


### 41. [Budgeted Multi-Source Counterfactual Annotation for Off-Policy Evaluation](https://arxiv.org/abs/2610.10974)

**<font color=#1a73e8>作者：</font>** Biao Xiang, Ali Eshragh, Yuexing Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Off-policy evaluation (OPE) estimates the value of a target policy from logged data, but limited behavior-policy coverage can force high-variance reweighting or reward-model extrapolation. Counterfactual annotations can add evidence about unobserved actions, yet practical sources, including domain experts and large language models (LLMs), may be costly, biased, or noisy. We study budgeted acquisition of such annotations for contextual-bandit OPE. Given source-specific costs and error profiles, we formulate an integer allocation problem over context-action pairs and annotation sources to minimize the component of estimator variance that depends on the annotation plan. We characterize when annotations are valuable through a first-annotation threshold and local annotation-value regimes. For the coupled multi-source problem, we develop a majorization-minimization algorithm with dynamic-programming subroutines that monotonically improves the objective. Experiments in synthetic clinical and LLM-annotated education bandits show that our allocation method reduces fixed-profile mean squared error (MSE) by 20.58% and 10.77%, respectively, relative to no annotation.

---


### 42. [Optimizing Large Language Models with Chained LMOs](https://arxiv.org/abs/2610.10975)

**<font color=#1a73e8>作者：</font>** Sungyoon Kim, Kaan Ozkara, Youngsuk Park  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Muon has motivated a growing family of optimizers that compose multiple matrix normalizations, but these methods remain fragmented and lack a unified perspective. We introduce chained linear minimization oracles (chained LMOs), which cast these methods as compositions of LMOs. Despite their empirical success, many chains fall outside the standard LMO framework and can diverge on smooth convex objectives. To explain why composition can nevertheless help, we turn to linear associative memory and show that chaining can improve over Muon under anisotropic embeddings. Empirically, we propose TensorChain, a novel optimizer within the framework that stacks compatible weight matrices across different layers and normalizes the 3d tensor across its axes. In Qwen3 0.6B and 1.7B pretraining, TensorChain outperforms all chained baselines in average token efficiency, with average token savings of 9.6% over Muon at matched validation loss.

---


### 43. [Fluid-Gen-Zero: Grounding Pretrained Video Generators in Physics without Training](https://arxiv.org/abs/2610.10984)

**<font color=#1a73e8>作者：</font>** Hong Huang, Yuqiu Liu, Chenyu You 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present Fluid-Gen-Zero, a training-free framework for physics-aware fluid-object interaction video generation that decouples physical reasoning from appearance synthesis. Our key insight is to delegate motion dynamics to a physics simulator while preserving the appearance modeling capacity of pretrained video generators. We bridge these two domains through a two-level agentic workflow: generation-time planning, where a vision-language model (VLM) agent interprets intent and the simulation rollout to organize generation clips, and latent-space guidance, which injects simulation signals into denoising through region-aware latent wrapping. This plug-and-play design is compatible with current video foundation models. We further introduce a benchmark for fluid-object interaction video generation. Across Tora (CogVideoX-based), VACE and WanMove (Wan-based), Fluid-Gen-Zero consistently improves simulation alignment, reducing object trajectory error by 26.7%-81.5% and fluid fEPE (fluid flow endpoint error) by 67.9%-84.0%, while largely preserving perceptual quality. In a human preference study, raters favor Fluid-Gen-Zero in 55.1%-74.4% of same-backbone comparisons across three backbones, and in 90.4%-94.2% of comparisons against simulation-based methods. Code and data will be released upon acceptance.

---


### 44. [Back in Style: A Sociolinguistic Approach to Authoring and Measuring Persona Fidelity in User Simulation](https://arxiv.org/abs/2610.10988)

**<font color=#1a73e8>作者：</font>** Lex Konnelly, Elena Khasanova, Riqiang Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As agentic systems gain commercial popularity, user simulators increasingly serve as measurement instrument for their evaluation. However, the fidelity of simulated users in comparison to real human users is generally low, and typically assessed by costly, subjective LLM judges. In this pilot study, we ask whether fidelity can instead be measured deterministically by treating a user persona sociolinguistically: as a social type that emerges from observable linguistic style, rather than one predicted by labels or descriptions a model must extrapolate into behaviour. We author personas as concrete stylistic rates, which lets us transfer two established, model-free instruments -- authorship-verification stylometry and lexicon-based content analysis -- as fidelity diagnostics. We A/B-test the sociolinguistic schema against a flat descriptive baseline across five task-oriented customer-service agents. Results show that the sociolinguistic schema improves both stylistic adherence and stylometric distinguishability for most of the tested models, with a caveat that persona style fidelity does not necessarily equal persona "naturalness". We argue that a sociolinguistic approach to persona design is a promising path towards more diverse and representative user personas, and that these metrics are most valuable in an error-attribution analysis, localizing where fidelity breaks down. This is a first step towards interventions that move user simulations closer to faithful renderings of diverse and variable linguistic outputs.

---


### 45. [Omni-Diffusion-Distill: Few-Step Distillation of Unified Multimodal Diffusion Large Language Models](https://arxiv.org/abs/2610.10990)

**<font color=#1a73e8>作者：</font>** Hong Huang, Chenhongyi Yang, Junzhe Sun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unified multimodal diffusion large language models (dLLMs) offer a single architecture for both image generation and multimodal understanding, but their iterative decoding requires tens to hundreds of forward passes. Existing few-step distillation methods largely focus on either image generation or text generation, making it unclear how to compress a fully discrete multimodal dLLM into a single efficient student while preserving both generation and understanding. We introduce Omni-Diffusion-Distill, a unified two-stage distillation framework that retains strong generation and understanding capabilities while substantially reducing the inference cost of a unified multimodal dLLM. Omni-Diffusion-Distill aligns the distillation of both generation and understanding, for both images and text, in the discrete token space. In the first stage, the student is trained to skip decoding steps by replaying cached teacher trajectories, and in the second stage the student is refined on intermediate states along its own rollouts. We further remedy two sources of degradation in unified distillation with a pairwise collision penalty that reduces repetition under parallel text decoding, and entropy-matched guidance that prevents entropy collapse caused by fitting the sharpened teacher distribution in image generation. Omni-Diffusion-Distill achieves state-of-the-art trade-offs between decoding efficiency and generation and understanding performance for multimodal dLLMs, reducing image generation from 128 to 8 decoding steps and multimodal understanding from 512 to 64, giving 18.2x and 21.2x wall-clock speedups. Under these budgets, it scores 0.828 on GenEval and 83.0 on DPG-Bench for text-to-image generation, while reaching GPT judge scores of 20.0 on MM-Vet and 57.2 on COCO captioning (twice the teacher's 28.4 at the same steps) for multimodal understanding.

---


### 46. [How Narrative Wrapping Affects LLM Refusal: A Cross-Language Benchmark and Defense](https://arxiv.org/abs/2610.11005)

**<font color=#1a73e8>作者：</font>** Zhankai Ye, Yanning Wang, Yukai Jin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Safety-aligned language models often refuse a harmful request stated directly but answer the same request inside a role-play or narrative wrapper. We measure this vulnerability across languages and registers: attack success on Qwen3-1.7B is already 89.4% in English and 93.0% in modern Chinese, and reaches 95.7% in Classical Chinese. We build GUISE, a benchmark for systematically studying this vulnerability. It includes parallel requests in English, modern Chinese, and Classical Chinese, matched harmful and benign pairs, wrapper types held out for evaluation, and a stricter criterion that counts warn-then-answer responses as attack successes. Representation analysis shows that language and register move harmful-request representations only slightly away from the model's refusal direction, whereas narrative wrappers move them much farther away. We propose AXIS, which combines preference optimisation with a rotation objective that aligns harmful-request representations with the refusal direction and a commitment objective that trains the model to refuse completely rather than produce a warn-then-answer response. Across Qwen3-1.7B, Qwen3-4B and GLM-4-9B, AXIS achieves the highest combined safety and usability score among the compared methods.

---


### 47. [Curating Always-Loaded Context for LLM Agents: A Capacitated Assortment Model with Censored Feedback](https://arxiv.org/abs/2610.11007)

**<font color=#1a73e8>作者：</font>** Zexuan Liu, Yuning Yang, Tiancheng Zhao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> At the start of every session, LLM agents load a fixed context file, such as $\texttt{this http URL}$. Each loaded token in the file is charged again in every later round of the session, and these files can degrade performance as they grow in size. However, in practice, human or automated curators usually grow these files by appending.
We formulate context curation as a capacitated assortment problem. Instructions consume tokens under a finite attention capacity; adding an instruction never raises the compliance of the others, while retained instructions incur a per-session setup cost.
We prove an upper bound on the optimal file size, regardless of the number of available candidate instructions, and that appending every instruction with positive standalone value can be arbitrarily worse in net value than selecting an optimal subset. A token budget also limits the loss when the token price is underestimated.
We then examine what can be learned from past sessions and how this information can guide decisions to add or remove instructions. Feedback is inherently censored: the benefits and harms of loaded instructions are observable, whereas missing instructions generate feedback only when their absence causes harm.
In this setting, we show that deleting instructions ignored by agents can inevitably remove helpful ones. We characterize how much evidence should be collected before adding an instruction. Besides, we bound regret when human reviewers can inspect only a limited number of edits per period. Empirical experiments further show that irrelevant rules drawn from real context files reduce language-model compliance.

---


### 48. [Prompts versus Rules: Auditing and Controlling Speech Naturalness Behaviors in Voice User Simulators](https://arxiv.org/abs/2610.11015)

**<font color=#1a73e8>作者：</font>** Riqiang Wang, Elena Khasanova, Harsh Saini 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As voice agents gain more popularity commercially, the user simulators used to evaluate the deployed agents are also being developed to include more realistic, variable, and diverse speech naturalness behaviors -- disfluency, interruption and backchanneling. The quality of the user simulator directly affects the validity of agent evaluation results. However, we find that most studies so far have not examined in detail whether the intended configuration for these behaviors is realized in the simulation. In this study, we audit the realized naturalness behaviors of tau-Voice, our own LLM-based prompting approach across three models, and our rule-based injection algorithm for disfluency, interruption, and backchanneling. We find that prompting for these behaviors is unreliable and produces speech inconsistent with the instructions, placed and distributed less naturally than the instruction implies. In contrast, our rule-based, model-free algorithm produces controllable and diverse naturalness behaviors more aligned with natural speech. Our results suggest that LLMs not purpose-trained for user simulation are not sufficient on their own to represent authentic user behavior, and that linguistically informed deterministic approaches or specialized models are needed to close the gap; auditing and reporting realized naturalness behaviors, rather than configured settings, is what makes that gap visible.

---


### 49. [Mid-Training Language Models on Raw Video](https://arxiv.org/abs/2610.11019)

**<font color=#1a73e8>作者：</font>** Jaedong Hwang, Xiaoqian Shen, Ernie Chang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models learn mostly from paired image-text data or annotated video, and raw web video is rarely used to further train an existing language model. We study whether raw video, with no captions and no text loss, can serve as mid-training data for a pretrained language model. Frames are encoded into continuous visual tokens, and the language model learns to predict the next visual token. We mid-train Qwen3-1.7B on raw clips from YT-Temporal-1B and then apply the same image-text instruction tuning to it and to the model without mid-training, so that the two differ only in mid-training. The mid-trained model scores 2.9 points higher on average across four video benchmarks and 5.1 points higher across ten image benchmarks, spanning perception, document, and chart tasks. Text performance is preserved even though mid-training includes no text, with an average of 48.9 across 14 text benchmarks compared with 48.0 for the model without mid-training. Analyses across training show that the image and video gains emerge within 30% of training and plateau thereafter, varying by less than 0.5 points. Predicting captions fails to outperform next-visual-token prediction, demonstrating that video mid-training can remain purely self-supervised without the computational overhead or labeling noise of automated captioning.

---


### 50. [Intent Graph: Navigating the Analytical Reasoning Space for Exploratory Data Analysis](https://arxiv.org/abs/2610.11025)

**<font color=#1a73e8>作者：</font>** Junran Yang, Shruti Badrish, Teanna Barrett 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Exploratory data analysis (EDA) is rarely open-ended in practice: analysts work from high-level domain questions toward the concrete analyses that can answer them, prioritizing directions with domain knowledge and prior hypotheses. Large language models (LLMs) can supply such knowledge, but their responses are unstructured, leaving analysts no way to see what has been explored, what is missing, or why one direction was chosen over another. We present DAG-EDA, a system that lets analysts and an LLM co-navigate the space of possible analyses through two linked structures. An intent graph, governed by a grammar of analytical intent, decomposes an ambiguous natural-language question into progressively concrete analysis tasks, keeping alternative framings open and letting analysts branch, backtrack, and compare paths. A multi-layered knowledge graph externalizes the LLM's domain knowledge, linking domain concepts to the dataset variables that can measure them, so analysts can inspect and contest how their question is grounded in the data. Both graphs are constructed from only the dataset and the analyst's question, and the analyses the analyst reaches are rendered as interactive dashboards. We illustrate the system through a usage scenario and describe a user study design for examining whether the system scaffold analysts' reasoning and navigation.

---


> [!TIP]
> 当前位于：**1-50**（第 1/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-288](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
